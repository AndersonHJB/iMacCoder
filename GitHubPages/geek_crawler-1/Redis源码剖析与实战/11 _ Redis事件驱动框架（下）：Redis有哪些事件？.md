<audio title="11 _ Redis事件驱动框架（下）：Redis有哪些事件？" src="https://static001.geekbang.org/resource/audio/58/a7/5819fb8c525da36915a0yycd2ffe75a7.mp3" controls="controls"></audio> 
<p>你好，我是蒋德钧。</p><p>在<a href="https://time.geekbang.org/column/article/407901">第9讲</a>中，我给你介绍了Linux提供的三种IO多路复用机制，分别是select、poll和epoll，这是Redis实现事件驱动框架的操作系统层支撑技术。</p><p>紧接着在上节课，我带你学习了Redis事件驱动框架的基本工作机制，其中介绍了事件驱动框架基于的Reactor模型，并以IO事件中的客户端连接事件为例，给你介绍了<strong>框架运行的基本流程</strong>：从server初始化时调用aeCreateFileEvent函数注册监听事件，到server初始化完成后调用aeMain函数，而aeMain函数循环执行aeProceeEvent函数，来捕获和处理客户端请求触发的事件。</p><p>但是在上节课当中，我们主要关注的是框架基本流程，所以到这里，你或许仍然存有一些疑问，比如说：</p><ul>
<li>Redis事件驱动框架监听的IO事件，除了上节课介绍的客户端连接以外，还有没有其他事件？而除了IO事件以外，框架还会监听其他事件么？</li>
<li>这些事件的创建和处理又分别对应了Redis源码中的哪些具体操作？</li>
</ul><p>今天这节课，我就来给你介绍下Redis事件驱动框架中的两大类事件类型：<strong>IO事件和时间事件，以及它们相应的处理机制。</strong></p><p>事实上，了解和学习这部分内容，一方面可以帮助我们更加全面地掌握，Redis事件驱动框架是如何以事件形式，处理server运行过程中面临的请求操作和多种任务的。比如，正常的客户端读写请求是以什么事件、由哪个函数进行处理，以及后台快照任务又是如何及时启动的。</p><!-- [[[read_end]]] --><p>因为事件驱动框架是Redis server运行后的核心循环流程，了解它何时用什么函数处理哪种事件，对我们排查server运行过程中遇到的问题，是很有帮助的。</p><p>另一方面，我们还可以学习到如何在一个框架中，同时处理IO事件和时间事件。我们平时开发服务器端程序，经常需要处理周期性任务，而Redis关于两类事件的处理实现，就给了我们一个不错的参考。</p><p>好，为了对这两类事件有个相对全面的了解，接下来，我们先从事件驱动框架循环流程的数据结构及其初始化开始学起，因为这里面就包含了针对这两类事件的数据结构定义和初始化操作。</p><h2>aeEventLoop结构体与初始化</h2><p>首先，我们来看下Redis事件驱动框架循环流程对应的数据结构aeEventLoop。这个结构体是在事件驱动框架代码<a href="https://github.com/redis/redis/tree/5.0/src/ae.h">ae.h</a>中定义的，记录了框架循环运行过程中的信息，其中，就包含了记录两类事件的变量，分别是：</p><ul>
<li><strong>aeFileEvent类型的指针*events，表示IO事件</strong>。之所以类型名称为aeFileEvent，是因为所有的IO事件都会用文件描述符进行标识；</li>
<li><strong>aeTimeEvent类型的指针*timeEventHead，表示时间事件</strong>，即按一定时间周期触发的事件。</li>
</ul><p>此外，aeEventLoop结构体中还有一个<strong>aeFiredEvent类型的指针*fired</strong>，这个并不是一类专门的事件类型，它只是用来记录已触发事件对应的文件描述符信息。</p><p>下面的代码显示了Redis中事件循环的结构体定义，你可以看下。</p><pre><code>typedef struct aeEventLoop {
    …
    aeFileEvent *events; //IO事件数组
    aeFiredEvent *fired; //已触发事件数组
    aeTimeEvent *timeEventHead; //记录时间事件的链表头
    …
    void *apidata; //和API调用接口相关的数据
    aeBeforeSleepProc *beforesleep; //进入事件循环流程前执行的函数
    aeBeforeSleepProc *aftersleep;  //退出事件循环流程后执行的函数
} aeEventLoop;
</code></pre><p>了解了aeEventLoop结构体后，我们再来看下，这个结构体是如何初始化的，这其中就包括了IO事件数组和时间事件链表的初始化。</p><h3>aeCreateEventLoop函数的初始化操作</h3><p>因为Redis server在完成初始化后，就要开始运行事件驱动框架的循环流程，所以，aeEventLoop结构体在<a href="http://github.com/redis/redis/tree/5.0/src/server.c">server.c</a>的initServer函数中，就通过调用<strong>aeCreateEventLoop函数</strong>进行初始化了。这个函数的参数只有一个，是setsize。</p><p>下面的代码展示了initServer函数中对aeCreateEventLoop函数的调用。</p><pre><code>initServer() {
…
//调用aeCreateEventLoop函数创建aeEventLoop结构体，并赋值给server结构的el变量
server.el = aeCreateEventLoop(server.maxclients+CONFIG_FDSET_INCR);
…
}
</code></pre><p>从这里我们可以看到<strong>参数setsize</strong>的大小，其实是由server结构的maxclients变量和宏定义CONFIG_FDSET_INCR共同决定的。其中，maxclients变量的值大小，可以在Redis的配置文件redis.conf中进行定义，默认值是1000。而宏定义CONFIG_FDSET_INCR的大小，等于宏定义CONFIG_MIN_RESERVED_FDS的值再加上96，如下所示，这里的两个宏定义都是在<a href="https://github.com/redis/redis/blob/5.0/src/server.h">server.h</a>文件中定义的。</p><pre><code>#define CONFIG_MIN_RESERVED_FDS 32
#define CONFIG_FDSET_INCR (CONFIG_MIN_RESERVED_FDS+96)
</code></pre><p>好了，到这里，你可能有疑问了：aeCreateEventLoop函数的参数setsize，设置为最大客户端数量加上一个宏定义值，可是<strong>这个参数有什么用呢</strong>？这就和aeCreateEventLoop函数具体执行的初始化操作有关了。</p><p>接下来，我们就来看下aeCreateEventLoop函数执行的操作，大致可以分成以下三个步骤。</p><p><strong>第一步，aeCreateEventLoop函数会创建一个aeEventLoop结构体类型的变量eventLoop</strong>。然后，该函数会给eventLoop的成员变量分配内存空间，比如，按照传入的参数setsize，给IO事件数组和已触发事件数组分配相应的内存空间。此外，该函数还会给eventLoop的成员变量赋初始值。</p><p><strong>第二步，aeCreateEventLoop函数会调用aeApiCreate函数</strong>。aeApiCreate函数封装了操作系统提供的IO多路复用函数，假设Redis运行在Linux操作系统上，并且IO多路复用机制是epoll，那么此时，aeApiCreate函数就会调用epoll_create创建epoll实例，同时会创建epoll_event结构的数组，数组大小等于参数setsize。</p><p>这里你需要注意，aeApiCreate函数是把创建的epoll实例描述符和epoll_event数组，保存在了aeApiState结构体类型的变量state，如下所示：</p><pre><code>typedef struct aeApiState {  //aeApiState结构体定义
    int epfd;   //epoll实例的描述符
    struct epoll_event *events;   //epoll_event结构体数组，记录监听事件
} aeApiState;

