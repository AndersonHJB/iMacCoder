---
title: Linux 的计划任务
tags: []
id: '1528'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-28 11:04:33
---

## 检测环境

Windows 是大家用的最多的，当然 Linux 和 Macos 也不能少。这里并不介绍有 GUI 的定时计划，而是介绍命令行工具 **crontab** 。

> **crontab** crontab 命令常见于 Unix 和类 Unix 的操作系统之中，用于设置周期性被执行的指令。该命令从标准输入设备读取指令，并将其存放于 “crontab” 文件中，以供之后读取和执行。

Linux 和 Macos 都支持 crontab。本文使用到的系统和工具，分别是 Ubuntu 系统 18 版本，Termius 命令行工具。【工具和命令可以自行准备，因为命令行是所有 Linux 和 Macos 都通用的。】 先进入到 Linux 环境下，因为我用的是云服务器，所以需要远程登录：

```python
➜  ~ ssh root@39.101.132.5
```

将上一节课的 py 代码，放进来，如果没有我们直接创建一下这个 Python 文件：

```python
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# touch timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# vim timing-todo.py
```

![image.png](https://img-blog.csdnimg.cn/img_convert/5f2412fc753775f7bd6f0da136878ab9.png) 输入 ls 看文件存在么：

```bash
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# ls
timing-todo.py
```

如果忘记代码，看下面：

```python
import datetime
import random
with open('todo.txt','a',encoding='utf8') as file:
    random_num = random.randint(1,10000)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.writelines("当前时间：{} 随机数值：{}\n".format(current_time, random_num))
```

再来检测下 Python 程序，是否正常。python2 或者 python3 安装了一个即可。

```bash
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3
Python 3.6.9 (default, Oct  8 2020, 12:12:24)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
root@iZ8vb8h5pbkzfj43uzuuc9Z:~#
```

python 环境正常，然后就是使用 Python 启动 py 文件，看下能否生成对应的 todo.txt 文件，以及查看文件内容是否正确，如下内容：

```bash
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# ls
timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# ls
timing-todo.py  todo.txt
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# cat todo.txt
当前时间：2021-02-28 10:33:16 随机数值：7985
```

我们可以多运行几次：

```bash
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# cat todo.txt
当前时间：2021-02-28 10:33:16 随机数值：7985
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# python3 timing-todo.py
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# cat todo.txt
当前时间：2021-02-28 10:33:16 随机数值：7985
当前时间：2021-02-28 10:34:18 随机数值：7217
当前时间：2021-02-28 10:34:19 随机数值：4409
当前时间：2021-02-28 10:34:20 随机数值：3555
当前时间：2021-02-28 10:34:21 随机数值：4538
当前时间：2021-02-28 10:34:22 随机数值：9540
当前时间：2021-02-28 10:34:22 随机数值：925
当前时间：2021-02-28 10:34:23 随机数值：5913
```

系统命令介绍：

*   ls，展示当前目录中的文件
*   cat 文件，展示文件的具体内容

一切正常，接下来就是 crontab 环节。

## 准备 crontab

crontab 的安装命令：

```bash
sudo apt-get install crontab
```

命令行介绍：

*   crontab：可能是自带，也可能不自带，需要安装
*   sudo：是使用最高权限安装命令行，也许你用的账户本身就是 root，就不需要 sudo
*   apt-get：是 ubuntu 的安装命令，例如 macos 是 brew ，而 centos 和 redhat 都不一样

安装好之后，需要开始编辑定时任务。 首先是展示一下定时任务，使用命令行：crontab -l，会提示没有文件，或者提示 no crontab for adminx ，都表示当前没有定时任务，如下内容：

```bash
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# crontab -l
no crontab for root
```

## 准备编辑器

接下来就是新建定时任务，使用命令：crontab -e，进入文件，开始编辑任务。这中间可能会有个小插曲，让你选择编辑器，推荐 nano 这款，简单好用。 然后进入编辑页面，如下截图： ![image.png](https://img-blog.csdnimg.cn/img_convert/19b8f2e48c774155cd70a61a1d9eba30.png) 底部是按键提示，中间是文本，可以编辑的内容，# 那些是帮助文档，可以保留可以删除，没影响。

## 新增定时任务

将光标移到文档底部，然后增加一行定时任务，如下截图： ![image.png](https://img-blog.csdnimg.cn/img_convert/030d627e8b5451691417e1238cbd2c94.png) 这样就是增加一个定时任务，任务的写法是 \* \* \* \* python3 /root/timing-todo.py，对应的意思是：依次展开，是 minute hour day month week command 先看后面的命令，是使用python3执行那个文件的命令行，非常简单。

## crontab 命令介绍

那 5 个 \* 号怎么理解？如下解释：

*   第一个 \* 位置代表分钟，\* 代表每分钟
*   第二个代表小时
*   第三个代表天
*   第四个代表月
*   第五个代表周

举个例子：

> 每分钟执行： \* \* \* \* \* 每五分钟执行： \*/5 \* \* \* \* 每小时执行： 0 \* \* \* \* 每天执行： 0 0 \* \* \* 每周执行： 0 0 \* \* 0 每月执行： 0 0 1 \* \* 每年执行： 0 0 1 1 \*

### 补充

计划任务语法有 5 个字段，中间用空格分隔，每个字段代表一个时间单位。

```bash
┌───────────── 分钟 (0 - 59)
│ ┌───────────── 小时 (0 - 23)
│ │ ┌───────────── 日 (1 - 31)
│ │ │ ┌───────────── 月 (1 - 12 或 JAN-DEC)
│ │ │ │ ┌───────────── 星期 (0 - 6 或 SUN-SAT)
│ │ │ │ │
│ │ │ │ │
│ │ │ │ │
* * * * *
```

每个时间字段的含义：

符号

描述

举例

`*`

任意值

`* * * * *` 每天每小时每分钟

`,`

值分隔符

`1,3,4,7 * * * *` 每小时的 1 3 4 7 分钟

`-`

范围

`1-6 * * * *` 每小时的 1-6 分钟

`/`

每

`*/15 * * * *` 每隔 15 分钟

那我们写的那条命令，就是每分钟，使用 python3 执行一次 timing-todo.py 文件。

## 保存和退出

写好后，ctrl+o 写入文件，ctrl+x 退出编辑模式，回到命令模式，多了一行提示，crontab: installing new crontab 新增一条 crontab 任务。 ![image.png](https://img-blog.csdnimg.cn/img_convert/0a517b60a01b1c0a523f065fc350efd8.png) 然后使用 crontab -l 看下是否注册了，如下图：

> 原本的系统出现问题，我找了另一台服务器操作图片。

![image.png](https://img-blog.csdnimg.cn/img_convert/91cb60f9afe23583f20bd96af8d6652b.png) 一切正常。 现在等几分钟，因为定时任务设置的是每分钟都会执行一次，所以几分钟后，使用 ls 命令查看 todo.txt 是否生成，以及使用 cat 命令，查看文件中的内容。

## 效果展示

few three minutes later.............. 粘贴一下效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/1ecfb267ecf880ffb5d3c1b78c8b7888.png) 等了三分钟，效果很好，正常执行了。 如果 todo.txt 需要清除，重新记录内容，就需要用到删除，使用 rm 删除命令，命令行是：rm todo.txt

## 主观练习题

回想下，crontab 命令的前五个位置，代表啥？ 以及下方命令，都是什么时候运行？

*   *   *   *   *   \*
*   \*/5 \* \* \* \*
*   0 \* \* \* \*
*   0 0 \* \* \*
*   0 0 \* \* 0
*   0 0 1 \* \*
*   0 0 1 1 \*