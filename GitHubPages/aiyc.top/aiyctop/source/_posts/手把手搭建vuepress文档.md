---
title: 手把手搭建VuePress文档
tags: []
id: '1981'
categories:
  - - VuePress开发
date: 2021-10-12 00:16:03
---

你好，我悦创。 原本想用 gitbook 实现流沙团队文旦，奈何出现一堆奇奇怪怪的 bug 后，我花了一天时间写完文档，然后决定放弃它使用 VuePress。

# 1\. 准备条件（Prerequisites）

1.  Node.js v12+
2.  Yarn v1 classic (Optional)

## 1.1 Node.js 安装

大佬级别直接看下面这句话，就没啥问题： 这个安装很简单，只需要下载，然后一路 next 即可。下载链接：[https://nodejs.org/en/](https://nodejs.org/en/) 小白继续看看下来： 用于所有主流平台的官方软件包，可访问 [http://nodejs.cn/download/](http://nodejs.cn/download/) 安装 Node.js 的其中一种非常便捷的方式是通过软件包管理器。 对于这种情况，每种操作系统都有其自身的软件包管理器。 在 macOS 上，Homebrew 是业界的标准，在安装之后可以非常轻松地安装 Node.js（通过在 CLI 中运行以下命令）：

```cmd
brew install node
```

其他适用于 Linux 和 Windows 的软件包管理器列出在 [https://nodejs.org/en/download/package-manager/](https://nodejs.org/en/download/package-manager/) 。 nvm 是一种流行的运行 Node.js 的方式。 例如，它可以轻松地切换 Node.js 版本，也可以安装新版本用以尝试并且当出现问题时轻松地回滚。 这对于使用旧版本的 Node.js 来测试代码非常有用。 详见 [https://github.com/creationix/nvm](https://github.com/creationix/nvm)。 [NVM 常用命令](https://www.aiyc.top/1946.html)：[https://www.aiyc.top/1946.html](https://www.aiyc.top/1946.html) 建议，如果刚入门并且还没有用过 Homebrew，则使用官方的安装程序，否则，Homebrew 是更好的解决方案。 无论如何，当安装 Node.js 之后，就可以在命令行中访问 node 可执行程序。

## 1.2 安装 yarn（Optional）

```cmd
npm install --global yarn
yarn --version
```

# 2\. 快速上手

> 本文会帮助你从头搭建一个简单的 VuePress 文档。如果你想在一个现有项目中使用 VuePress 管理文档，从步骤 3 开始。

## 2.1 创建并进入一个新目录

**我用的是 Windws 下使用 Linux 命令，Windows 直接界面创建文件夹，cmd 进入文件夹就可以了。**

> PS：[买不起MacBook，使用Windows 10配置zsh命令行做开发](https://www.aiyc.top/1976.html)：[https://www.aiyc.top/1976.html](https://www.aiyc.top/1976.html) 有时候还不是很好用。

```cmd
mkdir vuepress-starter && cd vuepress-starter
```

**命令解析：**

```cmd
mkdir 项目文件夹名称 && cd 项目文件夹名称
```

**我的操作：**

```cmd
# mkdir quicksand_vuepress && cd quicksand_vuepress
aiyc@aiyc:/mnt/d/gitee_all/quicksand_vuepress$
```

**命令也可以分开：**

```cmd
mkdir vuepress-starter
cd vuepress-starter
```

## 2.2 使用你喜欢的包管理器进行初始化

```cmd
git init
yarn init # npm init
```

**我的操作：**

```cmd
clela@AIYC D:\gitee_all\quicksand_vuepress
# yarn init # npm init
yarn init v1.22.15
question name (quicksand_vuepress): quicksand_vuepress
question version (1.0.0): 1.0.0
question description: "流沙团队电子书1.0"
question entry point (index.js): index.js
question repository url: https://github.com/QuicksandTeam/quicksandteam.github.io
question author (aiyc <1432803776@qq.com>):
question license (MIT):
question private:
success Saved package.json
Done in 132.92s.
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7e3b41674b1b47048b1cf8df61ebdd93.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/f4939db63ea5417ba3759366fb123c17.png)

## 2.3 将 VuePress 安装为本地依赖

我们已经不再推荐全局安装 VuePress

```sh
yarn add -D vuepress@next
# npm install -D vuepress@next
# yarn add -D vuepress
# npm install -D vuepress # next 意味着最新版。last 意味着旧版本
```

> **注意** 如果你的现有项目依赖了 webpack 3.x，我们推荐使用 Yarn (opens new window)而不是 npm 来安装 VuePress。因为在这种情形下，npm 会生成错误的依赖树。

### **坑 1：最新版的 VuePress 需要大于 V12.13.0**

```cmd
clela@AIYC D:\gitee_all\quicksand_vuepress
# yarn add -D vuepress@next
yarn add v1.22.15
info No lockfile found.
[1/4] Resolving packages...
warning vuepress > @vuepress/bundler-webpack > webpack-dev-server > url > querystring@0.2.0: The querystring API is considered Legacy. new code should use the URLSearchParams API instead.
warning vuepress > @vuepress/bundler-webpack > webpack-dev-server > sockjs > uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
[2/4] Fetching packages...
error copy-webpack-plugin@9.0.1: The engine "node" is incompatible with this module. Expected version ">= 12.13.0". Got "10.12.0"
error Found incompatible module.
info Visit https://yarnpkg.com/en/docs/cli/add for documentation about this command
```

需要切换 nodejs 的版本，这里还是推荐使用 nvm：[https://www.aiyc.top/1946.html](https://www.aiyc.top/1946.html)

## 2.4 在 package.json 中添加一些 [scripts](https://classic.yarnpkg.com/en/docs/package-json#toc-scripts)

这一步骤是可选的，但我们推荐你完成它。在下文中，我们会默认这些 scripts 已经被添加。

```json
{
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  }
}
```

**其实，这个文件，在我初始化的时候就创建了。不过我再补充一下上面的内容。** 为了，防止你真的是零基础小白。我这里把里面的全部内容 copy 出来，直接修改也可以。

```json
{
  "name": "quicksand_vuepress",
  "version": "1.0.0",
  "description": "流沙团队电子书",
  "main": "index.js",
  "repository": "https://github.com/QuicksandTeam/quicksandteam.github.io",
  "author": "aiyc <1432803776@qq.com>",
  "license": "MIT",
  "devDependencies": {
    "vuepress": "^2.0.0-beta.26"
  },
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  }
}

```

## 2.5 将默认的临时目录和缓存目录添加到 `.gitignore` 文件中

**Linxu or Mac：**

```sh
echo 'node_modules' >> .gitignore
echo '.temp' >> .gitignore
echo '.cache' >> .gitignore
```

Windows 直接创建文件 `.gitignore` 写入如下内容：

```txt
node_modules
.temp
.cache
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/eaa2a93696d64dc5842a8478ba7c79a0.png)

