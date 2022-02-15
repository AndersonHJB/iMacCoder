---
title: 01-初识 pygame 游戏开发
tags: []
id: '1809'
categories:
  - - Pygame
date: 2021-07-31 16:30:08
---

你好，我是悦创。接下来三十天，我将持续更新 Python pygame 的基础游戏开发教程。文章都会对应视频教程，视频教程将在公众号：AI悦创，发布。

## 目录

本次，文章目标：

1.  Python 的第三方库
2.  pygame 的简单介绍
3.  创建窗体、背景

## 1\. Python 的第三方库

Python 本身具有一些基本功能和函数，但是明显并不能覆盖所有我们需要的功能，比如图像的处理、大量数据计算分析等，这时就是要第三方库。 这种第三方库在 Python 中使用 pip 来安装、升级、卸载等管理；Python 官方库网址：[https://pypi.org/](https://pypi.org/) 接下来的文章都会使用 pygame 库来开发 Python 游戏，我们就需要安装 pygame，在终端输入以下命令来安装 pygame：

```python
pip install pygame
```

安装时需要连接网络，见到 ”done“ ”success“ 即表示安装成功，如果在后续编码时无法找到 pygame 库，重装即可。

## 2\. pygame 简单介绍

pygame 是 Python 中比较流行的游戏库，它提供的函数能够处理图像、文字、声音等，也有一些商业游戏项目采用 pygame 开发，但一般来说不适合开发大型游戏，我们学习 Python 编程用它比较合适（另外从此处开始，就要大量使用函数等内容了，难度会有所上升）。

> 案例 1： 新建文件来测试一下 pygame 安装效果，同时学习库的导入方法。

```python
# file:Lesson_01.py
import pygame # 导入 pygame 库
# 然后导入 pygame 库中的 aliens 例子
import pygame.examples.aliens
# 运行这个 aliens 的主函数入口
pygame.examples.aliens.main()
```

**代码解析：**

*   `import pygame` ：要使用额外的库，都需要通过 import 来导入对应的库；
*   如果只想导入库的某一部分功能，也可以使用 “from 库名称 import 具体功能” 的方法。
*   本例子是自带的参考例子，一个外星人入侵小游戏，运行没问题表示安装 pygame 成功，examples 下层还有很多其他的样例游戏，可自行查看。

**运行结果：** ![在这里插入图片描述](https://img-blog.csdnimg.cn/d701968a6b764f38835e92bf899169d7.png)

## 3\. 创建窗体、背景

> 案例 1： 通过编写一个窗体界面，来体验 pygame 的初始化、颜色处理、事件获取等功能。

**说明：** 开始游戏编写之后代码较长，后文会都会按步骤给出，并进行说明，有的还会有简易流程图，另外代码注释中也会写明关键提示。

```python
# file:Lesson_02.py
import pygame # 导入 pygame 库
pygame.init() # 调用初始化函数
# 设定窗口的宽和高
size = width, height = 600, 400
# ↑ 上述多元赋值后又赋值给 size，成为元组
# 接下来创建屏幕，也是变量存储就可以
screen = pygame.display.set_mode(size)
# ---第一步完毕，程序运行会有窗口闪过---
```

**代码解析：**

*   size 处，先进行了多元赋值，将两个数值赋值给 width 和 height ，然后又赋值给了 size，变成元组（类似列表，但不可改变），这时整体形成多赋值，如果打印 size 结果会是 (600, 400) 。
*   screen 接收了 pygame 建立的对象，对象这个概念后面会再学。

**运行后会有如下图一闪而过的黑色窗体。** ![在这里插入图片描述](https://img-blog.csdnimg.cn/cad6acc4de9544778550077a9526543f.png) **说明：**

*   接下来跟着第一步后面编写，主要完成 **持续运行** 、**画面更新** 和 **单击右上角 x 退出程序** ，3 个功能。
    
*   退出功能需要使用 sys 库，这是一个内置库，不用额外下载安装，直接在文件头部 `import sys` 即可。
    

**想要程序持续运行，需要使用循环**

```python
import sys
# 想要程序持续运行，需要使用循环
while True:
    # 在循环中，每循环一次就判断要不要退出
    for event in pygame.event.get():
        # 使用 for 循环获取当前 pygame 窗体事件
        if event.type == pygame.QUIT:
            # 如果获取到的事件类型是 QUIT（退出）
            sys.exit() # 那么调用系统退出
    # 每次判断完毕后，就要更新窗口画面
    pygame.display.update() # update 意为更新
# ---第二步完毕，现在窗口不会闪退，可用鼠标关闭
```

**代码解析：**

*   每行代码我都有解析，希望好好看看注释；
*   注意缩进，每次遇到循环、判断、函数等，都要注意 4 个空格缩进，这样才能体现层级关系，才能让程序按预想正常运行（Python 严格依靠缩进来区别不同的代码块）

1.  接下来，添加窗口名称和背景颜色，这两句代码都写在循环前面。

```python
# ↓ 可以设定窗口的名称
pygame.display.set_caption("我的游戏")
# 定义一个列表存储背景色，采用 RGB 颜色表示
# 可搜索 RGB 颜色对照表选择自己喜欢的颜色数值
bgcolor = [0, 255, 255]
# 背景色需要使用 fill() 填充，我们放在循环里
```

2.  实际的填充颜色的代码写在循环里面。

```python
screen.fill(bgcolor) # 填充背景颜色
```

**代码解析：**

*   bgcolor：是一个列表，它保存了背景颜色的 RGB 信息，但是要注意，变量在实际使用前，都只是数字容器而已，并不能设定完变量就看到背景效果。
    
*   背景色设定放在循环中，这样就可以每次刷新背景了，这时才真的使用了 bgcolor 中存储的数值。
    

为了，让小白也能看懂，我把本阶段的完整代码放出来。

```python
import pygame # 导入 pygame 库
import sys
pygame.init() # 调用初始化函数
# 设定窗口的宽和高
size = width, height = 600, 400
# ↑ 上述多元赋值后又赋值给 size，成为元组
# 接下来创建屏幕，也是变量存储就可以
screen = pygame.display.set_mode(size)
# ---第一步完毕，程序运行会有窗口闪过---

# ↓ 可以设定窗口的名称
pygame.display.set_caption("我的游戏")
# 定义一个列表存储背景色，采用 RGB 颜色表示
# 可搜索 RGB 颜色对照表选择自己喜欢的颜色数值
bgcolor = [0, 255, 255]
# 背景色需要使用 fill() 填充，我们放在循环里

# 想要程序持续运行，需要使用循环
while True:
    # 在循环中，每循环一次就判断要不要退出
    for event in pygame.event.get():
        # 使用 for 循环获取当前 pygame 窗体事件
        if event.type == pygame.QUIT:
            # 如果获取到的事件类型是 QUIT（退出）
            sys.exit() # 那么调用系统退出
    screen.fill(bgcolor) # 填充背景颜色
    # 每次判断完毕后，就要更新窗口画面
    pygame.display.update() # update 意为更新
# ---第二步完毕，现在窗口不会闪退，可用鼠标关闭
```

再次运行程序，这时窗体名称和背景就变了。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/db560ccc22904c3b8840bcc8442444b2.png)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/c3ad2d3de7a1424f9e63e33068985ae0.png)