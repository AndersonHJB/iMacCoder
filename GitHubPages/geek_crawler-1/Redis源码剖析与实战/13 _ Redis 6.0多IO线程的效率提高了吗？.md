<audio title="13 _ Redis 6.0多IO线程的效率提高了吗？" src="https://static001.geekbang.org/resource/audio/aa/9c/aa9a5706579ea73bfe40daf4e613d09c.mp3" controls="controls"></audio> 
<p>你好，我是蒋德钧。</p><p>通过上节课的学习，我们知道Redis server启动后的进程会以单线程的方式，执行客户端请求解析和处理工作。但是，Redis server也会通过bioInit函数启动三个后台线程，来处理后台任务。也就是说，Redis不再让主线程执行一些耗时操作，比如同步写、删除等，而是交给后台线程异步完成，从而避免了对主线程的阻塞。</p><p>实际上，在2020年5月推出的Redis 6.0版本中，Redis在执行模型中还进一步使用了多线程来处理IO任务，这样设计的目的，就是为了充分利用当前服务器的多核特性，使用多核运行多线程，让多线程帮助加速数据读取、命令解析以及数据写回的速度，提升Redis整体性能。</p><p><strong>那么，这些多线程具体是在什么时候启动，又是通过什么方式来处理IO请求的呢？</strong></p><p>今天这节课，我就来给你介绍下Redis 6.0实现的多IO线程机制。通过这部分内容的学习，你可以充分了解到Redis 6.0是如何通过多线程来提升IO请求处理效率的。这样你也就可以结合实际业务来评估，自己是否需要使用Redis 6.0了。</p><p>好，接下来，我们先来看下多IO线程的初始化。注意，因为我们之前课程中阅读的是Redis 5.0.8版本的代码，所以在开始学习今天的课程之前，你还需要下载<a href="https://github.com/redis/redis/tree/6.0">Redis 6.0.15</a>的源码，以便能查看到和多IO线程机制相关的代码。</p><!-- [[[read_end]]] --><h2>多IO线程的初始化</h2><p>我在上一讲给你介绍过，Redis 5.0中的三个后台线程，是server在初始化过程的最后，调用InitSeverLast函数，而InitServerLast函数再进一步调用bioInit函数来完成的。如果我们在Redis 6.0中查看InitServerLast函数，会发现和Redis 5.0相比，该函数在调完bioInit函数后，又调用了<strong>initThreadedIO函数</strong>。而initThreadedIO函数正是用来初始化多IO线程的，这部分的代码调用如下所示：</p><pre><code>void InitServerLast() {
    bioInit();
    initThreadedIO();  //调用initThreadedIO函数初始化IO线程
    set_jemalloc_bg_thread(server.jemalloc_bg_thread);
    server.initial_memory_usage = zmalloc_used_memory();
}
</code></pre><p>所以下面，我们就来看下initThreadedIO函数的主要执行流程，这个函数是在<a href="http://github.com/redis/redis/tree/5.0/src/networking.c">networking.c</a>文件中实现的。</p><p><strong>首先，initThreadedIO函数会设置IO线程的激活标志。</strong>这个激活标志保存在redisServer结构体类型的全局变量server当中，对应redisServer结构体的成员变量io_threads_active。initThreadedIO函数会把io_threads_active初始化为0，表示IO线程还没有被激活。这部分代码如下所示：</p><pre><code>void initThreadedIO(void) {
	server.io_threads_active = 0;
	…
}
</code></pre><p>这里，你要注意一下，刚才提到的<strong>全局变量server</strong>是Redis server运行时，用来保存各种全局信息的结构体变量。我在<a href="https://time.geekbang.org/column/article/406556">第8讲</a>给你介绍Redis server初始化过程的时候，提到过Redis server的各种参数初始化配置，都是保存在这个全局变量server中的。所以，当你在阅读Redis源码时，如果在某个函数中看到变量server，要知道其实就是这个全局变量。</p><p><strong>紧接着，initThreadedIO函数会对设置的IO线程数量进行判断。</strong>这个数量就是保存在全局变量server的成员变量io_threads_num中的。那么在这里，IO线程的数量判断会有三种结果。</p><p>第一种，如果IO线程数量为1，就表示只有1个主IO线程，initThreadedIO函数就直接返回了。此时，Redis server的IO线程和Redis 6.0之前的版本是相同的。</p><pre><code>if (server.io_threads_num == 1) return;
</code></pre><p>第二种，如果IO线程数量大于宏定义IO_THREADS_MAX_NUM（默认值为128），那么initThreadedIO函数会报错，并退出整个程序。</p><pre><code>if (server.io_threads_num &gt; IO_THREADS_MAX_NUM) {
        …  //报错日志记录
        exit(1);  //退出程序
 }
