---
title: 09-一篇带你熟练使用多线程与原理「Thread」
tags: []
id: '755'
categories:
  - - Python3 网络爬虫系统教学
date: 2020-07-26 09:28:34
---

我们知道，在一台计算机中，我们可以同时打开许多软件，比如同时浏览网页、听音乐、打字等等，看似非常正常。但仔细想想，为什么计算机可以做到这么多软件同时运行呢？这就涉及到计算机中的两个重要概念：多进程和多线程了。 同样，在编写爬虫程序的时候，为了提高爬取效率，我们可能想同时运行多个爬虫任务。这里同样需要涉及多进程和多线程的知识。 本课时，我们就先来了解一下多线程的基本原理，以及在 Python 中如何实现多线程。

## 1\. 全局解释器锁

> **全局解释器锁** （英语：Global Interpreter Lock，缩写 **GIL**） 是 **计算机程序设计语言解释器** 用于 **同步线程** 的一种机制，它使得任何时刻仅有 **一个线程** 在执行，即便在 **多核心处理器** 上，使用 **GIL** 的解释器也只允许同一时间执行一个线程。常见的使用 **GIL** 的解释器有 **CPython** 与 **Ruby MRI**。

如果，你对上面的不理解，也没有问题。通俗的解释就是：你电脑是 **一核或者多核** ，还是你的代码写了了多个线程，但因为 **GIL** 锁的存在你也就只能运行一个线程，无法同时运行多个线程。 接下来，我们来用个图片来解释一下： ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200726092552.jpg) 比如图中，假如你开了两个线程（**Py thread1** 、**Py tread2**），

1.  当我们线程一（**Py thread1**）开始执行时，这个线程会去我们的解释器中申请到一个锁。也就是我们的 **GIL** 锁；
2.  然后，解释器接收到一个请求的时候呢，它就会到我们的 **OS** 里面，申请我们的系统线程；
3.  系统统一你的线程执行的时候，就会在你的 **CPU** 上面执行。（假设你现在是四核CPU）；
4.  而我们的另一个线程二（**py thread2**）也在同步运行。
5.  而线程二在向这个解释器申请 **GIL** 的时候线程二会卡在这里（Python 解释器），因为它的 **GIL** 锁已经被线程一给拿走了（也就是说：他要进去执行，必须拿到这把锁）；
6.  线程二要运行的话，就必须等我们的线程一运行完成之后（也就是把我们的 **GIL** 释放之后（图片中的第5步）线程二才能拿到这把锁）；
7.  当线程二拿到这把锁之后就和线程一的运行过程一样。

```python
① Create > ② GIL > ③ 申请原生线程(OS) > ④ CPU 执行（如果有其他线程，都会卡在 Python 解释器的外边）
```

###### 这个锁其实是 Python 之父想一劳永逸解决线程的安全问题（也就是禁止多线程同时运行）

## 2\. 多线程的含义

说起多线程，就不得不先说什么是线程。然而想要弄明白什么是线程，又不得不先说什么是进程。 进程我们可以理解为是一个可以独立运行的程序单位。 比如：

1.  打开一个浏览器，这就开启了一个浏览器进程；
2.  打开一个文本编辑器，这就开启了一个文本编辑器进程。

但一个进程中是可以同时处理很多事情的。 比如：

1.  在浏览器中，我们可以在多个选项卡中打开多个页面。

*   有的页面在播放音乐，
*   有的页面在播放视频，
*   有的网页在播放动画，它们可以同时运行，互不干扰。

**为什么能同时做到同时运行这么多的任务呢？** 这里就需要引出线程的概念了，其实这一个个任务，实际上就对应着一个个线程的执行。 **而进程呢？** 它就是线程的集合，进程就是由一个或多个线程构成的，线程是操作系统进行**运算调度的最小单位**，是进程中的一个最小运行单元。 比如： 上面所说的浏览器进程，其中的播放音乐就是一个线程，播放视频也是一个线程，当然其中还有很多其他的线程在同时运行，这些线程的**并发或并行**执行最后使得整个浏览器可以同时运行这么多的任务。 了解了线程的概念，多线程就很容易理解了，多线程就是一个进程中同时执行多个线程，前面所说的浏览器的情景就是典型的多线程执行。

## 3\. 并发和并行

说到多进程和多线程，这里就需要再讲解两个概念，那就是并发和并行。我们知道，一个程序在计算机中运行，其底层是处理器通过运行一条条的指令来实现的。

### 3.1 并发

