---
title: gitbook的入坑之路
tags: []
id: '1980'
categories:
  - - GitBook开发笔记
date: 2021-10-11 20:34:55
---

你好，我是悦创。 安装 gitbook 教程很多，我这里就不详细展开了，可以点击这个链接查看：[https://www.aiyc.top/1947.html](https://www.aiyc.top/1947.html) 如果链接失效，可以留言。 这里主要说一下我安装 gitbook 中所遇到的坑。

# 1\. 问题：安装 gitbook 出现

```cmd
TypeError: cb.apply is not a function 
```

## 解决办法：nodejs 降级

安装 gitbook 的一些问题 gitbook init 和 if (cb) cb.apply(this, arguments)，cb.apply is not a function

### 一，使用 gitbook init 时，卡在了 Installing GitBook 3.2.3 这一步

**解决办法：**

1.  翻墙
2.  使用淘宝镜像下载：
3.  npm下载路径，检查是不是淘宝镜像：

```cmd
npm config get registry
npm config set registry https://registry.npm.taobao.org
```

切换成淘宝镜像 再检查是不是淘宝镜像：

```cmd
npm config get registry
```

再安装：

```cmd
gitbook init
```

之前是一直卡在这里，我打了三篇代码没好！！设置之后，打了一局，回头一看，就出来了！ 但是报错了！！！但这又是另一个悲伤的故事。。。

### 二，if (cb) cb.apply(this, arguments)，cb.apply is not a function

产生了如下的报错： ![在这里插入图片描述](https://img-blog.csdnimg.cn/6a749f8aeef74035b4e19b56964dc155.png) 产生这个报错的原因在于，nodejs 的版本不对，不支持这个 gitbook. 有两个解决办法： **一，切换 nodejs 的版本：** 切换成 nodejs 的 v10.21.0 版本就会成功。 当然啦，在这里，我又接触到了新的知识！因为 nodejs 的版本很多，所以，就有 nodejs 的版本控制工具，可以方便地切换版本！ 这是这个方法的博客地址，[https://www.aiyc.top/1946.html](https://www.aiyc.top/1946.html) 二，第二个方法呢，就更方便且不要脸了，就是把报错的代码注释掉！ 直接打开报错的文件： `C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_modules\npm\node_modules\graceful-fs\polyfills.js` 错误的位置在代码的第287行，就是这个死乞白赖的函数！！！

```cmd
function statFix (orig) {
  if (!orig) return orig
  // Older versions of Node erroneously returned signed integers for
  // uid + gid.
  return function (target, cb) {
    return orig.call(fs, target, function (er, stats) {
      if (!stats) return cb.apply(this, arguments)
      if (stats.uid < 0) stats.uid += 0x100000000
      if (stats.gid < 0) stats.gid += 0x100000000
      if (cb) cb.apply(this, arguments)
    })
  }
}
```

这个函数的作用是用来修复 node.js 的一些 bug ,但是我就为了学个 gitbook ,没必要难为我自己！ 所以，我就找到这个函数的调用： ![在这里插入图片描述](https://img-blog.csdnimg.cn/4ec68f571b8f45afacdbfc1e06cc9ec1.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/f6a43ff1d12c4990aa227c1c60e3e91c.png) 就成这样子啦！嘿嘿~ ![在这里插入图片描述](https://img-blog.csdnimg.cn/b4cba8a8c0244ee9a17279921c2b4d1c.png)

# 2\. 问题：使用 gitbook 编译后公式显示为源码

## 解决办法：安装 mathjax 插件

1.  关于 mathjax 突然不能用了

**warning: 对于这个问题我并没有弄清楚原理，稀里糊涂就解决了，大家谨慎观看** 刚一开始我想在 gitbook 中使用 mathjax 写数学公式，但是按照网上的步骤 首先要有 node.js 环境 根目录创建 book.json 文件 内容为 {plugins: \["mathjax"\];} 然后根目录执行 gitbook install./ 那么我出现的问题是下载不下来，也许是真的需要多等一会，但是我是个急性子，直接 Google，发现一篇文章：[https://www.aiyc.top/1979.html](https://www.aiyc.top/1979.html)

> gitbook 官方已不再维护插件，mathjax 由于关闭了 cdn 而导致 gitbook 的 mathjax 的官方镜像出问题了。 因此在这里写了一个插件 gitbook-plugin-mathjax-pro

*   `npm install mathjax@2.7.7`
*   接着在 `book.json` 中引入：

```cmd
{
    "plugins": ["mathjax-pro"]
}
```

*   最后安装：`gitbook install ./`

虽然这次成功了，但是当我对第二个 book 使用同样的方式时，下载成功了，但是生成 book 的时候却报错了：

> Error with plugin “mathjax-pro”: Cannot find module 'mathjax/unpacked/MathJax

继续查，这次上百度，找到了这篇文章：[https://zhuanlan.zhihu.com/p/125577482](https://zhuanlan.zhihu.com/p/125577482)

> 在生成 pdf 或者生成网页时，mathjax 会报错，一般出现在新安装 mathjax 或者更新 mathjax 后，解决办法为,为 mathjax 降级，安装 2.7.6版本 `npm install mathjax@2.7.6`

然后我就稀里糊涂地直接在根目录下执行 `npm install mathjax@2.7.6` 然后继续 `gitbook serve` markdown 里的内容是这样的：

```markdown
## 3. 子查询的分类
+ **IN / NOT IN** 子查询；
+ $$\theta -Some / \theta-All$$ 子查询；
+ **EXISTS / NOT EXISTS** 子查询；
```

结果很完美： ![在这里插入图片描述](https://img-blog.csdnimg.cn/9352f0ae70b04c748e59720b4f658ecf.png)

# 3\. 问题：安装 mathjax 失败

```cmd
PluginError: Error with plugin "mathjax-pro": Cannot find module 'mathjax/unpacked/MathJax'
```

## 解决办法：先安装mathjax@2.7.6

同上！

# 4\. 问题：安装报错

```cmd
npm WARN saveError ENOENT: no such file or directory, open 'C:\Users\username\package.json'
```

## 解决办法：先执行命名 npm init

npm WARN saveError ENOENT: no such file or directory 解决 安装完成 node.js 后使用 npm 安装 vue 报错如下：

```cmd
C:\Users\lxz>npm uninstall vueWcsp
npm WARN saveError ENOENT: no such file or directory, open 'C:\Users\lxz\package.json'
npm WARN enoent ENOENT: no such file or directory, open 'C:\Users\lxz\package.json'
npm WARN lxz No description
npm WARN lxz No repository field.
npm WARN lxz No README data
npm WARN lxz No license field.


up to date in 0.765s
```

根据错误提示，是系统没有 ‘package.json’ 这个文件导致。这个文件的作用就是管理你本地安装的 npm 包，一个 package.json 文件可以做如下事情： 展示项目所依赖的 npm 包 允许你指定一个包的版本\[范围\] 让你建立起稳定，意味着你可以更好的与其他开发者共享 此刻我们需要执行命令：

```cmd
npm init
```

创建 package.json 文件，系统会提示相关配置，也可以使用命令：

```cmd
npm init -y
```

直接创建 package.json 文件，这样创建好处是必填项已经帮你填好，执行完命令后可以看到用户路径下多了一个 package.json 文件。 关于 gitbook 我更多文章：

1.  [http://www.chengweiyang.cn/gitbook/index.html](http://www.chengweiyang.cn/gitbook/index.html)
2.  [http://note.heifahaizei.com/book/](http://note.heifahaizei.com/book/)
3.  [https://juejin.cn/post/6931225754264928269](https://juejin.cn/post/6931225754264928269)
4.  [https://chrisniael.gitbooks.io/gitbook-documentation/content/](https://chrisniael.gitbooks.io/gitbook-documentation/content/)
5.  [https://yangjh.oschina.io/gitbook/faq/Plugins.html](https://yangjh.oschina.io/gitbook/faq/Plugins.html) 有测验功能教程
6.  [https://learn-gitbook.gitbook.io/gitbook/](https://learn-gitbook.gitbook.io/gitbook/)
7.  [https://allen5183.gitbooks.io/gitbook/content/plugins/quizzes/introduce.html](https://allen5183.gitbooks.io/gitbook/content/plugins/quizzes/introduce.html) 搭配 5

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/0a945d71ee33472fb78c05a7f3914cf9.png)