---
title: Python获取系统时间详解！
tags: []
id: '1868'
categories:
  - - Python图书管理系统
  - - time and datetime
date: 2021-09-02 12:02:36
---

你好，我是悦创。 最近准备给一对一学员，升级 Python 零基础的课程内容，就开发这个 Python 项目实战《图书管理系统》的开发，对于涉及的一些知识点，我接下来也会放在这里面。 这里我整理的两种方法，可以自行选择。

## 方法一：datetime

### 1\. 导入模块：

```python
import datetime
```

### 2\. 获取当前时间：

```python
theTime = datetime.datetime.now()
print(theTime)
```

得到的时间格式是：

```python
2021-09-02 10:38:40.420351
```

直接复制代码测试：

```python
import datetime

theTime = datetime.datetime.now()
print(theTime)
```

目前 [AI悦创·在线编程](https://www.aiycoj.cn/) 已经上线，你还可以直接点击，此链接直接运行：Code link：[https://www.aiycoj.cn/?id=b513626c-6794-4e58-835c-2248bb4a8023](https://www.aiycoj.cn/?id=b513626c-6794-4e58-835c-2248bb4a8023)

> PS：不知道在线编程网站，目前会运行到什么时候，因为后期准备重新开发，敬请期待！欢迎关注公众号：AI悦创。

当然，我们也可以按照我们所需要的方式获取指定格式的时间。

### 3\. 设置指定格式

```python
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S,%f'
```

该格式为：`年-月-日 时：分：秒，毫秒` 。可根据自己的需求删减。

### 4\. 使用指定格式

```python
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
```

测试代码：

```python
import datetime

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S,%f'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=7c7da4c1-df8a-44ea-92ee-8a05a22bff5c](https://www.aiycoj.cn/?id=7c7da4c1-df8a-44ea-92ee-8a05a22bff5c) 这里需要注意的是可能涉及到毫秒的取位问题，在这便顺便讲解一下 Python实现如何取位：

```python
import datetime
ISOTIMEFORMAT_F = '%f'
f_time1 = datetime.datetime.now().strftime(ISOTIMEFORMAT_F)
f_time2 = f_time1[:3]
print(f"f_time1:{f_time1}")
print(f"f_time2:{f_time2}")
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=4f006540-3689-4e19-9f65-6deab1533ec9](https://www.aiycoj.cn/?id=4f006540-3689-4e19-9f65-6deab1533ec9) 当我们要显示中文的时候呢？

### 5\. 直接写！

啥叫直接写？很简单：

```python
import datetime

ISOTIMEFORMAT = '%Y年-%m月-%d日 %H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=14e03178-3118-4fcf-bbe9-efa5cba1df7f](https://www.aiycoj.cn/?id=14e03178-3118-4fcf-bbe9-efa5cba1df7f)

## 方法二：time

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。 Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。 时间间隔是以秒为单位的浮点小数。 每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。 Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳, 如下实例：

```python
import time  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=ce0583af-b5d8-4fee-b2c2-d5c19713e447](https://www.aiycoj.cn/?id=ce0583af-b5d8-4fee-b2c2-d5c19713e447) 以上实例输出结果：

```python
当前时间戳为: 1630551916.453543
```

时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX 和 Windows 只支持到 2038 年。

### 1\. 什么是时间元组？

很多 Python 函数用一个元组装起来的 9 组数字处理时间：

序号

字段

值

0

4位数年

2008

1

月

1 到 12

2

日

1到31

3

小时

0到23

4

分钟

0到59

5

秒

0到61 (60或61 是闰秒)

6

一周的第几日

0到6 (0是周一)

7

一年的第几日

1到366 (儒略历)

8

夏令时

\-1, 0, 1, -1是决定是否为夏令时的旗帜

上述也就是 `struct_time` 元组。这种结构具有如下属性：

序号

属性

值

0

tm\_year

2008

1

tm\_mon

1 到 12

2

tm\_mday

1 到 31

3

tm\_hour

0 到 23

4

tm\_min

0 到 59

5

tm\_sec

0 到 61 (60或61 是闰秒)

6

tm\_wday

0到6 (0是周一)

7

tm\_yday

一年中的第几天，1 到 366

8

tm\_isdst

是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1

### 2\. 获取当前时间

从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如 localtime 之类的函数。

```python
import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=b8869e37-0118-42f4-bc07-bede88822cbf](https://www.aiycoj.cn/?id=b8869e37-0118-42f4-bc07-bede88822cbf) 以上实例输出结果：

```python
本地时间为 : time.struct_time(tm_year=2021, tm_mon=9, tm_mday=2, tm_hour=11, tm_min=10, tm_sec=45, tm_wday=3, tm_yday=245, tm_isdst=0)
```

### 3\. 获取格式化的时间

```python
import time

localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=553a2db9-b187-4aec-bce9-ad52c42cabcd](https://www.aiycoj.cn/?id=553a2db9-b187-4aec-bce9-ad52c42cabcd) 以上实例输出结果：

```python
本地时间为 : Thu Sep  2 11:13:42 2021
```

### 4\. 格式化日期

我们可以使用 time 模块的 strftime 方法来格式化日期，：

```python
time.strftime(format[, t])
```

```python
import time

# 格式化成2021-09-02 11:25:35形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Thu Sep 02 11:25:35 2021形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Thu Sep 02 11:25:35 2021"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=bf80a27c-6740-4b72-8bc5-68257b2b301b](https://www.aiycoj.cn/?id=bf80a27c-6740-4b72-8bc5-68257b2b301b) 以上实例输出结果：

```python
2021-09-02 11:34:33
Thu Sep 02 11:34:33 2021
1630553135.0
```

### 5\. Python 中时间日期格式化符号：

*   %y：两位数的年份表示（00-99）
*   %Y：四位数的年份表示（000-9999）
*   %m：月份（01-12）
*   %d：月内中的一天（0-31）
*   %H：24小时制小时数（0-23）
*   %I：12小时制小时数（01-12）
*   %M：分钟数（00=59）
*   %S：秒（00-59）
*   %a：本地简化星期名称
*   %A：本地完整星期名称
*   %b：本地简化的月份名称
*   %B：本地完整的月份名称
*   %c：本地相应的日期表示和时间表示
*   %j：年内的一天（001-366）
*   %p：本地 A.M. 或 P.M. 的等价符
*   %U：一年中的星期数（00-53）星期天为星期的开始
*   %w：星期（0-6），星期天为星期的开始
*   %W：一年中的星期数（00-53）星期一为星期的开始
*   %x：本地相应的日期表示
*   %X：本地相应的时间表示
*   %Z：当前时区的名称
*   %%：%号本身

### 6\. 获取某月日历

Calendar 模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：

```python
import calendar

year = 2021
month = 1
cal = calendar.month(year, month)
print(f"以下输出{year}年{month}月份的日历:")
print(cal)
```

在线直接运行：Code link：[https://www.aiycoj.cn/?id=48b881cf-0e09-498c-8fc3-5b29cb6e5bf1](https://www.aiycoj.cn/?id=48b881cf-0e09-498c-8fc3-5b29cb6e5bf1) 以上实例输出结果：

```python
以下输出2021年1月份的日历:
    January 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

### 7\. Time 模块

Time 模块包含了以下内置函数，既有时间处理的，也有转换时间格式的： ![在这里插入图片描述](https://img-blog.csdnimg.cn/bc34c4e62d214966ae0d0b3cef4d1973.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/35fea138b8734f27acb4139f8f1f9853.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/cdef8621af6c40cc9a829442fd65e256.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/72152858ecf14b93a563db76de042c80.png) Time 模块包含了以下2个非常重要的属性：

序号

属性及描述

1

**time.timezone** 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。

2

**time.tzname** 属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

### 日历（Calendar）模块

此模块的函数都是日历相关的，例如打印某月的字符月历。 星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用`calendar.setfirstweekday()` 函数。模块包含了以下内置函数： ![在这里插入图片描述](https://img-blog.csdnimg.cn/460094dcace04a5899f39d4a5391bf96.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/d8e99f1b5025430eb55d8f0592aa38be.png)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/3d9228d32f2a4510b0be31ad8904c609.png)