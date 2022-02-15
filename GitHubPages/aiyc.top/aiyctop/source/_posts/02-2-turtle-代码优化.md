---
title: 02-2-Turtle 代码优化
tags: []
id: '1806'
categories:
  - - Python Turtle
date: 2021-07-25 18:50:03
---

你好，我是悦创。 上一篇文章，我带你使用 Turtle 学会了画风筝，但是代码不够优美，这篇我来带你优化一下。 第一个是画一个风筝的代码优化，原来的代码自行看上一篇。优化后代码：

```python
import turtle


def kite(speed=1, position_x=0, position_y=0):
    """
    speed：画笔速度
    position_x：x 坐标
    position_y：y 坐标
    default：坐标初始值为 0
    """
    turtle.speed(speed)
    turtle.goto(position_x, position_y)

    for i in range(30):
        turtle.forward(i)
        turtle.left(90)
    turtle.exitonclick()  # 防止运行完，窗口消失


if __name__ == '__main__':
    kite(speed=2, position_x=-200, position_y=200)
```

运行结果如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/63f233795ee8a169366048ed1b53510c.png) 接下来，我们来优化画四个角落的风筝，但不需要风筝线。

```python
import turtle


def kite(speed=1, position_x=0, position_y=0, exit_click=False):
    """
    speed：画笔速度
    position_x：x 坐标
    position_y：y 坐标
    exit_click：画完，窗口是否保留
    default：坐标初始值为 0
    """
    turtle.speed(speed)
    turtle.pen(pendown=False)
    turtle.goto(position_x, position_y)
    turtle.pen(pendown=True)
    # turtle.pendown()
    for i in range(160):
        turtle.forward(i)
        turtle.left(90)
    if exit_click:
        # 防止运行完，窗口消失
        turtle.exitonclick()


if __name__ == '__main__':
    kite(speed=120, position_x=-200, position_y=200)
    kite(speed=120, position_x=-200, position_y=-200)
    kite(speed=120, position_x=0, position_y=0)
    kite(speed=120, position_x=200, position_y=200)
    kite(speed=120, position_x=200, position_y=-200, exit_click=True)
```

![image.png](https://img-blog.csdnimg.cn/img_convert/83928a1756e3feb06525922370e61a90.png)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/524376bf97a04a0fa1aa7563fe8a1b56.png)