英文叫作 `concurrency`。它是指同一时刻只能有一条指令执行，但是多个线程的对应的指令被快速轮换地执行。比如： 一个处理器，它先执行线程 A 的指令一段时间，再执行线程 B 的指令一段时间，再切回到线程 A 执行一段时间。 由于处理器执行指令的速度和切换的速度非常非常快，人完全感知不到计算机在这个过程中有多个线程切换上下文执行的操作，这就使得宏观上看起来多个线程在同时运行。但微观上只是这个处理器在连续不断地在多个线程之间切换和执行，每个线程的执行一定会占用这个处理器一个时间片段，同一时刻，其实只有一个线程在执行。

### 3.2 并行

英文叫作 `parallel`。它是指同一时刻，有**多条指令在多个处理器上同时执行**，并行必须要依赖于多个处理器。不论是从宏观上还是微观上，多个线程都是在同一时刻一起执行的。 **并行只能在多处理器系统中存在**，如果我们的计算机处理器只有一个核，那就不可能实现并行。 而并发在单处理器和多处理器系统中都是可以存在的，因为仅靠一个核，就可以实现并发。 **举个例子** 比如系统处理器需要同时运行多个线程。如果系统处理器只有一个核，那它只能通过并发的方式来运行这些线程。如果系统处理器有多个核，当一个核在执行一个线程时，另一个核可以执行另一个线程，这样这两个线程就实现了并行执行，当然其他的线程也可能和另外的线程处在同一个核上执行，它们之间就是并发执行。具体的执行方式，就取决于操作系统的调度了。 ![在这里插入图片描述](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200726092600.png)

## 4\. 多线程适用场景

在一个程序进程中，有一些操作是比较耗时或者需要等待的，比如等待数据库的查询结果的返回，等待网页结果的响应。如果使用单线程，处理器必须要等到这些操作完成之后才能继续往下执行其他操作，而这个线程在等待的过程中，处理器明显是可以来执行其他的操作的。如果使用多线程，处理器就可以在某个线程等待的时候，去执行其他的线程，从而从整体上提高执行效率。 像上述场景，线程在执行过程中很多情况下是需要等待的。 **比如** 网络爬虫就是一个非常典型的例子，爬虫在向服务器发起请求之后，有一段时间必须要等待服务器的响应返回，这种任务就属于 IO 密集型任务。对于这种任务，如果我们启用多线程，处理器就可以在某个线程等待的过程中去处理其他的任务，从而提高整体的爬取效率。 但并不是所有的任务都是 IO 密集型任务，还有一种任务叫作计算密集型任务，也可以称之为 CPU 密集型任务。顾名思义，就是任务的运行一直需要处理器的参与。此时如果我们开启了多线程，一个处理器从一个计算密集型任务切换到切换到另一个计算密集型任务上去，处理器依然不会停下来，始终会忙于计算，这样并不会节省总体的时间，因为需要处理的任务的计算总量是不变的。如果线程数目过多，反而还会在线程切换的过程中多耗费一些时间，整体效率会变低。 所以，如果任务不全是计算密集型任务，我们可以使用多线程来提高程序整体的执行效率。尤其对于网络爬虫这种 IO 密集型任务来说，使用多线程会大大提高程序整体的爬取效率。

## 5\. Python 实现多线程

在 Python 中，实现多线程的模块叫作 `threading`，是 Python 自带的模块。下面我们来了解下使用 threading 实现多线程的方法。 在具体实现之前，我们先来测试一下多线程与当线程裸奔的速度对比，为了更加直观，我这里使用把每种线程代码单独写出来并做对比： **单线程裸奔：（这也是一个主线程（main thread））**

```python
import time

def start():
    for i in range(1000000):
        i += i
    return

# 不使用任何线程（裸着来）
def main():
    start_time = time.time()
    for i in range(10):
        start()
    print(time.time()-start_time)
if __name__ == '__main__':
    main()
```

**输出：**

```python
6.553307056427002
```

**注意：因为每台电脑的性能不一样，所运行的结果也相对不同（请按实际情况分析）**

* * *

**接下来我们写一个多线程**

> 我们先创建个字典 **(thread\_name\_time)** 来存储我们每个线程的名称与对应的时间

```python
import threading,time

def start():
    for i in range(1000000):
        i += i
    return

# # 不使用任何线程（裸着来）
# def main():
#   start_time = time.time()
#   for i in range(10):
#       start()
#   print(time.time()-start_time)
# if __name__ == '__main__':
#   main()

def main():
    start_time = time.time()
    thread_name_time = {}# 我们先创建个字典 (thread_name_time) 用来来存储我们每个线程的名称与对应的时间

    for i in range(10):
        # 也就是说，每个线程顺序执行
        thread = threading.Thread(target=start)# target=写你要多线程运行的函数，不需要加括号
        thread.start()# 上一行开启了线程，这一行是开始运行（也就是开启个 run）
        thread_name_time[i] = thread # 添加数据到我们的字典当中，这里为什么要用i做key？这是因为这样方便我们join


    for i in range(10):
        thread_name_time[i].join()
    #   join() 等待线程执行完毕（也就是说卡在这里，这个线程执行完才会执行下一步）
    print(time.time()-start_time)

if __name__ == '__main__':
    main()
```

