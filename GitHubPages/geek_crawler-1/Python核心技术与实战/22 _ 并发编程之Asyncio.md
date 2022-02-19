<audio title="22 _ 并发编程之Asyncio" src="https://static001.geekbang.org/resource/audio/45/d4/45dc75a64d1633ef7c4508ae3f5d00d4.mp3" controls="controls"></audio> 
<p>你好，我是景霄。</p><p>上节课，我们一起学习了Python并发编程的一种实现——多线程。今天这节课，我们继续学习Python并发编程的另一种实现方式——Asyncio。不同于协程那章，这节课我们更注重原理的理解。</p><p>通过上节课的学习，我们知道，在处理I/O操作时，使用多线程与普通的单线程相比，效率得到了极大的提高。你可能会想，既然这样，为什么还需要Asyncio？</p><p>诚然，多线程有诸多优点且应用广泛，但也存在一定的局限性：</p><ul>
<li>比如，多线程运行过程容易被打断，因此有可能出现race condition的情况；</li>
<li>再如，线程切换本身存在一定的损耗，线程数不能无限增加，因此，如果你的 I/O操作非常heavy，多线程很有可能满足不了高效率、高质量的需求。</li>
</ul><p>正是为了解决这些问题，Asyncio应运而生。</p><h2>什么是Asyncio</h2><h3>Sync VS Async</h3><p>我们首先来区分一下Sync（同步）和Async（异步）的概念。</p><ul>
<li>所谓Sync，是指操作一个接一个地执行，下一个操作必须等上一个操作完成后才能执行。</li>
<li>而Async是指不同操作间可以相互交替执行，如果其中的某个操作被block了，程序并不会等待，而是会找出可执行的操作继续执行。</li>
</ul><p>举个简单的例子，你的老板让你做一份这个季度的报表，并且邮件发给他。</p><!-- [[[read_end]]] --><ul>
<li>如果按照Sync的方式，你会先向软件输入这个季度的各项数据，接下来等待5min，等报表明细生成后，再写邮件发给他。</li>
<li>但如果按照Async的方式，再你输完这个季度的各项数据后，便会开始写邮件。等报表明细生成后，你会暂停邮件，先去查看报表，确认后继续写邮件直到发送完毕。</li>
</ul><h3>Asyncio工作原理</h3><p>明白了Sync 和Async，回到我们今天的主题，到底什么是Asyncio呢？</p><p>事实上，Asyncio和其他Python程序一样，是单线程的，它只有一个主线程，但是可以进行多个不同的任务（task），这里的任务，就是特殊的future对象。这些不同的任务，被一个叫做event loop的对象所控制。你可以把这里的任务，类比成多线程版本里的多个线程。</p><p>为了简化讲解这个问题，我们可以假设任务只有两个状态：一是预备状态；二是等待状态。所谓的预备状态，是指任务目前空闲，但随时待命准备运行。而等待状态，是指任务已经运行，但正在等待外部的操作完成，比如I/O操作。</p><p>在这种情况下，event loop会维护两个任务列表，分别对应这两种状态；并且选取预备状态的一个任务（具体选取哪个任务，和其等待的时间长短、占用的资源等等相关），使其运行，一直到这个任务把控制权交还给event loop为止。</p><p>当任务把控制权交还给event loop时，event loop会根据其是否完成，把任务放到预备或等待状态的列表，然后遍历等待状态列表的任务，查看他们是否完成。</p><ul>
<li>如果完成，则将其放到预备状态的列表；</li>
<li>如果未完成，则继续放在等待状态的列表。</li>
</ul><p>而原先在预备状态列表的任务位置仍旧不变，因为它们还未运行。</p><p>这样，当所有任务被重新放置在合适的列表后，新一轮的循环又开始了：event loop继续从预备状态的列表中选取一个任务使其执行…如此周而复始，直到所有任务完成。</p><p>值得一提的是，对于Asyncio来说，它的任务在运行时不会被外部的一些因素打断，因此Asyncio内的操作不会出现race condition的情况，这样你就不需要担心线程安全的问题了。</p><h3>Asyncio用法</h3><p>讲完了Asyncio的原理，我们结合具体的代码来看一下它的用法。还是以上节课下载网站内容为例，用Asyncio的写法我放在了下面代码中（省略了异常处理的一些操作），接下来我们一起来看：</p><pre><code>import asyncio
import aiohttp
import time

async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))

async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)

def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()

## 输出
Read 63153 from https://en.wikipedia.org/wiki/Java_(programming_language)
Read 31461 from https://en.wikipedia.org/wiki/Portal:Society
Read 23965 from https://en.wikipedia.org/wiki/Portal:Biography
Read 36312 from https://en.wikipedia.org/wiki/Portal:History
Read 25203 from https://en.wikipedia.org/wiki/Portal:Arts
Read 15160 from https://en.wikipedia.org/wiki/The_C_Programming_Language
Read 28749 from https://en.wikipedia.org/wiki/Portal:Mathematics
Read 29587 from https://en.wikipedia.org/wiki/Portal:Technology
Read 79318 from https://en.wikipedia.org/wiki/PHP
Read 30298 from https://en.wikipedia.org/wiki/Portal:Geography
Read 73914 from https://en.wikipedia.org/wiki/Python_(programming_language)
Read 62218 from https://en.wikipedia.org/wiki/Go_(programming_language)
Read 22318 from https://en.wikipedia.org/wiki/Portal:Science
Read 36800 from https://en.wikipedia.org/wiki/Node.js
Read 67028 from https://en.wikipedia.org/wiki/Computer_science
Download 15 sites in 0.062144195078872144 seconds
</code></pre><p>这里的Async和await关键字是Asyncio的最新写法，表示这个语句/函数是non-block的，正好对应前面所讲的event loop的概念。如果任务执行的过程需要等待，则将其放入等待状态的列表中，然后继续执行预备状态列表里的任务。</p><p>主函数里的asyncio.run(coro)是Asyncio的root call，表示拿到event loop，运行输入的coro，直到它结束，最后关闭这个event loop。事实上，asyncio.run()是Python3.7+才引入的，相当于老版本的以下语句：</p><pre><code>loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(coro)
finally:
    loop.close()
