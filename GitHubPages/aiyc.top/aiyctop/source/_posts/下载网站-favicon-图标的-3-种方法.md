---
title: 下载网站 favicon 图标的 3 种方法
tags: []
id: '1778'
categories:
  - - uncategorized
date: 2021-07-02 20:30:38
---

你好，我是悦创。 在工作中，有时候我们会需要用到一些网站图标，但是浏览器上没有提供直接下载网站图标的方法，想要下载必须使用一些技巧，本文中就来分享下获取网站 favicon 的几种方法。

## 1.直接访问 favicon 地址获取 ico 文件

对于熟悉网站开发的人来说，相信很多人都知道网站的 favicon 是如何设置的，就是把一个文件名为 `favicon.ico` 的图片上传到网站根目录，然后浏览器就会自动识别其为网站的标签页的图标。 知道了这个后，我们就可以直接访问这个网址下载图标，格式为 `域名/favicon.ico` 比如 Google 的网站图标就是：

```code
https://www.google.com/favicon.ico
```

百度的 favicon 图标地址就是

```code
https://www.baidu.com/favicon.ico
```

访问网址后，我们再右键 – 图片存储为就可以了 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210702202405623.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 下载好的图片为原版的 `favicon.ico` 文件，文件大小同网站，不过需要注意的是一些网站并不支持这种方法，比如本站因为使用的 WordPress 自带的 favicon 设置功能，就不支持直接访问下载。

## 2.使用 favicon下载的网站

如果你遇到了不能直接访问下载的网站，或者想要更简单的下载方法，那么一些 favicon下载的网站是非常好的选择，这样的网站有很多，下面分享 2 个比较不错的

### 2.1 Favicon Grabber

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210702202517962.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) [Favicon Grabber](https://favicongrabber.com/) 是一个开源的 Favicon 下载网站，可以一键抓取下载任意网站的 favicon ，推荐它主要原因是颜值高，使用起来方便，只需要输入网址，再点击右侧的 Try it Grab 即可抓取到网站的图标

### 2.2 The Favicon Finder

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021070220262314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) [The Favicon Finder](https://besticon-demo.herokuapp.com/) 这个网站虽然界面并不是很简明，但是它的功能其实很强大，可以一键抓取到所有尺寸的favicon，比如上面的github网站，就抓取到了5个不同的图标，你可以挑选最需要的使用

## 3\. 使用 API 获取网站 favicon

一些网站还提供专门的 API 给其他的开发者或者特殊用途使用，可以更快捷的获取到网站图标

### 3.1 Google 的 API

```
https://www.google.com/s2/favicons?domain=google.com
```

```code
https://www.google.com/s2/favicons?domain=
```

使用 Google 的 API，你只需要把后面的域名改成自己的，就可以获取到对应的网站图标了，图片格式为 PNG，大小 `16*16` 像素

### 3.2 The Favicon Finder 的 API

```
https://besticon-demo.herokuapp.com/icon?url=google.com&size=80..120..200
```

The Favicon Finder 的 API 和它的网站一样，提供了很多专业级的参数选项，你可以在它的[Github文档](https://github.com/mat/besticon/blob/master/Readme.markdown)上查看到具体的用法