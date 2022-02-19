<audio title="27 _ 从MOVED、ASK看集群节点如何处理命令？" src="https://static001.geekbang.org/resource/audio/ed/52/eda0ba8875c5c6d5299ca9da3e30ee52.mp3" controls="controls"></audio> 
<p>你好，我是蒋德钧。</p><p></p><p>在上节课一开始我给你介绍了，我们在Redis Cluster这个模块中会学习三部分内容：节点间如何传递信息和运行状态、节点如何处理命令，以及数据如何在节点间迁移。那么通过上节课的学习，现在我们已经了解了Gossip协议的基本实现，也就是支持集群节点间信息和运行状态传递的数据结构、关键函数设计与实现。</p><p>所以在今天这节课，我们就来了解下集群命令处理的实现。这部分内容不仅包括了集群节点处理一个命令的基本流程，更重要的是，我们可以掌握集群特定命令MOVED、ASK是如何实现的。这两个命令对应了Redis Cluster中请求重定向的处理场景，了解了这部分内容之后，我们就可以参考Redis Cluster，来设计和实现分布式系统中的请求重定向。</p><p></p><p>接下来，我们先来看下集群节点处理一个命令的基本流程，这可以让我们对集群节点的实现有个整体观。</p><p></p><h2>集群节点处理命令的基本流程</h2><p>我在<a href="https://time.geekbang.org/column/article/411558">第14讲</a>中提到过，Redis server处理一条命令的过程可以分成四个阶段，分别是<strong>命令读取、命令解析、命令执行和结果返回</strong>。而和单个Redis server一样，Redis Cluster中的节点，也是按照相同的阶段来处理命令的。</p><p>因此，集群节点在各阶段处理命令的入口函数和单个Redis server也是一样的，如下图所示。你也可以再去回顾下第14讲中，我介绍的命令处理详细流程。</p><!-- [[[read_end]]] --><p><img src="https://static001.geekbang.org/resource/image/53/b6/53b6b983f429fa7d298546dbc217d9b6.jpg?wh=1920x1080" alt="图片"></p><p>但是，在其中的命令执行阶段，如果Redis server是一个集群节点，那么在命令执行的过程中，就会增加额外的处理流程，而这个流程正对应了Redis Cluster中可能遇到的请求重定向问题。</p><p></p><p>这里所说的<strong>请求重定向</strong>，是指客户端给一个集群节点发送命令后，节点发现客户端请求的数据并不在本地。因此，节点需要让客户端的请求，重新定向发给实际拥有数据的节点，这样客户端的命令才能正常执行。</p><p></p><p>而你需要注意，请求重定向其实是分布式系统设计过程中需要面对的一个常见问题。尤其对于像Redis Cluster这样，没有使用中心化的第三方系统来维护数据分布的分布式系统来说，<strong>当集群由于负载均衡或是节点故障而导致数据迁移时，请求重定向是不可避免的</strong>。所以，了解这个设计环节，对于你开发分布式系统同样具有重要的参考价值。</p><p></p><p>那么，下面我们就先来看下在命令执行阶段中，针对集群节点增加的处理流程，这是在processCommand函数（在server.c文件）中实现的。</p><p></p><p>processCommand函数在执行过程中，会判断当前节点是否处于集群模式，这是通过全局变量server的<strong>cluster_enable标记</strong>来判断的。如果当前节点处于集群模式，processCommand函数会判断是否需要执行重定向。</p><p></p><p>当然，如果当前节点收到的命令来自于它在集群中的主节点，或者它收到的命令并没有带key参数，那么在这些情况下，集群节点并不会涉及重定向请求的操作。不过，这里有一个不带key参数的命令是一个例外，就是<strong>EXEC命令</strong>。如果当前节点收到EXEC命令，processCommand函数仍然会判断是否要进行请求重定向。</p><p></p><p>那么，processCommand函数具体是如何判断是否要执行请求重定向的呢？</p><p></p><p>其实，它是调用了<strong>getNodeByQuery函数</strong>（在<a href="https://github.com/redis/redis/tree/5.0/src/cluster.c">cluster.c</a>文件中），来查询当前收到的命令能在哪个集群节点上进行处理。如果getNodeByQuery函数返回的结果是空，或者查询到的集群节点不是当前节点，那么，processCommand函数就会调用clusterRedirectClient函数（在cluster.c文件中），来实际执行请求重定向。</p><p></p><p>下面的代码展示了集群节点处理命令过程中针对请求重定向增加的流程，你可以看下。</p><pre><code class="language-plain">int processCommand(client *c) {
&nbsp;&nbsp; …
&nbsp;&nbsp; //当前Redis server启用了Redis Cluster模式；收到的命令不是来自于当前借的主节点；收到的命令包含了key参数，或者命令是EXEC
&nbsp;&nbsp; if (server.cluster_enabled &amp;&amp; !(c-&gt;flags &amp; CLIENT_MASTER)
	&amp;&amp; !(c-&gt;flags &amp; CLIENT_LUA &amp;&amp; server.lua_caller-&gt;flags &amp; CLIENT_MASTER)
	&amp;&amp; !(c-&gt;cmd-&gt;getkeys_proc == NULL &amp;&amp; c-&gt;cmd-&gt;firstkey == 0 &amp;&amp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; c-&gt;cmd-&gt;proc != execCommand))
	{
	&nbsp;&nbsp; …
	&nbsp;&nbsp; clusterNode *n = getNodeByQuery(c,c-&gt;cmd,c-&gt;argv,c-&gt;argc, &amp;hashslot,&amp;error_code); //查询当前命令可以被哪个集群节点处理
	&nbsp;&nbsp; if (n == NULL || n != server.cluster-&gt;myself) {
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; …
	&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;clusterRedirectClient(c,n,hashslot,error_code); //实际执行请求重定向
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return C_OK;
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }
	&nbsp;&nbsp;&nbsp; }
</code></pre><p>当然，如果不需要执行请求重定向，那么processCommand函数会继续执行后续的流程，并调用call函数实际运行命令。</p><p>下图展示了processCommand函数针对集群节点增加的基本执行逻辑，你可以再回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/91/7d/91ce0579f5465806b6ed2c95b749c67d.jpg?wh=1920x1080" alt="图片"></p><p></p><p>好，接下来，我们就来看下getNodeByQuery函数是如何查询能处理一条命令的集群节点的。</p><p></p><h2>如何查询能运行命令的集群节点？</h2><p>首先，我们来看下getNodeByQuery函数的原型，如下所示：</p><pre><code class="language-plain">clusterNode *getNodeByQuery(client *c, struct redisCommand *cmd, robj **argv, int argc, int *hashslot, int *error_code)
</code></pre><p>它的函数参数包括了节点收到的命令及参数。同时，它的参数中还包括了两个指针：hashslot和error_code，这两个指针分别表示命令访问的key所在的slot（哈希槽），以及函数执行后的错误代码。此外，getNodeByQuery函数的返回值是clusterNode类型，表示的是能处理命令的集群节点。</p><p></p><p>然后，我们来看下getNodeByQuery函数的具体执行过程，这个过程基本可以分成三个步骤来完成。</p><p></p><h3>第一步，使用multiState结构体封装收到的命令</h3><p></p><p>因为集群节点可能收到<strong>MULTI命令</strong>，而MULTI命令表示紧接着它的多条命令是需要作为一个事务来执行的。当Redis server收到客户端发送的MULTI命令后，它会调用MULTI命令的处理函数multiCommand（在<a href="https://github.com/redis/redis/tree/5.0/src/multi.c">multi.c</a>文件中），在表示客户端的结构体变量client中设置<strong>CLIENT_MULTI标记</strong>，如下所示：</p><pre><code class="language-plain">void multiCommand(client *c) {
&nbsp;&nbsp; …
&nbsp;&nbsp; c-&gt;flags |= CLIENT_MULTI; //在客户端的标记中设置CLIENT_MULTI
&nbsp;&nbsp; addReply(c,shared.ok);
}
</code></pre><p>而在刚才介绍的命令执行函数processCommand中，它在处理命令时，会判断客户端变量client中是否有CLIENT_MULTI标记。如果有的话，processCommand会调用<strong>queueMultiCommand函数</strong>，把后续收到的命令缓存在client结构体的mstate成员变量中。mstate成员变量的类型是<strong>multiState结构体</strong>，它记录了MULTI命令后的其他命令以及命令个数。</p><p></p><p>下面的代码展示了processCommand函数对CLIENT_MULTI标记的处理，你可以看下。你也可以进一步阅读queueMultiCommand函数（在multi.c文件中）和client结构体（在<a href="https://github.com/redis/redis/tree/5.0/src/server.h">server.h</a>文件中），详细了解MULTI后续命令的记录过程。</p><pre><code class="language-plain">int processCommand(client *c) {
…
//客户端有CLIENT_MULTI标记，同时当前命令不是EXEC，DISCARD, MULTI和WATCH
if (c-&gt;flags &amp; CLIENT_MULTI &amp;&amp;
&nbsp; c-&gt;cmd-&gt;proc != execCommand &amp;&amp; c-&gt;cmd-&gt;proc != discardCommand &amp;&amp;
&nbsp; c-&gt;cmd-&gt;proc != multiCommand &amp;&amp; c-&gt;cmd-&gt;proc != watchCommand)
&nbsp; {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; queueMultiCommand(c); //缓存命令
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; …
&nbsp; }
</code></pre><p>其实，刚才介绍的Redis server处理MULTI命令和缓存后续命令的流程，<strong>对于集群节点来说，也是同样适用的</strong>。也就是对于getNodeByQuery函数来说，它在查询命令访问的key时，就需要考虑MULTI命令的情况。</p><p>那么，为了使用同样的数据结构，来处理MULTI命令的后续命令和常规的单条命令，getNodeByQuery函数就使用了multiState结构体，来封装当前要查询的命令，如下所示：</p><pre><code class="language-plain">multiState *ms, _ms; //使用multiState结构体封装要查询的命令
…
if (cmd-&gt;proc == execCommand) { //如果收到EXEC命令，那么就要检查MULTI后续命令访问的key情况，所以从客户端变量c中获取mstate
&nbsp;&nbsp; …
&nbsp;&nbsp; ms = &amp;c-&gt;mstate;
} else {
&nbsp;&nbsp; ms = &amp;_ms;&nbsp; //如果是其他命令，那么也使用multiState结构体封装命令
&nbsp;&nbsp; _ms.commands = &amp;mc;
&nbsp;&nbsp; _ms.count = 1;&nbsp; //封装的命令个数为1
&nbsp;&nbsp; mc.argv = argv; //命令的参数
&nbsp;&nbsp; mc.argc = argc; //命令的参数个数
&nbsp;&nbsp; mc.cmd = cmd; //命令本身
}
</code></pre><p>这里你需要<strong>注意</strong>，MULTI命令后缓存的其他命令并不会立即执行，而是需要等到EXEC命令执行时才会执行。所以，在刚才的代码中，getNodeByQuery函数也是在收到EXEC命令时，才会从客户端变量c中获取缓存的命令mstate。</p><p>好了，到这里，你就可以看到，getNodeByQuery函数使用multiState结构体，封装了当前的命令。而接下来，它就会检查命令访问的key了。</p><p></p><h3>第二步，针对收到的每个命令，逐一检查这些命令访问的key所在的slots</h3><p></p><p>getNodeByQuery函数会根据multiState结构中记录的命令条数，执行一个循环，逐一检查每条命令访问的key。具体来说，它会调用<strong>getKeysFromCommand函数</strong>（在<a href="https://github.com/redis/redis/tree/5.0/src/db.c">db.c</a>文件中）获取命令中的key位置和key个数。</p><p></p><p>然后，它会针对每个key，调用<strong>keyHashSlot函数</strong>（在cluster.c文件中）查询这个key所在的slot，并在全局变量server的cluster成员变量中，查找这个slot所属的集群节点，如下所示：</p><p></p><pre><code class="language-plain">for (i = 0; i &lt; ms-&gt;count; i++) {
&nbsp;&nbsp; …
&nbsp;&nbsp; //获取命令中的key位置和key个数
&nbsp;&nbsp; keyindex = getKeysFromCommand(mcmd,margv,margc,&amp;numkeys);
   //针对每个key执行
&nbsp;&nbsp; for (j = 0; j &lt; numkeys; j++) {
	…
	int thisslot = keyHashSlot((char*)thiskey-&gt;ptr, //获取key所属的slot&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sdslen(thiskey-&gt;ptr));
	if (firstkey == NULL) {
	&nbsp;&nbsp; …
	&nbsp;&nbsp; slot = thisslot;
	&nbsp;&nbsp; n = server.cluster-&gt;slots[slot]; //查找key所属的slot对应的集群节点
	}
	…
&nbsp;&nbsp;&nbsp; }
}
</code></pre><p>紧接着，getNodeByQuery函数会根据查找的集群节点结果进行判断，主要有以下三种情况。</p><p></p><ul>
<li>情况一：查找的集群节点为空，此时它会报错，将error_code设置为CLUSTER_REDIR_DOWN_UNBOUND。</li>
</ul><pre><code class="language-plain">if (n == NULL) {
&nbsp;&nbsp; …
&nbsp;&nbsp;&nbsp; if (error_code)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *error_code = CLUSTER_REDIR_DOWN_UNBOUND;
&nbsp;&nbsp;&nbsp; return NULL;
}
</code></pre><ul>
<li>情况二：查找的集群节点就是当前节点，而key所属的slot正在<strong>做数据迁出操作</strong>，此时，getNodeByQuery函数会设置变量migrating_slot为1，表示正在做数据迁出。</li>
</ul><p></p><ul>
<li>情况三：key所属的slot正在<strong>做数据迁入操作</strong>，此时，getNodeByQuery函数会设置变量importing_slot为1，表示正在做数据迁入。</li>
</ul><p>情况二和三的代码逻辑如下所示：</p><pre><code class="language-plain">//如果key所属的slot正在迁出，则设置migrating_slot为1
if (n == myself &amp;&amp; server.cluster-&gt;migrating_slots_to[slot] != NULL)
{
   migrating_slot = 1;
} //如果key所属的slot正在迁入，则设置importing_slot为1
else if (server.cluster-&gt;importing_slots_from[slot] != NULL) {
&nbsp;&nbsp;&nbsp;importing_slot = 1;
}
</code></pre><p>这里，你需要注意的是，如果命令包含的key不止1个，而且这些keys不在同一个slot，那么getNodeByQuery函数也会报错，并把error_code设置为CLUSTER_REDIR_CROSS_SLOT。</p><p>到这里，getNodeByQuery函数就查找到了命令访问的key所在的slot，以及对应的集群节点。而此时，如果节点正在做数据迁出或迁入，那么，getNodeByQuery函数就会调用<strong>lookupKeyRead函数</strong>（在db.c文件中），检查命令访问的key是否在当前节点的数据库中。如果没有的话，它会用一个变量<strong>missing_keys</strong>，记录缺失的key数量，如下所示：</p><pre><code class="language-plain">//如果key所属slot正在迁出或迁入，并且当前访问的key不在本地数据库，那么增加missing_keys的大小
if ((migrating_slot || importing_slot) &amp;&amp; lookupKeyRead(&amp;server.db[0],thiskey) == NULL)
{
&nbsp;   missing_keys++;
}
</code></pre><p>接下来，getNodeByQuery函数就会根据slot的检查情况来返回相应的结果了。</p><h3>第三步，根据slot的检查结果返回hashslot、error_code和相应的集群节点</h3><p>在getNodeByQuery函数的返回结果中，我们可以重点关注以下四种情况。</p><p><strong>情况一</strong>：命令访问key所属的slot没有对应的集群节点，此时，getNodeByQuery函数会返回当前节点。在这种情况下，有可能是集群有故障导致无法查找到slot所对应的节点，而error_code中会有相应的报错信息。</p><pre><code class="language-plain">if (n == NULL) return myself;
</code></pre><p><strong>情况二</strong>：命令访问key所属的slot正在做数据迁出或迁入，而且当前命令就是用来执行数据迁移的MIGRATE命令，那么，getNodeByQuery函数会返回当前节点，如下所示：</p><pre><code class="language-plain">if ((migrating_slot || importing_slot) &amp;&amp; cmd-&gt;proc == migrateCommand)
   return myself;
</code></pre><p><strong>情况三</strong>：命令访问key所属的slot正在做数据迁出，并且命令访问的key在当前节点数据库中缺失了，也就是刚才介绍的missing_keys大于0。此时，getNodeByQuery函数会把error_code设置为CLUSTER_REDIR_ASK，并返回数据迁出的目标节点。</p><pre><code class="language-plain">&nbsp;if (migrating_slot &amp;&amp; missing_keys) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (error_code) *error_code = CLUSTER_REDIR_ASK;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return server.cluster-&gt;migrating_slots_to[slot];
	}
</code></pre><p><strong>情况四</strong>：命令访问key所属的slot对应的节点不是当前节点，而是其他节点，此时，getNodeByQuery函数会把error_code设置为CLUSTER_REDIR_MOVED，并返回key所属slot对应的实际节点。</p><pre><code class="language-plain">if (n != myself &amp;&amp; error_code) *error_code = CLUSTER_REDIR_MOVED;
&nbsp;&nbsp;&nbsp; return n;
</code></pre><p>好了，到这里，我们就了解了getNodeByQuery函数对命令访问key的查询过程了。我画了张图，展示了getNodeByQuery函数基本执行过程，你可以再回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/72/65/727022d24a5f15d2fc2f8fa65dbda565.jpg?wh=1920x1080" alt="图片"></p><p>那么，有了key所属节点的查询结果后，processCommand函数接下来又会如何进行请求重定向呢?</p><p></p><p>实际上，这一步是通过执行请求重定向的函数<strong>clusterRedirectClient</strong>来完成的。</p><h2>请求重定向函数clusterRedirectClient的执行</h2><p>当getNodeByQuery函数查到的集群节点为空或者不是当前节点时，clusterRedirectClient函数就会被调用。</p><p>而clusterRedirectClient函数的逻辑比较简单，它就是<strong>根据getNodeByQuery函数返回的error_code的不同值，执行相应的代码分支</strong>，主要是把key所属slot对应集群节点的情况返回给客户端，从而让客户端根据返回的信息作出相应处理。比如：</p><ul>
<li>当error_code被设置成<strong>CLUSTER_REDIR_CROSS_SLOT</strong>时，clusterRedirectClient函数就返回给客户端“key不在同一个slot中”的报错信息；</li>
<li>当error_code被设置成<strong>CLUSTER_REDIR_MOVED</strong>时，clusterRedirectClient函数会返回MOVED命令，并把key所属的slot、slot实际所属的节点IP和端口号，返回给客户端；</li>
<li>当error_code被设置成<strong>CLUSTER_REDIR_ASK</strong>时，clusterRedirectClient函数会返回ASK命令，并把key所属的slot、slot正在迁往的目标节点IP和端口号，返回给客户端。</li>
</ul><p></p><p>下面的代码展示了刚才介绍的clusterRedirectClient函数对三种error_code的处理，你可以看下。</p><pre><code class="language-plain">void clusterRedirectClient(client *c, clusterNode *n, int hashslot, int error_code) {
if (error_code == CLUSTER_REDIR_CROSS_SLOT) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; addReplySds(c,sdsnew("-CROSSSLOT Keys in request don't hash to the same slot\r\n"));
}
…
else if (error_code == CLUSTER_REDIR_MOVED || error_code == CLUSTER_REDIR_ASK)
&nbsp;&nbsp;&nbsp; {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; addReplySds(c,sdscatprintf(sdsempty(),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "-%s %d %s:%d\r\n",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(error_code == CLUSTER_REDIR_ASK) ? "ASK" : "MOVED",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; hashslot,n-&gt;ip,n-&gt;port));
	}
	…
}
</code></pre><p>这样，集群节点处理收到的命令的过程就结束了。</p><p>最后，我还想提醒你注意一点，就是Redis Cluster的客户端和针对单个Redis server的客户端，在实现上是有差别的。Redis Cluster客户端需要能处理节点返回的报错信息，比如说，如果集群节点返回MOVED命令，客户端就需要根据这个命令，以及其中包含的实际节点IP和端口号，来访问实际有数据的节点。</p><p></p><h2>小结</h2><p>今天这节课，我给你介绍了集群节点对客户端命令的处理过程。和单个Redis server处理命令的过程相似，集群节点也会经历命令读取、解析、执行和返回结果四个阶段，并且集群节点也使用了和单Redis server相同的入口处理函数。</p><p></p><p>不过你要知道的是，Redis Cluster会因为负载均衡或节点故障等原因而执行数据迁移，而这就会导致客户端访问的key并不在接收到命令的集群节点上。因此，集群节点在命令执行函数processCommand中，针对集群模式，就增加了额外的处理逻辑。这主要是包括调用<strong>getNodeByQuery函数</strong>查询访问的key实际所属的节点，以及根据查询结果调用<strong>clusterRedirectClient函数</strong>执行请求重定向。</p><p></p><p>事实上，对于分布式集群来说，Redis Cluster设计实现的请求重定向机制是一个不错的参考示例。其中，MOVED和ASK两种重定向情况，就充分考虑了数据正在迁移的场景，这种设计值得我们学习。而且，getNodeByQuery函数在查询key所属的slot和节点时，也充分考虑了Redis的事务操作，在对命令访问key进行查询时，巧妙地使用了<strong>同一个数据结构multiState</strong>，来封装事务涉及的多条命令和常规的单条命令，增加了代码的复用程度，这一点也非常值得学习。</p><p></p><p>当然，在这节课里我们也多次提到了数据迁移，那么在下节课，我就会给你介绍Redis Cluster中数据迁移的具体实现。</p><p></p><p></p><h2>每课一问</h2><p>processCommand函数在调用完getNodeByQuery函数后，实际调用clusterRedirectClient函数进行请求重定向前，会根据当前命令是否是EXEC，分别调用discardTransaction和flagTransaction两个函数。那么，你能通过阅读源码，知道这里调用discardTransaction和flagTransaction的目的是什么吗?</p><pre><code class="language-plain">int processCommand(client *c) {
…
clusterNode *n = getNodeByQuery(c,c-&gt;cmd,c-&gt;argv,c-&gt;argc,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;hashslot,&amp;error_code);
if (n == NULL || n != server.cluster-&gt;myself) {
&nbsp;&nbsp; if (c-&gt;cmd-&gt;proc == execCommand) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; discardTransaction(c);
&nbsp;&nbsp; } else {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; flagTransaction (c);
&nbsp;&nbsp; }
&nbsp;&nbsp; clusterRedirectClient(c,n,hashslot,error_code);
&nbsp;&nbsp; return C_OK;
	}
	…
	}
</code></pre>