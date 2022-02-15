---
title: 04-Pygame 面向对象与音乐
tags: []
id: '1831'
categories:
  - - Pygame
date: 2021-08-05 07:43:56
---

你好，我是悦创。 上一片我们讲了 pygame 的按键和鼠标，并且我也把缺少的注视今天🈶️发了出来，昨天公众号文章标题还忘记写了。害。。。

1.  [03-pygame 键盘与鼠标](https://blog.csdn.net/qq_33254766/article/details/119344370)
2.  [03-pygame 键盘与鼠标(代码注释添加）](https://blog.csdn.net/qq_33254766/article/details/119383692)

## 目录

1.  面向对象的概念
2.  音乐播放
3.  播放器制作

## 1\. 面向对象的概念

> 案例 1：新建文件，编写如下代码，了解面向对象的概念。

我接下来，来稍微的介绍一下，Python 是面向对象的语言，可以提高大规模编程的效率。我们可以先看类的概念，就是具有相同特征的东西叫做一类。 比如：

*   法国人、小日本都是人类（个人偏见，其他随意，盲裁就更厉害了。）都有眼睛、鼻子、嘴巴。
*   狗：旺财、大黄啥的都是狗，它们都是狗这类的。

类是允许有不同属性，比如都是人类，就有好人坏了，也有盲人裁判。当然还有高矮胖瘦都有。 Python 类在使用的时候需要先实例化，也就是输入属性信息创建出一个具体的例子，如这里的 tom，这个实例称为对象。

```python
'''
面向对象
'''


# 创建一个hello类
class hello(object):
    """
    创建一个用于问候的类
    首先设定这个类具有的属性，因为是问候
    所以属性有名字、问候语、年龄
    """

    def __init__(self, name, hello_words, age):  # 初始属性
        self.name = name  # 将传入的数值保存到属性中
        self.hello_words = hello_words
        self.age = age

    # 这个类中有一个函数，用来输出问候语句，用到的参数就是
    # 这个类当中所设定的属性值
    def say_hello(self):  # 类函数
        print("%s,my name is %s,I'm %d years old." \
              % (self.hello_words, self.name, self.age))
# ⬆️ %s 表示字符串，%d 表示整数，中间的 \ 表示一行写不下了


aiyc = hello('aiyc', 'nice to meet you', 10)  # 创建一个hello类型的对象，名为aiyc，属性已赋值
aiyc.say_hello()  # 调用对象中的函数
```

## 2\. 音乐播放

> 案例 2：新建文件，编写如下代码，使用 pygame 提供的函数实现音乐播放。

和之前的惯例一样，我们先上代码，然后再写代码解析。 **所需要素材记得关注公众号：AI悦创，后台回复 pygame 获取。**

```python
'''
音乐的处理
'''
import pygame
import sys

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.mixer.init()  # 初始化混音器
# 👇 load() 载入背景音乐，play() 播放。
pygame.mixer.music.load('hop hop-aiyc.mp3')
pygame.mixer.music.play(-1)
# 播放次数，-1 表示一直循环
pygame.mixer.music.set_volume(0.1)
# 音量最大 1.0
t = pygame.mixer.Sound('beep1.ogg')
# 创建声音，不能太长
t.play()  # 播放此声音

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
```

**代码解析：** 接下来，我们来解析一下我们的代码。

*   声音文件名称：`hop hop-aiyc.mp3` 原创声音，严谨商用。可以改成自己喜欢的音乐。
*   `play()` 可以有两个参数，第一个表示循环次数，-1 就一直循环，第二个参数表示播放起始时间，默认从头播放。
*   直接播放声音，可以用 `Sound()` 来实例化一个声音，比如这里的 t ，然后可以用这个 t 对象，`play()` 就是播放， `Stop()` 就是停止播放（文件不要过大，过长，否则载入失败。）

## 3\. 播放器制作

> 案例 3：新建文件，编写如下代码，制作模拟播放器，可以通过鼠标单击暂停和继续播放。

```python
import pygame, sys, time

pygame.init()
size = width, height = 360, 120
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AI悦创·Pygame 播放器")
pygame.mixer.init()  # 初始化混音器
pygame.mixer.music.load('hop hop-aiyc.mp3')  # 音量最大 1.0
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
status = 1  # 存储播放状态的变量
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1 and status == 0:
                status = 1  # 每次点击就切换状态
            elif e.button == 1 and status == 1:
                status = 0
    if status == 1:  # 状态 1 就是连续播放
        pygame.mixer.music.unpause()  # 继续播放
        screen.fill((0, 255, 0))  # 背景色，下面是画实心的圆圈。
        pygame.draw.circle(screen, (255, 0, 0), (60, 60), 50)
    if status == 0:
        pygame.mixer.music.pause()
        screen.fill((255, 0, 0))
        pygame.draw.circle(screen, (0, 255, 0), (60, 60), 50)
    # 假的进度条
    pygame.draw.line(screen, (0, 0, 255), (120, 80), (350, 80), 10)
    pygame.display.update()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/485c6405f35b43efbcb9df5c8f45ec37.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/0c6a379439bb4558ad6dfc3e7b82c6f3.png)