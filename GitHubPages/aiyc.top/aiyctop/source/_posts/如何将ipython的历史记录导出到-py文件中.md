---
title: 如何将IPython的历史记录导出到.py文件中?
tags: []
id: '1907'
categories:
  - - IPython
date: 2021-09-19 20:01:30
---

你好，我是悦创。 经常给一对一学员上课的时候，会用到 IPython 来演示代码，毕竟 IPython 不用不知道，一用根本停不下来。我都不想用 Pycharm 来调试代码了。 但是，用了这么久，一直惯性思维回答编程一对一学员： **IPython 的优点是我刚刚说的这些，但是就是代码保存不了。** 很多人问我，我也一直是这个想法并且做的非常彻底去回答。但是，今天一个学员，学计算机专业的在伯克利，上课后问我：老师，IPython 真的不能保留「保存」代码？ 我说是的！非常肯定的回答，一直都是这个回答的不会有错！但是，当听见这句话的时候，我惊呆了：**从来如此就是对的吗？** 那一瞬间，好像有什么东西破碎一般，所有自我的矇昧体现了出来。我想起了柴静的《看见》中的一句话：**要想“看见”，就要从蒙昧中睁开眼来。这才是最困难的地方，因为蒙昧就是我自身，像石头一样成了心里的坝。** 然后我就去找了一下，然后就有了下面的小笔记： **回到上面的问题, 两种办法解决：**

1.  用 `%hist` 保存后把 `%` 开头的删掉再执行。

```python
Input[1]:%hist -f filename.py
```

2.  用 `%logstart` 和 `%logstop` 。它会把你所用的 `%` 命令对应的的 `Python` 代码（如下面的 magic…）。

```python
In [7]: %logstart /tmp/test_log.py
Activating auto-logging. Current session state plus future input saved.
Filename       : /tmp/test_log.py
Mode           : backup
Output logging : False
Raw input log  : False
Timestamping   : False
State          : active
 In [8]: a = 10
 In [9]: b = a*a
 In [10]: %who
a        b
 In [11]: %logstop
 In [12]: !cat /tmp/test_log.py
# IPython log file

357x46
357*46
54*32
53*42
52*43
532*4
get_ipython().magic(u'logstart /tmp/test_log.py')
a = 10
b = a*a
get_ipython().magic(u'who')
get_ipython().magic(u'logstop')
```

3.  例如，对于你的用例，有 [`%save` magic command](http://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-save) 你只需输入`%save my_useful_session 10-20 23`保存输入行 10 至 20 和 23 到 `my_useful_session.py`

* * *

如果你的 IPython 会话如下所示

```python
In [1] : import numpy as np
....
In [135]: counter=collections.Counter(mapusercluster[3])
In [136]: counter
Out[136]: Counter({2: 700, 0: 351, 1: 233})
```

你希望将行从 1 保存到 135，然后在同一个 IPython 会话上使用以下命令

```python
In [137]: %save aiyc.py 1-135
```

这将所有 Python 语句保存在当前目录(启动 IPython 的位置)中的 `aiyc.py` 文件中。 **此外，文件指出：**

> 此函数使用与[%history](http://ipython.readthedocs.io/en/5.x/interactive/magics.html#magic-history)对于输入范围，然后将行保存到指定的文件名。

例如，这允许引用较早的会话，例如

```ipython
%save current_session ~0/
%save previous_session ~1/
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/d6d9bac70681443ca0c86d67729d6b72.png)