</code></pre><p>第三种，如果IO线程数量大于1，并且小于宏定义IO_THREADS_MAX_NUM，那么，initThreadedIO函数会执行一个循环流程，该流程的循环次数就是设置的IO线程数量。</p><p>如此一来，在该循环流程中，initThreadedIO函数就会给以下四个数组进行初始化操作。</p><ul>
<li><strong>io_threads_list数组</strong>：保存了每个IO线程要处理的客户端，将数组每个元素初始化为一个List类型的列表；</li>
<li><strong>io_threads_pending数组</strong>：保存等待每个IO线程处理的客户端个数；</li>
<li><strong>io_threads_mutex数组</strong>：保存线程互斥锁；</li>
<li><strong>io_threads数组</strong>：保存每个IO线程的描述符。</li>
</ul><p>这四个数组的定义都在networking.c文件中，如下所示：</p><pre><code>pthread_t io_threads[IO_THREADS_MAX_NUM];   //记录线程描述符的数组
pthread_mutex_t io_threads_mutex[IO_THREADS_MAX_NUM];  //记录线程互斥锁的数组
_Atomic unsigned long io_threads_pending[IO_THREADS_MAX_NUM];  //记录线程待处理的客户端个数
list *io_threads_list[IO_THREADS_MAX_NUM];  //记录线程对应处理的客户端
</code></pre><p>然后，在对这些数组进行初始化的同时，initThreadedIO函数还会根据IO线程数量，<strong>调用pthread_create函数创建相应数量的线程</strong>。我在上节课给你介绍过，pthread_create函数的参数包括创建线程要运行的函数和函数参数（*tidp、*attr、*start_routine、*arg）。</p><p>所以，对于initThreadedIO函数来说，它创建的线程要运行的函数是<strong>IOThreadMain</strong>，参数是当前创建线程的编号。不过要注意的是，这个编号是从1开始的，编号为0的线程其实是运行Redis server主流程的主IO线程。</p><p>以下代码就展示了initThreadedIO函数对数组的初始化，以及创建IO线程的过程，你可以看下。</p><pre><code>for (int i = 0; i &lt; server.io_threads_num; i++) {
 
        io_threads_list[i] = listCreate();
        if (i == 0) continue; //编号为0的线程是主IO线程
 
        pthread_t tid;
        pthread_mutex_init(&amp;io_threads_mutex[i],NULL);  //初始化io_threads_mutex数组
        io_threads_pending[i] = 0;   //初始化io_threads_pending数组
        pthread_mutex_lock(&amp;io_threads_mutex[i]);
        //调用pthread_create函数创建IO线程，线程运行函数为IOThreadMain
        if (pthread_create(&amp;tid,NULL,IOThreadMain,(void*)(long)i) != 0) {
            … //出错处理
        }
        io_threads[i] = tid;  //初始化io_threads数组，设置值为线程标识
    }