**输出**

```python
6.2037984102630615
```

```python
# 6.553307056427002 裸奔
# 6.2037984102630615 单线程顺序执行
# 6.429047107696533 线程并发
```

> 我们可以看到，速度上的区别不大。 多线程并发不如单线程顺序执行快 这是得不偿失的 造成这种情况的原因就是 GIL 这里是计算密集型，所以不适用

在我们执行加减乘除或者图像处理的时候，都是在从 **CPU** 上面执行才可以。Python 因为 GIL 存在，同一时期肯定只有一个线程在执行，这样这样就是造成我们开是个线程和一个线程没有太大区别的原因。 而我们的网络爬虫大多时候是属于 **IO** 密集与计算机密集 ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200726092606.png)

> BIOS：B：Base、I：Input、O：Output、S：System

也就是你电脑一开机的时候就会启动。 **1\. 计算密集型**

> 在上面的时候，我们开启了两个线程，如果这两个线程要同时执行，那同一时期 **CPU** 上只有一个线程在执行。 那从上图可知，那这两个线程就需要频繁的在上下文切换。 Ps：我们这个绿色表示我们这个线程正在执行，红色代表阻塞。 所以，我们可以明显的观察到，线程的上下文切换也是需要消耗资源的（时间-ms）不断的归还和拿取 **GIL** 等，切换上下文。明显造成很大的资源浪费。

**2\. IO 密集型**

> 我们现在假设，有个服务器程序（**Socket**）也就是我们新开的一个程序（也就是我们网络爬虫的最底层）开始爬取目标网页了，我们那个网页呢，有两个线程同时运行，我们线程二已经请求成功开始运行了，也就是上图的 （**Thread 2**）绿色一条路过去。 而我们的线程一（**Thread 1**）- **Datagram**（这里它开启了一个 **UDP**），然后等待数据建立（也就是等待哪些 **HTML、CSS 等数据返回**）也就是说，在 **Ready to receive（recvfrom）**之间都是准备阶段。这样就是有一段时间一直阻塞，而我们的线程二可以一直无停歇也不用切换上下文就一直在运行。**这样的 IO 密集型就有很大的好处**。

##### IO 密集型，这样就把我们等待的时间计算进去了，节省了大部分时间。

###### 这里我们需要注意的是，我们的多线程是运行在 IO 密集型上的，我们得区分清楚。

还有就是，资源等待，比如有时候我们使用浏览器发起了一个 **Get** 请求，那浏览器图标上面在**转圈圈**的时候就是我们请求资源等待的时间，（也就是图上面的 **Datagram 到 Ready to receive** ）数据建立到数据接收（就是转圈圈的时间）。我们完全就不需要执行它，就让它等待就好。**这个时候让另一个线程去执行就好**

> 换言之就是：第一个线程，我们爬取那个网页转圈圈的时候让另一个线程继续爬取。这样就避免了资源浪费。（把时间都利用起来）

**注意：** 请求资源是不需要 **CPU** 进行计算的，**CPU** 参与是很少的，而我们第一个例子，计算数字的 **for** 循环中，是需要 **CPU** 进行计算的。

* * *

### 5.1 Thread 直接创建子线程

#### 5.1.1 非守护线程

复杂的操作之前需要一个简单的示例开始：

```python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author：AI悦创 @DateTime ：2019/10/25 9:50 @Function ：功能  Development_tool ：PyCharm
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.

import threading, time

def start():
    time.sleep(1)
    print(threading.current_thread().name) # 当前线程名称
    print(threading.current_thread().is_alive()) # 当前线程状态
    print(threading.current_thread().ident) # 当前线程的编号

print('start')
# 要使用多线程哪个函数>>>target=函数,name=给这个多线程取个名字
# 如果你不起一个名字的话，那那它会自己去起一个名字的（pid）也就是个 ident
# 类似声明
thread = threading.Thread(target=start,name='my first thread')

# 每个线程写完你不start()的话，就类似只是声明
thread.start()
print('stop')

# 输出
start
stop
my first thread
True
2968
```

如果有参数的话，我们就对多线程参数进行传参数。代码示例：

```python
import threading, time

def start(num):
    time.sleep(num)
    print(threading.current_thread().name)
    print(threading.current_thread().isAlive())
    print(threading.current_thread().ident)

print('start')
thread = threading.Thread(target=start,name='my first thread', args=(1,))

thread.start()
print('stop')
```

解析： 我认认真看一下我们的运行结果，

start

