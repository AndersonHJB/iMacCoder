---
title: Pathlib 比 OS 更好的路径库
tags: []
id: '1465'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-14 12:03:53
---

该模块提供表示文件系统路径的类，其语义适用于不同的操作系统。路径类被分为提供纯计算操作而没有 I/O 的 [纯路径](https://docs.python.org/zh-cn/3/library/pathlib.html#pure-paths)，以及从纯路径继承而来但提供 I/O 操作的 [具体路径](https://docs.python.org/zh-cn/3/library/pathlib.html#concrete-paths)。 ![image.png](https://img-blog.csdnimg.cn/img_convert/08edce4aa6c8be4e56ccd4e8c98e9e31.png) 如果以前从未用过此模块，或不确定哪个类适合完成任务，那要用的可能就是 [`Path`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.Path)。它在运行代码的平台上实例化为 [具体路径](https://docs.python.org/zh-cn/3/library/pathlib.html#concrete-paths)。 **在一些用例中纯路径很有用，例如：**

1.  如果你想要在 Unix 设备上操作 Windows 路径（或者相反）。你不应在 Unix 上实例化一个 [`WindowsPath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.WindowsPath)，但是你可以实例化 [`PureWindowsPath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PureWindowsPath)。
    
2.  你只想操作路径但不想实际访问操作系统。在这种情况下，实例化一个纯路径是有用的，因为它们没有任何访问操作系统的操作。
    
3.  总结：纯路径就只有路径，具体路径看操作。

## 基础使用

**导入主类：**

```python
In [1]: from pathlib import Path
```

**列出子目录：**

```python
In [2]: p = Path(".")

In [3]: [x for x in p.iterdir() if x.is_dir()]
Out[3]:
[PosixPath('第四章：Word自动化处理'),
 PosixPath('第五章：PTT自动化处理'),
 PosixPath('第三章：Excel自动化处理')]
```

*   **iterdir()：**遍历此目录中的文件。对于特殊路径 “**.**” 和 “**..**” 不会产生任何结果。
*   **is\_dir()：**此路径是否为目录。

**列出当前目录树下的所有 Python 源代码文件：**

```python
In [45]: list(p.glob('**/*.py'))
Out[45]:
[PosixPath('第五章：PTT自动化处理/8.Python生成数据动图/data_change_to_gif.py'),
 PosixPath('第三章：Excel自动化处理/10.多线程Excel像素画/Excel_paint.py')]
```

**在目录树中移动：**

```python
In [51]: p = Path('/etc')

In [52]: q = p / 'init.d' / 'reboot'

In [53]: q
Out[53]: PosixPath('/etc/init.d/reboot')

In [54]: q.resolve()
Out[54]: PosixPath('/private/etc/init.d/reboot')
```

**查询路径的属性：**

```python
In [61]: p = Path(".")

In [62]: p.exists() # 此路径是否指向一个已存在的文件或目录，目录存在则为：True，不存在则为：False
Out[62]: True

In [63]: p.is_dir() # 如果路径指向一个目录（或者一个指向目录的符号链接）则返回 True，如果指向其他类型的文件则返回 False。简化的翻译：此路径是否为目录。
Out[63]: True
```

\*\*

## 纯路径

**纯路径对象提供了不实际访问文件系统的路径处理操作。**有三种方式来访问这些类，也是不同的风格： **_class \_pathlib.PurePath(_\*pathsegments\_)** 一个通用的类，代表当前系统的路径风格（实例化为 [`PurePosixPath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PurePosixPath) 或者 [`PureWindowsPath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PureWindowsPath)）：

```python
In [74]: from pathlib import PurePath

In [75]: PurePath('setup.py')      # Running on a Unix machine
Out[75]: PurePosixPath('setup.py')
```

每一个 _pathsegments_ 的元素可能是一个代表路径片段的字符串，一个返回字符串的实现了 [`os.PathLike`](https://docs.python.org/zh-cn/3/library/os.html#os.PathLike) 接口的对象，或者另一个路径对象：

```python
In [76]: PurePath('foo', 'some/path', 'bar')
Out[76]: PurePosixPath('foo/some/path/bar')

In [77]: PurePath(Path('foo'), Path('bar'))
Out[77]: PurePosixPath('foo/bar')
```

当 _pathsegments_ 为空的时候，假定为当前目录：

```python
In [86]: PurePath()
Out[86]: PurePosixPath('.')
```

当给出一些绝对路径，最后一位将被当作锚（模仿 [`os.path.join()`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.join) 的行为）:

```python
In [90]: from pathlib import PurePath, PureWindowsPath

In [91]: PurePath('/etc', '/usr', 'lib64')
Out[91]: PurePosixPath('/usr/lib64')

In [92]: PureWindowsPath('c:/Windows', '/Program Files')
Out[92]: PureWindowsPath('c:/Program Files')
```

假斜线和单独的点都会被消除，但是双点 （`‘..’`） 不会，以防改变符号链接的含义。

```python
In [93]: PurePath('foo//bar')
Out[93]: PurePosixPath('foo/bar')

In [94]: PurePath('foo/./bar')
Out[94]: PurePosixPath('foo/bar')

In [95]: PurePath('foo/../bar')
Out[95]: PurePosixPath('foo/../bar')
```

（一个很 naïve 的做法是让 `PurePosixPath('foo/../bar')` 等同于 `PurePosixPath('bar')`，如果 `foo` 是一个指向其他目录的符号链接那么这个做法就将出错） 纯路径对象实现了 [`os.PathLike`](https://docs.python.org/zh-cn/3/library/os.html#os.PathLike) 接口，允许它们在任何接受此接口的地方使用。 _在 3.6 版更改: \_添加了 [`os.PathLike`](https://docs.python.org/zh-cn/3/library/os.html#os.PathLike) 接口支持。 \_class \_pathlib.PurePosixPath(_\*pathsegments\_) 一个 [`PurePath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PurePath) 的子类，路径风格不同于 Windows 文件系统：

```python
In [98]: PurePosixPath('/etc')
Out[98]: PurePosixPath('/etc')
```

_pathsegments_ 参数的指定和 [`PurePath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PurePath) 相同。 _class \_`pathlib.``PureWindowsPath`(_\*pathsegments\_) [`PurePath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PurePath) 的一个子类，路径风格为 Windows 文件系统路径：

```python
In [100]: PureWindowsPath('c:/Program Files/')
Out[100]: PureWindowsPath('c:/Program Files')
```

_pathsegments_ 参数的指定和 [`PurePath`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.PurePath) 相同。 无论你正运行什么系统，你都可以实例化这些类，因为它们提供的操作不做任何系统调用。

## 通用性质

路径是不可变并可哈希的。相同风格的路径可以排序与比较。这些性质尊重对应风格的大小写转换语义：

```python
In [101]: PurePosixPath('foo') == PurePosixPath('FOO')
Out[101]: False

In [102]: PureWindowsPath('foo') == PureWindowsPath('FOO')
Out[102]: True

In [103]: PureWindowsPath('FOO') in { PureWindowsPath('foo') }
Out[103]: True

In [104]: PureWindowsPath('C:') < PureWindowsPath('d:')
Out[104]: True
```

不同风格的路径比较得到不等的结果并且无法被排序：

```python
In [105]: PureWindowsPath('foo') == PurePosixPath('foo')
Out[105]: False
```

更多知识点可以参考：[https://docs.python.org/zh-cn/3/library/pathlib.html](https://docs.python.org/zh-cn/3/library/pathlib.html)