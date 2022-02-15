---
title: 05-pygame弹球游戏（上）
tags: []
id: '1838'
categories:
  - - Pygame
date: 2021-08-09 09:06:50
---

你好，我是悦创。 前面我们讲了，一些 pygame 的操作，接下来呢，我们成功步入实战阶段。

## 目录

1.  游戏介绍
2.  弹球游戏

## 1\. 游戏介绍

足球在画面中运动，遇到上、左、右以及接杆就会反弹，且接杆接住会积分，如果掉落到下面，则游戏结束。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/7eff8bb7d25141d6a4869079ec4d5305.png)

## 2\. 小球

1.  新建文件夹，文件夹下面创建 py 文件、图片文件，然后我们开始编写代码。本篇用的是图片，可以改成画出来的圆形。

接下来，编写基础代码：

```python
import pygame, sys
from pygame.locals import *

# 初始化 pygame
pygame.init()
screen = pygame.display.set_mode([800, 700])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
```

2.  创建一个专门控制小球的类，用来给定小球的样式。得到小球的矩形选框，然后获得获得小球矩形选框的左侧与顶部的边缘，还有小球的移动速度。

```python
# 创建球类
class Myballclass(pygame.sprite.Sprite):
    # 给出图矩形速度并给定对应的值
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.smoothscale(self.image, (80, 70))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
```

3.  创建球类实例化对象，然后显示到屏幕上。

```python
# 球类给定值
myball = Myballclass(r'football.png', ball_speed, [10, 20])
# 刷新时间
time = 30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(myball.image, myball.rect)
    pygame.display.flip()
```

4.  现在开始让球运动起来并进行反弹，当小球移动到最边缘时速度取反（这部分写在球类中，另外通过 self 来表示类的属性）。

```python
# 球的移动
    def ball_move(self):
        self.rect = self.rect.move(self.speed)
        # 控制小球在游戏界面内
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
```

5.  类需要编写结束函数。仍然让小球不断运动，然后判断游戏结束，并对游戏结束时要显示的字进行处理。

```python
 # 游戏结束
    def over(self):
        self.rect = self.rect.move(self.speed)

        # 当小球底部大于界面高度时判定游戏结束
        if self.rect.bottom > screen.get_height():
            # SysFount  从系统字体中创建一个font对象（字体样式， 大小）
            font = pygame.font.SysFont('宋体', 40)

            # render  在新的surface上绘制文本（文本， 抗锯齿， 颜色， 背景）
            text_surface = font.render(u"Game Over", True, (0, 0, 255))
            screen.blit(text_surface, (screen.get_width() // 2, screen.get_height() // 2))
            return 0
```

下部分，明天继续！

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/14347805187b46efbcdd4399d4e06aa2.png)