**stop**

**my first thread**

**True**

**2968**

我们会发现并不是按我们正常的逻辑执行这一系列的代码。 而是，先执行完 **start 然后就直接 stop** 然后才会执行我们函数的其他三项。 一个线程它就直接贯穿到底了。也就是先把我们主线程里面的代码运行完，然后才会运行它里面的代码。 我们的代码并不是当代码执行到 **thread.start()** 等它执行完再执行 **print('stop')** 。而是，我们线程执行到**thread.start()** 继续向下执行，同时再执行里面的代码（也就是**start()**函数里面的代码）。(不会卡在 `thread.start()` 那里) **也不会随着主线程结束而结束**

> 因为，程序在执行到 **print('stop')** 之后就是主线程结束，而里面开的线程是我们自己开的。当我们主线程执行这个 stop 就已经结束了。 这种不会随着主线程结束而销毁的，这种线程它叫做：非守护线程

1.  主线程会跳过创建的线程继续执行；
2.  直到创建线程运行完毕；
3.  程序结束；

既然，有非守护线程。那就还有守护线程。不要急，我再举个非守护线程的例子。 首先，我们可以使用 Thread 类来创建一个线程，创建时需要指定 target 参数为运行的方法名称，如果被调用的方法需要传入额外的参数，则可以通过 `Thread`的 `args`参数来指定。示例如下：

```python
import threading, time

def target(second):
    print(f'Threading {threading.current_thread().name} is runing')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} ended')

print(f'Threading {threading.current_thread().name} is runing')

for i in [1, 5]:
    t = threading.Thread(target=target, args=[i])
    # t = threading.Thread(target=target, args=(i,))
    t.start()
print(f'Threading {threading.current_thread().name} is ended')

# 输出
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 1s
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading MainThread is ended
Threading Thread-1 ended
Threading Thread-2 ended
```

在这里我们首先声明了一个方法，叫作 target，它接收一个参数为 `second`，通过方法的实现可以发现，这个方法其实就是执行了一个 `time.sleep` 休眠操作，`second`参数就是休眠秒数，其前后都 `print`了一些内容，其中线程的名字我们通过 `threading.current_thread().name` 来获取出来，如果是主线程的话，其值就是 `MainThread`，如果是子线程的话，其值就是 `Thread-*`。 然后我们通过 `Thead`类新建了两个线程，`target`参数就是刚才我们所定义的方法名，`args`以列表的形式传递。两次循环中，这里 `i` 分别就是 `1` 和 `5`，这样两个线程就分别休眠 `1` 秒和 `5` 秒，声明完成之后，我们调用 `start` 方法即可开始线程的运行。 观察结果我们可以发现，这里一共产生了三个线程，分别是主线程 `MainThread`和两个子线程 `Thread-1、Thread-2`。另外我们观察到，主线程首先运行结束，紧接着 `Thread-1、Thread-2` 才接连运行结束，分别间隔了 `1` 秒和 `4` 秒。这说明主线程并没有等待子线程运行完毕才结束运行，而是直接退出了，有点不符合常理。 如果我们想要主线程等待子线程运行完毕之后才退出，可以让每个子线程对象都调用下 `join`方法，实现如下：

```python
for i in [1, 5]:
    t = threading.Thread(target=target, args=[i])
    t.start()
    t.join()

# 输出
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 1s
Threading Thread-1 ended
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading Thread-2 ended
Threading MainThread is ended
```

这样，主线程必须等待子线程都运行结束，主线程才继续运行并结束。

### 5.2 继承 Thread 类创建子线程

另外，我们也可以通过继承 Thread 类的方式创建一个线程，该线程需要执行的方法写在类的 run 方法里面即可。上面的例子的等价改写为：

```python
import threading, time
class MyThread(threading.Thread):
    def __init__(self, second):
        threading.Thread.__init__(self)
        self.second = second
    def run(self):
        print(f'Threading {threading.current_thread().name} is runing')
        print(f'Threading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is runing')

for i in [1, 5]:
    t = MyThread(i)
    t.start()
    t.join()
print(f'Threading {threading.current_thread().name} is ended')


# 输出
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 1s
Threading Thread-1 is ended
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading Thread-2 is ended
Threading MainThread is ended
```

可以看到，两种实现方式，其运行效果是相同的。

### 5.3 守护线程

在线程中有一个叫作守护线程的概念，如果一个线程被设置为守护线程，那么意味着这个线程是“不重要”的，这意味着，如果主线程结束了而该守护线程还没有运行完，那么它将会被强制结束。在 Python 中我们可以通过 `setDaemon`方法来将某个线程设置为守护线程。 如果要修改成守护线程，那你就得在 `thread.start()`前面加一个：

```python
thread.setDaemon(True)
```