static int aeApiCreate(aeEventLoop *eventLoop) {
    aeApiState *state = zmalloc(sizeof(aeApiState));
    ...
    //将epoll_event数组保存在aeApiState结构体变量state中
    state-&gt;events = zmalloc(sizeof(struct epoll_event)*eventLoop-&gt;setsize);
    ...
    //将epoll实例描述符保存在aeApiState结构体变量state中
    state-&gt;epfd = epoll_create(1024); 
</code></pre><p>紧接着，aeApiCreate函数把state变量赋值给eventLoop中的apidata。这样一来，eventLoop结构体中就有了epoll实例和epoll_event数组的信息，这样就可以用来基于epoll创建和处理事件了。我一会儿还会给你具体介绍。</p><pre><code>eventLoop-&gt;apidata = state;
</code></pre><p><strong>第三步，aeCreateEventLoop函数会把所有网络IO事件对应文件描述符的掩码，初始化为AE_NONE，表示暂时不对任何事件进行监听。</strong></p><p>我把aeCreateEventLoop函数的主要部分代码放在这里，你可以看下。</p><pre><code>aeEventLoop *aeCreateEventLoop(int setsize) {
    aeEventLoop *eventLoop;
    int i;
   
    //给eventLoop变量分配内存空间
	if ((eventLoop = zmalloc(sizeof(*eventLoop))) == NULL) goto err;
	//给IO事件、已触发事件分配内存空间
    eventLoop-&gt;events = zmalloc(sizeof(aeFileEvent)*setsize);
    eventLoop-&gt;fired = zmalloc(sizeof(aeFiredEvent)*setsize);
    …
    eventLoop-&gt;setsize = setsize;
    eventLoop-&gt;lastTime = time(NULL);
    //设置时间事件的链表头为NULL
    eventLoop-&gt;timeEventHead = NULL;
	…
	//调用aeApiCreate函数，去实际调用操作系统提供的IO多路复用函数
	if (aeApiCreate(eventLoop) == -1) goto err;
	 
    //将所有网络IO事件对应文件描述符的掩码设置为AE_NONE
    for (i = 0; i &lt; setsize; i++)
        eventLoop-&gt;events[i].mask = AE_NONE;
    return eventLoop;
 
    //初始化失败后的处理逻辑，
    err:
    …
}
</code></pre><p>好，那么从aeCreateEventLoop函数的执行流程中，我们其实可以看到以下<strong>两个关键点</strong>：</p><ul>
<li>事件驱动框架监听的IO事件数组大小就等于参数setsize，这样决定了和Redis server连接的客户端数量。所以，当你遇到客户端连接Redis时报错“max number of clients reached”，你就可以去redis.conf文件修改maxclients配置项，以扩充框架能监听的客户端数量。</li>
<li>当使用Linux系统的epoll机制时，框架循环流程初始化操作，会通过aeApiCreate函数创建epoll_event结构数组，并调用epoll_create函数创建epoll实例，这都是使用epoll机制的准备工作要求，你也可以再回顾下第9讲中对epoll使用的介绍。</li>
</ul><p>到这里，框架就可以创建和处理具体的IO事件和时间事件了。所以接下来，我们就先来了解下IO事件及其处理机制。</p><h2>IO事件处理</h2><p>事实上，Redis的IO事件主要包括三类，分别是可读事件、可写事件和屏障事件。</p><p>其中，可读事件和可写事件其实比较好理解，也就是对应于Redis实例，我们可以<strong>从客户端读取数据或是向客户端写入数据</strong>。而屏障事件的主要作用是用来<strong>反转事件的处理顺序</strong>。比如在默认情况下，Redis会先给客户端返回结果，但是如果面临需要把数据尽快写入磁盘的情况，Redis就会用到屏障事件，把写数据和回复客户端的顺序做下调整，先把数据落盘，再给客户端回复。</p><p>我在上节课给你介绍过，在Redis源码中，IO事件的数据结构是aeFileEvent结构体，IO事件的创建是通过aeCreateFileEvent函数来完成的。下面的代码展示了aeFileEvent结构体的定义，你可以再回顾下：</p><pre><code>typedef struct aeFileEvent {
    int mask; //掩码标记，包括可读事件、可写事件和屏障事件
    aeFileProc *rfileProc;   //处理可读事件的回调函数
    aeFileProc *wfileProc;   //处理可写事件的回调函数
    void *clientData;  //私有数据
} aeFileEvent;
</code></pre><p>而对于aeCreateFileEvent函数来说，在上节课我们已经了解了它是通过aeApiAddEvent函数来完成事件注册的。那么接下来，我们再从代码级别看下它是如何执行的，这可以帮助我们更加透彻地理解，事件驱动框架对IO事件监听是如何基于epoll机制对应封装的。</p><h3>IO事件创建</h3><p>首先，我们来看aeCreateFileEvent函数的原型定义，如下所示：</p><pre><code>int aeCreateFileEvent(aeEventLoop *eventLoop, int fd, int mask, aeFileProc *proc, void *clientData)
</code></pre><p>这个函数的参数有5个，分别是循环流程结构体*eventLoop、IO事件对应的文件描述符fd、事件类型掩码mask、事件处理回调函数<code>*proc</code>，以及事件私有数据<code>*clientData</code>。</p><p>因为循环流程结构体<code>*eventLoop</code>中有IO事件数组，这个数组的元素是aeFileEvent类型，所以，每个数组元素都对应记录了一个文件描述符（比如一个套接字）相关联的监听事件类型和回调函数。</p><p>aeCreateFileEvent函数会先根据传入的文件描述符fd，在eventLoop的IO事件数组中，获取该描述符关联的IO事件指针变量<code>*fe</code>，如下所示：</p><pre><code>aeFileEvent *fe = &amp;eventLoop-&gt;events[fd];
</code></pre><p>紧接着，aeCreateFileEvent函数会调用aeApiAddEvent函数，添加要监听的事件：</p><pre><code>if (aeApiAddEvent(eventLoop, fd, mask) == -1)
   return AE_ERR;
</code></pre><p>aeApiAddEvent函数实际上会调用操作系统提供的IO多路复用函数，来完成事件的添加。我们还是假设Redis实例运行在使用epoll机制的Linux上，那么aeApiAddEvent函数就会调用epoll_ctl函数，添加要监听的事件。我在第9讲中其实已经给你介绍过epoll_ctl函数，这个函数会接收4个参数，分别是：</p><ul>
<li>epoll实例；</li>
<li>要执行的操作类型（是添加还是修改）；</li>
<li>要监听的文件描述符；</li>
<li>epoll_event类型变量。</li>
</ul><p>那么，<strong>这个调用过程是如何准备epoll_ctl函数需要的参数，从而完成执行的呢？</strong></p><p>首先，epoll实例是我刚才给你介绍的aeCreateEventLoop函数，它是通过调用aeApiCreate函数来创建的，保存在了eventLoop结构体的apidata变量中，类型是aeApiState。所以，aeApiAddEvent函数会先获取该变量，如下所示：</p><pre><code>static int aeApiAddEvent(aeEventLoop *eventLoop, int fd, int mask) {
    //从eventLoop结构体中获取aeApiState变量，里面保存了epoll实例
	aeApiState *state = eventLoop-&gt;apidata;
    ...
 }
</code></pre><p>其次，对于要执行的操作类型的设置，aeApiAddEvent函数会根据传入的文件描述符fd，在eventLoop结构体中IO事件数组中查找该fd。因为IO事件数组的每个元素，都对应了一个文件描述符，而该数组初始化时，每个元素的值都设置为了AE_NONE。</p><p>所以，如果要监听的文件描述符fd在数组中的类型不是AE_NONE，则表明该描述符已做过设置，那么操作类型就是修改操作，对应epoll机制中的宏定义EPOLL_CTL_MOD。否则，操作类型就是添加操作，对应epoll机制中的宏定义EPOLL_CTL_ADD。这部分代码如下所示：</p><pre><code>//如果文件描述符fd对应的IO事件已存在，则操作类型为修改，否则为添加
 int op = eventLoop-&gt;events[fd].mask == AE_NONE ?
            EPOLL_CTL_ADD : EPOLL_CTL_MOD;
</code></pre><p>第三，epoll_ctl函数需要的监听文件描述符，就是aeApiAddEvent函数接收到的参数fd。</p><p>最后，epoll_ctl函数还需要一个epoll_event类型变量，因此aeApiAddEvent函数在调用epoll_ctl函数前，会新创建epoll_event类型<strong>变量ee。</strong>然后，aeApiAddEvent函数会设置变量ee中的监听事件类型和监听文件描述符。</p><p>aeApiAddEvent函数的参数mask，表示的是要监听的事件类型掩码。所以，aeApiAddEvent函数会根据掩码值是可读（AE_READABLE）或可写（AE_WRITABLE）事件，来设置ee监听的事件类型是EPOLLIN还是EPOLLOUT。这样一来，Redis事件驱动框架中的读写事件就能够和epoll机制中的读写事件对应上来。下面的代码展示了这部分逻辑，你可以看下。</p><pre><code>…
struct epoll_event ee = {0}; //创建epoll_event类型变量
…
//将可读或可写IO事件类型转换为epoll监听的类型EPOLLIN或EPOLLOUT
if (mask &amp; AE_READABLE) ee.events |= EPOLLIN;
if (mask &amp; AE_WRITABLE) ee.events |= EPOLLOUT;
ee.data.fd = fd;  //将要监听的文件描述符赋值给ee
…	
</code></pre><p>好了，到这里，aeApiAddEvent函数就准备好了epoll实例、操作类型、监听文件描述符以及epoll_event类型变量，然后，它就会调用epoll_ctl开始实际创建监听事件了，如下所示：</p><pre><code>static int aeApiAddEvent(aeEventLoop *eventLoop, int fd, int mask) {
...
//调用epoll_ctl实际创建监听事件
if (epoll_ctl(state-&gt;epfd,op,fd,&amp;ee) == -1) return -1;
return 0;
}
</code></pre><p>了解了这些代码后，我们可以学习到事件驱动框架是如何基于epoll，封装实现了IO事件的创建。那么，在Redis server启动运行后，最开始监听的IO事件是可读事件，对应于客户端的连接请求。具体是initServer函数调用了aeCreateFileEvent函数，创建可读事件，并设置回调函数为acceptTcpHandler，用来处理客户端连接。这部分内容，你也可以再回顾下第10讲。</p><p>接下来，我们再来看下一旦有了客户端连接请求后，IO事件具体是如何处理的呢？</p><h3>读事件处理</h3><p>当Redis server接收到客户端的连接请求时，就会使用注册好的<strong>acceptTcpHandler函数</strong>进行处理。</p><p>acceptTcpHandler函数是在<a href="http://github.com/redis/redis/tree/5.0/src/networking.c">networking.c</a>文件中，它会接受客户端连接，并创建已连接套接字cfd。然后，acceptCommonHandler函数（在networking.c文件中）会被调用，同时，刚刚创建的已连接套接字cfd会作为参数，传递给acceptCommonHandler函数。</p><p>acceptCommonHandler函数会调用createClient函数（在networking.c文件中）创建客户端。而在createClient函数中，我们就会看到，aeCreateFileEvent函数被再次调用了。</p><p>此时，aeCreateFileEvent函数会针对已连接套接字上，创建监听事件，类型为AE_READABLE，回调函数是readQueryFromClient（在networking.c文件中）。</p><p>好了，到这里，事件驱动框架就增加了对一个客户端已连接套接字的监听。一旦客户端有请求发送到server，框架就会回调readQueryFromClient函数处理请求。这样一来，客户端请求就能通过事件驱动框架进行处理了。</p><p>下面代码展示了createClient函数调用aeCreateFileEvent的过程，你可以看下。</p><pre><code>client *createClient(int fd) {
…
if (fd != -1) {
        …
        //调用aeCreateFileEvent，监听读事件，对应客户端读写请求，使用readQueryFromclient回调函数处理
        if (aeCreateFileEvent(server.el,fd,AE_READABLE,
            readQueryFromClient, c) == AE_ERR)
        {
            close(fd);
            zfree(c);
            return NULL;
        } }
…
}
</code></pre><p>为了便于你掌握从监听客户端连接请求到监听客户端常规读写请求的事件创建过程，我画了下面这张图，你可以看下。</p><p><img src="https://static001.geekbang.org/resource/image/52/e9/5212d6d61a9e5d8aaefc88497fd5aee9.jpg?wh=2000x1093" alt=""></p><p>了解了事件驱动框架中的读事件处理之后，我们再来看下写事件的处理。</p><h3>写事件处理</h3><p>Redis实例在收到客户端请求后，会在处理客户端命令后，将要返回的数据写入客户端输出缓冲区。下图就展示了这个过程的函数调用逻辑：</p><p><img src="https://static001.geekbang.org/resource/image/31/df/3107452361f9366189e4d4080f3153df.jpg?wh=1888x1005" alt=""></p><p>而在Redis事件驱动框架每次循环进入事件处理函数前，也就是在框架主函数aeMain中调用aeProcessEvents，来处理监听到的已触发事件或是到时的时间事件之前，都会调用server.c文件中的<strong>beforeSleep函数</strong>，进行一些任务处理，这其中就包括了调用handleClientsWithPendingWrites函数，它会将Redis sever客户端缓冲区中的数据写回客户端。</p><p>下面给出的代码是事件驱动框架的主函数aeMain。在该函数每次调用aeProcessEvents函数前，就会调用beforeSleep函数，你可以看下。</p><pre><code>void aeMain(aeEventLoop *eventLoop) {
    eventLoop-&gt;stop = 0;
	while (!eventLoop-&gt;stop) {
	    //如果beforeSleep函数不为空，则调用beforeSleep函数
        if (eventLoop-&gt;beforesleep != NULL)
            eventLoop-&gt;beforesleep(eventLoop);
        //调用完beforeSleep函数，再处理事件
        aeProcessEvents(eventLoop, AE_ALL_EVENTS|AE_CALL_AFTER_SLEEP);
    }
}
</code></pre><p>这里你要知道，beforeSleep函数调用的handleClientsWithPendingWrites函数，会遍历每一个待写回数据的客户端，然后调用writeToClient函数，将客户端输出缓冲区中的数据写回。下面这张图展示了这个流程，你可以看下。</p><p><img src="https://static001.geekbang.org/resource/image/18/05/18c8bfaab29a890fb15edcca3971bb05.jpg?wh=2000x1125" alt=""></p><p>不过，如果输出缓冲区的数据还没有写完，此时，handleClientsWithPendingWrites函数就会<strong>调用aeCreateFileEvent函数，创建可写事件</strong>，并设置回调函数sendReplyToClient。sendReplyToClient函数里面会调用writeToClient函数写回数据。</p><p>下面的代码展示了handleClientsWithPendingWrite函数的基本流程，你可以看下。</p><pre><code>int handleClientsWithPendingWrites(void) {
    listIter li;
	listNode *ln;
	…
    //获取待写回的客户端列表
	listRewind(server.clients_pending_write,&amp;li);
	//遍历每一个待写回的客户端
	while((ln = listNext(&amp;li))) {
	   client *c = listNodeValue(ln);
	   …
	   //调用writeToClient将当前客户端的输出缓冲区数据写回
	   if (writeToClient(c-&gt;fd,c,0) == C_ERR) continue;
	   //如果还有待写回数据
	   if (clientHasPendingReplies(c)) {
	            int ae_flags = AE_WRITABLE;
	            //创建可写事件的监听，以及设置回调函数
	             if (aeCreateFileEvent(server.el, c-&gt;fd, ae_flags,
	                sendReplyToClient, c) == AE_ERR)
	            {
	                   …
	            }
	  } }
}
</code></pre><p>好了，我们刚才了解的是读写事件对应的回调处理函数。实际上，为了能及时处理这些事件，Redis事件驱动框架的aeMain函数还会循环<strong>调用aeProcessEvents函数，来检测已触发的事件，并调用相应的回调函数进行处理。</strong></p><p>从aeProcessEvents函数的代码中，我们可以看到该函数会调用aeApiPoll函数，查询监听的文件描述符中，有哪些已经就绪。一旦有描述符就绪，aeProcessEvents函数就会根据事件的可读或可写类型，调用相应的回调函数进行处理。aeProcessEvents函数调用的基本流程如下所示：</p><pre><code>int aeProcessEvents(aeEventLoop *eventLoop, int flags){
…
//调用aeApiPoll获取就绪的描述符
numevents = aeApiPoll(eventLoop, tvp);
…
for (j = 0; j &lt; numevents; j++) {
	aeFileEvent *fe = &amp;eventLoop-&gt;events[eventLoop-&gt;fired[j].fd];
	…
    //如果触发的是可读事件，调用事件注册时设置的读事件回调处理函数
	if (!invert &amp;&amp; fe-&gt;mask &amp; mask &amp; AE_READABLE) {
	      fe-&gt;rfileProc(eventLoop,fd,fe-&gt;clientData,mask);
	                fired++;
	}
    //如果触发的是可写事件，调用事件注册时设置的写事件回调处理函数
	if (fe-&gt;mask &amp; mask &amp; AE_WRITABLE) {
	                if (!fired || fe-&gt;wfileProc != fe-&gt;rfileProc) {
	                    fe-&gt;wfileProc(eventLoop,fd,fe-&gt;clientData,mask);
	                    fired++;
	                }
	            }
	…
	} }
	…
}
</code></pre><p>到这里，我们就了解了IO事件的创建函数aeCreateFileEvent，以及在处理客户端请求时对应的读写事件和它们的处理函数。那么接下来，我们再来看看事件驱动框架中的时间事件是怎么创建和处理的。</p><h2>时间事件处理</h2><p>其实，相比于IO事件有可读、可写、屏障类型，以及不同类型IO事件有不同回调函数来说，时间事件的处理就比较简单了。下面，我们就来分别学习下它的定义、创建、回调函数和触发处理。</p><h3>时间事件定义</h3><p>首先，我们来看下时间事件的结构体定义，代码如下所示：</p><pre><code>typedef struct aeTimeEvent {
    long long id; //时间事件ID
    long when_sec; //事件到达的秒级时间戳
    long when_ms; //事件到达的毫秒级时间戳
    aeTimeProc *timeProc; //时间事件触发后的处理函数
    aeEventFinalizerProc *finalizerProc;  //事件结束后的处理函数
    void *clientData; //事件相关的私有数据
    struct aeTimeEvent *prev;  //时间事件链表的前向指针
    struct aeTimeEvent *next;  //时间事件链表的后向指针
} aeTimeEvent;
</code></pre><p>时间事件结构体中主要的变量，包括以秒记录和以毫秒记录的时间事件触发时的时间戳when_sec和when_ms，以及时间事件触发后的处理函数<code>*timeProc</code>。另外，在时间事件的结构体中，还包含了前向和后向指针<code>*prev</code>和<code>*next</code>，这表明<strong>时间事件是以链表的形式组织起来的</strong>。</p><p>在了解了时间事件结构体的定义以后，我们接着来看下，时间事件是如何创建的。</p><h3>时间事件创建</h3><p>与IO事件创建使用aeCreateFileEvent函数类似，<strong>时间事件的创建函数是aeCreateTimeEvent函数</strong>。这个函数的原型定义如下所示：</p><pre><code>long long aeCreateTimeEvent(aeEventLoop *eventLoop, long long milliseconds, aeTimeProc *proc, void *clientData, aeEventFinalizerProc *finalizerProc)
</code></pre><p>在它的参数中，有两个需要我们重点了解下，以便于我们理解时间事件的处理。一个是<strong>milliseconds</strong>，这是所创建时间事件的触发时间距离当前时间的时长，是用毫秒表示的。另一个是*<strong>proc</strong>，这是所创建时间事件触发后的回调函数。</p><p>aeCreateTimeEvent函数的执行逻辑不复杂，主要就是创建一个时间事件的<strong>变量te</strong>，对它进行初始化，并把它插入到框架循环流程结构体eventLoop中的时间事件链表中。在这个过程中，aeCreateTimeEvent函数会<strong>调用aeAddMillisecondsToNow函数</strong>，根据传入的milliseconds参数，计算所创建时间事件具体的触发时间戳，并赋值给te。</p><p>实际上，Redis server在初始化时，除了创建监听的IO事件外，也会调用aeCreateTimeEvent函数创建时间事件。下面代码显示了initServer函数对aeCreateTimeEvent函数的调用：</p><pre><code>initServer() {
…
//创建时间事件
if (aeCreateTimeEvent(server.el, 1, serverCron, NULL, NULL) == AE_ERR){
… //报错信息
}
}
</code></pre><p>从代码中，我们可以看到，<strong>时间事件触发后的回调函数是serverCron</strong>。所以接下来，我们就来了解下serverCron函数。</p><h3>时间事件回调函数</h3><p>serverCron函数是在server.c文件中实现的。<strong>一方面</strong>，它会顺序调用一些函数，来实现时间事件被触发后，执行一些后台任务。比如，serverCron函数会检查是否有进程结束信号，若有就执行server关闭操作。serverCron会调用databaseCron函数，处理过期key或进行rehash等。你可以参考下面给出的代码：</p><pre><code>...
//如果收到进程结束信号，则执行server关闭操作
 if (server.shutdown_asap) {
        if (prepareForShutdown(SHUTDOWN_NOFLAGS) == C_OK) exit(0);
        ...
 }
