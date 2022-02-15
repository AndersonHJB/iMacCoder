---
title: Python | 判定IP地址合法性的四种方法
tags: []
id: '1275'
categories:
  - - Python
  - - Python 小玩意
  - - Python 杂谈
date: 2020-12-10 14:59:52
---

你好，我是悦创。 IP 合法性校验是开发中非常常用的，看起来很简单的判断，作用确很大，写起来比较容易出错，今天我们来总结一下，看一下3种常用的IP地址合法性校验的方法。 先了解 IPV4 的 IP 格式，它的形式应该为：(1~255).(0~255).(0~255).(0~255)

## 1\. 正则表达式判定法

最简单的实现方法是构造一个正则表达式。判断用户的输入与正则表达式是否匹配。若匹配则是正确的IP地址，否则不是正确的IP地址。 下面给出相对应的验证 ip 的正则表达式：

```python
^(1\d{2}2[0-4]\d25[0-5][1-9]\d[1-9])\.(1\d{2}2[0-4]\d25[0-5][1-9]\d\d)\.(1\d{2}2[0-4]\d25[0-5][1-9]\d\d)\.(1\d{2}2[0-4]\d25[0-5][1-9]\d\d)$
```

\\d表示0~9的任何一个数字 {2}表示正好出现两次 \[0-4\]表示0~4的任何一个数字 的意思是或者 1\\d{2}的意思就是100~199之间的任意一个数字 2\[0-4\]\\d的意思是200~249之间的任意一个数字 25\[0-5\]的意思是250~255之间的任意一个数字 \[1-9\]\\d的意思是10~99之间的任意一个数字 \[1-9\])的意思是1~9之间的任意一个数字 .的意思是.点要转义（特殊字符类似，@都要加\\转义） 代码如下：

```python
import re
def check_ip(ipAddr):
    compile_ip=re.compile('^(1\d{2}2[0-4]\d25[0-5][1-9]\d[1-9])\.(1\d{2}2[0-4]\d25[0-5][1-9]\d\d)\.(1\d{2}2[0-4]\d25[0-5][1-9]\d\d)\.(1\d{2}2[0-4]\d25[0-5][1-9]\d\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False
```

## 2\. 字符串拆解法

把 ip 地址当作字符串，以 . 为分隔符分割，进行判断：

```python
# !/usr/bin/python
import os, sys


def check_ip(ipAddr):
    import sys
    addr = ipAddr.strip().split('.')  # 切割IP地址为一个列表
    # print addr
    if len(addr) != 4:  # 切割后列表必须有4个参数
        print
        "check ip address failed!"
        sys.exit()
    for i in range(4):
        try:
            addr[i] = int(addr[i])  # 每个参数必须为数字，否则校验失败
        except:
            print
            "check ip address failed!"
            sys.exit()
        if addr[i] <= 255 and addr[i] >= 0:  # 每个参数值必须在0-255之间
            pass
        else:
            print
            "check ip address failed!"
            sys.exit()
        i += 1
    else:
        print
        "check ip address success!"


if len(sys.argv) != 2:  # 传参加本身长度必须为2
    print
    "Example: %s 10.0.0.1 " % sys.argv[0]
    sys.exit()
else:
    check_ip(sys.argv[1])  # 满足条件调用校验IP函数
```

## 3\. 引入 IPy 类库

IPy 库是一个处理IP比较强大的第三方库。涉及到计算大量的 IP 地址，包括网段、网络掩码、广播地址、子网数、IP 类型等别担心，Ipy 模块拯救你。Ipy 模块可以很好的辅助我们高效的完成 IP 的规划工作。 IPy 库的安装方法请根据自己的操作系统自行查找，有很多详细例子。

```python
import IPy


def is_ip(address):
    try:
        IPy.IP(address)
        return True
    except Exception as  e:
        return False
```

## 4\. 使用 Python 自带方法，比如 Socket 里面的 inet\_aton()

```python
import socket

def checkIP(strIP):
    try:
        socket.inet_aton(strIP)
        return True
    except socket.error:
        return False
```

## 总结

三种方法都能够准确的判断出 ip（IP V4）地址的合法性， 正则表达式代码量少， 逻辑简单， 但是正则表达式繁琐， 字符串判定法容易理解，但是代码量大， 使用类库，判断简洁，但是需要引入额外的库。各有利弊， 使用时自行选择即可。