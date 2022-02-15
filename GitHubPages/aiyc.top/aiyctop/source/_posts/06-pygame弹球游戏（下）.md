---
title: 06-pygame弹球游戏（下）
tags: []
id: '1833'
categories:
  - - Pygame
date: 2021-08-07 12:44:40
---

你好，我是悦创。 前面我们讲了一个小实战，接下来呢，我们来继续把这个弹球小实战写完。上一篇链接：[05-pygame弹球游戏（上）](https://blog.csdn.net/qq_33254766/article/details/119425432) 接下来，我们来完成接杆的代码。

## 接杆

创建接杆，同样是将接杆作为一个类来进行创建，规定它的大小颜色以及矩形选框，并且获取矩形的左侧与顶部位置。

```python
class Mybraclass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        # 控制接杆的大小
        image_surface = pygame.Surface([100, 20])
        # 接杆颜色
        image_surface.fill([213, 213, 213])

        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
```

实例化接杆对象，并显示到屏幕。

```python
# 循环外面
mybar = Mybraclass([270, 600])

# 循环里面
screen.blit(mybar.image, mybar.rect)
```

让接杆移动起来，要跟随鼠标移动，这里用到了鼠标事件中的 MOUSEMOTION ，然后进行碰撞检测。在写碰撞检测之前，有时候需要将进行碰撞检测放到一个组里面，当某个元素与组内元素发生碰撞时，则进行速度取反。

```python
# 将我的球类放入组中
ballgroup = pygame.sprite.Group(myball)

# 写在循环中
# 当鼠标滑过时将新建一个鼠标划过的事件并赋值给接杆的中心点
        if event.type == pygame.MOUSEMOTION:
            mybar.rect.centerx = event.pos[0]
    # 小球与接杆的碰撞检测
    if pygame.sprite.spritecollide(mybar, ballgroup, False):
        myball.speed[1] = -myball.speed[1]
```

帧率、积分变量和分数显示。

1.  帧率、积分变量和分数

```python
clock = pygame.time.Clock()

ball_speed = [4, -4]
score = 0
```

```python
# 小球与接杆的碰撞检测
    if pygame.sprite.spritecollide(mybar, ballgroup, False):
        myball.speed[1] = -myball.speed[1]
        time = time + 1
        score = score + 10
    clock.tick(time)

    screen.fill([255, 255, 255])
    font = pygame.font.SysFont('', 20)
    text_surface = font.render(u"score:" + str(score), True, (0, 0, 255))
    screen.blit(text_surface, (32, 24))
```

上面的代码，多有碎片化，接下来我就把完整的代码放出来：

```python
import sys
import pygame
from pygame.locals import *


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

    # 球的移动
    def ball_move(self):
        self.rect = self.rect.move(self.speed)
        # 控制小球在游戏界面内
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]

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


class Mybraclass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        # 控制接杆的大小
        image_surface = pygame.Surface([100, 20])
        # 接杆颜色
        image_surface.fill([213, 213, 213])

        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# 初始化pygame
pygame.init()
screen = pygame.display.set_mode([800, 700])
clock = pygame.time.Clock()

ball_speed = [4, -4]
score = 0

# 球类给定值
myball = Myballclass(r'football.png', ball_speed, [10, 20])
mybar = Mybraclass([270, 600])
# 将我的球类放入组中
ballgroup = pygame.sprite.Group(myball)

# # 刷新时间
time = 30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 当鼠标滑过时将新建一个鼠标划过的事件并赋值给接杆的中心点
        if event.type == pygame.MOUSEMOTION:
            mybar.rect.centerx = event.pos[0]
    # 小球与接杆的碰撞检测
    if pygame.sprite.spritecollide(mybar, ballgroup, False):
        myball.speed[1] = -myball.speed[1]
        time = time + 1
        score = score + 10
    clock.tick(time)

    screen.fill([255, 255, 255])
    font = pygame.font.SysFont('', 20)
    text_surface = font.render(u"score:" + str(score), True, (0, 0, 255))
    screen.blit(text_surface, (32, 24))

    myball.ball_move()
    myball.over()
    screen.blit(myball.image, myball.rect)
    screen.blit(mybar.image, mybar.rect)
    pygame.display.flip()
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/a7beb456c8f24ff4bd6f5c2b2e9cb740.png)