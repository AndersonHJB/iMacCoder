---
title: Pyinstaller打包Tkinter创建的GUI 应用程序
tags: []
id: '2136'
categories:
  - - Python GUI
date: 2022-01-05 15:53:46
---

你好，我是悦创。 花了 3h 编写的1.0站酷图片爬虫已经上线两天，但是出现了诸多 bug。所以，进行优化再次打包，就像顺便做个小打包笔记。项目链接：[https://github.com/AndersonHJB/zcool\_crawler](https://github.com/AndersonHJB/zcool_crawler)

1.  pip 来安装 Pyinstaller 模块

```python
pip install Pyinstaller
```

2.  命令行输入：
    
    ```python
    pyinstaller -i favicon.ico -F -w main.py
    ```
    

`-F` 生成一个文件，`-w` 用于隐藏命令行。无法生成 exe，提示 `'gbk' codec can't decode byte 0x80 in position 166: illegal multibyte sequence`，原因是源码中有两行 print 输出，而我将默认带的 stdout 控制台去掉了（`-w` 参数）。去掉这两行输出。 这样就成功了。

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/ca8c30e5478a41879df3049a1c8ea46e.png)