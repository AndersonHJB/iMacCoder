---
title: Python3 assert（断言）
tags: []
id: '1942'
categories:
  - - 技术杂谈
date: 2021-10-07 09:48:45
---

你好，我是悦创。 Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。 断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/effaa78ceabe4d94a8deebb11af37cad.png) 语法格式如下：

```python
assert expression
```

等价于：

```python
if not expression:
    raise AssertionError
```

assert 后面也可以紧跟参数:

```python
assert expression [, arguments]
```

等价于：

```python
if not expression:
    raise AssertionError(arguments)
```

以下为 assert 使用实例：

```python
In [1]: assert True     # 条件为 true 正常执行

In [2]: assert False    # 条件为 false 触发异常
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-e791502d049f> in <module>
----> 1 assert False    # 条件为 false 触发异常

AssertionError:

In [3]: assert 1==1    # 条件为 true 正常执行

In [4]: assert 1==2    # 条件为 false 触发异常
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-4-2585f74381e7> in <module>
----> 1 assert 1==2    # 条件为 false 触发异常

AssertionError:

In [5]: assert 1==2, '1 不等于 2'
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-5-791fb45a4dbb> in <module>
----> 1 assert 1==2, '1 不等于 2'

AssertionError: 1 不等于 2
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png)