</code></pre><p>好了，现在我们再来看下，刚才介绍的IO线程启动后要运行的函数IOThreadMain。了解这个函数，可以帮助我们掌握IO线程实际做的工作。</p><h2>IO线程的运行函数IOThreadMain</h2><p>IOThreadMain函数也是在networking.c文件中定义的，它的主要执行逻辑是一个<strong>while(1)循环</strong>。在这个循环中，IOThreadMain函数会把io_threads_list数组中，每个IO线程对应的列表读取出来。</p><p>就像我在前面给你介绍的一样，io_threads_list数组中会针对每个IO线程，使用一个列表记录该线程要处理的客户端。所以，IOThreadMain函数就会从每个IO线程对应的列表中，进一步取出要处理的客户端，然后判断线程要执行的操作标记。这个操作标记是用变量io_threads_op表示的，它有两种取值。</p><ul>
<li><strong>io_threads_op的值为宏定义IO_THREADS_OP_WRITE</strong>：这表明该IO线程要做的是写操作，线程会调用writeToClient函数将数据写回客户端。</li>
<li><strong>io_threads_op的值为宏定义IO_THREADS_OP_READ</strong>：这表明该IO线程要做的是读操作，线程会调用readQueryFromClient函数从客户端读取数据。</li>
</ul><p>这部分的代码逻辑你可以看看下面的代码。</p><pre><code>void *IOThreadMain(void *myid) {
…
while(1) {
   listIter li;
   listNode *ln;
   //获取IO线程要处理的客户端列表
   listRewind(io_threads_list[id],&amp;li);
   while((ln = listNext(&amp;li))) {
      client *c = listNodeValue(ln); //从客户端列表中获取一个客户端
      if (io_threads_op == IO_THREADS_OP_WRITE) {
         writeToClient(c,0);  //如果线程操作是写操作，则调用writeToClient将数据写回客户端
       } else if (io_threads_op == IO_THREADS_OP_READ) {
          readQueryFromClient(c-&gt;conn); //如果线程操作是读操作，则调用readQueryFromClient从客户端读取数据
       } else {
          serverPanic(&quot;io_threads_op value is unknown&quot;);
       }
   }
   listEmpty(io_threads_list[id]); //处理完所有客户端后，清空该线程的客户端列表
   io_threads_pending[id] = 0; //将该线程的待处理任务数量设置为0
 
   }
}
</code></pre><p>我也画了下面这张图，展示了IOThreadMain函数的基本流程，你可以看下。</p><p><img src="https://static001.geekbang.org/resource/image/03/5a/03232ff01d8b0fca4af0981b7097495a.jpg?wh=2000x1125" alt=""></p><p>好了，到这里你应该就了解了，每一个IO线程运行时，都会不断检查是否有等待它处理的客户端。如果有，就根据操作类型，从客户端读取数据或是将数据写回客户端。你可以看到，这些操作都是Redis要和客户端完成的IO操作，所以，这也是为什么我们把这些线程称为IO线程的原因。</p><p>那么，你看到这里，可能也会产生一些疑问，<strong>IO线程要处理的客户端是如何添加到io_threads_list数组中的呢？</strong></p><p>这就要说到Redis server对应的全局变量server了。server变量中有两个List类型的成员变量：clients_pending_write和clients_pending_read，它们分别记录了待写回数据的客户端和待读取数据的客户端，如下所示：</p><pre><code>struct redisServer {
...
list *clients_pending_write;  //待写回数据的客户端
list *clients_pending_read;  //待读取数据的客户端
...
}
</code></pre><p>你要知道，Redis server在接收到客户端请求和给客户端返回数据的过程中，会根据一定条件，推迟客户端的读写操作，并分别把待读写的客户端保存到这两个列表中。然后，Redis server在每次进入事件循环前，会再把列表中的客户端添加到io_threads_list数组中，交给IO线程进行处理。</p><p>所以接下来，我们就先来看下，Redis是如何推迟客户端的读写操作，并把这些客户端添加到clients_pending_write和clients_pending_read这两个列表中的。</p><h2>如何推迟客户端读操作？</h2><p>Redis server在和一个客户端建立连接后，就会开始监听这个客户端上的可读事件，而处理可读事件的回调函数是<strong>readQueryFromClient</strong>。我在<a href="https://time.geekbang.org/column/article/408857">第11讲</a>中给你介绍了这个过程，你可以再去回顾下。</p><p>那么这里，我们再来看下Redis 6.0版本中的readQueryFromClient函数。这个函数一开始会先从传入参数conn中获取客户端c，紧接着就调用postponeClientRead函数，来判断是否推迟从客户端读取数据。这部分的执行逻辑如下所示：</p><pre><code>void readQueryFromClient(connection *conn) {
    client *c = connGetPrivateData(conn);  //从连接数据结构中获取客户
    ...
    if (postponeClientRead(c)) return;  //判断是否推迟从客户端读取数据
    ...
}
</code></pre><p>现在，我们就来看下<strong>postponeClientRead函数</strong>的执行逻辑。这个函数会根据四个条件判断能否推迟从客户端读取数据。</p><p><strong>条件一：全局变量server的io_threads_active值为1</strong></p><p>这表示多IO线程已经激活。我刚才说过，这个变量值在initThreadedIO函数中是会被初始化为0的，也就是说，多IO线程初始化后，默认还没有激活（我一会儿还会给你介绍这个变量值何时被设置为1）。</p><p><strong>条件二：全局变量server的io_threads_do_read值为1</strong></p><p>这表示多IO线程可以用于处理延后执行的客户端读操作。这个变量值是在Redis配置文件redis.conf中，通过配置项io-threads-do-reads设置的，默认值为no，也就是说，多IO线程机制默认并不会用于客户端读操作。所以，如果你想用多IO线程处理客户端读操作，就需要把io-threads-do-reads配置项设为yes。</p><p><strong>条件三：ProcessingEventsWhileBlocked变量值为0</strong></p><p>这表示processEventsWhileBlokced函数没有在执行。ProcessingEventsWhileBlocked是一个全局变量，它会在processEventsWhileBlokced函数执行时被设置为1，在processEventsWhileBlokced函数执行完成时被设置为0。</p><p>而processEventsWhileBlokced函数是在<a href="https://github.com/redis/redis/tree/5.0/src/networking.c">networking.c</a>文件中实现的。当Redis在读取RDB文件或是AOF文件时，这个函数会被调用，用来处理事件驱动框架捕获到的事件。这样就避免了因读取RDB或AOF文件造成Redis阻塞，而无法及时处理事件的情况。所以，当processEventsWhileBlokced函数执行处理客户端可读事件时，这些客户端读操作是不会被推迟执行的。</p><p><strong>条件四：客户端现有标识不能有CLIENT_MASTER、CLIENT_SLAVE和CLIENT_PENDING_READ</strong></p><p>其中，CLIENT_MASTER和CLIENT_SLAVE标识分别表示客户端是用于主从复制的客户端，也就是说，这些客户端不会推迟读操作。CLIENT_PENDING_READ本身就表示一个客户端已经被设置为推迟读操作了，所以，对于已带有CLIENT_PENDING_READ标识的客户端，postponeClientRead函数就不会再推迟它的读操作了。</p><p>总之，只有前面这四个条件都满足了，postponeClientRead函数才会推迟当前客户端的读操作。具体来说，postponeClientRead函数会给该客户端设置CLIENT_PENDING_REA标识，并调用listAddNodeHead函数，把这个客户端添加到全局变量server的clients_pending_read列表中。</p><p>我把postponeClientRead函数的代码放在这里，你可以看下。</p><pre><code>int postponeClientRead(client *c) {
    //判断IO线程是否激活，
    if (server.io_threads_active &amp;&amp; server.io_threads_do_reads &amp;&amp;          
         !ProcessingEventsWhileBlocked &amp;&amp;
        !(c-&gt;flags &amp; (CLIENT_MASTER|CLIENT_SLAVE|CLIENT_PENDING_READ)))
    {
        c-&gt;flags |= CLIENT_PENDING_READ; //给客户端的flag添加CLIENT_PENDING_READ标记，表示推迟该客户端的读操作
        listAddNodeHead(server.clients_pending_read,c); //将客户端添加到clients_pending_read列表中
        return 1;
    } else {
        return 0;
    }
}
</code></pre><p>好，现在你已经知道，Redis是在客户端读事件回调函数readQueryFromClient中，通过调用postponeClientRead函数来判断和推迟客户端读操作。下面，我再带你来看下Redis是如何推迟客户端写操作的。</p><h2>如何推迟客户端写操作？</h2><p>Redis在执行了客户端命令，要给客户端返回结果时，会调用<strong>addReply函数</strong>将待返回结果写入客户端输出缓冲区。</p><p>而在addReply函数的一开始，该函数会调用<strong>prepareClientToWrite函数</strong>，来判断是否推迟执行客户端写操作。下面代码展示了addReply函数对prepareClientToWrite函数的调用，你可以看下。</p><pre><code>void addReply(client *c, robj *obj) {
    if (prepareClientToWrite(c) != C_OK) return;
    ...
}
</code></pre><p>所以这里，我们继续来看下prepareClientToWrite函数。这个函数会根据客户端设置的标识进行一系列的判断。其中，该函数会调用<strong>clientHasPendingReplies函数</strong>，判断当前客户端是否还有留存在输出缓冲区中的数据等待写回。</p><p>如果没有的话，那么，prepareClientToWrite就会调用<strong>clientInstallWriteHandler函数</strong>，再进一步判断能否推迟该客户端写操作。下面的代码展示了这一调用过程，你可以看下。</p><pre><code>int prepareClientToWrite(client *c) {
   ...
   //如果当前客户端没有待写回数据，调用clientInstallWriteHandler函数
   if (!clientHasPendingReplies(c)) clientInstallWriteHandler(c);
   return C_OK;
}
</code></pre><p>那么这样一来，我们其实就知道了，能否推迟客户端写操作，最终是由clientInstallWriteHandler函数来决定的，这个函数会判断两个条件。</p><ul>
<li><strong>条件一</strong>：客户端没有设置过CLIENT_PENDING_WRITE标识，即没有被推迟过执行写操作。</li>
<li><strong>条件二</strong>：客户端所在实例没有进行主从复制，或者客户端所在实例是主从复制中的从节点，但全量复制的RDB文件已经传输完成，客户端可以接收请求。</li>
</ul><p>一旦这两个条件都满足了，clientInstallWriteHandler函数就会把客户端标识设置为CLIENT_PENDING_WRITE，表示推迟该客户端的写操作。同时，clientInstallWriteHandler函数会把这个客户端添加到全局变量server的待写回客户端列表中，也就是clients_pending_write列表中。</p><pre><code>void clientInstallWriteHandler(client *c) {
    //如果客户端没有设置过CLIENT_PENDING_WRITE标识，并且客户端没有在进行主从复制，或者客户端是主从复制中的从节点，已经能接收请求
    if (!(c-&gt;flags &amp; CLIENT_PENDING_WRITE) &amp;&amp;
        (c-&gt;replstate == REPL_STATE_NONE ||
         (c-&gt;replstate == SLAVE_STATE_ONLINE &amp;&amp; !c-&gt;repl_put_online_on_ack)))
    {
        //将客户端的标识设置为待写回，即CLIENT_PENDING_WRITE
        c-&gt;flags |= CLIENT_PENDING_WRITE;
        listAddNodeHead(server.clients_pending_write,c);  //将可获得加入clients_pending_write列表
    }
}
</code></pre><p>为了便于你更好地理解，我画了一张图，展示了Redis推迟客户端写操作的函数调用关系，你可以再回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/67/50/672977e056fba83aba183f82600c6d50.jpg?wh=2000x949" alt=""></p><p>不过，当Redis使用clients_pending_read和clients_pending_write两个列表，保存了推迟执行的客户端后，<strong>这些客户端又是如何分配给多IO线程执行的呢？</strong>这就和下面两个函数相关了。</p><ul>
<li>handleClientsWithPendingReadsUsingThreads函数：该函数主要负责将clients_pending_read列表中的客户端分配给IO线程进行处理。</li>
<li>handleClientsWithPendingWritesUsingThreads函数：该函数主要负责将clients_pending_write列表中的客户端分配给IO线程进行处理。</li>
</ul><p>所以接下来，我们就来看下这两个函数的具体操作。</p><h2>如何把待读客户端分配给IO线程执行？</h2><p>首先，我们来了解<strong>handleClientsWithPendingReadsUsingThreads函数</strong>。这个函数是在beforeSleep函数中调用的。</p><p>在Redis 6.0版本的代码中，事件驱动框架同样是调用aeMain函数来执行事件循环流程，该循环流程会调用aeProcessEvents函数处理各种事件。而在aeProcessEvents函数实际调用aeApiPoll函数捕获IO事件之前，beforeSleep函数会被调用。</p><p>这个过程如下图所示，你可以看下。</p><p><img src="https://static001.geekbang.org/resource/image/b8/87/b823cf93b7dcyy10069136c4a5c78787.jpg?wh=2000x969" alt=""></p><p>handleClientsWithPendingReadsUsingThreads函数的主要执行逻辑可以分成四步。</p><p><strong>第一步</strong>，该函数会先根据全局变量server的io_threads_active成员变量，判定IO线程是否激活，并且根据server的io_threads_do_reads成员变量，判定用户是否设置了Redis可以用IO线程处理待读客户端。只有在IO线程激活，并且IO线程可以用于处理待读客户端时，handleClientsWithPendingReadsUsingThreads函数才会继续执行，否则该函数就直接结束返回了。这一步的判断逻辑如以下代码所示：</p><pre><code>if (!server.io_threads_active || !server.io_threads_do_reads) 
return 0;
</code></pre><p><strong>第二步</strong>，handleClientsWithPendingReadsUsingThreads函数会获取clients_pending_read列表的长度，这代表了要处理的待读客户端个数。然后，该函数会从clients_pending_read列表中逐一取出待处理的客户端，并用客户端在列表中的序号，对IO线程数量进行取模运算。</p><p>这样一来，我们就可以根据取模得到的余数，把该客户端分配给对应的IO线程进行处理。紧接着，handleClientsWithPendingReadsUsingThreads函数会<strong>调用listAddNodeTail函数，把分配好的客户端添加到io_threads_list列表的相应元素中</strong>。我刚才给你介绍过，io_threads_list数组的每个元素是一个列表，对应保存了每个IO线程要处理的客户端。</p><p>为了便于你理解，我来给你举个例子。</p><p>假设IO线程数量设置为3，clients_pending_read列表中一共有5个待读客户端，它们在列表中的序号分别是0，1，2，3和4。在这一步中，0号到4号客户端对线程数量3取模的结果分别是0，1，2，0，1，这也对应了即将处理这些客户端的IO线程编号。这也就是说，0号客户端由0号线程处理，1号客户端有1号线程处理，以此类推。你可以看到，这个分配方式其实就是把待处理客户端，以<strong>轮询方式</strong>逐一分配给各个IO线程。</p><p>我画了下面这张图，展示了这个分配结果，你可以再看下。</p><p><img src="https://static001.geekbang.org/resource/image/3e/cc/3ea75f26c5c1fb527e4ec99fe07a4ccc.jpg?wh=2000x790" alt=""></p><p>以下代码展示的就是以轮询方式将客户端分配给IO线程的执行逻辑：</p><pre><code>int processed = listLength(server.clients_pending_read);
listRewind(server.clients_pending_read,&amp;li);
int item_id = 0;
while((ln = listNext(&amp;li))) {
        client *c = listNodeValue(ln);
        int target_id = item_id % server.io_threads_num;
        listAddNodeTail(io_threads_list[target_id],c);
        item_id++;
 }