需要在我们启动之前设置。 **示例一如下：** 添加之前：

```python
import threading, time

def start(num):
    time.sleep(num)
    print(threading.current_thread().name) # 当前线程的名字
    print(threading.current_thread().isAlive())
    print(threading.current_thread().ident)

print('start') # 主线程开始
thread = threading.Thread(target=start,name='my first thread', args=(1,))# 可以使用 for 循环来添加多个
thread.start()
print('stop') # 主线程结束

# 运行结果
start
stop
my first thread
True
15816
```

添加之后：

```python
import threading, time

def start(num):
    time.sleep(num)
    print(threading.current_thread().name) # 当前线程的名字
    print(threading.current_thread().isAlive())
    print(threading.current_thread().ident)

print('start') # 主线程开始
thread = threading.Thread(target=start,name='my first thread', args=(1,))# 可以使用 for 循环来添加多个
thread.setDaemon(True) # 在 start 开始之前设置
thread.start()
print('stop') # 主线程结束

# 运行结果
start
stop
```

我们可以看见，程序直接运行：start、stop，执行到 **print('stop') 它就结束了。**也就随着我们的主线程结束而结束。并不管它里面还有什么没有执行完。（也不会管他里面的 `time.sleep()`）我们的主线程一结束，我们的守护线程就会随着主线程一起销毁。 **我们日常启动的是非守护线程，守护线程用的较少。** 守护线程会伴随主线程一起结束，`setDaemon`设置为 True 即可。 **示例二如下：** 添加之前：

```python
import threading, time

def target(second):
    print(f'Threading {threading.current_thread().name} is runing')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is runing')
t1 = threading.Thread(target=target, args=[2])
t1.start()
t2 = threading.Thread(target=target, args=[5])
t2.start()
print(f'Threading {threading.current_thread().name} is ended')

# 运行结果
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 2s
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading MainThread is ended
Threading Thread-1 is ended
Threading Thread-2 is ended
```

添加之后：

```python
import threading, time

def target(second):
    print(f'Threading {threading.current_thread().name} is runing')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is runing')
t1 = threading.Thread(target=target, args=[2])
t1.start()
t2 = threading.Thread(target=target, args=[5])
t2.setDaemon(True)
t2.start()
print(f'Threading {threading.current_thread().name} is ended')

# 运行结果
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 2s
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading MainThread is ended
Threading Thread-1 is ended
```

在这里我们通过 `setDaemon`方法将 `t2`设置为了守护线程，这样主线程在运行完毕时，`t2`线程会随着线程的结束而结束。 运行结果：

```python
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 2s
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading MainThread is ended
Threading Thread-1 is ended
```

可以看到，我们没有看到 `Thread-2`打印退出的消息，`Thread-2` 随着主线程的退出而退出了。 不过细心的你可能会发现，这里并没有调用 `join`方法，如果我们让 `t1`和 `t2`都调用 `join`方法，主线程就会仍然等待各个子线程执行完毕再退出，不论其是否是守护线程。

### 5.4 互斥锁

接下来是比较难的知识点，还是从简单的知识点开始。 **比方**说我们现在有两个线程，一个是求加一千万次，另一个是减一千万次。 按原本得计划来说，一个加一千万一个减一千万结果应该还是零。可是最终得结果并不是等于零，我们多运行几次会发现几次得出来得结果并不相同。多线程代码如下：

```python
import threading
import time

number = 0

def addNumber(i):
    time.sleep(i)
    global number
    for i in range(1000000):
        number += 1
    print("加",number)

def downNumber(i):
    time.sleep(i)
    global number
    for i in range(1000000):
        number -= 1
    print("减",number)

print("start") # 输出一个开始
thread = threading.Thread(target = addNumber, args=(2,)) #开启一个线程（声明）
thread2 = threading.Thread(target = downNumber, args=(2,)) # 开启第二个线程（声明）
thread.start() # 开始
thread2.start() # 开始
thread.join()
thread2.join()
# join 阻塞在这里，直到我们得阻塞线程执行完毕才会向下执行
print("外", number)
print("stop")
```

就算单线程也会出现两个值：1000000 与 -1000000，两个函数谁先运行就是输出谁的结果，为什么呢？因为两个函数调用的是全局变量 **number** 所以，如果先运行加法函数，加法得到的结果是 1000000 ，那全局下的 number 的值也会变成：1000000 ，那减法的操作亦然就是 0。反过来也是一个意思。代码如下：

