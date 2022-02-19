<audio title="20 _ AOF重写（下）：重写时的新写操作记录在哪里？" src="https://static001.geekbang.org/resource/audio/fb/8f/fba8f72c785916772ac8a19cb65bdf8f.mp3" controls="controls"></audio> 
<p>你好，我是蒋德钧。</p><p>在上节课，我给你介绍了AOF重写过程，其中我带你重点了解了AOF重写的触发时机，以及AOF重写的基本执行流程。现在你已经知道，AOF重写是通过重写子进程来完成的。</p><p></p><p>但是在上节课的最后，我也提到了在AOF重写时，主进程仍然在接收客户端写操作，<strong>那么这些新写操作会记录到AOF重写日志中吗？如果需要记录的话，重写子进程又是通过什么方式向主进程获取这些写操作的呢？</strong></p><p></p><p>今天这节课，我就来带你了解下AOF重写过程中所使用的管道机制，以及主进程和重写子进程的交互过程。这样一方面，你就可以了解AOF重写日志包含的写操作的完整程度，当你要使用AOF日志恢复Redis数据库时，就知道AOF能恢复到的程度是怎样的。另一方面，因为AOF重写子进程就是通过操作系统提供的管道机制，来和Redis主进程交互的，所以学完这节课之后，你还可以掌握管道技术，从而用来实现进程间的通信。</p><p></p><p>好了，接下来，我们就先来了解下管道机制。</p><p></p><h2>如何使用管道进行父子进程间通信？</h2><p>首先我们要知道，当进程A通过调用fork函数创建一个子进程B，然后进程A和B要进行通信时，我们通常都需要依赖操作系统提供的通信机制，而<strong>管道</strong>（pipe）就是一种用于父子进程间通信的常用机制。</p><!-- [[[read_end]]] --><p></p><p>具体来说，管道机制在操作系统内核中创建了一块缓冲区，父进程A可以打开管道，并往这块缓冲区中写入数据。同时，子进程B也可以打开管道，从这块缓冲区中读取数据。这里，<strong>你需要注意的是</strong>，进程每次往管道中写入数据时，只能追加写到缓冲区中当前数据所在的尾部，而进程每次从管道中读取数据时，只能从缓冲区的头部读取数据。</p><p>其实，管道创建的这块缓冲区就像一个先进先出的队列一样，写数据的进程写到队列尾部，而读数据的进程则从队列头读取。下图就展示了两个进程使用管道进行数据通信的过程，你可以看下。</p><p><img src="https://static001.geekbang.org/resource/image/c1/ff/c16041a949bcef79fcb87805214715ff.jpg?wh=1768x465" alt="图片"></p><p></p><p>好了，了解了管道的基本功能后，我们再来看下使用管道时需要注意的一个关键点。<strong>管道中的数据在一个时刻只能向一个方向流动</strong>，这也就是说，如果父进程A往管道中写入了数据，那么此时子进程B只能从管道中读取数据。类似的，如果子进程B往管道中写入了数据，那么此时父进程A只能从管道中读取数据。而如果父子进程间需要同时进行数据传输通信，我们就需要创建两个管道了。</p><p></p><p>下面，我们就来看下怎么用代码实现管道通信。这其实是和操作系统提供的管道的系统调用pipe有关，pipe的函数原型如下所示：</p><pre><code class="language-plain">int pipe(int pipefd[2]);&nbsp;
</code></pre><p>你可以看到，pipe的参数是一个<strong>数组pipefd</strong>，表示的是管道的文件描述符。这是因为进程在往管道中写入或读取数据时，其实是使用write或read函数的，而write和read函数需要通过<strong>文件描述符</strong>才能进行写数据和读数据操作。</p><p></p><p>数组pipefd有两个元素pipefd[0]和pipefd[1]，分别对应了管道的读描述符和写描述符。这也就是说，当进程需要从管道中读数据时，就需要用到pipefd[0]，而往管道中写入数据时，就使用pipefd[1]。</p><p></p><p>这里我写了一份示例代码，展示了父子进程如何使用管道通信，你可以看下。</p><pre><code class="language-plain">int main()&nbsp;
{&nbsp;
&nbsp;&nbsp;&nbsp; int fd[2], nr = 0, nw = 0;&nbsp;
&nbsp;&nbsp;&nbsp; char buf[128];&nbsp;
&nbsp;&nbsp;&nbsp; pipe(fd);&nbsp;
&nbsp;&nbsp;&nbsp; pid = fork();&nbsp;
&nbsp;&nbsp; &nbsp;&nbsp;
	if(pid == 0) {
	&nbsp;&nbsp;&nbsp; //子进程调用read从fd[0]描述符中读取数据
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; printf("child process wait for message\n");&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nr = read(fds[0], buf, sizeof(buf))&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; printf("child process receive %s\n", buf);
	}else{&nbsp;
	&nbsp;&nbsp;&nbsp;&nbsp; //父进程调用write往fd[1]描述符中写入数据
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; printf("parent process send message\n");&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; strcpy(buf, "Hello from parent");&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nw = write(fd[1], buf, sizeof(buf));&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; printf("parent process send %d bytes to child.\n", nw);&nbsp;
&nbsp;&nbsp;&nbsp; }&nbsp;
&nbsp;&nbsp;&nbsp; return 0;&nbsp;
}&nbsp;
</code></pre><p>从代码中，你可以看到，在父子进程进行管道通信前，我们需要在代码中定义用于保存读写描述符的<strong>数组fd</strong>，然后调用pipe系统创建管道，并把数组fd作为参数传给pipe函数。紧接着，在父进程的代码中，父进程会调用write函数往管道文件描述符fd[1]中写入数据，另一方面，子进程调用read函数从管道文件描述符fd[0]中读取数据。</p><p>这里，为了便于你理解，我也画了一张图，你可以参考。</p><p><img src="https://static001.geekbang.org/resource/image/4a/a7/4a7932d7a371cfc610bb6d79fe0e96a7.jpg?wh=1920x1080" alt="图片"></p><p>好了，现在你就了解了如何使用管道来进行父子进程的通信了。那么下面，我们就来看下在AOF重写过程中，重写子进程是如何用管道和主进程（也就是它的父进程）进行通信的。</p><p></p><h2>AOF重写子进程如何使用管道和父进程交互？</h2><p>我们先来看下在AOF重写过程中，都创建了几个管道。</p><p>这实际上是AOF重写函数rewriteAppendOnlyFileBackground在执行过程中，通过调用<strong>aofCreatePipes函数</strong>来完成的，如下所示：</p><pre><code class="language-plain">int rewriteAppendOnlyFileBackground(void) {
…
if (aofCreatePipes() != C_OK) return C_ERR;
…
}
</code></pre><p>这个aofCreatePipes函数是在<a href="https://github.com/redis/redis/tree/5.0/src/aof.c">aof.c</a>文件中实现的，它的逻辑比较简单，可以分成三步。</p><p><strong>第一步</strong>，aofCreatePipes函数创建了包含6个文件描述符元素的<strong>数组fds</strong>。就像我刚才给你介绍的，每一个管道会对应两个文件描述符，所以，数组fds其实对应了AOF重写过程中要用到的三个管道。紧接着，aofCreatePipes函数就调用pipe系统调用函数，分别创建三个管道。</p><p></p><p>这部分代码如下所示，你可以看下。</p><pre><code class="language-plain">int aofCreatePipes(void) {
&nbsp;&nbsp;&nbsp; int fds[6] = {-1, -1, -1, -1, -1, -1};
&nbsp;&nbsp;&nbsp; int j;
&nbsp;&nbsp;&nbsp; if (pipe(fds) == -1) goto error; /* parent -&gt; children data. */
&nbsp;&nbsp;&nbsp; if (pipe(fds+2) == -1) goto error; /* children -&gt; parent ack. */
	if (pipe(fds+4) == -1) goto error;
	…}
}
</code></pre><p><strong>第二步</strong>，aofCreatePipes函数会调用<strong>anetNonBlock函数</strong>（在<a href="https://github.com/redis/redis/tree/5.0/src/anet.c">anet.c</a>文件中），将fds</p><p>数组的第一和第二个描述符（fds[0]和fds[1]）对应的管道设置为非阻塞。然后，aofCreatePipes函数会调用<strong>aeCreateFileEvent函数</strong>，在数组fds的第三个描述符(fds[2])上注册了读事件的监听，对应的回调函数是aofChildPipeReadable。aofChildPipeReadable函数也是在aof.c文件中实现的，我稍后会给你详细介绍它。</p><p></p><pre><code class="language-plain">int aofCreatePipes(void) {
…
if (anetNonBlock(NULL,fds[0]) != ANET_OK) goto error;
if (anetNonBlock(NULL,fds[1]) != ANET_OK) goto error;
if (aeCreateFileEvent(server.el, fds[2], AE_READABLE, aofChildPipeReadable, NULL) == AE_ERR) goto error;
…
}
</code></pre><p>这样，在完成了管道创建、管道设置和读事件注册后，最后一步，aofCreatePipes函数会将数组fds中的六个文件描述符，分别复制给server变量的成员变量，如下所示：</p><pre><code class="language-plain">int aofCreatePipes(void) {
…
server.aof_pipe_write_data_to_child = fds[1];
server.aof_pipe_read_data_from_parent = fds[0];
server.aof_pipe_write_ack_to_parent = fds[3];
server.aof_pipe_read_ack_from_child = fds[2];
server.aof_pipe_write_ack_to_child = fds[5];
server.aof_pipe_read_ack_from_parent = fds[4];
…
}
</code></pre><p>在这一步中，我们就可以从server变量的成员变量名中，看到aofCreatePipes函数创建的三个管道，以及它们各自的用途。</p><ul>
<li><strong>fds[0]和fds[1]</strong>：对应了主进程和重写子进程间用于传递操作命令的管道，它们分别对应读描述符和写描述符。</li>
<li><strong>fds[2]和fds[3]</strong>：对应了重写子进程向父进程发送ACK信息的管道，它们分别对应读描述符和写描述符。</li>
<li><strong>fds[4]和fds[5]</strong>：对应了父进程向重写子进程发送ACK信息的管道，它们分别对应读描述符和写描述符。</li>
</ul><p></p><p>下图也展示了aofCreatePipes函数的基本执行流程，你可以再回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/39/18/3966573fd97e10f41e9bbbcc6e919718.jpg?wh=1920x1080" alt="图片"></p><p>好了，了解了AOF重写过程中的管道个数和用途后，下面我们再来看下这些管道具体是如何使用的。</p><p></p><h3>操作命令传输管道的使用</h3><p>实际上，当AOF重写子进程在执行时，主进程还会继续接收和处理客户端写请求。这些写操作会被主进程正常写入AOF日志文件，这个过程是由<strong>feedAppendOnlyFile函数</strong>（在aof.c文件中）来完成。</p><p>feedAppendOnlyFile函数在执行的最后一步，会判断当前是否有AOF重写子进程在运行。如果有的话，它就会调用<strong>aofRewriteBufferAppend函数</strong>（在aof.c文件中），如下所示：</p><pre><code class="language-plain">if (server.aof_child_pid != -1)
&nbsp; &nbsp; &nbsp; &nbsp; aofRewriteBufferAppend((unsigned char*)buf,sdslen(buf));
</code></pre><p>aofRewriteBufferAppend函数的作用是将参数buf，追加写到全局变量server的aof_rewrite_buf_blocks这个列表中。<br>
这里，你需要注意的是，<strong>参数buf是一个字节数组</strong>，feedAppendOnlyFile函数会将主进程收到的命令操作写入到buf中。而aof_rewrite_buf_blocks列表中的每个元素是<strong>aofrwblock结构体类型</strong>，这个结构体中包括了一个字节数组，大小是AOF_RW_BUF_BLOCK_SIZE，默认值是10MB。此外，aofrwblock结构体还记录了字节数组已经使用的空间和剩余可用的空间。</p><p>以下代码展示了aofrwblock结构体的定义，你可以看下。</p><pre><code class="language-plain">typedef struct aofrwblock {
&nbsp; &nbsp; unsigned long used, free; //buf数组已用空间和剩余可用空间
&nbsp; &nbsp; char buf[AOF_RW_BUF_BLOCK_SIZE]; //宏定义AOF_RW_BUF_BLOCK_SIZE默认为10MB
} aofrwblock;
</code></pre><p>这样一来，aofrwblock结构体就相当于是一个10MB的数据块，记录了AOF重写期间主进程收到的命令，而aof_rewrite_buf_blocks列表负责将这些数据块连接起来。当aofRewriteBufferAppend函数执行时，它会从aof_rewrite_buf_blocks列表中取出一个aofrwblock类型的数据块，用来记录命令操作。</p><p>当然，如果当前数据块中的空间不够保存参数buf中记录的命令操作，那么aofRewriteBufferAppend函数就会再分配一个aofrwblock数据块。</p><p>好了，当aofRewriteBufferAppend函数将命令操作记录到aof_rewrite_buf_blocks列表中之后，它还会<strong>检查aof_pipe_write_data_to_child管道描述符上是否注册了写事件</strong>，这个管道描述符就对应了我刚才给你介绍的fds[1]。</p><p>如果没有注册写事件，那么aofRewriteBufferAppend函数就会调用<strong>aeCreateFileEvent函数</strong>，注册一个写事件，这个写事件会监听aof_pipe_write_data_to_child这个管道描述符，也就是主进程和重写子进程间的操作命令传输管道。</p><p>当这个管道可以写入数据时，写事件对应的回调函数aofChildWriteDiffData（在aof.c文件中）就会被调用执行。这个过程你可以参考下面的代码：</p><pre><code class="language-plain">void aofRewriteBufferAppend(unsigned char *s, unsigned long len) {
...
//检查aof_pipe_write_data_to_child描述符上是否有事件
if (aeGetFileEvents(server.el,server.aof_pipe_write_data_to_child) == 0) {
     //如果没有注册事件，那么注册一个写事件，回调函数是aofChildWriteDiffData
&nbsp; &nbsp; &nbsp;aeCreateFileEvent(server.el, server.aof_pipe_write_data_to_child,
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AE_WRITABLE, aofChildWriteDiffData, NULL);
}
...}
</code></pre><p>其实，刚才我介绍的写事件回调函数aofChildWriteDiffData，它的<strong>主要作用</strong>是从aof_rewrite_buf_blocks列表中逐个取出数据块，然后通过aof_pipe_write_data_to_child管道描述符，将数据块中的命令操作通过管道发给重写子进程，这个过程如下所示：</p><pre><code class="language-plain">void aofChildWriteDiffData(aeEventLoop *el, int fd, void *privdata, int mask) {
...
while(1) {
   //从aof_rewrite_buf_blocks列表中取出数据块
   ln = listFirst(server.aof_rewrite_buf_blocks);
&nbsp; &nbsp;block = ln ? ln-&gt;value : NULL;
   if (block-&gt;used &gt; 0) {
      //调用write将数据块写入主进程和重写子进程间的管道
&nbsp; &nbsp;   nwritten = write(server.aof_pipe_write_data_to_child,
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;block-&gt;buf,block-&gt;used);
      if (nwritten &lt;= 0) return;
            ...
        }
 ...}}
