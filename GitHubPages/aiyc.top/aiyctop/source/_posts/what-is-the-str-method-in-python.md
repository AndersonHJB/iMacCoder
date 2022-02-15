---
title: What is the __str__ method in Python?
tags: []
id: '2074'
categories:
  - - uncategorized
date: 2021-12-10 17:35:39
---

[![https://gitee.com/huangjiabaoaiyc/image/raw/master/202112101630483.png](https://gitee.com/huangjiabaoaiyc/image/raw/master/202112101630483.png "https://gitee.com/huangjiabaoaiyc/image/raw/master/202112101630483.png")](https://gitee.com/huangjiabaoaiyc/image/raw/master/202112101630483.png "https://gitee.com/huangjiabaoaiyc/image/raw/master/202112101630483.png")

## The need for `__str__` method:

The **`__str__` method** in Python represents the class objects as a string – it can be used for classes. The `__str__` method should be defined in a way that is easy to read and outputs all the members of the class. This method is also used as a debugging tool when the members of a class need to be checked. The `__str__` method is called when the following functions are invoked on the object and return a string:

*   print()
*   str()

If we have not defined the `__str__`, then it will call the `__repr__` method. The **`__repr__` method** returns a string that describes the pointer of the object by default (if the programmer does not define it).

## How to call `__str__` method

### 1\. Default implementation

```python
class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject.__repr__())
print(myObject)
```

输出：

```python
<__main__.MyClass object at 0x7f3f7d34d1f0>
<__main__.MyClass object at 0x7f3f7d34d1f0>
<__main__.MyClass object at 0x7f3f7d34d1f0>
```

The above code shows an example where neither `__str__` nor `__repr__` are defined. Calling `__str__` calls the default `__repr__` method, and they all give the same output, the pointer of our object.

### 2\. Custom `__str__` method

```python
class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __str__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())
```

输出：

```python
MyClass(x=12345 ,y=Hello)
MyClass(x=12345 ,y=Hello)
MyClass(x=12345 ,y=Hello)
<__main__.MyClass object at 0x7feb029681f0>
```

The code above shows the output once you have defined the `__str__` method. When `__str__`, `print()`, or `str()` are called you will get your defined output. Make note that the `__repr__` output remains the same.

### 3\. `__repr__` method defined only

```python
class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __repr__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())
```

输出：

```python
MyClass(x=12345 ,y=Hello)
MyClass(x=12345 ,y=Hello)
MyClass(x=12345 ,y=Hello)
MyClass(x=12345 ,y=Hello)
```

In the first example we saw that when **str** is not defined it automatically calls the **repr** method. Therefore, the output of all the functions - **str**, str(), and **repr** - are the same. Moreover, the **repr** method does not necessarily need to return a string. In case it does not return a string, the print() statements will throw an error.

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![](https://img-blog.csdnimg.cn/c9f56f26bb854de18ef76629c5d47c0f.png)