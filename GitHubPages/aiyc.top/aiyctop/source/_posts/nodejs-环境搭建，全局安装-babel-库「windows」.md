---
title: nodejs 环境搭建，全局安装 babel 库「Windows」
tags: []
id: '749'
categories:
  - - AST系列
date: 2020-07-24 13:22:00
---

### nodejs 环境搭建，全局安装 babel 库「Windows」

因为操作 AST 的库是 node 的 babel 库，因此需要安装 nodejs 。 因为我的电脑是 Win10 系统，因此以 Win10 系统为例。 首先打开网站: [**Nodejs官方网站**](https://nodejs.org/zh-cn/) ，下载长期支持版: ![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200724132007.png) 然后一步一步安装即可。安装后，打开命令行工具 cmd，输入 node，查看是否安装成功: ![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200724132013.png) 怎么运行一个 JavaScript 文件？ 在桌面新建一个 hello.js 文件，注意后缀名是 .js，然后打开该文件输入:

```javascript
console.log('Hello,JavaScript!');
```

保存即可。 在桌面处打开 cmd，输入命令 node hello.js ,回车即可运行: ![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200724132016.png) 怎么全局安装 babel 库？ 按下快捷键 win + R,输入 cmd，然后再输入命令:

```cmd
npm install @babel/core -g
```

像下面这样: ![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200724132020.png) 一般来说，像这么安装的库不会有什么问题，但是在 win 上面做开发会有很多意想不到的问题。这么安装也会报错: ![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200724132023.png) 这个时候可以尝试下下面的方法,添加环境变量: 变量名: NODE\_PATH 变量值1：

```cmd
C:\Users\Administrator\AppData\Roaming\npm\node_modules
```

变量值2：

```cmd
C:\Users\Administrator\AppData\Roaming\npm\node_modules\@babel\core\node_modules
```

如果这样还是没有办法，说明你的 win 系统跟我一样，特别的烂，这个时候我们可以在某文件夹下面安装 babel 库，比如我在 E 盘，新建一个 AST 的目录文件夹，然后再这个文件夹里安装即可，命令:

```cmd
npm install @babel/core
```

下图就表示安装成功了， ![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200724132028.png) 不过每次需要在该文件夹下运行 js 文件，调用 babel 库才不会报错。 如果你还是想在任意位置运行调用 babel 库不报错，可以尝试下面的方法：

```cmd
const parser = require("E:\\AST\\node_modules\\@babel/parser");
```

补全 babel 库的路径即可。这样就可以在任意位置运行了。 也可以参考下面的这篇文章: [**更改node全局安装位置**](https://www.jianshu.com/p/38e3b6fe5f7a?tdsourcetag=s_pcqq_aiomsg) 在我电脑上测试没有成功，不过你们可以试试。