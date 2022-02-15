---
title: 02-pygame 图片处理
tags: []
id: '1817'
categories:
  - - Pygame
date: 2021-08-01 21:48:42
---

你好，我是悦创。前面我们开始的为期 30天的更新挑战第一篇，接下来我们是第二篇。第一篇的课程视频，也已经在微信公众号里面了。有兴趣的可以关注公众号：AI悦创。上一篇的链接：[https://mp.weixin.qq.com/s/Fth21WgO6f89dzNLSBZUoA](https://mp.weixin.qq.com/s/Fth21WgO6f89dzNLSBZUoA)

## 目录

1.  载入图片、调整大小
2.  图片显示规则
3.  足球反弹

## 1\. 载入图片、调整大小

> 案例 1：新建文件，准备好两个图片文件（可自行下载喜欢的图片，这两个图片完整文件名已经改为 `football.png` 和 `background.jpg` ），三个文件放同一文件夹内。然后编码进行图片载入和调整大小。

![在这里插入图片描述](https://img-blog.csdnimg.cn/d4942496a4bd4604bdefe137d1d0569a.jpg) ![在这里插入图片描述](https://img-blog.csdnimg.cn/d880fc4f4d634b3c8367e4811a5600b8.png) 为了，方便后续的阅读，退出处理部分已经写成函数 `quit()` 写成函数部分，我在零基础一对一部分已经讲解过了，如果有需要学 Python 零基础一对一的人欢迎联系报名，长期招收。

```python
import pygame # 导入 pygame 库
import sys # 导入系统库，无需安装
pygame.init() # 调用初始化函数
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('我的游戏')

def quit(): # 把退出处理写成函数，方便之后阅读。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# 使用变量保存载入的图片，图片函数一般在 image 中
football = pygame.image.load('football.png') # 载入的图片会被认为是一层一层的面，称为 surface
football = pygame.transform.smoothscale(football, (60, 60))
# ↑ 通过 transform 改变 surface 的大小，存回变量中

while True:
    quit() # 调用退出处理函数，判断要不要退出
    # ↓ 使用 blit() 显示图片，第二个参数是图片坐标
    screen.blit(football, (100, 100))
    pygame.display.update() # update 意为更新
```

**代码解析：**

*   pygame 中的图像相关函数在 image 里，载入使用 `load()` 。
*   载入时填写图片完整名称，载入时的图片数据被视为一个表面（surface），这个面可以改变坐标和大小。
*   显示图片时，使用创建的屏幕来显示（PS：我们的东西肯定是放在屏幕上面来显示的）所以这里用了 screen，显示函数是 `blit()` ，它有两个参数，分别是要显示的面和这坐标。

## 2\. 图片显示规则

*   在 pygame 中采用屏幕左上角为坐标原点，向下为 y 正方向，向右为 x 正方向。

![在这里插入图片描述](https://img-blog.csdnimg.cn/4b4068c545f74860bc35d64468109ac6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

*   显示图片的时候指定图片坐标，也是图片的左上角，surface 默认 `(0, 0)` 。
    
*   先显示的图片会被后面显示的图片覆盖住，所以背景图片要先显示。
    

```python
bg = pygame.image.load('background.jpg')
bg = pygame.transform.smoothscale(bg, (600, 400))
```

```python
screen.blit(bg, (0, 0)) # 从左上角开始显示背景图片
```

为了，防止小白不理解，不知到代码放在哪里，下面放上代码图片： ![在这里插入图片描述](https://img-blog.csdnimg.cn/cac14ffdd62b4abe9fce6c33cfc15c15.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) **注意：** 载入背景图片后，设定为窗口一样的大小，然后将坐标设为 `(0, 0)` ，此时正好铺满背景。

## 3\. 足球反弹

> 案例 2： 让足球在球场中运动，碰到边界就反弹，在原理的代码上做如下的修改。

**我来提示一下：** 我们知道图片显示的位置依靠坐标来定决定，那么坐标变化就意味着图片的运动。 图片坐标要变化，写定的数值显然是不可以的，所以用变量来表示坐标和对应的速度。 碰到边界实际上就是坐标超出了屏幕的大小了，需要注意图片上下左右的坐标，要考虑图片的尺寸。 这里我就直接放在完整代码：

```python
import pygame, sys

pygame.init()
# 创建游戏窗口大小
size = width, height = 600,400
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("我的世界")
# 加载足球图像
football = pygame.image.load(r'football.png')
# 调整图像的大小
football = pygame.transform.smoothscale(football, (width//6, height//4))
# 加载背景图片
background = pygame.image.load(r'background.jpg').convert_alpha()
# 调整图像的大小
background = pygame.transform.smoothscale(background, (width, height))

# 设置游戏的图标
pygame.display.set_icon(football)
# 获取图像的外切矩形
ball_rect = football.get_rect()
# 定义速度
speed = [1,1]
# 创建颜色
bgcolor = pygame.Color('black')
# 创建控制频率的clock
fclock = pygame.time.Clock()
# 定义刷新频率
fps = 300
while True:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 设置背景的颜色
    screen.fill(bgcolor)
    # 绘制背景图片
    screen.blit(background, (0, 0))
    # 设定足球的运动
    ball_rect = ball_rect.move(speed[0], speed[1])
    # 足球的上边Y轴坐标<0或者足球的下边的Y轴坐标>创建窗口的高度
    if ball_rect.top < 0 or ball_rect.bottom >height:
        speed[1] = -speed[1]
    # 足球的左边的X坐标<X轴的0坐标或者右边的坐标>创建窗口宽度
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    # 在屏幕中的矩形中绘制图形
    screen.blit(football, ball_rect)
    # 刷新游戏场景
    pygame.display.update()
    # 控制游戏场景刷新率
    fclock.tick(fps)
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/354fb7f2362b4fa19db1ff92563d12c9.png)