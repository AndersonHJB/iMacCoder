---
title: Python邮件的定期报告
tags: []
id: '1532'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-01 08:31:51
---

https://github.com/AndersonHJB/Play-with-office-automation

## 介绍

使用系统的定期任务，可以准时的让程序执行，还可以结合邮件做汇报工作。 本文的内容，使用邮件的定期任务，结合前面的邮件汇报，每次执行完，都进行邮件的汇报工作。

## 编辑器展示

首先准备代码部分，如下截图【文件夹中含源码】： ![image.png](https://img-blog.csdnimg.cn/img_convert/fc036a3fb12c43b944e764f30b772220.png) 当前截图，打开的是一个文件夹，名字是 todo-task ，里面有一个空的 **init**.py 文件，以及 send\_qq\_mail.py 和 timing-todo.py ，以及 timing-todo-file.py 。

## py 源码准备和测试

第二个是需要执行的文件，第一个是发送邮件的文件，第三个是发邮件时携带附件，多了个文件名，如下代码：

```bash
import datetime
import random
from send_qq_mail import send_mail

with open('todo.txt','a',encoding='utf8') as file:
    random_num = random.randint(1,10000)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.writelines("当前时间：{} 随机数值：{}\n".format(current_time, random_num))
    subject = "定期任务执行完成"
    contents = ["当前时间：{} 随机数值：{}\n".format(current_time, random_num),'todo.txt']
    send_mail(subject,contents)
```

首先是测试代码是否正常，执行 todo 和 todo-file 的两个 py 文件，效果图如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/9f21b016c36153ed473e49bf2bcf55db.png) 一个是携带附件的，一个是纯文字的，正常。

## 配置定时任务

接下来编辑下 win 定时任务，将这个目录放到桌面，方便查看效果，以及查看邮箱的接收。

*   创建任务，名称是 python-todo-file-send\_mail
*   触发是从任意时间开始，每 5 分钟执行一次，持续一小时
*   操作是启动电脑的 Python，进入到目标文件夹，执行 timing-todo-file.py

配置图展示： ![image.png](https://img-blog.csdnimg.cn/img_convert/55f823558af76dafb3b7f75d607094ff.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/b79920ef7f714b0756d1868f1a92643a.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/90a87fd247c2a28742ee025ef983033f.png) 等待执行，注意观察邮件的接收。

## 效果展示

一段时间后.......... 截图看下邮箱效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/134323bc1ee103c8d98f31ac0af852b5.png) 图中，下面两个是文件测试，一个纯文字，一个有附件。上面的四个，都是定时任务执行的代码，所发出的邮件，四个都是带附件的，都是 todo.txt

## 【单选题】练习

windows 定时任务中，有程序、参数、起始位置，哪个是必须的？

*   \[ \] 起始位置
*   \[ \] 程序
*   \[ \] 参数