```python
import threading
import time

number = 0

def addNumber(i = None):
    # time.sleep(i)
    global number
    for i in range(1000000):
        number += 1
    print("加",number)

def downNumber(i = None):
    # time.sleep(i)
    global number
    for i in range(1000000):
        number -= 1
    print("减",number)

addNumber()
downNumber()
print(number)

# 运行结果
加 1000000
减 0
0

# 反过来运行
downNumber()
addNumber()
print(number)

# 运行结果
减 -1000000
加 0
0

# 再来一个差不多的例子：
import threading
import time

number = 0

def addNumber():
    global number
    for i in range(1000000):
        number += 1
    print("加",number)
    return number

def downNumber():
    global number
    for i in range(1000000):
        number -= 1
    print("减",number)
    return number

sum_num = downNumber() + addNumber()
print("Result", sum_num)

# 输出
减 -1000000
加 0
Result -1000000


# 修改以下代码，其他不变：
sum_num = addNumber() + downNumber()

# 输出
加 1000000
减 0
Result 1000000
```

由上面的多线程代码，我可以发现结果：两个线程操作同一个数字，最后得到的数字是混乱的。为什么说是混乱的呢？ 我们现在所要做的是一个赋值，`number += 1` 其实也就是 `number = number + 1`，的这个操作。而在我们的 Python 当中，我们是先：计算右边的，然后赋值给左边的，一共两步。 我先来看一下正确的运行流程：

```python
# 我们的 number = 0
# 第一步是先运行我们的代码：
a = number + 1 # 等价于 0+1=1 
# 也就是先运行右边的，然后赋值给 a

number = a # 然后，再把 a 的结果赋值个 number

# 上面运行完加法之后，我们加下来运行减肥的操作。
b = number - 1 # 等价于 1-1 = 0
# 然后，赋值个 number

# 最后 number 等于 0
number = 0
```

上面的过成是正确的流程，可在多线程里面呢？

```python
number = 0 # 开始初始值 0
a = number+1 # 等价于 0+1=1
# 这个地方要注意！！！
# 在运行完上面一步的时候，还没来得急把结果赋值给 number
# 就开始运行减法操作：
b = number-1 # 等价于 0-1=-1
# 然后，这两个运行结束之后就被赋值：
number=b # b = -1
number=a # a = 1

# 最终得结果为：
number = 1
```

上面就是我们刚才结果错乱得原因，也就是说：我们计算和赋值是两部分，但是该多线程它没有顺序执行，这也就是我们所说的线程不安全。 因为，执行太快了，两个线程交互交织在一起，最终得到我们这个错误结果。以上就是线程不安全的问题。 这就是需要 **Lock 锁**，给它上一把锁，来达到我们 **number** 的效果，这个时候为了避免错误，我们要给他上一把锁了。再给你讲解上锁之前呢，**接下来，我们来讲一点复杂的例子：** 在一个进程中的**多个线程是共享资源的**， **比如** 在一个进程中，有一个全局变量 count 用来计数，现在我们声明多个线程，每个线程运行时都给 `count` 加 `1`，让我们来看看效果如何，代码实现如下：

```python
import threading, time

count = 0

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        temp = count + 1
        time.sleep(0.001)
        count = temp
threads = []
for _ in range(1000):
    thread = MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
# print(len(threads))
print(f'Final count: {count}')
```

在这里，我们声明了 1000 个线程，每个线程都是现取到当前的全局变量 count 值，然后休眠一小段时间，然后对 count 赋予新的值。 那这样，按照常理来说，最终的 count 值应该为 1000。但其实不然，我们来运行一下看看。 运行结果如下：

```python
Final count: 69
```

最后的结果居然只有 69，而且多次运行或者换个环境运行结果是不同的。 **这是为什么呢？** 因为 count 这个值是共享的，每个线程都可以在执行 temp = count 这行代码时拿到当前 count 的值，但是这些线程中的一些线程可能是并发或者并行执行的，这就导致不同的线程拿到的可能是同一个 count 值，最后导致有些线程的 count 的加 1 操作并没有生效，导致最后的结果偏小。 所以，如果多个线程同时对某个数据进行读取或修改，就会出现不可预料的结果。为了避免这种情况，我们需要对多个线程进行同步，要实现同步，我们可以对需要操作的数据进行加锁保护，这里就需要用到 `threading.Lock`了。 **加锁保护是什么意思呢？** 就是说，某个线程在对数据进行操作前，需要先加锁，这样其他的线程发现被加锁了之后，就无法继续向下执行，会一直等待锁被释放，只有加锁的线程把锁释放了，其他的线程才能继续加锁并对数据做修改，修改完了再释放锁。这样可以确保同一时间只有一个线程操作数据，多个线程不会再同时读取和修改同一个数据，这样最后的运行结果就是对的了。 我们可以将代码修改为如下内容： 示例一的修改：

