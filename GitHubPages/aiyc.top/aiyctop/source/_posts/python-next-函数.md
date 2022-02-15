---
title: Python next() 函数
tags: []
id: '1931'
categories:
  - - uncategorized
date: 2021-10-02 15:19:46
---

你好，我是悦创。

## 描述

**next()** 返回迭代器的下一个项目。 **next()** 函数要和生成迭代器的 **iter()** 函数一起使用。

## 语法

next 语法：

```cmd
next(iterable[, default])
```

参数说明：

*   iterable -- 可迭代对象
*   default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。

## 返回值

返回下一个项目。

## 实例

以下实例展示了 next 的使用方法：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```

输出结果为：

```cmd
1
2
3
4
5
```

```python
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

[![https://img-blog.csdnimg.cn/a148a20d5d9b45628dac21e17520655b.png](https://img-blog.csdnimg.cn/a148a20d5d9b45628dac21e17520655b.png "https://img-blog.csdnimg.cn/a148a20d5d9b45628dac21e17520655b.png")](https://img-blog.csdnimg.cn/a148a20d5d9b45628dac21e17520655b.png "https://img-blog.csdnimg.cn/a148a20d5d9b45628dac21e17520655b.png")