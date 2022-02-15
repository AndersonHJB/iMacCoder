---
title: 02-如何安装 Node.js
tags: []
id: '1955'
categories:
  - - NodeJS
date: 2021-10-08 15:06:36
---

你好，我是悦创。 Node.js 可以通过多种方式进行安装。 这篇文章重点介绍了最常见、最方便的几种。 用于所有主流平台的官方软件包，可访问 http://nodejs.cn/download/。 安装 Node.js 的其中一种非常便捷的方式是通过软件包管理器。 对于这种情况，每种操作系统都有其自身的软件包管理器。 在 macOS 上，[Homebrew](https://brew.sh/) 是业界的标准，在安装之后可以非常轻松地安装 Node.js（通过在 CLI 中运行以下命令）：

```bash
brew install node
```

其他适用于 Linux 和 Windows 的软件包管理器列出在 https://nodejs.org/en/download/package-manager/。 `nvm` 是一种流行的运行 Node.js 的方式。 例如，它可以轻松地切换 Node.js 版本，也可以安装新版本用以尝试并且当出现问题时轻松地回滚。 这对于使用旧版本的 Node.js 来测试代码非常有用。 详见 https://github.com/creationix/nvm。 建议，如果刚入门并且还没有用过 Homebrew，则使用官方的安装程序，否则，Homebrew 是更好的解决方案。 无论如何，当安装 Node.js 之后，就可以在命令行中访问 `node` 可执行程序。

#### [下一篇](https://www.aiyc.top/1957.html)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png)