```python
import threading
import time

lock = threading.Lock() # 创建一个最简单的 读写锁
number = 0

def addNumber():
    global number
    for i in range(1000000):
        lock.acquire() # 先获取
        number += 1
        # 中间的这个过程让他强制有这个计算和赋值的过程，也就是让他执行完这两个操作，后再切换。
        # 这样就不会完成计算后，还没来的及赋值就跑到下一个去了。
        # 这样也就防止了线程不安全的情况
        lock.release() # 再释放

def downNumber():
    global number
    for i in range(1000000):
        lock.acquire()
        number -= 1
        lock.release()

print("start") # 输出一个开始
thread = threading.Thread(target = addNumber) #开启一个线程（声明）
thread2 = threading.Thread(target = downNumber) # 开启第二个线程（声明）
thread.start() # 开始
thread2.start() # 开始
thread.join()
thread2.join()
# join 阻塞在这里，直到我们得阻塞线程执行完毕才会向下执行
print("外", number)
print("stop")

# 输出
start
外 0
stop
```

在代码：**lock.acquire() 与 lock.release()** 中间的这个过程让它强制有这个计算和赋值的过程，也就是让他执行完这两个操作，后再切换。这样就不会完成计算后，还没来的及赋值就跑到下一个去了。这样也就防止了线程不安全的情况。 然后，就是我们第一个线程拿到这把锁的 **lock.acquire()** 了，那另一个线程就会在 **lock.acquire()** 阻塞了，直到我们另一个线程把 **lock.release()** 锁释放，然后拿到锁执行，就这样不断地切换拿锁执行。 **死锁：**就是前面的线程拿到锁之后，运行完却不释放锁，下一个线程在等待前一个线程释放锁，这种就是死锁。说的直白一点就是，相互等待。就像照镜子一样，你中有我，我中有你。也就是在没有 release 的这种情况。（你等我表白，我等你表白） **示例二的加锁**

```python
# -*- coding: utf-8 -*-
# @Author: clela
# @Date:   2020-04-08 22:08:33
# @Last Modified by:   clela
# @Last Modified time: 2020-04-09 10:31:59
import threading, time

count = 0

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire() # 获取锁
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock.release() # 释放锁

lock = threading.Lock()
threads = []
for _ in range(1000):
    thread = MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(f'Final count: {count}')
```

在这里我们声明了一个 lock 对象，其实就是 threading.Lock 的一个实例，然后在 run 方法里面，获取 count 前先加锁，修改完 count 之后再释放锁，这样多个线程就不会同时获取和修改 count 的值了。 运行结果如下：

```python
Final count: 1000
```

这样运行结果就正常了。 关于 Python 多线程的内容，这里暂且先介绍这些，关于 `theading`更多的使用方法，如信号量、队列等，可以参考官方文档：https://docs.python.org/zh-cn/3.7/library/threading.html#module-threading。

### 5.5 递归锁 RLOCK

再次复用，一个锁可以再嵌套一个锁。向我们上面的普通锁，一个线程里面，你只能获取一次。如果获取第二次就会报错。 递归锁什么时候用呢？需要更低精度的，力度更小，为了更小的力度。

```python
import threading
import time

class Test:
    rlock = threading.RLock()
    def __init__(self):
        self.number = 0

    def execute(self, n):
        # 原本是获取锁和释放锁，那如果有时候你忘记了写 lock.release() 那就变成了死锁。
        # 而 with 可以解决这个问题。
        with Test.rlock:
            # with 内部有个资源释放的机制
            self.number += n

    def add(self):
        with Test.rlock:
            self.execute(1)

    def down(self):
        with Test.rlock:
            self.execute(-1)

def add(test):
    for i in range(1000000):
        test.add()

def down(test):
    for i in range(1000000):
        test.down()

if __name__ == '__main__':
    thread = Test() # 实例化
    t1 = threading.Thread(target=add, args=(thread,))
    t2 = threading.Thread(target=down, args=(thread,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(t.number)

```

我们会发现这个递归锁是比较耗费时间的，也就死我们获取锁与释放锁都是进行上下文切换导致资源消耗的，所以说开启的锁越多，所耗费的资源也就越多，程序的运行速度也就越慢。一些大的工程很少上这么多的锁，因为这个锁的速度会拖慢你整个程序的运行速度。所以得思考好，用不用这些东西。

### 5.6 Python 多线程的问题

由于 Python 中 GIL 的限制，导致不论是在单核还是多核条件下，在同一时刻只能运行一个线程，导致 Python 多线程无法发挥多核并行的优势。 GIL 全称为 Global Interpreter Lock，中文翻译为全局解释器锁，**其最初设计是出于数据安全而考虑的。** 在 Python 多线程下，每个线程的执行方式如下：

*   获取 GIL
*   执行对应线程的代码
*   释放 GIL