</code></pre><p>这样，当handleClientsWithPendingReadsUsingThreads函数完成客户端的IO线程分配之后，它会将IO线程的操作标识设置为<strong>读操作</strong>，也就是IO_THREADS_OP_READ。然后，它会遍历io_threads_list数组中的每个元素列表长度，等待每个线程处理的客户端数量，赋值给 io_threads_pending数组。这一过程如下所示：</p><pre><code> io_threads_op = IO_THREADS_OP_READ;
 for (int j = 1; j &lt; server.io_threads_num; j++) {
        int count = listLength(io_threads_list[j]);
        io_threads_pending[j] = count;
 }
</code></pre><p><strong>第三步</strong>，handleClientsWithPendingReadsUsingThreads函数会将io_threads_list数组0号列表（也就是io_threads_list[0]元素）中的待读客户端逐一取出来，并调用readQueryFromClient函数进行处理。</p><p>其实，handleClientsWithPendingReadsUsingThreads函数本身就是由IO主线程执行的，而io_threads_list数组对应的0号线程正是IO主线程，所以，这里就是让主IO线程来处理它的待读客户端。</p><pre><code>  listRewind(io_threads_list[0],&amp;li);  //获取0号列表中的所有客户端
    while((ln = listNext(&amp;li))) {
        client *c = listNodeValue(ln);
        readQueryFromClient(c-&gt;conn);
    }
    listEmpty(io_threads_list[0]); //处理完后，清空0号列表
