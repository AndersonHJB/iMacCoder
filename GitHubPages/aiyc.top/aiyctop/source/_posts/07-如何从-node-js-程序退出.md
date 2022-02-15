---
title: 07-如何从 Node.js 程序退出
tags: []
id: '1964'
categories:
  - - NodeJS
date: 2021-10-08 15:38:19
---

你好，我是悦创。 有很多种方法可以终止 Node.js 应用程序。 当在控制台中运行程序时，可以使用 `ctrl-C` 将其关闭，但是这里要讨论的是以编程的方式退出。 `process` 核心模块提供了一种便利的方法，可以以编程的方式退出 Node.js 程序：`process.exit()`。 当 Node.js 运行此行代码时，进程会被立即强制终止。 这意味着任何待处理的回调、仍在发送中的任何网络请求、任何文件系统访问、或正在写入 `stdout` 或 `stderr` 的进程，所有这些都会被立即非正常地终止。 可以传入一个整数，向操作系统发送退出码：

```javascript
process.exit(1)
```

默认情况下，退出码为 `0`，表示成功。 不同的退出码具有不同的含义，可以在系统中用于程序与其他程序的通信。 有关退出码的信息，详见 http://nodejs.cn/api/process.html#process\_exit\_codes 也可以设置 `process.exitCode` 属性：

```javascript
process.exitCode = 1
```

当程序结束时，Node.js 会返回该退出码。 当进程完成所有处理后，程序会正常地退出。 使用 Node.js 启动服务器，例如 HTTP 服务器：

```javascript
const express = require('express')
const app = express()

app.get('/', (req, res) => {
  res.send('你好')
})

app.listen(3000, () => console.log('服务器已就绪'))
```

这个程序永远不会结束。 如果调用 `process.exit()`，则任何当前等待中或运行中的请求都会被中止。 这不太友好。 在这种情况下，需要向该命令发送 SIGTERM 信号，并使用进程的信号处理程序进行处理：

> 注意：`process` 不需要 "require"，它是自动可用的。

```javascript
const express = require('express')

const app = express()

app.get('/', (req, res) => {
  res.send('你好')
})

const server = app.listen(3000, () => console.log('服务器已就绪'))

process.on('SIGTERM', () => {
  server.close(() => {
    console.log('进程已终止')
  })
})
```

> 什么是信号？信号是一个 POSIX 内部通信系统：发送通知给进程，以告知其发生的事件。

`SIGKILL` 是告诉进程要立即终止的信号，理想情况下，其行为类似于 `process.exit()`。 `SIGTERM` 是告诉进程要正常终止的信号。它是从进程管理者（如 `upstart` 或 `supervisord`）等发出的信号。 可以从程序内部另一个函数中发送此信号：

```javascript
process.kill(process.pid, 'SIGTERM')
```

或从另一个正在运行的 Node.js 程序、或从系统中运行的其他任何的应用程序（能知道要终止的进程的 PID）。

#### [下一篇](https://www.aiyc.top/1966.html)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png)