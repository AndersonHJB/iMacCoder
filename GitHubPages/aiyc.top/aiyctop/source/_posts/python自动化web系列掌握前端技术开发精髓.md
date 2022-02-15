---
title: Python自动化web系列掌握前端技术开发精髓
tags: []
id: '1537'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-04 10:51:29
---

网页内容，由三部分组成，分别是 html、css 和 javascript 。

*   html 是网页面部分
*   css 是美化网页的操作
*   javascript 是让网页可以交互起来

前端内容，html 是必须的，css 可以交给前端框架，js 也可以交给框架。 所以本问课这里主要介绍 html 部分和认识一个前端框架。html 是一种标记语言，结构是这样的的 内容 ，一个尖括号的起始标签，一个尖括号带 / 的结束标签。并且这种成对的标签，是可以嵌套的。

## HTML 基础

以上是 html 语法规则，下面来认识下基础 html 结构。

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>
<body>
    AI悦创，内容。
</body>
</html>
```

代码解释：

*   顶部第一行是申明，现在的 HTML 已经到了第五代。
*   然后 html 标签是开始，所有内容全部放在 html 标签里面。
*   html 内部只有 head 和 body 标签两个，也叫作网页的头和身体部分头部用于存放网页的说明，例如 title、meta 等标签身体部分放网页内容，就是你在浏览器中看到的内容
*   title 是特定的标签，就是这个网页的名字，展示在浏览器的标签页部分的信息

用浏览器打开，可以得到如下效果： ![image.png](https://img-blog.csdnimg.cn/img_convert/f309622c657f2a57f9ff70210dc7da27.png)

## BootStrap 是什么

以上是 html 的基础结构，接下来了解下前端框架，这里要介绍的是 Bootstrap 。 Bootstrap 是非常著名的前端框架之一，也是最早的前端框架。

> **一个小疑问：为什么会有前端框架的出现？**做网站，费时费力，网站难的是后台的服务搭建，这部分是用户看不到的，用户看到的地方是网页内容。及时你的后台在强大，前端效果不好看，用户也会觉得你这个站很low。 但并不是所有的人都懂如何美化网页，所有一个现成的前端框架就非常有必要的。使用前端框架，可以快速的实现你要的内容，并且配合上具体的使用文档，及时没有网页开发经验，也可以按照说明，快速的完成一个还算美观的前端页面。

关于 Bootstrap 的官方中文文档，官方链接：[Bootstrap官方中文](https://v3.bootcss.com/)

## 学习 Bootstrap

中文文档介绍很详细，看着就可以制作属于你自己的网页了。下面给出两个网页，一个是文章列表页，另一个是文章的详情页，源码文件夹中都有，如下截图【左侧效果，右侧源码】： ![image.png](https://img-blog.csdnimg.cn/img_convert/754c333e88aed05dbefbcb224f330eb9.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/d5d957965283f720dd57512ee3dcffa1.png) 这两个网页都是使用的 Bootstrap 框架做的，使用方式都是使用 cdn 链接的方式载入，比较快。

## 【选词填空】小练习

前端技术，主要是\_\_\_\_\_\_\_\_ 、\_\_\_\_\_\_\_\_和 \_\_\_\_\_\_\_\_。 \_\_\_\_\_\_\_\_是前端框架。

*   \[ \] JavaScript
*   \[ \] Django
*   \[ \] CSS
*   \[ \] HTML
*   \[ \] Bootstrap
*   \[ \] Python