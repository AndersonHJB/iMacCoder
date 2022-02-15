---
title: 03-Python turtle 模块实战：绘制机器猫前的分析
tags: []
id: '1804'
categories:
  - - Python Turtle
date: 2021-07-24 16:12:05
---

你好，我是悦创。 在上一节教程中，我们学习了海龟绘图。本节教程，我们将使用前面介绍过的知识，为绘制一幅机器猫的图形做准备。

## 程序分析

我们先来看一下机器猫的样子，如图 1 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/389c8acc49364a7eab2821f804b175bb.png)

图 1

它有大大的脑袋、圆圆的眼睛、红红的鼻头，嘴巴两边各有 3 根胡子。 脑袋和身体用一条红色的丝带分隔开，因为图 1 中的这只机器猫是坐着的，所以我们没有看到腿，只有圆圆的脚露在外面。此外，机器猫还有胳膊和圆圆的手。最后，别忘了机器猫还有标志性的铃铛和口袋。 我们可以使用在之前学习过的自定义函数，按照机器猫的身体部位来定义各个绘制函数：

*   head（头）
    
*   eyes（眼睛）
    
*   nose（鼻子）
    
*   mouth（嘴）
    
*   whiskers（胡子）
    
*   body（身体）
    
*   feet（脚）
    
*   arms（胳膊）
    
*   hands（手）
    
*   bell（铃铛）
    
*   package（口袋）。
    

函数的名字就表明了该函数负责绘制的身体部位。 我们可以看到，这些身体部位大部分是由圆形和矩形组成，所以为了能够重复使用相同的代码段，避免不必要地复制和粘贴代码，我们还需要定义两个基础函数——一个是绘制圆形的函数 `drawRound()`，一个是绘制矩形的 `drawRect()` 函数。

## 导入模块和设置画笔

因为要使用海龟绘图，所以我们需要先导入 turtle 模块。我们将采用导入模块的第二种方法：

```python
from turtle import *
```

使用这种方法，可以导入 turtle 模块中所有的方法和变量，然后就可以直接调用方法了，而不需要再添加 `turtle.` 前缀。 现在，我们可以直接将代码写为 `setup(500, 500)`，而不需要再添加前缀写成 `turtle.setup(500, 500)`。 然后我们对画笔做一些基本设置，代码如下。

```python
# 创建画布
window = Screen()
# 设置窗口大小
setup(500, 500)
# 设置画笔
speed(10)
shape("turtle")
colormode(255)
```

**代码解析：**

*   调用 `setup(500, 500)`，将画布大小设置为 500 像素宽，500 像素高。调用 `speed(10)` 将画笔速度设置为10。
    
*   调用 `shape("turtle")`，将光标设置为小海龟。调用 `colormode(255)` 设置 RGB 色彩值范围为 0～255。
    

## 基础函数

### 绘制圆形

我们定义一个 `drawRound()` 函数，用它来绘制圆形。这里为它设置两个参数，分别是表示所绘制的圆的半径的 size 和表示是否填充的 filled。

*   首先，调用 `pendown()` 函数表示落笔。然后，判断参数 filled 是否等于 True。如果等于 True，表示要填充，那么就调用 `begin_fill()` 函数；否则，不调用该函数，表示没有填充。
    
*   然后调用 `setheading(180)`，设置小海龟启动时运动的方向，就是让小海龟调个头。
    
*   调用 `circle(size, 360)`，画一个半径为 size 的圆。然后还要判断参数 filled 是否等于 True，如果等于 True，意味着前面调用过 `begin_fill()` 函数，则这里调用 `end_fill()` 函数表示填充完毕。
    

`drawRound()` 函数的代码如下所示。

```python
def drawRound(size, filled):
    pendown()  # 我们其他部分代码有可能有抬笔，所以这个部分还是需要填写 pendown
    if filled == True:
        begin_fill()
    setheading(180)
    circle(size, 360)
    if filled == True:
        end_fill()
```

### 绘制矩形

接下来，我们定义了一个 `drawRect()` 函数，用它来绘制矩形。这里为它指定 3 个参数，分别是表示所绘制的矩形的长的 length，表示所绘制的矩形的宽的 width，以及表示是否填充的 filled。

*   首先调用 `setheading(0)` ，设置小海龟启动时运动的方向，就是让小海龟头朝右。
    
*   然后调用 `pendown()` 函数，表示落笔。判断参数 filled 是否等于 True。如果等于 True，表示要填充，就调用 `begin_fill()` 函数；否则，不调用函数，表示没有填充。
    
*   最后 `forward(length)` ，绘制一条边。然后调用 `right(90)` ，让光标向右旋转 90 度。调用 `forward(width)` ，绘制另一条边。调用 `right(90)` ，让光标向右旋转 90 度。调用 `forward(length)`，绘制第三条边。调用 `right(90)`，让光标向右旋转 90 度。调用 `forward(width)` ，绘制第四条边。然后还要判断参数 filled 是否等于 True，如果等于，则调用 end\_fill() 函数表示填充完毕。
    

`drawRect()` 函数的代码如下所示。

```python
def drawRect(length, width, filled):
    setheading(0)
    pendown()
    if filled == True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled == True:
        end_fill()
```

## 本次文章的完整代码

```python
from turtle import *

# 创建画布
window = Screen()
# 设置窗口大小
setup(500, 500)
# 设置画笔
speed(10)
shape("turtle")
colormode(255)


def drawRound(size, filled):
    pendown()  # 我们其他部分代码有可能有抬笔，所以这个部分还是需要填写 pendown
    if filled == True:
        begin_fill()
    setheading(180)
    circle(size, 360)
    if filled == True:
        end_fill()


def drawRect(length, width, filled):
    setheading(0)
    pendown()
    if filled == True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled == True:
        end_fill()

```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh ![在这里插入图片描述](https://img-blog.csdnimg.cn/a4129f6d27f24502b022a9de2a8c7e91.png)