---
title: Python 中 return 和 print 的作用及区别
tags: []
id: '637'
categories:
  - - 7 天零基础章节测试
date: 2020-07-13 13:29:49
---

### 一图胜千里

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200713132925.png)

#### print的作用是输出数据到控制端,就是打印在你能看到的界面上

*   print的作用还是比较容易理解的

```python
print (1)
print('asdfghj')

输出结果
1
asdfghj
```

如上就是输出数据到控制端

#### return的作用之一是返回计算的值

*   没有return语句

```python
x = 1
y = 2
def add(x, y):
    z = x + y
print(add(x,y))

输出结果
None
```

没有return语句，所以没能给函数add()赋值，打印出来也就是空值(None)。

*   有return语句

```python
x = 1
y = 2
def add(x, y):
    z = x + y
    return z
print(add(x,y))

输出结果
3
```

**注意：return 返回值只能通过 print 打印才会显示出来，但在交互式模式下不需要 print 打印**

```python
def func1():
    for i in range(1, 5):
        return (i)

print(func1())
print("......")
func1()

输出结果
1
......
```

如上，直接调用func1(),是没有输出结果的。

#### 来个复杂的 print 和 return 相结合

```python
x = 1
y = 2
def add(x, y):
    z = x + y
    print(z)
print(add(x,y))

输出结果
3
None
```

在打印函数add (x, y)时，函数add (x, y)会执行print (z)语句得到3的，但add(x,y)返回值是None，所以打印输出结果应为3,None

#### print 和 return 程序执行方面

```python
def func1():
    for i in range(1, 5):
        print (i)

def func2():
    for i in range(1, 5):
        return (i)

func1()

print("..............")
print(func2())

输出结果
1
2
3
4
..............
1
```

程序读到 return() 语句,其后的语句不会再被执行，所以打印 func2(),只输出**"1"**这个结果就退回了。 而 print() 语句不同，其后的语句依然会被执行，所以调用 func1() 时，值**"1"、"2"、"3"、"4"**都输出了。