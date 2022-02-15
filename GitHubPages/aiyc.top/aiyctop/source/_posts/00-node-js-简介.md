---
title: 00-Node.js 简介
tags: []
id: '1951'
categories:
  - - NodeJS
date: 2021-10-08 14:48:46
---

你好，我是悦创。 Node.js 是一个开源与跨平台的 JavaScript 运行时环境。 它是一个可用于几乎任何项目的流行工具！ Node.js 在浏览器外运行 V8 JavaScript 引擎（Google Chrome 的内核）。 这使 Node.js 表现得非常出色。 Node.js 应用程序运行于单个进程中，无需为每个请求创建新的线程。 Node.js 在其标准库中提供了一组异步的 I/O 原生功能（用以防止 JavaScript 代码被阻塞），并且 Node.js 中的库通常是使用非阻塞的范式编写的（从而使阻塞行为成为例外而不是规范）。 当 Node.js 执行 I/O 操作时（例如从网络读取、访问数据库或文件系统），Node.js 会在响应返回时恢复操作，而不是阻塞线程并浪费 CPU 循环等待。 这使 Node.js 可以在一台服务器上处理数千个并发连接，而无需引入管理线程并发的负担（这可能是重大 bug 的来源）。 Node.js 具有独特的优势，因为为浏览器编写 JavaScript 的数百万前端开发者现在除了客户端代码之外还可以编写服务器端代码，而无需学习完全不同的语言。 在 Node.js 中，可以毫无问题地使用新的 ECMAScript 标准，因为不必等待所有用户更新其浏览器，你可以通过更改 Node.js 版本来决定要使用的 ECMAScript 版本，并且还可以通过运行带有标志的 Node.js 来启用特定的实验中的特性。

## 大量的库

npm 的简单结构有助于 Node.js 生态系统的激增，现在 npm 仓库托管了超过 1,000,000 个可以自由使用的开源库包。

## Node.js 应用程序的示例

Node.js 最常见的 Hello World 示例是 Web 服务器：

```nodejs
const http = require('http')

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('你好世界\n')
})

server.listen(port, hostname, () => {
  console.log(`服务器运行在 http://${hostname}:${port}/`)
})
```

此代码首先引入了 Node.js [`http` 模块](http://nodejs.cn/api/http.html)。 Node.js 具有出色的[标准库](http://nodejs.cn/api/)，包括对网络的一流支持。 `http` 的 `createServer()` 方法会创建新的 HTTP 服务器并返回它。 服务器被设置为监听指定的端口和主机名。 当服务器就绪后，回调函数会被调用，在此示例中会通知我们服务器正在运行。 每当接收到新的请求时，[`request` 事件](http://nodejs.cn/api/http.html#http_event_request)会被调用，并提供两个对象：一个请求（[`http.IncomingMessage`](http://nodejs.cn/api/http.html#http_class_http_incomingmessage) 对象）和一个响应（[`http.ServerResponse`](http://nodejs.cn/api/http.html#http_class_http_serverresponse) 对象）。 这两个对象对于处理 HTTP 调用至关重要。 第一个对象提供了请求的详细信息。 在这个简单的示例中没有使用它，但是你可以访问请求头和请求数据。 第二个对象用于返回数据给调用方。 在此示例中：

```nodejs
res.statusCode = 200
```

设置 statusCode 属性为 200，以表明响应成功。 设置 Content-Type 响应头：

```nodejs
res.setHeader('Content-Type', 'text/plain')
```

关闭响应，添加内容作为 `end()` 的参数：

```nodejs
res.end('你好世界\n')
```

## Node.js 框架和工具

Node.js 是一个底层的平台。 为了使开发者做事变得容易又来劲，社区在 Node.js 上构建了数千个库。 久而久之，其中许多已成为受欢迎的选择。 以下是一些值得学习的清单：

*   [**AdonisJs**](https://adonisjs.com/): 一个全栈框架，高度专注于开发者的效率、稳定和信任。 Adonis 是最快的 Node.js Web 框架之一。
*   [**Express**](https://expressjs.com/): 提供了创建 Web 服务器的最简单但功能最强大的方法之一。 它的极简主义方法，专注于服务器的核心功能，是其成功的关键。
*   [**Fastify**](https://fastify.io/): 一个 Web 框架，高度专注于提供最佳的开发者体验（以最少的开销和强大的插件架构）。 Fastify 是最快的 Node.js Web 框架之一。
*   [**Gatsby**](https://www.gatsbyjs.com/): 一个基于 [React](https://reactjs.org/)、由 [GraphQL](https://graphql.org/) 驱动的静态网站生成器，具有非常丰富的插件和启动器生态系统。
*   [**hapi**](https://hapijs.com/): 一个富框架，用于构建应用程序和服务，使开发者可以专注于编写可重用的应用程序逻辑，而不必花费时间来搭建基础架构。
*   [**koa**](http://koajs.com/): 由 Express 背后的同一个团队构建，旨在变得更简单更轻巧。 新项目的诞生是为了满足创建不兼容的更改而又不破坏现有社区。
*   [**Loopback.io**](https://loopback.io/): 使构建需要复杂集成的现代应用程序变得容易。
*   [**Meteor**](https://meteor.com/): 一个强大的全栈框架，以同构的方式使用 JavaScript 构建应用（在客户端和服务器上共享代码）。 曾经是提供所有功能的现成工具，现在可以与前端库 [React](https://reactjs.org/)，[Vue](https://vuejs.org/) 和 [Angular](https://angular.io/) 集成。 也可以用于创建移动应用。
*   [**Micro**](https://github.com/zeit/micro): 提供了一个非常轻量级的服务器，用于创建异步的 HTTP 微服务。
*   [**NestJS**](https://nestjs.com/): 一个基于 TypeScript 的渐进式 Node.js 框架，用于构建企业级的高效、可靠和可扩展的服务器端应用程序。
*   [**Next.js**](https://nextjs.org/): 一个 [React](https://reactjs.org/) 框架，可为你提供生产所需的所有功能的最佳开发者体验：混合静态和服务器渲染、TypeScript 支持、智能捆绑、路由预取等。
*   [**Nx**](https://nx.dev/): 使用 NestJS、Express、[React](https://reactjs.org/)、[Angular](https://angular.io/) 等进行全栈开发的工具包！ Nx 有助于将开发工作从一个团队（构建一个应用程序）扩展到多个团队（在多个应用程序上进行协作）！
*   [**Sapper**](https://sapper.svelte.dev/): Sapper 是一个用于构建各种规模的 Web 应用程序的框架，具有出色的开发体验和灵活的基于文件系统的路由。还提供 SSR 等！
*   [**Socket.io**](https://socket.io/): 一个实时通信引擎，用于构建网络应用程序。
*   [**Strapi**](https://strapi.io/): Strapi 是一个灵活的开源 Headless CMS，可使开发者可以自由选择自己喜欢的工具和框架，同时还允许编辑人员轻松地管理和分发其内容。 通过使管理面板和 API 可以通过插件系统进行扩展，Strapi 使全球最大的公司能够加速内容交付，同时构建优美的数字体验。

##### [下一篇](https://www.aiyc.top/1952.html)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

[![https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png "https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png")](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png "https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png")