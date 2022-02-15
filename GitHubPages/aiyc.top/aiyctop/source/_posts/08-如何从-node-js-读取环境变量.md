---
title: 08-如何从 Node.js 读取环境变量
tags: []
id: '1966'
categories:
  - - NodeJS
date: 2021-10-08 15:46:19
---

你好，我是悦创。 Node.js 的 `process` 核心模块提供了 `env` 属性，该属性承载了在启动进程时设置的所有环境变量。 这是访问 NODE\_ENV 环境变量的示例，该环境变量默认情况下被设置为 `development`。

> 注意：`process` 不需要 "require"，它是自动可用的。

```javascript
process.env.NODE_ENV // "development"
```

在脚本运行之前将其设置为 "production"，则可告诉 Node.js 这是生产环境。 可以用相同的方式访问设置的任何自定义的环境变量。

#### 下一篇：待更新

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png)