---
title: 02-Python turtle 模块精讲
tags: []
id: '1803'
categories:
  - - Python Turtle
date: 2021-07-23 12:31:09
---

你好，我是悦创。 Python 标准库中有个 turtle 模块，俗称海龟绘图，它提供了一些简单的绘图工具，可以在标准的应用程序窗口中绘制各种图形。 turtle 的绘图方式非常简单直观，就像一只尾巴上蘸着颜料的小海龟在电脑屏幕上爬行，随着它的移动就能画出线条来。使用海龟绘图，我们只用几行代码就能够创建出令人印象深刻的视觉效果，而且还可以跟随海龟的移动轨迹，看到每行代码是如何影响它的移动的。 这能够帮助我们更好地理解代码的逻辑。所以海龟绘图也经常用作新手学习 Python 的一种工具。

## 创建画布

我们来看看海龟是如何工作的。首先，我们要导入 turtle 模块。然后我们要创建空白的窗口作为画布，窗口的大小是 800 个像素的宽度和 800 个像素的高度。然后创建一枝画笔，并且将光标的形状设置为一只海龟。代码如下。

```python
import turtle

window = turtle.Screen()
# turtle.setup(800, 800)
turtle.setup(width=800, height=800)
t = turtle.Pen()
turtle.shape("turtle") # 一只海龟的形状
```

运行这段代码，我们可以看到一个空白的窗口，中间有一个小海龟，如图 1 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/89b31d5e0eaf43ac876816126f319d89.png)

图 1

turtle 程序窗口的绘图区域使用直角坐标系，可以使用 X 坐标和 Y 坐标组成的一个坐标系统，将舞台映射为一个逻辑网格。 我们设置窗口的大小是宽和高都是 800 个像素。X 轴的坐标从 −400 到 400，而Y轴的坐标也是从 −400 到 400。海龟的初始位置在窗口的绘图区域的正中央 (0,0)，头朝 X 轴的正方向，如图 2 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/d3784aeecbf2de8e98faf732cc0a60c6.png)

图 2

> 提示：一个像素就是屏幕上的一个点，也就是可以表现出的最小元素。我们在屏幕上看到的所有东西都是由像素组成的。

## 移动海龟

接下来，我们想让海龟移动起来。控制海龟移动有很多命令，我们先来看一条简单的命令，用 `forward()` 方法让海龟向前移动 100 个像素：

```python
turtle.forward(100)
```

*   forward 就是让海龟向前移动的命令，100 是移动的距离。
    
*   让海龟向后移动的命令是 backward，括号中的参数是移动距离，以像素为单位。
    

另外，我们还可以让海龟改变方向。

*   命令 left 是向左转
    
*   命令 right 是向右转
    

这时候，括号中的参数表示要旋转的角度。 我们来看一个示例，让海龟画一个正方形，代码如下。

```python
import turtle

turtle.forward(100)  # 移动
turtle.left(90)  # 向左转 90 度
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
```

运行这段代码，可以看到海龟画出了一个方块，并且方向朝下，如图 3 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/b3ed1fefc6cede22f5c23731fbead771.png)

图 3

你也许会感到好奇，虽然是叫海龟绘图，可是我们并没有看到海龟的踪迹呀。 这是因为，默认情况下，光标是个箭头，如果想看到这只可爱的小海龟，需要调用 `shape()` 方法，并且把 `turtle` 作为参数传递给该方法。 另外，还可以调用 `setheading()` 来设置小乌龟启动时运动的方向，其参数是个数字，表示要旋转的角度。我们来看一个示例，代码如下。

```python
import turtle

turtle.shape("turtle")
turtle.forward(100)
turtle.setheading(180)
```

在这段代码中，我们先将光标改为小乌龟，然后画一条直线，接下来让小乌龟调个头，最终的效果如图 4 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/ab4eb0eea547451c9754d4350ea28d03.png)

图 4

还有一个 `home()` 方法，它表示让小海龟回到初始画笔的位置。我们在刚才的代码后面，增加一句 `turtle.home()` ，代码如下。

```python
import turtle

turtle.shape("turtle")
turtle.forward(100)
turtle.setheading(180)
turtle.home()
```

那么最终的结果就是，小海龟又回到了初始的位置，如图 5 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/cc5cc96192674917b891fad4250cf264.png)

图 5

不过这里要注意一点，这个 `turtle.home()` 回到开始，过程也是会画出来的。例如下面代码：

```python
import turtle

turtle.shape("turtle")
turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.home()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/a61fa6cfec40470d97021ca5f78cd010.png) 小海龟除了可以画直线，还可以绘制圆形和弧形。我们使用 `circle()` 函数来按照给定的半径画圆，这个函数有 3 个参数，分别是：

*   radius：半径，正数表示所画的圆的圆心在画笔的左边，负数表示所画的圆的圆心在画笔的右边；
    
*   extent：弧度，这是一个可选的参数，如果没有指定值，表示画圆；
    
*   steps：做半径为 radius 的圆的内切正多边形，多边形边数为 steps。这也是一个可选的参数。
    

我们试着画一个圆，看一下效果，代码如下。

```python
import turtle

