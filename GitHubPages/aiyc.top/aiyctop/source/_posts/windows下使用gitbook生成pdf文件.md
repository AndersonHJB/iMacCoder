---
title: Windows下使用gitbook生成PDF文件
tags: []
id: '1969'
categories:
  - - GitBook开发笔记
date: 2021-10-09 10:58:01
---

你好，我是悦创。 最近，在搞 gitbook 的时候，生成 pdf 出现了问题。然后有了以下解决方法。

## 安装 calibre

calibre 是一个支持PDF/EPUB/MOBI等文件格式转换的工具，可以前往[官网](https://calibre-ebook.com/)查看下载并安装。 当然也可以点击这个链接：[https://download.calibre-ebook.com/](https://download.calibre-ebook.com/) 安装完成后需要设置环境变量，将 calibre 装目录增加到环境变量：

```cmd
默认安装的目录
C:\Program Files\Calibre2
```

## gitbook

```cmd
npm install -g gitbook-cli
gitbook fetch 3.2.3
```

## 生成 PDF

下载一个项目以供测试：

```cmd
前往网站下载
https://github.com/apachecn/dataviz-zh

或者使用git
git clone https://github.com/apachecn/dataviz-zh.git
```

命令行界面切入到目录下面，运行以下命令生成 PDF

```cmd
gitbook pdf

或者生成其他文件格式
gitbook <pdfepubmobi>
```

我这里用的是我自己的项目：

```cmd
clela@AIYC D:\gitee_all\quicksand_suanfa
# gitbook pdf .
info: 7 plugins are installed
info: 6 explicitly listed
info: loading plugin "highlight"... OK
info: loading plugin "search"... OK
info: loading plugin "lunr"... OK
info: loading plugin "sharing"... OK
info: loading plugin "fontsettings"... OK
info: loading plugin "theme-default"... OK
info: found 14 pages
info: found 14 asset files
info: >> generation finished with success in 6.8s !
info: >> 1 file(s) generated

clela@AIYC D:\gitee_all\quicksand_suanfa
#
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/a63e33ae3c5d4e23a82cf79876f70843.png)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/2feddd39d97748048190d5e3dac56c56.png)