## 2.6 创建你的第一篇文档

```sh
mkdir docs && echo '# Hello quicksand' > docs/README.md
```

Windows 的话，直接创建就好啦。把创建的文档放在 docs 文件夹下（这个文件夹自己创建）。

## 2.7 在本地启动服务器

```sh
yarn docs:dev # npm run docs:dev
```

当我们运行 `yarn docs:dev` 就相当于运行 `vuepress dev docs` VuePress 会在 [http://localhost:8080在新窗口打开](http://localhost:8080/) 启动一个热重载的开发服务器。当你修改你的 Markdown 文件时，浏览器中的内容也会自动更新。 现在，你应该已经有了一个简单可用的 VuePress 文档网站。接下来，了解一下 VuePress [配置](https://v2.vuepress.vuejs.org/zh/guide/configuration.html) 相关的内容。

# 3\. 配置

## 3.1 配置文件

如果没有任何配置，你的 VuePress 站点仅有一些最基础的功能。为了更好地自定义你的网站，让我们首先在你的文档目录（docs）下创建一个 `.vuepress` 目录，所有 VuePress 相关的文件都将会被放在这里。你的项目结构可能是这样：

```cmd
├─ docs
│  ├─ .vuepress
│  │  └─ config.js
│  └─ README.md
├─ .gitignore
└─ package.json
```

VuePress 站点必要的配置文件是 `.vuepress/config.js`，它应该导出一个 JavaScript 对象。如果你使用 TypeScript ，你可以将其替换为 `.vuepress/config.ts` ，以便让 VuePress 配置得到更好的类型提示。 如果你是 JavaScript ：

```JavaScript
module.exports = {
  lang: 'zh-CN',
  title: '你好， 流沙团队！',
  description: '这是团队的第一个 VuePress 站点',

  themeConfig: {
    logo: 'https://vuejs.org/images/logo.png',
  },
}
```

如果你是 TypeScript ：

```TypeScript
import { defineUserConfig } from 'vuepress'
import type { DefaultThemeOptions } from 'vuepress'

export default defineUserConfig<DefaultThemeOptions>({
  lang: 'en-US',
  title: 'Hello quicksandTeam',
  description: 'Just playing around',

  themeConfig: {
    logo: 'https://vuejs.org/images/logo.png',
  },
})
```

> **提示** 我们接下来会把这个配置对象称为 VuePress 配置.

## 3.2 配置作用域

你可能已经注意到了，在 VuePress 配置中有一项 `themeConfig` 配置项。 在 `themeConfig` 外部的配置项属于 **站点配置** ，而在 `themeConfig` 内部的配置项则属于 **主题配置**。

### 3.2.1 站点配置

站点配置的意思是，无论你使用什么主题，这些配置项都可以生效。 我们知道，每一个站点都应该有它的 `lang`, `title` 和 `description` 等属性，因此 VuePress 内置支持了这些属性的配置。 **提示：** 前往 [配置参考](https://v2.vuepress.vuejs.org/zh/reference/config.html) 查看所有站点配置。 这里我做一些我自己的配置。 VuePress 配置的参考文档，可以通过配置文件来设置这些配置。 VuePress 约定的配置文件为（按照优先顺序）：

*   当前工作目录 `cwd` 下：
    *   `vuepress.config.ts`
    *   `vuepress.config.js`

* * *

*   源文件目录 `sourceDir` 下：
    *   `.vuepress/config.ts`
    *   `.vuepress/config.js`

你也可以通过 [命令行接口](https://v2.vuepress.vuejs.org/zh/reference/cli.html) 的 `--config` 选项来指定配置文件。

#### 1\. base

*   类型： `string`
    
*   默认值： `/`
    

**详情：** **如果你想让你的网站部署到一个子路径下，你将需要设置它。** 它的值应当总是以斜杠开始，并以斜杠结束。 举例来说，如果你想将你的网站部署到 `https://quicksandteam.github.io/aiyc/`，那么 `base` 应该被设置成 `"/aiyc/"`。 `base` 将会作为前缀自动地插入到所有以 `/` 开始的其他选项的链接中，所以你只需要指定一次。 **参考：** - [指南 > 静态资源 > Base Helper](https://v2.vuepress.vuejs.org/zh/guide/assets.html#base-helper) - [指南 > 部署](https://v2.vuepress.vuejs.org/zh/guide/deployment.html)

#### 2\. lang

*   类型： `string`
    
*   默认值： `en-US`
    

**详情：** 站点的语言。 它将会在最终渲染出的 HTML 中作为 `<html>` 标签的 `lang` 属性。 它可以设置在不同语言的 locales 中。中文：zh-CN **参考：**

*   [配置 > locales](https://v2.vuepress.vuejs.org/zh/reference/config.html#locales)

#### 3\. title

*   类型： `string`
    
*   默认值： `''`
    

**详情：** 站点的标题。 它将会作为所有页面标题的后缀，并且在默认主题的导航栏中显示。 它可以设置在不同语言的 locales 中。 **参考：**

*   [配置 > locales](https://v2.vuepress.vuejs.org/zh/reference/config.html#locales)

#### 4\. description

*   类型： `string`
    
*   默认值： `''`
    

**详情：** 站点的描述。 它将会在最终渲染出的 HTML 中作为 `<meta name="description" />` 标签的 `content` 属性。它会被每个页面的 Frontmatter 中的 `description` 字段覆盖。 它可以设置在不同语言的 locales 中。 **参考：**

*   [配置 > locales](https://v2.vuepress.vuejs.org/zh/reference/config.html#locales)
*   [Frontmatter > description](https://v2.vuepress.vuejs.org/zh/reference/frontmatter.html#description)

#### 5\. head

*   类型： `HeadConfig[]`
    
*   默认值： `[]`
    

**详情：** 在最终渲染出的 HTML 的 `<head>` 标签内加入的额外标签。 你可以通过 `[tagName, { attrName: attrValue }, innerHTML?]` 的格式来添加标签。 它可以设置在不同语言的 locales 中。 **示例：** 增加一个自定义的 favicon ：

```js
module.exports = {
  head: [['link', { rel: 'icon', href: '/images/logo.png' }]],
}
```

渲染为：

```markup
<head>
  <link rel="icon" href="/images/logo.png" />
</head>
```

虽然，后面我会放上我写的配置，但是现在我还是放一下这个 head 的多个 html 写法：

```json
head: [
            ['link', { rel: 'icon', type: "image/png", href: 'images/favicon.ico',}],
            ['meta', { name: "keywords", content: "流沙团队：AI悦创、久远,编程一对一教学,Python,爬虫,深度学习,机器学习,数据分析,网络,IT,技术,博客,算法与数据结构"}]
            ],
```

那我对应的文件夹以及图片的结构呢？ ![在这里插入图片描述](https://img-blog.csdnimg.cn/aa6e66e3ace84a7a9eb2da46d6e4ac70.png#pic_center) **参考：** [https://v2.vuepress.vuejs.org/zh/guide/assets.html](https://v2.vuepress.vuejs.org/zh/guide/assets.html) **参考：**

*   [配置 > locales](https://v2.vuepress.vuejs.org/zh/reference/config.html#locales)
*   [Frontmatter > head](https://v2.vuepress.vuejs.org/zh/reference/frontmatter.html#head)

#### 6\. locales

*   类型： `{ [path: string]: Partial<SiteLocaleData> }`
*   默认值： `{}`

**详情：** 多语言支持的各个语言 locales 。

*   [lang](https://v2.vuepress.vuejs.org/zh/reference/config.html#lang)
*   [title](https://v2.vuepress.vuejs.org/zh/reference/config.html#title)
*   [description](https://v2.vuepress.vuejs.org/zh/reference/config.html#description)
*   [head](https://v2.vuepress.vuejs.org/zh/reference/config.html#head)

**参考：** [指南 > I18n](https://v2.vuepress.vuejs.org/zh/guide/i18n.html) 写到 6 这个点呢，就不得不说怎么配置了。不过不是现在，是后面的站点配置。 不过写到这里，也就开始了主题的配置了。

* * *

### 3.2.2 主题配置

主题配置将会被 VuePress 主题来处理，所以它取决于你使用的主题是什么。 如果你没有设置 VuePress 配置的 `theme` 配置项，则代表使用的是默认主题。至于其他主题，等我有时间，我一定安排。如果你们着急就分享和关注公众号：AI悦创，并私信我哈。 **提示：** 前往 [默认主题 > 配置参考](https://v2.vuepress.vuejs.org/zh/reference/default-theme/config.html) 查看默认主题的配置。

#### 1\. home

*   类型： string
*   默认值： /

**详情：** 首页的路径。 它将被用于：

*   导航栏中 Logo 的链接
*   404 页面的 返回首页 链接

#### 2\. navbar

*   类型： `false (NavbarItem NavbarGroup string)[]`
*   默认值： `[]`

**详情：** 导航栏配置。 设置为 `false` 可以禁用导航栏。 为了配置导航栏元素，你可以将其设置为 _导航栏数组_ ，其中的每个元素是 `NavbarItem` 对象、 `NavbarGroup` 对象、或者字符串：

*   `NavbarItem` 对象应该有一个 `text` 字段和一个 `link` 字段，还有一个可选的 `activeMatch` 字段。
*   `NavbarGroup` 对象应该有一个 `text` 字段和一个 `children` 字段。 `children` 字段同样是一个 _导航栏数组_ 。
*   字符串应为目标页面文件的路径。它将会被转换为 `NavbarItem` 对象，将页面标题作为 `text` ，将页面路由路径作为 `link` 。

写到这里的时候，我发现文档很强很全，所以我直接待会把配置好的文件内容贴出来。 接下来，我配置一下，目前需要的导航栏： 目前设想，我需要：

*   专栏
*   Github
*   关于团队
*   资源分享
*   技术杂谈
*   付费教学
*   数据结构与算法
*   Java 入门
*   Python 入门
*   Go 入门
*   源码分析
*   广告
*   期末不挂科

#### 3\. 站点多语言配置

要启用 VuePress 的多语言支持，首先需要使用如下的文件目录结构：

```cmd
docs
├─ README.md
├─ foo.md
├─ nested
│  └─ README.md
└─ zh
   ├─ README.md
   ├─ foo.md
   └─ nested
      └─ README.md
```

那上面是官方给的结构，我是中国人，所以呢。我就把 zh 改成 en 吧。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/1074adea36b647b9b9f580f27b216cda.png) 然后，在你的 [配置文件](https://v2.vuepress.vuejs.org/zh/guide/configuration.html#配置文件) 中设置 `locales` 选项：

```js
module.exports = {
  locales: {
    // 键名是该语言所属的子路径
    // 作为特例，默认语言可以使用 '/' 作为其路径。
    '/': {
      lang: 'en-US',
      title: 'VuePress',
      description: 'Vue-powered Static Site Generator',
    },
    '/zh/': {
      lang: 'zh-CN',
      title: 'VuePress',
      description: 'Vue 驱动的静态网站生成器',
    },
  },
}
```

那和上面也是一样的，我要设置一个英文站点，但是显然上面的官方提供样例的配置是不够的，还需要看这个连接的文档： 所以我也一同配置一波：

```js
module.exports = {
  locales: {
    // 键名是该语言所属的子路径
    // 作为特例，默认语言可以使用 '/' 作为其路径。
    '/': {
      lang: 'zh-CN',
      title: '流沙团队',
      description: '一股无形的力量——流沙',
    },
    '/en/': {
      lang: 'en-US',
      title: 'QuickSandTeam',
      description: 'An invisible force -- quicksandteam',
    },
  },
}
```

如果一个语言没有声明 `lang`, `title`, `description` 或者 `head` ，VuePress 将会尝试使用顶层配置的对应值。如果每个语言都声明了这些值，那么顶层配置中的对应值可以被省略。 **提示：** 配置参考： [locales](https://v2.vuepress.vuejs.org/zh/reference/config.html#locales) 但是，上面的配置我发现显示的和我时间的语言有区别。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/6a6612dc0ce64546a8998117711b78dc.png) 第一个应该是中文，却上图那样显示。第二个也是： ![在这里插入图片描述](https://img-blog.csdnimg.cn/b285c5a77e2545c7b141d1e0c6523238.png) 第二个还算好一点，所以进行优化修改：

```js
themeConfig: {
  logo: 'https://vuejs.org/images/logo.png',

  locales: {
    '/': {
      selectLanguageText: "选择语言",
          selectLanguageName: '简体中文',
          selectLanguageText: '选择语言',
          selectLanguageAriaLabel: '选择语言',
    },
    '/en/': {
      selectLanguageText: "Languages",
      selectLanguageName: 'English',
    }
  },
```

待更新！

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/758220eab0fc40f6a8206cd2f34e204a.png)