---
title: Python获取内存中的数据
tags: []
id: '1917'
categories:
  - - uncategorized
date: 2021-09-27 12:23:25
---

你好，我是悦创。 最近一对一学员问的问题： ![在这里插入图片描述](https://img-blog.csdnimg.cn/b8557bb466ec4507854e2904a281eac2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQUnmgqbliJs=,size_20,color_FFFFFF,t_70,g_se,x_16) 在 c/c++ 中，通过&获取变量的内存地址，通过\*获取内存地址中的数据。 在 Python 中，通过 id 获取变量的内存地址，那如何通过内存地址获取数据呢？

```python
import ctypes

value = 'hello world'  # 定义一个字符串变量
address = id(value)  # 获取value的地址，赋给address
get_value = ctypes.cast(address, ctypes.py_object).value  # 读取地址中的变量
print(address, get_value)
```

```python
2723768404656 hello world
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/bf80f6fc2c9d42b5af1658f1601c9479.png)