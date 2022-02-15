---
title: Python Windows 的计划任务
tags: []
id: '1524'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-27 09:47:48
---

## 计划任务介绍

你好，我是悦创。计划任务，就是定期或者循环不间断的执行某个任务，做一些定期统计之类的操作。 每个系统中都会有定时任务工具，这里先介绍 Windows 的定时任务，也叫作任务计划程序。 首先说明，Windows 的任务计划程序是自带的，不需要额外安装，你只需要准备操作的内容。这里的内容，我们以启动 Python 的源码做文件写入操作，检测效果直接查看文件。

## 准备文件

先准备 Python 源码文件，文件名 **timing-todo.py**，是如下：

```python
import datetime
import random
with open('todo.txt','a',encoding='utf8') as file:
    random_num = random.randint(1,10000)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.writelines("当前时间：{} 随机数值：{}\n".format(current_time, random_num))
```

代码只有 6 行，其中 2 行还是导入，非常简单了。操作如下：

*   首先是打开文件，一个 **todo.txt** 的文件，用追加模式打开
*   随机生成一个 1-10000 的数值
*   获取当前时间，格式是 年-月-日 时:分:秒
*   写入在文件中追加一行内容，内容格式是：当前时间：具体时间 随机数值：具体数值\\n

非常简单，下面是单独测试的效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/e5de27fca141e1a6a24ca6c1b25d5d4f.png) 执行没有任何问题，现在就用**任务计划程序**来测试脚本的执行。

## 新建计划任务

首先打开 Windows 的任务计划程序，推荐使用左下角的 Win 按钮，搜索任务计划程序，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/e88c5792ba4248860f1f14aab4d29daf.png) 打开后，选择左侧菜单栏，顶部的任务计划程序（本地），鼠标右键，创建任务，注意是创建任务，不要创建基本任务。 ![image.png](https://img-blog.csdnimg.cn/img_convert/b4b1b3dc6a079eabe8291bf17b9f44f5.png) 然后就会出现弹框，默认界面输入一个名称即可，如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/fc64e7ac17c19fec6ff7550136e38301.png) 顶部有菜单栏，切换到触发器，配置执行时间和执行周期，我这里设置的是 2020年1月6号，晚上8点开始，并且每5分钟执行一次，持续一个小时，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/bcec39b50340b23c54edd580a9376b07.png) 按确定，保存这个配置。

## 指定脚本文件

接着切换到操作，这里是配置到时间了具体做什么，所以这里把执行 py 文件的命令配置上去，也就是执行命令。如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/d60a15226e73bceeeff363a2ab5c0137.png) 我这里写的是完整路径的命令，是 C:/Users/kelly/Anaconda3/python.exe timing-todo.py，指定特定的python，执行的启动位置是桌面，并且启动桌面上的 py 文件，对应生成的 todo.txt 文件也就在桌面上。 最后的效果图如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/c32fe462d7c36b5383dfb1d86d78e666.png)

## 【单选题】小练习

Windows 规定用户只能创建一个计划任务，是对还是错？

*   \[ \] 错
*   \[ \] 对