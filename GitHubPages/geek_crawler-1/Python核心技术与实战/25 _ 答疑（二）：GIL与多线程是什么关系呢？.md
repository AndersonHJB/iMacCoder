<audio title="25 _ 答疑（二）：GIL与多线程是什么关系呢？" src="https://static001.geekbang.org/resource/audio/2a/7e/2a39adf03fc5aaa05cfafafea3f0387e.mp3" controls="controls"></audio> 
<p>你好，我是景霄。</p><p>不知不觉中，我们又一起完成了第二大章进阶篇的学习。我非常高兴看到很多同学一直在坚持积极地学习，并且留下了很多高质量的留言，值得我们互相思考交流。也有一些同学反复推敲，指出了文章中一些表达不严谨或是不当的地方，我也表示十分感谢。</p><p>大部分留言，我都在相对应的文章中回复过了。而一些手机上不方便回复，或是很有价值很典型的问题，我专门摘录了出来，作为今天的答疑内容，集中回复。</p><h2>问题一：列表self append无限嵌套的原理</h2><p><img src="https://static001.geekbang.org/resource/image/9d/a0/9d6c8c7a5adc13e9119d08dc3f1052a0.png" alt=""></p><p>先来回答第一个问题，两个同学都问到了，下面这段代码中的x，为什么是无限嵌套的列表？</p><pre><code>x = [1]
x.append(x)
x
[1, [...]]
</code></pre><p>我们可以将上述操作画一个图，便于你更直观地理解：</p><p><img src="https://static001.geekbang.org/resource/image/00/5f/001a607f3f29f68975be3e706711325f.png" alt=""></p><p>这里，x指向一个列表，列表的第一个元素为1；执行了append操作后，第二个元素又反过来指向x，即指向了x所指向的列表，因此形成了一个无限嵌套的循环：[1, [1, [1, [1, …]]]]。</p><p>不过，虽然x是无限嵌套的列表，但x.append(x)的操作，并不会递归遍历其中的每一个元素。它只是扩充了原列表的第二个元素，并将其指向x，因此不会出现stack overflow的问题，自然不会报错。</p><p>至于第二点，为什么len(x)返回的是2？我们还是来看x，虽然它是无限嵌套的列表，但x的top level只有2个元素组成，第一个元素为1，第二个元素为指向自身的列表，因此len(x)返回2。</p><!-- [[[read_end]]] --><h2>问题二：装饰器的宏观理解</h2><p><img src="https://static001.geekbang.org/resource/image/17/6f/17fcf8a9ef8685025fb5f792bc26116f.png" alt=""></p><p>再来看第二个问题，胡峣同学对装饰器的疑问。事实上，装饰器的作用与意义，在于其可以通过自定义的函数或类，在不改变原函数的基础上，改变原函数的一些功能。</p><pre><code>Decorators is to modify the behavior of the function through a wrapper so we don't have to actually modify the function.
</code></pre><p>装饰器将额外增加的功能，封装在自己的装饰器函数或类中；如果你想要调用它，只需要在原函数的顶部，加上@decorator即可。显然，这样做可以让你的代码得到高度的抽象、分离与简化。</p><p>光说概念可能还是有点抽象，我们可以想象下面这样一个场景，从真实例子来感受装饰器的魅力。在一些社交网站的后台，有无数的操作在调用之前，都需要先检查用户是否登录，比如在一些帖子里发表评论、发表状态等等。</p><p>如果你不知道装饰器，用常规的方法来编程，写出来的代码大概是下面这样的：</p><pre><code># 发表评论
def post_comment(request, ...):
    if not authenticate(request):
        raise Exception('U must log in first')
    ...
    
# 发表状态
def post_moment(request, ...):
    if not authenticate(request):
        raise Exception('U must log in first')
    ...
</code></pre><p>显然，这样重复调用认证函数authenticate()的步骤，就显得非常冗余了。更好的解决办法，就是将认证函数authenticate()单独分离出来，写成一个装饰器，就像我们下面这样的写法。这样一来，代码便得到了高度的优化：</p><pre><code># 发表评论
@authenticate
def post_comment(request, ...):

# 发表状态
@authenticate
def post_moment(request, ...):
</code></pre><p>不过也要注意，很多情况下，装饰器并不是唯一的方法。而我这里强调的，主要是使用装饰器带来的好处：</p><ul>
<li>代码更加简洁；</li>
<li>逻辑更加清晰；</li>
<li>程序的层次化、分离化更加明显。</li>
</ul><p>而这也是我们应该遵循和优先选择的开发模式。</p><h2>问题三：GIL与多线程的关系</h2><p><img src="https://static001.geekbang.org/resource/image/34/f1/3492e32a3396872095242be23db19ef1.png" alt=""></p><p>第三个问题，new同学疑惑的是，GIL只支持单线程，而Python支持多线程，这两者之间究竟是什么关系呢？</p><p>其实，GIL的存在与Python支持多线程并不矛盾。前面我们讲过，GIL是指同一时刻，程序只能有一个线程运行；而Python中的多线程，是指多个线程交替执行，造成一个“伪并行”的结果，但是具体到某一时刻，仍然只有1个线程在运行，并不是真正的多线程并行。这个机制，我画了下面这张图来表示：</p><p><img src="https://static001.geekbang.org/resource/image/e0/7b/e09b09170e0d2990d2e7f4e6a0292d7b.png" alt=""></p><p>举个例子来理解。比如，我用10个线程来爬取50个网站的内容。线程1在爬取第1个网站时，被I/O block住了，处于等待状态；这时，GIL就会释放，而线程2就会开始执行，去爬取第2个网站，依次类推。等到线程1的I/O操作完成时，主程序便又会切回线程1，让其完成剩下的操作。这样一来，从用户角度看到的，便是我们所说的多线程。</p><h2>问题四：多进程与多线程的应用场景</h2><p><img src="https://static001.geekbang.org/resource/image/a8/12/a853c99985472bfabc59d76839df4d12.png" alt=""></p><p>第四个问题，这个在文章中多次提到，不过，我还是想在这里再次强调一下。</p><p>如果你想对CPU密集型任务加速，使用多线程是无效的，请使用多进程。这里所谓的CPU密集型任务，是指会消耗大量CPU资源的任务，比如求1到100000000的乘积，或者是把一段很长的文字编码后又解码等等。</p><p>使用多线程之所以无效，原因正是我们前面刚讲过的，Python多线程的本质是多个线程互相切换，但同一时刻仍然只允许一个线程运行。因此，你使用多线程，和使用一个主线程，本质上来说并没有什么差别；反而在很多情况下，因为线程切换带来额外损耗，还会降低程序的效率。</p><p>而如果使用多进程，就可以允许多个进程之间in parallel地执行任务，所以能够有效提高程序的运行效率。</p><p>至于 I/O密集型任务，如果想要加速，请优先使用多线程或Asyncio。当然，使用多进程也可以达到目的，但是完全没有这个必要。因为对I/O密集型任务来说，大多数时间都浪费在了I/O等待上。因此，在一个线程/任务等待I/O时，我们只需要切换线程/任务去执行其他  I/O操作就可以了。</p><p>不过，如果I/O操作非常多、非常heavy，需要建立的连接也比较多时，我们一般会选择Asyncio。因为Asyncio的任务切换更加轻量化，并且它能启动的任务数也远比多线程启动的线程数要多。当然，如果I/O的操作不是那么的heavy，那么使用多线程也就足够了。</p><p>今天主要回答这几个问题，同时也欢迎你继续在留言区写下疑问和感想，我会持续不断地解答。希望每一次的留言和答疑，都能给你带来新的收获和价值。</p><p></p>