---
title: 02|小菜成长之路，警惕沦为 API 调用侠
tags: []
id: '1663'
categories:
  - - Python源码解析
date: 2021-05-10 20:43:43
---

![image.png](https://img-blog.csdnimg.cn/img_convert/7929c9d2898243b6ac15da7c5b0fd144.png) 小菜(化名)在某互联网公司担任运维工程师，负责公司后台业务的运维保障工作。由于自己编程经验不多，平时有不少工作需要开发协助。 听说 Python 很火，能快速开发一些运维脚本，小菜也加入 Python 大军学起来。Python 语言确实简单，小菜很快就上手了，觉得自己应对运维开发工作已经绰绰有余，便不再深入研究。

# 背景

这天老板给小菜派了一个数据采集任务，要实时统计服务器 TCP 连接数。 需求背景是这样的：**开发同事需要知道服务的连接数以及不同状态连接的比例，以便判断服务状态**。因此，小菜需要开发一个脚本，定期采集并报告 TCP 连接数，提交数据格式定为 json：

```json
{
  "LISTEN": 4,
  "ESTABLISHED": 100,
  "TIME_WAIT": 10
}
```

作为运维工程师，小菜当然知道怎么查看系统 TCP 连接。Linux 系统中有两个命令可以办到，netstat 和ss：

```bash
$ netstat -nat
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 127.0.0.1:8388          0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 192.168.56.3:22         192.168.56.1:54983      ESTABLISHED
tcp6       0      0 :::22                   :::*                    LISTEN
```

```bash
$ ss -nat
State                    Recv-Q                    Send-Q                                         Local Address:Port                                         Peer Address:Port
LISTEN                   0                         128                                                127.0.0.1:8388                                              0.0.0.0:*
LISTEN                   0                         128                                            127.0.0.53%lo:53                                                0.0.0.0:*
LISTEN                   0                         128                                                  0.0.0.0:22                                                0.0.0.0:*
ESTAB                    0                         0                                               192.168.56.3:22                                           192.168.56.1:54983
LISTEN                   0                         128                                                     [::]:22                                                   [::]:*
```

小菜还知道 ss 命令比 netstat 命令要快，但至于为什么，小菜就不知道了。小菜很快找到老板，提出了自己的解决方案：**写一个 Python 程序，调用 ss 命令采集 TCP 连接信息，然后再逐条统计。** 老板告诉小菜，线上服务器很多都是最小化安装，并不能保证每台机器上都有ss或者netstat命令。老板还告诉小菜，程序开发要学会**站在巨人的肩膀上**。动手写代码前，先调研一番，看是否有现成的解决方案。**切忌重复造轮子**，浪费时间不说，可能代码质量还差，效果也不好。 最后老板给小菜指了条明路，让他回去再看看 psutil。psutil 是一个 Python 第三方包，用于采集系统性能数据，包括：CPU、内存、磁盘、网卡以及进程等等。临走前，老板还叮嘱小菜，完成工作后花点时间研究下这个库。

# psutil 方案

小菜搜索 psutil 发现，还有这么顺手的第三方库，喜出望外！他立马装好 psutil，准备开干：

```bash
$ pip install psutil
```

导入 psutil 后，一个函数调用就可以拿到系统所有连接，连接信息非常丰富：

```bash
>>> import psutil
>>> for conn in psutil.net_connections('tcp'):
...     print(conn)
...
sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='192.168.56.3', port=22), raddr=addr(ip='192.168.56.1', port=54983), status='ESTABLISHED', pid=None)
sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=8388), raddr=(), status='LISTEN', pid=None)
sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=22), raddr=(), status='LISTEN', pid=None)
sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.53', port=53), raddr=(), status='LISTEN', pid=None)
sconn(fd=-1, family=<AddressFamily.AF_INET6: 10>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='::', port=22), raddr=(), status='LISTEN', pid=None)
```

小菜很满意，感觉不用花多少时间就可搞定数据采集需求了，准时下班有望！噼里啪啦，很快小菜就写下这段代码：

```bash
import psutil
from collections import defaultdict

# 遍历每个连接，按连接状态累加
stats = defaultdict(int)
for conn in psutil.net_connections('tcp'):
    stats[conn.status] += 1

# 遍历每种状态，输出连接数
for status, count in stats.items():
    print(status, count)
```

小菜接着在服务器上测试这段代码，功能完全正常：

```bash
ESTABLISHED 1
LISTEN 4
```

小菜将数据采集脚本提交，并按既定节奏逐步发布到生产服务器上。开发同事很快就看到小菜采集的数据，都夸小菜能力不错，需求完成得很及时。小菜也很高兴，感觉 Python 没白学。如果用其他语言开发，说不定现在还在加班加点呢！**Life is short, use Python!** 果然没错！ 小菜愈发自信，早就把老板的话抛到脑后了。psutil 这个库这么好上手，有啥好深入研究的？

# 内存悲剧

突然有一天，其他同事紧急告诉小菜，他开发的采集脚本占用很多内存，CPU 也跑到了 100%，已经开始影响线上服务了。小菜还沉浸在成功的喜悦中，收到这个反馈如同晴天霹雳，有点举手无措。 业务同事告诉小菜，受影响的机器系统连接数非常大，质疑小菜是不是脚本存在性能问题。**小菜觉得很背，脚本只是调用 psutil 并统计数据，怎么可能存在性能问题？** 脚本影响线上服务，小菜压力很大，但不知道如何是好，只能跑去找老板寻求帮助。 老板要小菜第一时间停止数据采集，降低影响。复盘故障时，老板很敏锐地问小菜，是不是用容器保存所有连接了？小菜自己并没有，但是 psutil 这么做了：

```python
>>> psutil.net_connections()
[sconn(fd=-1, family=<AddressFamily.AF_INET6: 10>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='::', port=22), raddr=(), status='LISTEN', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=22), raddr=(), status='LISTEN', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.53', port=53), raddr=(), status='LISTEN', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='10.0.2.15', port=68), raddr=(), status='NONE', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='127.0.0.1', port=8388), raddr=(), status='NONE', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='192.168.56.3', port=22), raddr=addr(ip='192.168.56.1', port=54983), status='ESTABLISHED', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='127.0.0.53', port=53), raddr=(), status='NONE', pid=None), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=8388), raddr=(), status='LISTEN', pid=None)]
```

**psutil 将采集到的所有 TCP 连接放在一个列表里返回。如果服务器上有十万个 TCP 连接，那么列表里将有十万个连接对象。难怪采集脚本吃了那么多内存！** **老板告诉小菜，可以用生成器加以解决。与列表不同，生成器逐个返回数据，因此不会占用太多内存。** Python2 中 range 和 xrange 函数的区别也是一样的道理。 小菜从 pstuil fork 了一个分支，并将 net\_connections 函数改造成 **生成器** ：

```python
def net_connections():
    while True:
        if done:
            break

        # 解析一个TCP连接
        conn = xxx

        yield conn
```

代码上线后，采集脚本内存占用量果然下降了！**生成器**将统计算法的空间复杂度由原来的 O(n) 优化为O(1)。经过这次教训，小菜不敢再盲目自信了，他决定抽时间好好看看 psutil 的源码。

# 源码体会

深入学习源码后，小菜发现原来 psutil 采集 TCP 连接数的秘笈是：从 `/proc/net/tcp` 以及 `/proc/net/tcp6` 读取连接信息。由此，他还进一步了解到 procfs，这是一个伪文件系统，将内核空间信息以文件方式暴露到用户空间。`/proc/net/tcp` 文件则是提供内核 TCP 连接信息：

```bash
$ cat /proc/net/tcp
  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode
   0: 0100007F:20C4 00000000:0000 0A 00000000:00000000 00:00000000 00000000 65534        0 18183 1 0000000000000000 100 0 0 10 0
   1: 3500007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   101        0 16624 1 0000000000000000 100 0 0 10 0
   2: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 18967 1 0000000000000000 100 0 0 10 0
   3: 0338A8C0:0016 0138A8C0:D6C7 01 00000000:00000000 02:00023B11 00000000     0        0 22284 4 0000000000000000 20 13 23 10 20
```

小菜还注意到，连接信息看起来像个自定义类对象，但其实是一个 namedtuple：

```bash
# psutil.net_connections()
sconn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr',
                             'status', 'pid'])
```

小菜一开始并不知道作者为啥要这么做。后来，小菜开始研究 Python 源码，学习了 Python 类机制后他恍然大悟。Python 自定义类的每个实例对象均需要一个 dict 来保存对象属性，这也就是对象的属性空间。如果用自定义类来实现，每个连接都需要创建一个字典，而字典又是散列表实现的。如果系统存在成千上万的连接，开销可想而知。 小菜将学到的知识总结起来：对于**数量大**而**属性固定**的实体，没有必要用自定义类来实现，用 namedtuple更合适，开销更小。由此，小菜不经由衷佩服 psutil 的作者。

# CPU悲剧

后来小菜又收到业务反馈，采集脚本在高并发的服务器上，CPU 使用率很高，需要再优化一下。小菜回忆psutil 源码，很快就找到了性能瓶颈处：psutil 将连接信息所有字段都解析了，而采集脚本只需要其中的状态字段而已。跟老板商量后，小菜决定自行读取 procfs 来实现采集脚本，只解析状态字段，避免不必要的计算开销。**「只提取有需要的内容，不需要的内容舍去」**

## procfs 方案

直接读取 `/proc/net/tcp`，可以得到完整的 TCP 连接信息：

```python
>>> with open('/proc/net/tcp') as f:
...     for line in f:
...         print(line.rstrip())
...
  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode
   0: 0100007F:20C4 00000000:0000 0A 00000000:00000000 00:00000000 00000000 65534        0 18183 1 0000000000000000 100 0 0 10 0
   1: 3500007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   101        0 16624 1 0000000000000000 100 0 0 10 0
   2: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 18967 1 0000000000000000 100 0 0 10 0
   3: 0338A8C0:0016 0138A8C0:D6C7 01 00000000:00000000 02:0007169E 00000000     0        0 22284 3 0000000000000000 20 20 33 10 20
```

其中，IP、端口、状态等字段都是以十六进制编码的。例如，st 列表示状态，状态码 0A 表示 LISTEN。很快小菜就写下这段代码：

```python
from collections import defaultdict

stat_names = {
    '0A': 'LISTEN',
    '01': 'ESTABLISHED',
    # ...
}

# 遍历每个连接，按连接状态累加
stats = defaultdict(int)

with open('/proc/net/tcp') as f:
    # 跳过表头行
    f.readline()

    for line in f:
        st = line.strip().split()[3]
        stats[st] += 1

for st, count in stats.items():
    print(stat_names[st], count)
```

现在，小菜写代码比之前讲究多了。在统计连接数时，他并不急于将状态码解析成名字，而是按原样统计。等统计完成，他再一次性转换，这样状态码转换开销便降到最低：O(1) 而不是 O(n)。 这次改进符合业务同事预期，但小菜决定好好做一遍性能测试，不打无准备之仗。他找业务同事要了一个连接数最大的 `/proc/net/tcp` 样本，拉到本地测试。测试结果还算符合预期，采集脚本能够扛住十万连接采集压力。 性能测试中，小菜发现了一个比较奇怪的问题。同样的连接规模，把 `/proc/net/tcp` 拉到本地跑比直接在服务器上跑要快，而本地电脑性能肯定比不上服务器。他百思不得其解，又去找老板帮忙。 老板很快指出到其中的区别，将 `/proc/net/tcp` 拉到本地就成为普通**磁盘文件**，而 procfs 是内核映射出来的**伪文件**，并不是磁盘文件。他让小菜研究一下 Python 文件 IO 以及内核 IO 子系统在处理这两种文件时有什么区别，还让小菜特别留意 IO 缓冲区大小。

## IO 缓冲

小菜打开一个普通的磁盘文件，发现 Python 选的默认缓冲区大小是 4K(读缓存对象头152字节)：

```python
>>> f = open('test.py')
>>> f.buffer.__sizeof__()
4248
```

但是如果打开的是 procfs 文件，Python 选的缓冲区却只有 1K，相差了4倍呢！

```python
>>> f = open('/proc/net/tcp')
>>> f.buffer.__sizeof__()
1176
```

因此，理论上 Python 默认读取 procfs 发生的上下文切换次数是普通磁盘文件的 4倍，怪不得会慢。虽然小菜还不知道这种现象背后的原因，但是他已经知道怎么进行优化了。随即他决定将缓冲区设置为 1M以上，尽量避免 IO 上下文切换，以空间换时间：

```python
with open('/proc/net/tcp', buffering=1*1024*1024) as f:
    # ...
```

经过这次优化，采集脚本在大部分服务器上运行良好，基本可以高枕无忧了。而小菜也意识到**编程语言**以及**操作系统**等底层基础知识的重要性，他开始制定学习计划补全计算机基础知识。

# netlink 方案

后来负载均衡团队找到小菜，他们也想统计服务器上的连接信息。由于负载均衡服务器作为入口转发流量，连接数规模特别大，达到几十万，将近百万的规模。小菜决定好好进行性能测试，再视情况上线。 测试结果并不乐观，采集脚本要跑几十秒钟才完成，CPU 跑到 100%。小菜再次调高 IO 缓冲区，但效果不明显。小菜又测试了 ss 命令，发现 ss 命令要快很多。由于之前尝到了阅读源码的甜头，小菜很想到 ss 源码中寻找秘密。 由于项目时间较紧，老板提醒小菜先用 strace 命令追踪 ss 命令的系统调用，便可快速获悉 ss 的实现方式。老板演示了 strace 命令的用法，很快就找到了 ss 的秘密——Netlink：

```python
$ strace ss -nat
...
socket(AF_NETLINK, SOCK_RAWSOCK_CLOEXEC, NETLINK_SOCK_DIAG) = 3
...
```

Netlink套接字是 Linux 提供通讯机制，可用于内核与进程间、进程与进程间通讯。Netlink 下的 sock\_diag 子系统，提供了一种从内核获取套接字信息的新方式。 与 procfs 不同，sock\_diag 采用网络通讯的方式，内核作为服务端接收客户端进程查询请求，并以二进制数据包响应查询结果，效率更高。这就是 ss 比 netstat 更快的原因，ss 采用 Netlink 机制，而 netstat 采用 procfs 机制。 很不幸 Python 并没有提供 Netlink API，一般人可能又要干着急了。好在小菜先前有意识地研究了部分Python 源码，对 Python 的运行机制有所了解。他知道可以用 C 写一个 Python 扩展模块，在 C 语言中调用原生系统调用。 编写 Python C 扩展模块可不简单，对编程功底要求很高，必须全面掌握 Python 运行机制，特别是对象内存管理。一朝不慎可能导致程序异常退出、内存泄露等棘手问题。好在小菜已经不是当年的小菜了，他经受住了考验。 小菜的扩展模块上线后，效果非常好，顶住了百万级连接的采集压力。一个看似简单得不能再简单的数据采集需求，背后涉及的知识可真不少，没有一定的水平还真搞不定。好在小菜成长很快，他最终还是彻底地解决了性能问题，找回了久违的信心。

# 内核模块方案

虽然性能问题已经彻底解决，小菜还是没有将其淡忘。他时常想：如果可以将统计逻辑放在内核空间做，就不用在内核和进程之间传递大量连接信息了，效率应该是最高的！受限于当时的知识水平，小菜还没有能力实现这个设想。 后来小菜在研究 Linux 内核时，发现可以用内核模块来扩展内核的功能，结合 procfs 的工作原理，他找到了技术方案！他顺着 `/proc/net/tcp` 在内核中的实现源码，依样画葫芦写了这个内核模块：

```python
#include <linux/module.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <net/tcp.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Xiaocai");
MODULE_DESCRIPTION("TCP state statistics");
MODULE_VERSION("1.0");

// 状态名列表
static char *state_names[] = {
    NULL,
    "ESTABLISHED",
    "SYN_SENT",
    "SYN_RECV",
    "FIN_WAIT1",
    "FIN_WAIT2",
    "TIME_WAIT",
    "CLOSE",
    "CLOSE_WAIT",
    "LAST_ACK",
    "LISTEN",
    "CLOSING",
    NULL
};


static void stat_sock_list(struct hlist_nulls_head *head, spinlock_t *lock,
    unsigned int state_counters[])
{
    // 套接字节点指针(用于遍历)
    struct sock *sk;
    struct hlist_nulls_node *node;

    // 链表为空直接返回
    if (hlist_nulls_empty(head)) {
        return;
    }

    // 自旋锁锁定
    spin_lock_bh(lock);

    // 遍历套接字链表
    sk = sk_nulls_head(head);
    sk_nulls_for_each_from(sk, node) {
        if (sk->sk_state < TCP_MAX_STATES) {
            // 自增状态计数器
            state_counters[sk->sk_state]++;
        }
    }

    // 自旋锁解锁
    spin_unlock_bh(lock);
}


static int tcpstat_seq_show(struct seq_file *seq, void *v)
{
    // 状态计数器
    unsigned int state_counters[TCP_MAX_STATES] = { 0 };
    unsigned int state;

    // TCP套接字哈希槽序号
    unsigned int bucket;

    // 先遍历Listen状态
    for (bucket = 0; bucket < INET_LHTABLE_SIZE; bucket++) {
        struct inet_listen_hashbucket *ilb;

        // 哈希槽
        ilb = &tcp_hashinfo.listening_hash[bucket];

        // 遍历链表并统计
        stat_sock_list(&ilb->head, &ilb->lock, state_counters);
    }

    // 遍历其他状态
    for (bucket = 0; bucket < tcp_hashinfo.ehash_mask; bucket++) {
        struct inet_ehash_bucket *ilb;
        spinlock_t *lock;

        // 哈希槽链表
        ilb = &tcp_hashinfo.ehash[bucket];
        // 保护锁
        lock = inet_ehash_lockp(&tcp_hashinfo, bucket);

        // 遍历链表并统计
        stat_sock_list(&ilb->chain, lock, state_counters);
    }

    // 遍历状态输出统计值
    for (state = TCP_ESTABLISHED; state < TCP_MAX_STATES; state++) {
        seq_printf(seq, "%-12s: %d\n", state_names[state], state_counters[state]);
    }

    return 0;
}


static int tcpstat_seq_open(struct inode *inode, struct file *file)
{
    return single_open(file, tcpstat_seq_show, NULL);
}


static const struct file_operations tcpstat_file_ops = {
    .owner   = THIS_MODULE,
    .open    = tcpstat_seq_open,
    .read    = seq_read,
    .llseek  = seq_lseek,
    .release = single_release
};


static __init int tcpstat_init(void)
{
    proc_create("tcpstat", 0, NULL, &tcpstat_file_ops);
    return 0;
}


static __exit void tcpstat_exit(void)
{
    remove_proc_entry("tcpstat", NULL);
}

module_init(tcpstat_init);
module_exit(tcpstat_exit);
```

内核模块编译好并加载到内核后，procfs 文件系统提供了一个新文件 `/proc/tcpstat`，内容为统计结果：

```python
$ cat /proc/tcpstat
ESTABLISHED : 5
SYN_SENT    : 0
SYN_RECV    : 0
FIN_WAIT1   : 0
FIN_WAIT2   : 0
TIME_WAIT   : 1
CLOSE       : 0
CLOSE_WAIT  : 0
LAST_ACK    : 0
LISTEN      : 14
CLOSING     : 0
```

当用户程序读取这个文件时，内核虚拟文件系统 (VFS) 调用小菜在内核模块中写的处理函数：遍历内核 TCP 套接字完成统计并格式化统计结果。内核模块、VFS 以及套接字等知识超出专栏范围，不再赘述。 小菜在服务器上试验这个内核模块，真的快得飞起！

# 经验总结

小菜开始总结这次脚本开发工作中的经验教训，他列出了以下关键节点：

1.  依靠 psutil 采集，没有关注 psutil 实现导致性能问题；
2.  用生成器代替列表返回连接信息，解决内存瓶颈；
3.  直接读取 procfs 文件系统，部分解决 CPU 性能瓶颈；
4.  通过调节 IO 缓冲区大小，进一步降低 CPU 开销；
5.  用 Netlink 代替 procfs，彻底解决性能问题；
6.  实验内核模块思路，终极解决方案快得飞起；

这些问题节点，一个比一个深入，没有一定功底是搞不定的。小菜从刚开始跌跌撞撞，到后来独当一面，快速成长的关键在于善于在问题中总结经验教训：

*   程序开发完一定要做性能测试，看能够扛住多大的压力；
*   使用任何工具，需要准确理解其背后的原理，避免误用；
*   对编程语言以及操作系统源码要保持好奇心；
*   计算机基础知识很重要，需要及时补全才能达到新高度；
*   学会问题发散，举一反三；