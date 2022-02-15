---
title: 设置pycharm打开terminal终端，自动进入虚拟环境的办法
tags: []
id: '2079'
categories:
  - - Pycharm
date: 2021-12-11 16:16:25
---

你好，我是悦创。 本来一直打开 terminal，会直接进入对应的虚拟环境，直到有一天更新 pycharm 后，发现打开 terminal 后直接进入了 base 环境，每次都要手动 activate 一下，比较麻烦仔细观察才发现，terminal 使用了 windows 的powershell，如下图所示： ![在这里插入图片描述](https://img-blog.csdnimg.cn/bdb1b16c730c4e93945d9cc61a6613b2.png)

## 解决办法：

Settings --> Tools --> Terminal --> Shell Path，`将 powershell 修改为 cmd.exe`，如下图所示： ![在这里插入图片描述](https://img-blog.csdnimg.cn/126f695841a74022b90db7f6a1ab8abf.png) 修改 shell 过后，可以看到使用的是 windows 的 cmd shell ，并且会自动跳转到虚拟环境 ![在这里插入图片描述](https://img-blog.csdnimg.cn/3a3a48dcdec94c768571dc41d04bbd6f.png)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh，公众号：AI悦创

![在这里插入图片描述](https://img-blog.csdnimg.cn/25e21e53cba04a56885c4f84319f641b.png)