</code></pre><p>至于Asyncio版本的函数download_all()，和之前多线程版本有很大的区别：</p><pre><code>tasks = [asyncio.create_task(download_one(site)) for site in sites]
await asyncio.gather(*task)
</code></pre><p>这里的<code>asyncio.create_task(coro)</code>，表示对输入的协程coro创建一个任务，安排它的执行，并返回此任务对象。这个函数也是Python 3.7+新增的，如果是之前的版本，你可以用<code>asyncio.ensure_future(coro)</code>等效替代。可以看到，这里我们对每一个网站的下载，都创建了一个对应的任务。</p><p>再往下看，<code>asyncio.gather(*aws, loop=None, return_exception=False)</code>，则表示在event loop中运行<code>aws序列</code>的所有任务。当然，除了例子中用到的这几个函数，Asyncio还提供了很多其他的用法，你可以查看  <a href="https://docs.python.org/3/library/asyncio-eventloop.html">相应文档</a>  进行了解。</p><p>最后，我们再来看一下最后的输出结果——用时只有0.06s，效率比起之前的多线程版本，可以说是更上一层楼，充分体现其优势。</p><h2>Asyncio有缺陷吗？</h2><p>学了这么多内容，我们认识到了Asyncio的强大，但你要清楚，任何一种方案都不是完美的，都存在一定的局限性，Asyncio同样如此。</p><p>实际工作中，想用好Asyncio，特别是发挥其强大的功能，很多情况下必须得有相应的Python库支持。你可能注意到了，上节课的多线程编程中，我们使用的是requests库，但今天我们并没有使用，而是用了aiohttp库，原因就是requests库并不兼容Asyncio，但是aiohttp库兼容。</p><p>Asyncio软件库的兼容性问题，在Python3的早期一直是个大问题，但是随着技术的发展，这个问题正逐步得到解决。</p><p>另外，使用Asyncio时，因为你在任务的调度方面有了更大的自主权，写代码时就得更加注意，不然很容易出错。</p><p>举个例子，如果你需要await一系列的操作，就得使用asyncio.gather()；如果只是单个的future，或许只用asyncio.wait()就可以了。那么，对于你的future，你是想要让它run_until_complete()还是run_forever()呢？诸如此类，都是你在面对具体问题时需要考虑的。</p><h2>多线程还是Asyncio</h2><p>不知不觉，我们已经把并发编程的两种方式都给学习完了。不过，遇到实际问题时，多线程和Asyncio到底如何选择呢？</p><p>总的来说，你可以遵循以下伪代码的规范：</p><pre><code>if io_bound:
    if io_slow:
        print('Use Asyncio')
    else:
        print('Use multi-threading')
else if cpu_bound:
    print('Use multi-processing')
</code></pre><ul>
<li>如果是I/O bound，并且I/O操作很慢，需要很多任务/线程协同实现，那么使用Asyncio更合适。</li>
<li>如果是I/O bound，但是I/O操作很快，只需要有限数量的任务/线程，那么使用多线程就可以了。</li>
<li>如果是CPU bound，则需要使用多进程来提高程序运行效率。</li>
</ul><h2>总结</h2><p>今天这节课，我们一起学习了Asyncio的原理和用法，并比较了Asyncio和多线程各自的优缺点。</p><p>不同于多线程，Asyncio是单线程的，但其内部event loop的机制，可以让它并发地运行多个不同的任务，并且比多线程享有更大的自主控制权。</p><p>Asyncio中的任务，在运行过程中不会被打断，因此不会出现race condition的情况。尤其是在I/O操作heavy的场景下，Asyncio比多线程的运行效率更高。因为Asyncio内部任务切换的损耗，远比线程切换的损耗要小；并且Asyncio可以开启的任务数量，也比多线程中的线程数量多得多。</p><p>但需要注意的是，很多情况下，使用Asyncio需要特定第三方库的支持，比如前面示例中的aiohttp。而如果I/O操作很快，并不heavy，那么运用多线程，也能很有效地解决问题。</p><h2>思考题</h2><p>这两节课，我们学习了并发编程的两种实现方式，也多次提到了并行编程（multi-processing），其适用于CPU heavy的场景。</p><p>现在有这么一个需求：输入一个列表，对于列表中的每个元素，我想计算0到这个元素的所有整数的平方和。</p><p>我把常规版本的写法放在了下面，你能通过查阅资料，写出它的多进程版本，并且比较程序的耗时吗？</p><pre><code>import time
def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)

def main():
    start_time = time.perf_counter()  
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))
    
if __name__ == '__main__':
    main()
</code></pre><p>欢迎在留言区写下你的思考和答案，也欢迎你把今天的内容分享给你的同事朋友，我们一起交流、一起进步。</p><p></p>