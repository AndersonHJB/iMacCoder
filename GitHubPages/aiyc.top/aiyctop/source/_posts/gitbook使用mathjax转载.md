---
title: gitbook使用mathjax|转载
tags: []
id: '1979'
categories:
  - - GitBook开发笔记
date: 2021-10-11 20:18:23
---

你好，我是悦创。

> gitbook 官方已不再维护插件，mathjax 由于关闭了 cdn 而导致 gitbook 的 mathjax 的官方镜像出问题了。 因此在这里写了一个插件 gitbook-plugin-mathjax-pro。

## 怎么使用这个插件？

该插件使用的 mathjax 默认版本文 2.7.7， 因此以下均基于 2.7.7 介绍。

*   首先安装 mathjax

```cmd
npm install mathjax@2.7.7
```

*   接着在 book.json 中引入：

```cmd
{
    "plugins": ["mathjax-pro"]
}
```

*   最后安装

```cmd
gitbook install ./
```

接着就可以使用 mathjax 语法写数学公式了。 更多配置详见：[https://github.com/kevinkangkang/gitbook-plugin-mathjax-pro](https://github.com/kevinkangkang/gitbook-plugin-mathjax-pro)