turtle.circle(100, 300)
```

得到的图形如图 6 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/e104b4581ee046cea86dede53cd8a6aa.png)

图 6

还有两个经常用到的和移动有关的方法：

*   `turtle.goto(x, y)` 可以把画笔定位到指定的坐标；
    
*   `turtle.speed(speed)` 可以修改画笔运行的速度。
    

下面，我们来尝试绘制一个风筝。先通过 `goto()` 方法画一条线，表示风筝线，并且将光标移动到左上角。然后指定海龟运行速度为 2。接下来，利用 for 循环，绘制风筝头。代码如下

```python
import turtle
turtle.speed(2)
turtle.goto(-200, 200)
for x in range(30):
    turtle.forward(x)
    turtle.left(90)
```

得到的结果如图 7 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/ccd88ddc862f453faa6d181f393f1ec3.png)

图 7

## 画笔控制

我们可以控制画笔的**起笔**和**落笔**，以决定是否在屏幕上留下运动的轨迹。

*   当调用 `penup()` 方法，表示起笔，在此状态下不会画出运动的轨迹；
*   当调用 `pendown()` 方法，表示落笔，在此状态下会画出运动的轨迹。

我们可以这么理解，**海龟拿了一支笔，这只笔或朝上或朝下，当笔朝上时，海龟在移动过程中什么也不画，当笔朝下时，海龟用笔画下自己的轨迹。** 我们把刚才绘制风筝的代码稍作修改，现在，在画布的中央及上、下、左、右 4 个角，绘制出 5 个类似的风筝头，并且将绘制的速度提高到 10。代码如下。

```python
import turtle

turtle.speed(10)
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(200, -200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2cb7ad6c722a41309cb7361eaf0dc74b.png)

图 8

## 色彩

海龟绘图并不是只能够用黑色画笔绘图，还可以使用其他颜色画笔，甚至可以为图形填充颜色。下面我们来介绍几个和颜色相关的函数。

*   pencolor：设置画笔颜色；
    
*   fillcolor：设置填充颜色；
    
*   begin\_fill：填充形状前调用；
    
*   end\_fill：填充形状后调用。
    

光线有 3 种主要的颜色：红色、绿色和蓝色（红色、蓝色和黄色是绘画和颜料的主要颜色，但是计算机显示器使用的是光，而不是颜料）。通过将这 3 种颜色的不同的量组合起来，可以形成任何其他的颜色。 在 Pygame 中，我们使用 3 个整数的元组来表示颜色。元组中的第 1 个值，表示颜色中有多少红色。为0的整数值表示该颜色中没有红色，而 255 表示该颜色中的红色达到最大值。第 2 个值表示绿色，而第 3 个值表示蓝色。这些用来表示一种颜色的 3 个整数的元组，通常称为 RGB 值（RGB value）。 由于我们可以针对 3 种主要的颜色使用 0～255 的任何组合，这就意味着 Pygame 可以绘制 16 777 216 种不同的颜色，即 256×256×256 种颜色。然而，如果试图使用大于 255 的值或负值，将会得到类似`ValueError: invalid color argument` 的一个错误。 例如，我们创建元组 (0, 0, 0) 并且将其存储到一个名为 BLACK 的变量中。没有红色、绿色和蓝色的颜色量，最终的颜色是完全的黑色。黑色实际上就是任何颜色值都没有。元组 (255, 255, 255) 表示红色、绿色和蓝色都达到最大量，最终得到白色。白色是红色、绿色和蓝色的完全的组合。元组 (255, 0, 0) 表示红色达到最大量，而没有绿色和蓝色，因此，最终的颜色是红色。类似的，(0, 255, 0) 是绿色，而 (0, 0, 255) 是蓝色。 我们通过一个简单的示例，来看看如何使用色彩：

*   首先，调用 pencolor() 方法将画笔设置为红色，接着调用 fillcolor() 方法将填充色设置为绿色；
    
*   然后调用 begin\_fill() 方法，表示要开始填充；
    
*   接下来，调用 circle() 方法绘制圆，画笔是红色的，填充是绿色的，半径为 90 像素；
    
*   最后，调用 end\_fill() 方法结束填充。
    

代码如下。

```python
import turtle

turtle.pencolor("red")
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()
```

运行一下，绘制的图形效果如图 9 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/91cbbbdfce0c49c297606385d766a87f.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/3a2add9135d142fab9164ec95953a915.png)

图 9

除了可以直接输入颜色的“英文名称”（如上面的示例代码中的 red、green），我们还可以直接指定颜色的 RGB 色彩值。 海龟绘图专门有一个 colormode 函数用来指定 RGB 色彩值范围为 0～255 的整数或者 0～1 的小数。当参数是 255 的时候，表示采用 0～255 的整数值；当参数是 1.0 的时候，表示采用 0 到 1 的小数值。我们来看一个示例，代码如下。

```python
import turtle

turtle.colormode(255)
turtle.pencolor(255, 192, 203)
turtle.circle(90)
turtle.colormode(1.0)
turtle.pencolor(0.65, 0.16, 0.16)
turtle.circle(45)
```

我们两次调用了 `colormode()` 函数，第一次传给它的参数是 255，而后一次调用 `pencolor()` 函数就用 0 到 255 之间的整数作为参数来表示 RGB 色彩值，表示画笔的颜色是粉红色。然后绘制了一个大圆。 接下来我们再次调用 `colormode()` 函数，而后一次调用 `pencolor()` 函数就用 0 到 1 之间的小数作为参数来表示 RGB 色彩值，表示画笔的颜色是棕色。然后绘制了一个小圆。运行代码，得到的效果如图 10 所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/1bebbd49ec54431590b3d712831f47b3.png)

图 10

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/2f4738f13da1404aad2e8be842437e50.png)