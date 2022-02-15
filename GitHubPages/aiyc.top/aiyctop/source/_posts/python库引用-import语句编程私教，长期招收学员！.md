---
title: Python库引用-import语句|编程私教，长期招收学员！
tags: []
id: '1872'
categories:
  - - uncategorized
date: 2021-09-05 13:53:32
---

> 简介

库引用是Python扩充程序功能的方式, Python使用`import`关键字来实现库引用 Python库引用的方式总共有三种:

*   `import <库名>`
*   `from <库名> import <函数名>`
*   `import <库名> as <库别名>`

> 库引用方式(一): `import <库名>`

```python
# 引用库
import <库名>
# 调用库中的函数
<库名>.<函数名>(<函数参数>)
```

> 库引用方式(二): `from <库名> import <函数名>`

```python
# 引用库
from <库名> import <函数名>
# 或
from <库名> import *  # 表示引用库中的所有函数
# 调用库中的函数
<函数名>(<函数参数>)
```

**注意:** 虽然这种方式调用库中的函数方便, 但是**容易造成函数重名的问题**

> 库引用方式(三): `import <库名> as <库别名>`

```python
# 引用库
import <库名> as <库别名>
# 调用库中的函数
<库别名>.<函数名>(<函数参数>)
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/d3ea27d58a854eaa8d8144fe4583af91.png)