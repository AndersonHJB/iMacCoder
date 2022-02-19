<audio title="24 _ 从哨兵Leader选举学习Raft协议实现（下）" src="https://static001.geekbang.org/resource/audio/57/9b/577b4b0ba6b46dd324abbbedb6dece9b.mp3" controls="controls"></audio> 
<p>你好，我是蒋德钧。</p><p></p><p>上节课，我给你介绍了Raft协议的基本流程，以及哨兵实例工作的基本过程。哨兵是通过serverCron函数的周期性执行，进而在serverCron中调用sentinelTimer函数，实现周期性处理哨兵相关的时间事件。而sentinelTimer函数处理的时间事件，就包括了对哨兵监听的每个主节点，它会通过调用sentinelHandleRedisInstance函数，来检查主节点的在线状态，并在主节点客观下线时进行故障切换。</p><p></p><p>另外，我还带你了解了sentinelHandleRedisInstance函数执行过程的前三步操作，分别是重连断连的实例、周期性给实例发送检测命令，检测实例是否主观下线，这也分别对应了sentinelReconnectInstance、sentinelSendPeriodicCommands和sentinelCheckSubjectivelyDown这三个函数，你可以再回顾下。</p><p></p><p>那么，今天这节课，我接着来给你介绍sentinelHandleRedisInstance函数执行过程中的剩余操作，分别是检测主节点是否客观下线、判断是否需要执行故障切换，以及需要故障切换时的哨兵Leader选举的具体过程。</p><!-- [[[read_end]]] --><p></p><p>学完这节课的内容，你就可以对哨兵工作的过程有个全面了解了。并且，你可以掌握如何在代码层面实现Raft协议来完成Leader选举。这样，当你日后在分布式系统中实现分布式共识时，这部分内容就能帮助指导你的代码设计与实现了。</p><p></p><p>接下来，我们先来看下主节点的客观下线判断。</p><p></p><h2>主节点客观下线判断</h2><p>现在我们知道，哨兵在sentinelHandleRedisInstance函数中会<strong>调用sentinelCheckObjectivelyDown函数</strong>（在sentinel.c文件中），来检测主节点是否客观下线。</p><p></p><p>而sentinelCheckObjectivelyDown函数在执行时，除了会检查当前哨兵对主节点主观下线的判断结果，还需要结合监听相同主节点的其他哨兵，对主节点主观下线的判断结果。它把这些判断结果综合起来，才能做出主节点客观下线的最终判断。</p><p></p><p>从代码实现层面来看，在哨兵用来记录主节点信息的<strong>sentinelRedisInstance结构体</strong>中，本身已经用哈希表保存了监听同一主节点的其他哨兵实例，如下所示：</p><pre><code class="language-plain">typedef struct sentinelRedisInstance {
…
dict *sentinels;
…
}
</code></pre><p>这样一来，sentinelCheckObjectivelyDown函数通过遍历主节点记录的sentinels哈希表，就可以获取其他哨兵实例对同一主节点主观下线的判断结果。这也是因为，sentinels哈希表中保存的哨兵实例，它们同样使用了sentinelRedisInstance这个结构体，而这个结构体的成员变量flags，会记录哨兵对主节点主观下线的判断结果。</p><p>具体来说，sentinelCheckObjectivelyDown函数会<strong>使用quorum变量，来记录判断主节点为主观下线的哨兵数量</strong>。如果当前哨兵已经判断主节点为主观下线，那么它会先把quorum值置为1。然后，它会依次判断其他哨兵的flags变量，<strong>检查是否设置了SRI_MASTER_DOWN的标记</strong>。如果设置了，它就会把quorum值加1。</p><p>当遍历完sentinels哈希表后，sentinelCheckObjectivelyDown函数会判断quorum值是否大于等于预设定的quorum阈值，这个阈值保存在了主节点的数据结构中，也就是master-&gt;quorum，而这个阈值是在sentinel.conf配置文件中设置的。</p><p>如果实际的quorum值大于等于预设的quorum阈值，sentinelCheckObjectivelyDown函数就判断主节点为客观下线，并<strong>设置变量odown为1，</strong>而这个变量就是用来表示当前哨兵对主节点客观下线的判断结果的。</p><p>这部分的判断逻辑如下代码所示，你可以看下：</p><pre><code class="language-plain">void sentinelCheckObjectivelyDown(sentinelRedisInstance *master) {
…
//当前主节点已经被当前哨兵判断为主观下线
if (master-&gt;flags &amp; SRI_S_DOWN) {
&nbsp;&nbsp; quorum = 1; //当前哨兵将quorum值置为1
&nbsp; &nbsp;
&nbsp;&nbsp; di = dictGetIterator(master-&gt;sentinels);
&nbsp;&nbsp; while((de = dictNext(di)) != NULL) {&nbsp; //遍历监听同一主节点的其他哨兵
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sentinelRedisInstance *ri = dictGetVal(de);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (ri-&gt;flags &amp; SRI_MASTER_DOWN) quorum++;
&nbsp;&nbsp; }
&nbsp;&nbsp; dictReleaseIterator(di);
&nbsp;&nbsp; //如果quorum值大于预设的quorum阈值，那么设置odown为1。
&nbsp;&nbsp; if (quorum &gt;= master-&gt;quorum) odown = 1;
}
</code></pre><p>另外，这里我也画了一张图，展示了该判断逻辑，你可以再来回顾下。<br>
<img src="https://static001.geekbang.org/resource/image/c4/8f/c4201b2611c7e6c53604914b29b9418f.jpg?wh=1920x1080" alt="图片"></p><p>那么，一旦sentinelCheckObjectivelyDown函数判断主节点客观下线了，它就会调用sentinelEvent函数发送+odown事件消息，然后在主节点的flags变量中<strong>设置SRI_O_DOWN标记</strong>，如下所示：</p><pre><code class="language-plain">//判断主节点为客观下线
if (odown) {
&nbsp;&nbsp; //如果没有设置SRI_O_DOWN标记
&nbsp;&nbsp; if ((master-&gt;flags &amp; SRI_O_DOWN) == 0) {
&nbsp;&nbsp;&nbsp; sentinelEvent(LL_WARNING,"+odown",master,"%@ #quorum %d/%d",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; quorum, master-&gt;quorum); //发送+odown事件消息
&nbsp;&nbsp; &nbsp;master-&gt;flags |= SRI_O_DOWN;&nbsp; //在主节点的flags中记录SRI_O_DOWN标记
&nbsp;&nbsp;&nbsp; master-&gt;o_down_since_time = mstime(); //记录判断客观下线的时间
&nbsp;&nbsp; }
}
</code></pre><p>也就是说，<strong>sentinelCheckObjectivelyDown函数是通过遍历监听同一主节点的其他哨兵的flags变量，来判断主节点是否客观下线的。</strong></p><p></p><p>不过，你看完刚才的代码可能会有一个疑问，在上节课学习的sentinelCheckSubjectivelyDown函数中，如果哨兵判断主节点为主观下线，是会在主节点的flags变量中<strong>设置SRI_S_DOWN标记</strong>，如下所示：</p><pre><code class="language-plain">//哨兵已判断主节点为主观下线
…
//对应主节点的sentinelRedisInstance结构中flags没有记录主观下线
if ((ri-&gt;flags &amp; SRI_S_DOWN) == 0) {
&nbsp; &nbsp;…
&nbsp;&nbsp; ri-&gt;flags |= SRI_S_DOWN;&nbsp; //在主节点的flags中记录主观下线的标记，
}
</code></pre><p>但是，sentinelCheckObjectivelyDown函数，是检查监听同一主节点的其他哨兵flags变量中的SRI_MASTER_DOWN标记，<strong>那么其他哨兵的SRI_MASTER_DOWN标记是如何设置的呢?</strong></p><p></p><p>这就和sentinelAskMasterStateToOtherSentinels函数（在sentinel.c文件中）有关系了，下面，我们来具体了解下这个函数。</p><p></p><h3>sentinelAskMasterStateToOtherSentinels函数</h3><p>sentinelAskMasterStateToOtherSentinels函数的主要目的，是向监听同一主节点的其他哨兵发送is-master-down-by-addr命令，进而询问其他哨兵对主节点的状态判断。</p><p></p><p>它会调用redisAsyncCommand函数（在<a href="https://github.com/redis/redis/tree/5.0/deps/hiredis/async.c">async.c</a>文件中），依次向其他哨兵发送sentinel is-master-down-by-addr命令，同时，它设置了<strong>收到该命令返回结果的处理函数为sentinelReceiveIsMasterDownReply</strong>（在sentinel.c文件中），如下所示：</p><pre><code class="language-plain">void sentinelAskMasterStateToOtherSentinels(sentinelRedisInstance *master, int flags) {
…
di = dictGetIterator(master-&gt;sentinels);
//遍历监听同一主节点的其他哨兵
while((de = dictNext(di)) != NULL) {
&nbsp;&nbsp; sentinelRedisInstance *ri = dictGetVal(de);
&nbsp;&nbsp; …
&nbsp;&nbsp; //发送sentinel is-master-down-by-addr命令
&nbsp;&nbsp; retval = redisAsyncCommand(ri-&gt;link-&gt;cc,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sentinelReceiveIsMasterDownReply, ri,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "%s is-master-down-by-addr %s %s %llu %s",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sentinelInstanceMapCommand(ri,"SENTINEL"),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; master-&gt;addr-&gt;ip, port,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sentinel.current_epoch,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (master-&gt;failover_state &gt; SENTINEL_FAILOVER_STATE_NONE) ?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sentinel.myid : "*");
}
…
}
</code></pre><p>另外从代码中，我们可以看到，sentinel is-master-down-by-addr命令中还包括主节点IP、主节点端口号、当前纪元（sentinel.current_epoch）和实例ID。下面展示的就是这个命令的格式：</p><pre><code class="language-plain">sentinel is-master-down-by-addr 主节点IP 主节点端口 当前epoch 实例ID
</code></pre><p>在这其中，哨兵会根据当前主节点所处的状态来设置实例ID。如果主节点已经要开始进行故障切换了，那么，实例ID会被设置为当前哨兵自身的ID，否则就会被设置为*号。</p><p>这里你需要注意的是，主节点的数据结构是使用了<strong>master-&gt;failover_state</strong>来记录故障切换的状态，其初始值为SENTINEL_FAILOVER_STATE_NONE（对应的数值为0），当主节点开始故障切换时，这个状态值就会大于SENTINEL_FAILOVER_STATE_NONE了。</p><p></p><p>好了，在了解了sentinelAskMasterStateToOtherSentinels函数的基本执行过程之后，我们还需要知道：sentinelAskMasterStateToOtherSentinels函数向其他哨兵发出了sentinel is-master-down-by-addr命令后，其他哨兵是如何处理的呢？</p><h3>sentinel is-master-down-by-addr命令的处理</h3><p>其实，哨兵对于sentinel开头的命令，都是在<strong>sentinelCommand函数</strong>（在sentinel.c文件）中进行处理的。sentinelCommand函数会根据sentinel命令后面跟的不同子命令，来执行不同的分支，而is-master-down-by-addr就是一条子命令。</p><p></p><p>在is-master-down-by-addr子命令对应的代码分支中，sentinelCommand函数会根据命令中的主节点IP和端口号，来获取主节点对应的sentinelRedisInstance结构体。</p><p>紧接着，它会判断主节点的flags变量中是否有SRI_S_DOWN和SRI_MASTER标记，也就是说，sentinelCommand函数会检查当前节点是否的确是主节点，以及哨兵是否已经将该节点标记为主观下线了。如果条件符合，那么它会设置<strong>isdown变量</strong>为1，而这个变量表示的就是哨兵对主节点主观下线的判断结果。</p><p></p><p>然后，sentinelCommand函数会把当前哨兵对主节点主观下线的判断结果，返回给发送sentinel命令的哨兵。它返回的结果主要包含三部分内容，分别是<strong>当前哨兵对主节点主观下线的判断结果</strong>、<strong>哨兵Leader的ID</strong>，以及<strong>哨兵Leader所属的纪元</strong>。</p><p></p><p>sentinelCommand函数，对sentinel命令处理的基本过程如下所示：</p><pre><code class="language-plain">void sentinelCommand(client *c) {
…
// is-master-down-by-addr子命令对应的分支
else if (!strcasecmp(c-&gt;argv[1]-&gt;ptr,"is-master-down-by-addr")) {
…
//当前哨兵判断主节点为主观下线
if (!sentinel.tilt &amp;&amp; ri &amp;&amp; (ri-&gt;flags &amp; SRI_S_DOWN) &amp;&amp; (ri-&gt;flags &amp; SRI_MASTER))
&nbsp;&nbsp; isdown = 1;
…
addReplyMultiBulkLen(c,3); //哨兵返回的sentinel命令处理结果中包含三部分内容
addReply(c, isdown ? shared.cone : shared.czero); //如果哨兵判断主节点为主观下线，第一部分为1，否则为0
addReplyBulkCString(c, leader ? leader : "*"); //第二部分是Leader ID或者是*
addReplyLongLong(c, (long long)leader_epoch); //第三部分是Leader的纪元
…}
…}
</code></pre><p>你也可以参考下图：<br>
<img src="https://static001.geekbang.org/resource/image/57/fd/573b2cb64005925500d338030f61a1fd.jpg?wh=1920x1080" alt="图片"></p><p>好了，到这里你就已经知道，哨兵会通过sentinelAskMasterStateToOtherSentinels函数，向监听同一节点的其他哨兵发送sentinel is-master-down-by-addr命令，来获取其他哨兵对主节点主观下线的判断结果。而其他哨兵是使用sentinelCommand函数，来处理sentinel is-master-down-by-addr命令，并在命令处理的返回结果中，包含自己对主节点主观下线的判断结果。</p><p></p><p>不过从刚才的代码中，你也可以看到，在其他哨兵返回的sentinel命令处理结果中，会包含哨兵Leader的信息。其实，这是因为sentinelAskMasterStateToOtherSentinels函数发送的sentinel is-master-down-by-addr命令本身，也可以用来<strong>触发哨兵Leader选举</strong>。这个我稍后会给你介绍。</p><p></p><p>那么，我们再回到前面讲主节点客观下线判断时提出的问题，sentinelCheckObjectivelyDown函数要检查监听同一主节点的其他哨兵flags变量中的SRI_MASTER_DOWN标记，但是，其他哨兵的SRI_MASTER_DOWN标记是如何设置的呢？</p><p></p><p>这实际上是和哨兵在sentinelAskMasterStateToOtherSentinels函数中，向其他哨兵发送sentinel is-master-down-by-addr命令时，设置的<strong>命令结果处理函数sentinelReceiveIsMasterDownReply</strong>有关。</p><p></p><h3>sentinelReceiveIsMasterDownReply函数</h3><p>在sentinelReceiveIsMasterDownReply函数中，它会判断其他哨兵返回的回复结果。回复结果会包含我刚才介绍的三部分内容，分别是当前哨兵对主节点主观下线的判断结果、哨兵Leader的ID，以及哨兵Leader所属的纪元。这个函数会进一步检查，其中第一部分内容“当前哨兵对主节点主观下线的判断结果”是否为1。</p><p>如果是的话，这就表明对应的哨兵已经判断主节点为主观下线了，那么当前哨兵就会把自己记录的对应哨兵的flags，设置为SRI_MASTER_DOWN。</p><p></p><p>下面的代码就展示了sentinelReceiveIsMasterDownReply函数判断其他哨兵回复结果的执行逻辑，你可以看下。</p><pre><code class="language-plain">//r是当前哨兵收到的其他哨兵的命令处理结果
//如果返回结果包含三部分内容，并且第一，二，三部分内容的类型分别是整数、字符串和整数
if (r-&gt;type == REDIS_REPLY_ARRAY &amp;&amp; r-&gt;elements == 3 &amp;&amp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r-&gt;element[0]-&gt;type == REDIS_REPLY_INTEGER &amp;&amp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r-&gt;element[1]-&gt;type == REDIS_REPLY_STRING &amp;&amp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r-&gt;element[2]-&gt;type == REDIS_REPLY_INTEGER)
{
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;ri-&gt;last_master_down_reply_time = mstime();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //如果返回结果第一部分的值为1，则在对应哨兵的flags中设置SRI_MASTER_DOWN标记
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (r-&gt;element[0]-&gt;integer == 1) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ri-&gt;flags |= SRI_MASTER_DOWN;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }
</code></pre><p>所以到这里，你就可以知道，一个哨兵调用sentinelCheckObjectivelyDown函数，是直接检查其他哨兵的flags是否有SRI_MASTER_DOWN标记，而哨兵又是通过sentinelAskMasterStateToOtherSentinels函数，向其他哨兵发送sentinel is-master-down-by-addr命令，从而询问其他哨兵对主节点主观下线的判断结果的，并且会根据命令回复结果，在结果处理函数sentinelReceiveIsMasterDownReply中，设置其他哨兵的flags为SRI_MASTER_DOWN。下图也展示了这个执行逻辑，你可以再来整体回顾下。</p><p></p><p><img src="https://static001.geekbang.org/resource/image/51/7f/51c98fec129byy830c8878466c95337f.jpg?wh=1920x978" alt="图片"></p><p>那么，掌握了这个执行逻辑后，我们再来看下，哨兵选举是什么时候开始执行的。</p><p></p><h2>哨兵选举</h2><p>这里，为了了解哨兵选举的触发，我们先来复习下在上节课，我讲过的sentinelHandleRedisInstance函数中针对主节点的调用关系，如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/27/f7/276ee9fb08acf2405aa24b4658387df7.jpg?wh=1920x1042" alt="图片"></p><p>从图中可以看到，sentinelHandleRedisInstance会先调用sentinelCheckObjectivelyDown函数，再调用sentinelStartFailoverIfNeeded函数，判断是否要开始故障切换，如果sentinelStartFailoverIfNeeded函数的返回值为<strong>非0值</strong>，那么sentinelAskMasterStateToOtherSentinels函数会被调用。否则的话，sentinelHandleRedisInstance就直接调用sentinelFailoverStateMachine函数，并再次调用sentinelAskMasterStateToOtherSentinels函数。</p><p></p><p>那么，在这个调用关系中，sentinelStartFailoverIfNeeded会判断是否要进行故障切换，它的<strong>判断条件</strong>有三个，分别是：</p><ul>
<li>主节点的flags已经标记了SRI_O_DOWN；</li>
<li>当前没有在执行故障切换；</li>
<li>如果已经开始故障切换，那么开始时间距离当前时间，需要超过sentinel.conf文件中的sentinel failover-timeout配置项的2倍。</li>
</ul><p></p><p>这三个条件都满足后，sentinelStartFailoverIfNeeded就会调用<strong>sentinelStartFailover函数</strong>，开始启动故障切换，而sentinelStartFailover会将主节点的failover_state设置为SENTINEL_FAILOVER_STATE_WAIT_START，同时在主节点的flags设置SRI_FAILOVER_IN_PROGRESS标记，表示已经开始故障切换，如下所示：</p><pre><code class="language-plain">void sentinelStartFailover(sentinelRedisInstance *master) {
…
master-&gt;failover_state = SENTINEL_FAILOVER_STATE_WAIT_START;
master-&gt;flags |= SRI_FAILOVER_IN_PROGRESS;
…
}
</code></pre><p>而一旦sentinelStartFailover函数将主节点的failover_state设置为SENTINEL_FAILOVER_STATE_WAIT_START后，接下来，sentinelFailoverStateMachine函数就会执行状态机来完成实际的切换。不过，<strong>在实际切换前，sentinelAskMasterStateToOtherSentinels函数会被调用。</strong></p><p></p><p>看到这个调用关系，你可能会有个疑问：sentinelAskMasterStateToOtherSentinels函数是用来向其他哨兵询问对主节点主观下线的判断结果的，如果sentinelStartFailoverIfNeeded判断要开始执行故障切换，那么为什么还要调用sentinelAskMasterStateToOtherSentinels函数呢？</p><p></p><p>其实，这就和sentinelAskMasterStateToOtherSentinels函数的另一个作用有关了，这个函数除了会用来向其他哨兵询问对主节点状态的判断，它还可以用来<strong>向其他哨兵发起Leader选举</strong>。</p><p></p><p>在刚才给你介绍这个函数时，我提到它会给其他哨兵发送sentinel is-master-down-by-addr命令，这个命令包括主节点IP、主节点端口号、当前纪元（sentinel.current_epoch）和实例ID。其中，如果主节点的failover_state已经不再是SENTINEL_FAILOVER_STATE_NONE，那么实例ID会被设置为当前哨兵的ID。</p><p></p><p>而在sentinel命令处理函数中，如果检测到sentinel命令中的实例ID不为*号，那么就会调用<strong>sentinelVoteLeader函数</strong>来进行Leader选举。</p><pre><code class="language-plain">//当前实例为主节点，并且sentinel命令的实例ID不等于*号
if (ri &amp;&amp; ri-&gt;flags &amp; SRI_MASTER &amp;&amp; strcasecmp(c-&gt;argv[5]-&gt;ptr,"*")) {
&nbsp;&nbsp; //调用sentinelVoteLeader进行哨兵Leader选举
&nbsp;&nbsp; leader = sentinelVoteLeader(ri,(uint64_t)req_epoch, c-&gt;argv[5]-&gt;ptr,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&amp;leader_epoch);
}
</code></pre><p>下面，我们来具体了解下这个sentinelVoteLeader函数。</p><h3>sentinelVoteLeader函数</h3><p>sentinelVoteLeader函数会实际执行投票逻辑，这里我通过一个例子来给你说明。</p><p></p><p>假设哨兵A判断主节点master客观下线了，它现在向哨兵B发起投票请求，哨兵A的ID是req_runid。那么哨兵B在执行sentinelVoteLeader函数时，这个函数会判断哨兵A的纪元（req_epoch）、哨兵B的纪元（sentinel.current_epoch），以及master记录的Leader的纪元（master-&gt;leader_epoch）。按照Raft协议的定义，哨兵A就是Candidate节点，而哨兵B就是Follower节点。</p><p></p><p>我在上节课给你介绍Raft协议时有提到过，Candidate发起投票都是有轮次记录的，Follower在一轮投票中只能投一票。这里的纪元正是起到了<strong>轮次记录</strong>的作用。而sentinelVoteLeader函数判断纪元也是按照Raft协议的要求，让Follower在一轮中只能投一票。</p><p></p><p>那么，<strong>sentinelVoteLeader函数让哨兵B投票的条件是</strong>：master记录的Leader的纪元小于哨兵A的纪元，同时，哨兵A的纪元要大于或等于哨兵B的纪元。这两个条件保证了哨兵B还没有投过票，否则的话，sentinelVoteLeader函数就直接返回当前master中记录的Leader ID了，这也是哨兵B之前投过票后记录下来的。</p><p></p><p>下面的代码展示了刚才介绍的这部分逻辑，你可以看下。</p><pre><code class="language-plain">if (req_epoch &gt; sentinel.current_epoch) {
&nbsp;&nbsp; sentinel.current_epoch = req_epoch;
&nbsp;&nbsp; …
&nbsp;&nbsp; sentinelEvent(LL_WARNING,"+new-epoch",master,"%llu",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (unsigned long long) sentinel.current_epoch);
}
&nbsp;
if (master-&gt;leader_epoch &lt; req_epoch &amp;&amp; sentinel.current_epoch &lt;= req_epoch)
{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sdsfree(master-&gt;leader);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; master-&gt;leader = sdsnew(req_runid);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; master-&gt;leader_epoch = sentinel.current_epoch;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; …
}
return master-&gt;leader ? sdsnew(master-&gt;leader) : NULL;
</code></pre><p>那么现在，你就了解了sentinelVoteLeader函数是如何使用纪元判断来按照Raft协议完成哨兵Leader选举的了。</p><p>接下来，发起投票的哨兵仍然是通过sentinelReceiveIsMasterDownReply函数来处理其他哨兵对Leader投票的返回结果。这个返回结果，就像刚才给你介绍的，它的第二、三部分内容是哨兵Leader的ID，和哨兵Leader所属的纪元。发起投票的哨兵就可以从这个结果中获得其他哨兵对Leader的投票结果了。</p><p>最后，发起投票的哨兵在调用了sentinelAskMasterStateToOtherSentinels函数让其他哨兵投票后，会执行sentinelFailoverStateMachine函数。</p><p>如果主节点开始执行故障切换了，那么，主节点的failover_state，会被设置成SENTINEL_FAILOVER_STATE_WAIT_START。在这种状态下，sentinelFailoverStateMachine函数会调用sentinelFailoverWaitStart函数。而sentinelFailoverWaitStart函数，又会调用sentinelGetLeader函数，来判断发起投票的哨兵是否为哨兵Leader。发起投票的哨兵要想成为Leader，必须满足两个条件：</p><ul>
<li>一是，获得超过半数的其他哨兵的赞成票</li>
<li>二是，获得超过预设的quorum阈值的赞成票数。</li>
</ul><p>这两个条件，也可以从sentinelGetLeader函数中的代码片段看到，如下所示。</p><pre><code class="language-plain">//voters是所有哨兵的个数，max_votes是获得的票数
&nbsp;voters_quorum = voters/2+1;  //赞成票的数量必须是超过半数以上的哨兵个数
//如果赞成票数不到半数的哨兵个数或者少于quorum阈值，那么Leader就为NULL
&nbsp;if (winner &amp;&amp; (max_votes &lt; voters_quorum || max_votes &lt; master-&gt;quorum))
&nbsp; &nbsp; &nbsp; &nbsp; winner = NULL;
//确定最终的Leader
winner = winner ? sdsnew(winner) : NULL;
</code></pre><p>下图就展示了刚才介绍的确认哨兵Leader时的调用关系，你可以看下。</p><p><img src="https://static001.geekbang.org/resource/image/19/52/192b72d0cf77cfefee8e26952b4f1652.jpg?wh=1920x839" alt="图片"></p><p>好了，到这里，最终的哨兵Leader就能被确定了。</p><p></p><h2>小结</h2><p>好了，今天这节课的内容就到这里，我们来小结下。</p><p></p><p>今天这节课，我在上节课的基础上，重点给你介绍了哨兵工作过程中的客观下线判断，以及Leader选举。因为这个过程涉及哨兵之间的交互询问，所以并不容易掌握，你需要好好关注以下我提到的重点内容。</p><p></p><p>首先，客观下线的判断涉及三个标记的判断，分别是主节点flags中的SRI_S_DOWN和SRI_O_DOWN，以及哨兵实例flags中的SRI_MASTER_DOWN，我画了下面这张表，展示了这三个标记的设置函数和条件，你可以再整体回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/73/1f/738ea2375d2e302bb6742fa825650b1f.jpg?wh=1920x1027" alt="图片"></p><p>而一旦哨兵判断主节点客观下线了，那么哨兵就会<strong>调用sentinelAskMasterStateToOtherSentinels函数进行哨兵Leader选举</strong>。这里，你需要注意的是，向其他哨兵询问主节点主观下线状态，以及向其他哨兵发起Leader投票，都是通过sentinel is-master-down-by-addr命令实现的，而Redis源码是用了同一个函数sentinelAskMasterStateToOtherSentinels来发送该命令，所以你在阅读源码时，<strong>要注意区分sentinelAskMasterStateToOtherSentinels发送的命令是查询主节点主观下线状态还是进行投票</strong>。</p><p></p><p>最后，哨兵Leader选举的投票是在sentinelVoteLeader函数中完成的，为了符合Raft协议的规定，sentinelVoteLeader函数在执行时主要是要比较哨兵的纪元，以及master记录的Leader纪元，这样才能满足Raft协议对Follower在一轮投票中只能投一票的要求。</p><p>好了，到今天这节课，我们就了解了哨兵Leader选举的过程，你可以看到，虽然哨兵选举的最后执行逻辑就是在一个函数中，但是哨兵选举的触发逻辑是包含在了哨兵的整个工作过程中的，所以我们也需要掌握这个过程中的其他操作，比如主观下线判断、客观下线判断等。</p><p></p><h2>每课一问</h2><p>哨兵在sentinelTimer函数中调用sentinelHandleDictOfRedisInstances函数，对每个主节点都执行sentinelHandleRedisInstance函数，并且还会对主节点的所有从节点也执行sentinelHandleRedisInstance函数，那么，哨兵会判断从节点的主观下线和客观下线吗？</p>