</code></pre><p>好了，这样一来，你就了解了主进程其实是在正常记录AOF日志时，将收到的命令操作写入aof_rewrite_buf_blocks列表中的数据块，然后再通过aofChildWriteDiffData函数将记录的命令操作通过主进程和重写子进程间的管道发给子进程。</p><p>下图也展示了这个过程，你可以再来回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/ef/a9/efe1a110e7062e17aa964a3b1781bfa9.jpg?wh=1920x1080" alt="图片"></p><p>然后，我们接着来看下重写子进程，是如何从管道中读取父进程发送的命令操作的。</p><p>这实际上是由<strong>aofReadDiffFromParent函数</strong>（在aof.c文件中）来完成的。这个函数会使用一个64KB大小的缓冲区，然后调用read函数，读取父进程和重写子进程间的操作命令传输管道中的数据。以下代码也展示了aofReadDiffFromParent函数的基本执行流程，你可以看下。</p><pre><code class="language-plain">ssize_t aofReadDiffFromParent(void) {
&nbsp; &nbsp; char buf[65536]; //管道默认的缓冲区大小
&nbsp; &nbsp; ssize_t nread, total = 0;
    //调用read函数从aof_pipe_read_data_from_parent中读取数据
&nbsp; &nbsp; while ((nread =
&nbsp; &nbsp; &nbsp; read(server.aof_pipe_read_data_from_parent,buf,sizeof(buf))) &gt; 0) {
&nbsp; &nbsp; &nbsp; &nbsp; server.aof_child_diff = sdscatlen(server.aof_child_diff,buf,nread);
&nbsp; &nbsp; &nbsp; &nbsp; total += nread;
&nbsp; &nbsp; }
&nbsp; &nbsp; return total;
}
</code></pre><p>那么，从代码中，你可以看到aofReadDiffFromParent函数会通过<strong>aof_pipe_read_data_from_parent描述符</strong>读取数据。然后，它会将读取的操作命令追加到全局变量server的aof_child_diff字符串中。而在AOF重写函数rewriteAppendOnlyFile的执行过程最后，<strong>aof_child_diff字符串</strong>会被写入AOF重写日志文件，以便我们在使用AOF重写日志时，能尽可能地恢复重写期间收到的操作。</p><p>这个aof_child_diff字符串写入重写日志文件的过程，你可以参考下面给出的代码：</p><pre><code class="language-plain">int rewriteAppendOnlyFile(char *filename) {
...
//将aof_child_diff中累积的操作命令写入AOF重写日志文件
if (rioWrite(&amp;aof,server.aof_child_diff,sdslen(server.aof_child_diff)) == 0)
&nbsp; &nbsp; &nbsp; &nbsp; goto werr;
...
}
</code></pre><p>所以也就是说，aofReadDiffFromParent函数实现了重写子进程向主进程读取操作命令。那么在这里，我们还需要搞清楚的问题是：aofReadDiffFromParent函数会在哪里被调用，也就是重写子进程会在什么时候从管道中读取主进程收到的操作。</p><p>其实，aofReadDiffFromParent函数一共会被以下三个函数调用。</p><ul>
<li><strong>rewriteAppendOnlyFileRio函数</strong>：这个函数是由重写子进程执行的，它负责遍历Redis每个数据库，生成AOF重写日志，在这个过程中，它会不时地调用aofReadDiffFromParent函数。</li>
<li><strong>rewriteAppendOnlyFile函数</strong>：这个函数是重写日志的主体函数，也是由重写子进程执行的，它本身会调用rewriteAppendOnlyFileRio函数。此外，它在调用完rewriteAppendOnlyFileRio函数后，还会多次调用aofReadDiffFromParent函数，以尽可能多地读取主进程在重写日志期间收到的操作命令。</li>
<li><strong>rdbSaveRio函数</strong>：这个函数是创建RDB文件的主体函数。当我们使用AOF和RDB混合持久化机制时，这个函数也会调用aofReadDiffFromParent函数。</li>
</ul><p>从这里，我们可以看到，Redis源码在实现AOF重写过程中，其实会多次让重写子进程向主进程读取新收到的操作命令，这也是为了让重写日志尽可能多地记录最新的操作，提供更加完整的操作记录。</p><p>最后，我们再来看下重写子进程和主进程间用来传递ACK信息的两个管道的使用。</p><h3>ACK管道的使用</h3><p>刚才在介绍主进程调用aofCreatePipes函数创建管道时，你就了解到了，主进程会在aof_pipe_read_ack_from_child管道描述符上注册读事件。这个描述符对应了重写子进程向主进程发送ACK信息的管道。同时，这个描述符是一个<strong>读描述符</strong>，表示主进程从管道中读取ACK信息。</p><p>其实，重写子进程在执行rewriteAppendOnlyFile函数时，这个函数在完成日志重写，以及多次向父进程读取操作命令后，就会调用write函数，向aof_pipe_write_ack_to_parent描述符对应的管道中<strong>写入“！”</strong>，这就是重写子进程向主进程发送ACK信号，让主进程停止发送收到的新写操作。这个过程如下所示：</p><pre><code class="language-plain">int rewriteAppendOnlyFile(char *filename) {
...
if (write(server.aof_pipe_write_ack_to_parent,"!",1) != 1) goto werr;
...}
</code></pre><p>一旦重写子进程向主进程发送ACK信息的管道中有了数据，aof_pipe_read_ack_from_child管道描述符上注册的读事件就会被触发，也就是说，这个管道中有数据可以读取了。那么，aof_pipe_read_ack_from_child管道描述符上，注册的<strong>回调函数aofChildPipeReadable</strong>（在aof.c文件中）就会执行。</p><p>这个函数会判断从aof_pipe_read_ack_from_child管道描述符读取的数据是否是“！”，如果是的话，那它就会调用write函数，往aof_pipe_write_ack_to_child管道描述符上写入“！”，表示主进程已经收到重写子进程发送的ACK信息，同时它会给重写子进程回复一个ACK信息。这个过程如下所示：</p><pre><code class="language-plain">void aofChildPipeReadable(aeEventLoop *el, int fd, void *privdata, int mask) {
...
if (read(fd,&amp;byte,1) == 1 &amp;&amp; byte == '!') {
   ...
   if (write(server.aof_pipe_write_ack_to_child,"!",1) != 1) { ...}
}
...
}
</code></pre><p>好了，到这里，我们就了解了，重写子进程在完成日志重写后，是先给主进程发送ACK信息。然后主进程在aof_pipe_read_ack_from_child描述符上监听读事件发生，并调用aofChildPipeReadable函数向子进程发送ACK信息。</p><p>最后，重写子进程执行的rewriteAppendOnlyFile函数，会调用<strong>syncRead函数</strong>，从aof_pipe_read_ack_from_parent管道描述符上，读取主进程发送给它的ACK信息，如下所示：</p><pre><code class="language-plain">int rewriteAppendOnlyFile(char *filename) {
...
if (syncRead(server.aof_pipe_read_ack_from_parent,&amp;byte,1,5000) != 1  || byte != '!') goto werr
...
}
</code></pre><p>下图也展示了ACK管道的使用过程，你可以再回顾下。</p><p><img src="https://static001.geekbang.org/resource/image/41/59/416bb56f2c5af3bac4f2c4374300c459.jpg?wh=1920x1080" alt="图片"></p><p>这样一来，重写子进程和主进程之间就通过两个ACK管道，相互确认重写过程结束了。</p><h2>小结</h2><p>今天这节课，我主要给你介绍了在AOF重写过程中，主进程和重写子进程间的管道通信。这里，你需要重点关注管道机制的使用，以及主进程和重写子进程使用管道通信的过程。</p><p>在这个过程中，AOF重写子进程和主进程是使用了一个操作命令传输管道和两个ACK信息发送管道。<strong>操作命令传输管道</strong>是用于主进程写入收到的新操作命令，以及用于重写子进程读取操作命令，而<strong>ACK信息发送管道</strong>是在重写结束时，重写子进程和主进程用来相互确认重写过程的结束。最后，重写子进程会进一步将收到的操作命令记录到重写日志文件中。</p><p>这样一来，AOF重写过程中主进程收到的新写操作，就不会被遗漏了。因为一方面，这些新写操作会被记录在正常的AOF日志中，另一方面，主进程会将新写操作缓存在aof_rewrite_buf_blocks数据块列表中，并通过管道发送给重写子进程。这样，就能尽可能地保证重写日志具有最新、最完整的写操作了。</p><p></p><p>最后，我也再提醒你一下，今天这节课我们学习的管道其实属于<strong>匿名管道</strong>，是用在父子进程间进行通信的。如果你在实际开发中，要在非父子进程的两个进程间进行通信，那么你就需要用到命名管道了。而命名管道会以一个文件的形式保存在文件系统中，并会有相应的路径和文件名。这样，非父子进程的两个进程通过命名管道的路径和文件名，就可以打开管道进行通信了。</p><p></p><h2>每课一问</h2><p>今天这节课，我给你介绍了重写子进程和主进程间进行操作命令传输、ACK信息传递用的三个管道。那么，你在Redis源码中还能找见其他使用管道的地方吗？</p><p></p><p></p>