...
clientCron();  //执行客户端的异步操作
databaseCron(); //执行数据库的后台操作
...
</code></pre><p><strong>另一方面</strong>，serverCron函数还会以不同的频率周期性执行一些任务，这是通过执行宏run_with_period来实现的。</p><p>run_with_period宏定义如下，该宏定义会根据Redis实例配置文件redis.conf中定义的hz值，来判断参数_ms_表示的时间戳是否到达。一旦到达，serverCron就可以执行相应的任务了。</p><pre><code>#define run_with_period(_ms_) if ((_ms_ &lt;= 1000/server.hz) || !(server.cronloops%((_ms_)/(1000/server.hz))))
</code></pre><p>比如，serverCron函数中会以1秒1次的频率，检查AOF文件是否有写错误。如果有的话，serverCron就会调用flushAppendOnlyFile函数，再次刷回AOF文件的缓存数据。下面的代码展示了这一周期性任务：</p><pre><code>serverCron() {
   …
   //每1秒执行1次，检查AOF是否有写错误
   run_with_period(1000) {
        if (server.aof_last_write_status == C_ERR)
            flushAppendOnlyFile(0);
    }
   …
}
</code></pre><p>如果你想了解更多的周期性任务，可以再详细阅读下serverCron函数中，以run_with_period宏定义包含的代码块。</p><p>好了，了解了时间事件触发后的回调函数serverCron，我们最后来看下，时间事件是如何触发处理的。</p><h3>时间事件的触发处理</h3><p>其实，时间事件的检测触发比较简单，事件驱动框架的aeMain函数会循环调用aeProcessEvents函数，来处理各种事件。而aeProcessEvents函数在执行流程的最后，会<strong>调用processTimeEvents函数处理相应到时的任务</strong>。</p><pre><code>aeProcessEvents(){
…
//检测时间事件是否触发
if (flags &amp; AE_TIME_EVENTS)
        processed += processTimeEvents(eventLoop);
…
}
</code></pre><p>那么，具体到proecessTimeEvent函数来说，它的基本流程就是从时间事件链表上逐一取出每一个事件，然后根据当前时间判断该事件的触发时间戳是否已满足。如果已满足，那么就调用该事件对应的回调函数进行处理。这样一来，周期性任务就能在不断循环执行的aeProcessEvents函数中，得到执行了。</p><p>下面的代码显示了processTimeEvents函数的基本流程，你可以再看下。</p><pre><code>static int processTimeEvents(aeEventLoop *eventLoop) {
...
te = eventLoop-&gt;timeEventHead;  //从时间事件链表中取出事件
while(te) {
   ...
  aeGetTime(&amp;now_sec, &amp;now_ms);  //获取当前时间
  if (now_sec &gt; te-&gt;when_sec || (now_sec == te-&gt;when_sec &amp;&amp; now_ms &gt;= te-&gt;when_ms))   //如果当前时间已经满足当前事件的触发时间戳
  {
     ...
    retval = te-&gt;timeProc(eventLoop, id, te-&gt;clientData); //调用注册的回调函数处理
    ...
  }
  te = te-&gt;next;   //获取下一个时间事件
  ...
}
</code></pre><h2>小结</h2><p>这节课，我给你介绍了Redis事件驱动框架中的两类事件：IO事件和时间事件。</p><p>对于IO事件来说，它可以进一步分成可读、可写和屏障事件。因为可读、可写事件在Redis和客户端通信处理请求过程中使用广泛，所以今天我们重点学习了这两种IO事件。当Redis server创建Socket后，就会注册可读事件，并使用acceptTCPHandler回调函数处理客户端的连接请求。</p><p>当server和客户端完成连接建立后，server会在已连接套接字上监听可读事件，并使用readQueryFromClient函数处理客户端读写请求。这里，你需要再注意下，<strong>无论客户端发送的请求是读或写操作，对于server来说，都是要读取客户端的请求并解析处理</strong>。所以，server在客户端的已连接套接字上注册的是可读事件。</p><p>而当实例需要向客户端写回数据时，实例会在事件驱动框架中注册可写事件，并使用sendReplyToClient作为回调函数，将缓冲区中数据写回客户端。我总结了一张表格，以便你再回顾下IO事件和相应套接字、回调函数的对应关系。</p><p><img src="https://static001.geekbang.org/resource/image/4b/0c/4b354d1c4fd6eed66b58c14689018a0c.jpg?wh=2000x812" alt=""></p><p>然后，对于时间事件来说，它主要是用于在事件驱动框架中注册一些周期性执行的任务，以便Redis server进行后台处理。时间事件的回调函数是serverCron函数，你可以做进一步阅读了解其中的具体任务。</p><p>好了，从第9讲开始，我用了3节课，向你介绍Redis事件驱动框架的运行机制，本质上来说，事件驱动框架是基于操作系统提供的IO多路复用机制进行了封装，并加上了时间事件的处理。这是一个非常经典的事件框架实现，我希望你可以学习并掌握好它，然后用在你自己的系统开发中。</p><h2>每课一问</h2><p>已知，Redis事件驱动框架的aeApiCreate、aeApiAddEvent等等这些函数，是对操作系统提供的IO多路复用函数进行了封装，具体的IO多路复用函数分别是在<a href="https://github.com/redis/redis/tree/5.0/src/ae_epoll.c">ae_epoll.c</a>，<a href="https://github.com/redis/redis/tree/5.0/src/ae_evport.c">ae_evport.c</a>，<a href="https://github.com/redis/redis/tree/5.0/src/ae_kqueue.c">ae_kqueue.c</a>，<a href="https://github.com/redis/redis/tree/5.0/src/ae_select.c">ae_select.c</a>四个代码文件中定义的。那么你知道，Redis在调用aeApiCreate，aeApiAddEvent这些函数时，是根据什么条件来决定，具体调用哪个文件中的IO多路复用函数的吗？</p>