</code></pre><p>紧接着，handleClientsWithPendingReadsUsingThreads函数会执行一个while(1)循环，等待所有IO线程完成待读客户端的处理，如下所示：</p><pre><code> while(1) {
        unsigned long pending = 0;
        for (int j = 1; j &lt; server.io_threads_num; j++)
            pending += io_threads_pending[j];
        if (pending == 0) break;
    }
</code></pre><p><strong>第四步</strong>，handleClientsWithPendingReadsUsingThreads函数会再次遍历一遍clients_pending_read列表，依次取出其中的客户端。紧接着，它会判断客户端的标识中是否有CLIENT_PENDING_COMMAND。如果有CLIENT_PENDING_COMMAND标识，表明该客户端中的命令已经被某一个IO线程解析过，已经可以被执行了。</p><p>此时，handleClientsWithPendingReadsUsingThreads函数会调用processCommandAndResetClient函数执行命令。最后，它会直接调用processInputBuffer函数解析客户端中所有命令并执行。</p><p>这部分的代码逻辑如下所示，你可以看下。</p><pre><code>while(listLength(server.clients_pending_read)) {
        ln = listFirst(server.clients_pending_read);
        client *c = listNodeValue(ln);
        ...
        //如果命令已经解析过，则执行该命令
        if (c-&gt;flags &amp; CLIENT_PENDING_COMMAND) {
            c-&gt;flags &amp;= ~CLIENT_PENDING_COMMAND;
            if (processCommandAndResetClient(c) == C_ERR) {          
                continue;
            }
        }
        //解析并执行所有命令
        processInputBuffer(c);
}
</code></pre><p>好了，到这里，你就了解了clients_pending_read列表中的待读客户端，是如何经过以上四个步骤来分配给IO线程进行处理的。下图展示了这个主要过程，你可以再回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/1b/45/1b4bb7d5367d9184a9eacefbabfe3345.jpg?wh=2000x1125" alt=""></p><p>那么，接下来，我们再来看下待写客户端的分配和处理。</p><h2>如何把待写客户端分配给IO线程执行？</h2><p>和待读客户端的分配处理类似，待写客户端分配处理是由<strong>handleClientsWithPendingWritesUsingThreads函数</strong>来完成的。该函数也是在beforeSleep函数中被调用的。</p><p>handleClientsWithPendingWritesUsingThreads函数的主要流程同样也可以分成4步，其中，第2、3和4步的执行逻辑，和handleClientsWithPendingReadsUsingThreads函数类似。</p><p>简单来说，在第2步，handleClientsWithPendingWritesUsingThreads函数会把待写客户端，按照<strong>轮询方式</strong>分配给IO线程，添加到io_threads_list数组各元素中。</p><p>然后，在第3步，handleClientsWithPendingWritesUsingThreads函数会让主IO线程处理其待写客户端，并执行while(1)循环等待所有IO线程完成处理。</p><p>在第4步，handleClientsWithPendingWritesUsingThreads函数会再次检查clients_pending_write列表中，是否还有待写的客户端。如果有的话，并且这些客户端还有留存在缓冲区中的数据，那么，handleClientsWithPendingWritesUsingThreads函数就会调用connSetWriteHandler函数注册可写事件，而这个可写事件对应的回调函数是<strong>sendReplyToClient函数</strong>。</p><p>等到事件循环流程再次执行时，刚才handleClientsWithPendingWritesUsingThreads函数注册的可写事件就会被处理，紧接着sendReplyToClient函数会执行，它会直接调用writeToClient函数，把客户端缓冲区中的数据写回。</p><p>这里，<strong>你需要注意的是</strong>，connSetWriteHandler函数最终会映射为connSocketSetWriteHandler函数，而connSocketSetWriteHandler函数是在<a href="https://github.com/redis/redis/tree/5.0/src/connection.c">connection.c</a>文件中实现的。connSocketSetWriteHandler函数会调用aeCreateFileEvent函数创建AE_WRITABLE事件，这就是刚才介绍的可写事件的注册（关于aeCreateFileEvent函数的使用，你也可以再回顾下第11讲）。</p><p>不过，和handleClientsWithPendingReadsUsingThreads函数不同的是在第1步，handleClientsWithPendingWritesUsingThreads函数，<strong>会判断IO线程数量是否为1，或者待写客户端数量是否小于IO线程数量的2倍。</strong></p><p>如果这两个条件中有一个条件成立，那么handleClientsWithPendingWritesUsingThreads函数就不会用多线程来处理客户端了，而是会调用handleClientsWithPendingWrites函数由主IO线程直接处理待写客户端。这样做的目的，主要是为了在待写客户端数量不多时，避免采用多线程，从而<strong>节省CPU开销</strong>。</p><p>这一步的条件判断逻辑如下所示。其中，stopThreadedIOIfNeeded函数主要是用来判断待写客户端数量，是否不足为IO线程数量的2倍。</p><pre><code>if (server.io_threads_num == 1 || stopThreadedIOIfNeeded()) {
        return handleClientsWithPendingWrites();
}
</code></pre><p>另外，handleClientsWithPendingWritesUsingThreads函数在第1步中，还会<strong>判断IO线程是否已激活</strong>。如果没有激活，它就会调用startThreadedIO函数，把全局变量server的io_threads_active成员变量值设置为1，表示IO线程已激活。这步判断操作如下所示：</p><pre><code>if (!server.io_threads_active) startThreadedIO();
</code></pre><p>总之你要知道的就是，Redis是通过handleClientsWithPendingWritesUsingThreads函数，把待写客户端按轮询方式分配给各个IO线程，并由它们来负责写回数据的。</p><h2>小结</h2><p>今天这节课，我给你介绍了Redis 6.0中新设计实现的<strong>多IO线程机制</strong>。这个机制的设计主要是为了使用多个IO线程，来并发处理客户端读取数据、解析命令和写回数据。使用了多线程后，Redis就可以充分利用服务器的多核特性，从而<strong>提高IO效率</strong>。</p><p>总结来说，Redis 6.0先是在初始化过程中，根据用户设置的IO线程数量，创建对应数量的IO线程。</p><p>当Redis server初始化完成后正常运行时，它会在readQueryFromClient函数中通过调用postponeClientRead函数来决定是否推迟客户端读操作。同时，Redis server会在addReply函数中通过调用prepareClientToWrite函数，来决定是否推迟客户端写操作。而待读写的客户端会被分别加入到clients_pending_read和clients_pending_write两个列表中。</p><p>这样，每当Redis server要进入事件循环流程前，都会在beforeSleep函数中分别调用handleClientsWithPendingReadsUsingThreads函数和handleClientsWithPendingWritesUsingThreads函数，将待读写客户端<strong>以轮询方式分配给IO线程</strong>，加入到IO线程的待处理客户端列表io_threads_list中。</p><p>而IO线程一旦运行后，本身会一直检测io_threads_list中的客户端，如果有待读写客户端，IO线程就会调用readQueryFromClient或writeToClient函数来进行处理。</p><p>最后，我也想再提醒你一下，<strong>多IO线程本身并不会执行命令</strong>，它们只是利用多核并行地读取数据和解析命令，或是将server数据写回（下节课我还会结合分布式锁的原子性保证，来给你介绍这一部分的源码实现。）。所以，<strong>Redis执行命令的线程还是主IO线程</strong>。这一点对于你理解多IO线程机制很重要，可以避免你误解Redis有多线程同时执行命令。</p><p>这样一来，我们原来针对Redis 单个主IO线程做的优化仍然有效，比如避免bigkey、避免阻塞操作等。</p><h2>每课一问</h2><p>Redis 多IO线程机制使用startThreadedIO函数和stopThreadedIO函数，来设置IO线程激活标识io_threads_active为1和为0。此处，这两个函数还会对线程互斥锁数组进行解锁和加锁操作，如下所示。你知道为什么这两个函数要执行解锁和加锁操作么？</p><pre><code>void startThreadedIO(void) {
    ...
    for (int j = 1; j &lt; server.io_threads_num; j++)
        pthread_mutex_unlock(&amp;io_threads_mutex[j]);  //给互斥锁数组中每个线程对应的互斥锁做解锁操作
    server.io_threads_active = 1;
}

void stopThreadedIO(void) {
    ...
    for (int j = 1; j &lt; server.io_threads_num; j++)
        pthread_mutex_lock(&amp;io_threads_mutex[j]);  //给互斥锁数组中每个线程对应的互斥锁做加锁操作
    server.io_threads_active = 0;
}
</code></pre><p>欢迎在留言区分享你的答案和思考过程，如果觉得有收获，也欢迎你把今天的内容分享给更多的朋友。</p>