可见，某个线程想要执行，必须先拿到 GIL，我们可以把 GIL 看作是通行证，并且在一个 Python 进程中，GIL 只有一个。拿不到通行证的线程，就不允许执行。这样就会导致，即使是多核条件下，一个 Python 进程下的多个线程，同一时刻也只能执行一个线程。 不过对于爬虫这种 IO 密集型任务来说，这个问题影响并不大。而对于计算密集型任务来说，由于 GIL 的存在，多线程总体的运行效率相比可能反而比单线程更低。

### 5.7 避免 GIL

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200726092623.png) 前面开头已经提到：因为 **GIL** 的存在，所以不管我们开了多少线程，同一时间始终只有一个线程在执行。那我们该如何避免 **GIL** 呢？ 那这样的话，我们**不开线程**不就行，(它的的存在已经无法避免，那我们选择不使用它不就相当于不存在嘛）。那这是，你会想：那不开线程我们开啥呢？ 问的好！ 我们来开：**进程**，那怎么说？别急！请听我细细道来。 比方你有 **3 个 CPU**（当然，你可能有更多，这里就按 **3** 个 **CPU**来为例子），那我们就开 **3 个进程**就好。一个 **CPU** 上运行就好。 **Ps：我们的进程是可以同时运行的。** 我们可以看一下下面的图片： **任务管理器** ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200726092631.png) 我们 **任务管理** 上的每一项都是一个进程。 多进程比多线程不好的地方是什么呢？

> 多进程的创建和销毁开销也会更大，成本高。 你可能线程可以开许多的线程，但你的进程就是看你的 **CPU** 数量。 进程间无法看到对方数据，需要使用栈或者队列进行获取。 每个进程之间都是独立的。 就好像我们上面的谷歌浏览器和我们的 Pycharm 是没有任何关系的，谷歌浏览器上面的数据肯定不可能让 Pycharm 看到。这就是我们所说的进程之间的独立性。 如果你想要一个进行抓取数据，一个进行调用数据，那这时是不能直接调用的，需要你自己定义个结构才能使用。>>> 编程复杂度提升。

* * *

> 学员问题：任务管理器上面超过五六个进程。都是进程的话，怎么能开那么多呢？ 答：我们一个 CPU 不止能执行一个进程，就比如我的一个 CPU 里面密麻麻有许多进程。（比方我现在开六个进程）并发执行的。只不过计算机执行的速度非常快，这里我简单讲一下哈。这是计算机原理的课。 不管是任何操作系统，现在就拿单核操作系统来说：我们假设现在只有一个 CPU ，一个 CPU 里面六个**进程**，同一时间它只有一个进程在运行。不过我们计算执行速度非常快，这个程序执行完，它就会执行一个**上下文切换**，执行下一个。（因为，它执行的速度非常快，你就会感觉是并发执行一样。） 实际上，一个 CPU 同一时间只有一个进程在执行，一个进程里面它只有一个线程在执行。（当然，这个单核是五六年前了。现在肯定至少有双核。 那就说有第二个 CPU 了。 而第二个和 CPU 上面又有许多个 **进程**，两个 **CPU** 是互不相干。 那这时候，第一个 CPU 上面运行一个进程，而我们的第二个 CPU 上面也有一个进程，两个是互补相干。 （就相当于你开了两台电脑。） 但是同一个 CPU 在同一时间只有一个就进程。（不管你（电脑）速度多么快，实际上本质上（在那一秒）只有一个进程在执行。**如果你是双核，那就有两个进程。（四核就有四个进程）**

Python 有个不好的地方，刚刚上面讲到，如果我们有两个 CPU 那就有两个进程在执行（那四个 CPU 就是四个进程在执行），**但是因为 Python 当中存在着 GIL，它即使有四个 CPU 每次也只有一个线程能进去，**也就是说：同一时间当中，一个 CPU 上的一个进程中的一个线程在执行。剩下的都不能运行，我们的 Python 不能利用多核。 如果，大家用的是 C、Java、Go 这种的就没有这个说法了。

### 5.8 线程池

我找了许多包，这个包还是不错的：`Pip install threadpool`

```python
# project = 'Code', file_name = '线程池', author = 'AI悦创'
# time = '2020/3/3 0:05', product_name = PyCharm
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.

import time
import threadpool

# 执行比较耗时的函数，需要开多线程
def get_html(url):
    time.sleep(3)
    print(url)
# 按原本的单线程运行时间为：300s
# 而多线程池的化：30s
# 使用多线程执行 telent 函数
urls = [i for i in range(100)]
pool = threadpool.ThreadPool(10) # 建立线程池

# 提交任务给线程池
requests = threadpool.makeRequests(get_html, urls)

# 开始执行任务
for req in requests:
    pool.putRequest(req)
pool.wait()
```