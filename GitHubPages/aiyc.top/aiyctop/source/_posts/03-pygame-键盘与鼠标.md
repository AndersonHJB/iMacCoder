---
title: 03-pygame 键盘与鼠标
tags: []
id: '1830'
categories:
  - - Pygame
date: 2021-08-05 07:42:39
---

你好，我是悦创。前面一便天我们学习了：[02-pygame 图片处理](https://blog.csdn.net/qq_33254766/article/details/119296645) 接下来学习 pygame 的键盘与鼠标。长期招收一对一学员哦，公司正在逐步创办中 ing。

## 目录

1.  绘制图形
2.  键盘事件处理
3.  鼠标事件处理

## 1\. 绘制图形

> 案例 1：新建文件，准备好如下代码，然后添加实现绘制功能的代码。

```python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 11:33 上午
# @Author  : AI悦创
# @FileName: p.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
import pygame  # 导入 pygame 库
import sys  # 导入系统库，无需安装

pygame.init()  # 调用初始化函数
size = width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("我的游戏")


def quit():
    """
    把退出处理写成函数，方便之后阅读。
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


while True:
    quit()  # 调用退出处理函数，判断要不要退出
    pygame.display.update()  # update 意为更新
```

在循环部分添加如下几行代码，实现绘制图形。

```python
while True:
    quit()  # 调用退出处理函数，判断要不要退出
    pygame.display.update()  # update 意为更新
    # ⬇️ 绘制图形都在 draw 下层，画直线就用 line()
    pygame.draw.line(screen, (255, 0, 0), (100, 300), (200, 300), 2)
    # 画矩形，第一个参数表示绘制目标是 screen ，第二个元祖表示颜色绿色
    pygame.draw.rect(screen, (0, 255, 0), (10, 20, 100, 100), 10)
    # 画圆形也差不多，颜色之后是位置信息，所以是圆心和半径
    pygame.draw.circle(screen, (0, 0, 255), (300, 100), 50, 0)
    pygame.display.update()  # update 意为更新
```

虽然，上面有注释，我还是稍微讲一下。 A. 绘制函数都在 draw 层下面，画什么都写对应函数名，比如直线是 `line()` ，圆是 `circle()` 。 B. 这几个绘制函数的参数都差不多，前两个参数都是绘制显示的目标和颜色，不同点在于第三项，虽然第三个都是坐标，但是 `line()` 里面 `(100, 300)` 和 `(200, 300)` 表示线的起点终点坐标；`rect()` 里面 10、20 表示矩形左上角坐标，100、100 表示 x、y 方向的长度；`circle()` 里面是圆心，50 是半径；最后的 2、10、0 都是表示线的粗细，填 0 表示实心。 那我们来看看运行结果吧。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/c231064be82e4fdd9d9657771177f38a.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 其他的线，请忽略。有可能是我 Mac 电脑的问题。

## 2\. 键盘事件

> 案例 2： 案例 1 部分的代码中删去矩形、直线、退出处理，然后来编写键盘检测、用键盘来控制圆形的位置，按一下 w、s、a、d 中的任意一个，就会动一下位置。

```python
import pygame
import sys

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('我的游戏')
from pygame.locals import *  # 从pygame本地库导入所有键盘值，*表示所有

c_x, c_y = 300, 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                c_x -= 10
            if event.key == pygame.K_d:
                c_x += 10
            if event.key == pygame.K_w:
                c_y -= 10
            if event.key == pygame.K_s:
                c_y += 10
            if event.key == pygame.K_q:
                sys.exit()
    screen.fill((0, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (c_x, c_y), 50, 0)
    pygame.display.update()
```

**代码说明：**

*   使用键盘前，先要键入键盘值，通过 `import *` 表示导入所有键盘值。
*   键盘也是一种事件，所以和退出处理类似，直接用按键值来处理退出也可以。
*   获取到事件类型 KEYDOWN，说明键盘按下了，就可以用事件内的 key 来判断，键盘值都是用 K\_a 形式命名的，按键字母就是 `K_对应字母` 。

## 3\. 鼠标事件处理

> 案例 3：鼠标处理演示，如下代码实现的功能是用鼠标点一下圆形内部，圆形就改变颜色。

```python
import pygame
import sys

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('我的游戏')
from pygame.locals import *  # 从pygame本地库导入所有键盘值，*表示所有
from random import randint  # 从随机库导入整数随机
import math  # 导入数学库，一会好算鼠标坐标和圆心的距离

c_x, c_y = 300, 100
x, y = 0, 0
r, g, b = 0, 0, 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = event.pos[0]
                y = event.pos[1]
                inner = math.sqrt((x - c_x) ** 2 + (y - c_y) ** 2)
            if inner <= 50:
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 255, 255))
    pygame.draw.circle(screen, (r, g, b), (c_x, c_y), 50, 0)
    pygame.display.update()

```

**代码解析：**

*   因为要随机新颜色和计算是否单击在圆形内部，所以导入 randint 和 math 两个库用来随机计算。
*   鼠标也是⌚️，类型如果是 MOUSEBUTTONDOWN 说明鼠标按下了，这时可以获取鼠标的信息。
*   鼠标按下的键位，用 1、2、3 表示左、中、右，所以 “==1” 说明在左键按下。
*   鼠标的位置，在 `event.pos` 里面，是一个元祖，`pos[0]` 是 x，`pos[1]` 是 y；这里计算距离使用了两点距离公式 `(x1 - x2)^2 + (y1 - y2)^2` 并开方。

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/015a55628d36451b8e8fd62bcef2591c.png)