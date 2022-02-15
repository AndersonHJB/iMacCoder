---
title: CSDN不让复制css怎么控制不让选择和复制？
tags: []
id: '1561'
categories:
  - - 技术杂谈
date: 2021-03-11 19:18:13
---

CSS 禁止鼠标拖动选择文字，禁用页面内容选中和复制操作，只需使用user-select 属性即可。下面为各位详细介绍使用方法。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210311191128227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### css 怎么控制网页内容不让选择和复制？

要想通过 CSS 禁用页面内容选中和复制操作，需要增加如下代码：

```css
-moz-user-select: none; 
-webkit-user-select: none; 
-ms-user-select: none; 
-khtml-user-select: none; 
user-select: none;
```

### 1、禁止选中某一段文字

```css
<p id="copyright">不能复制的文字</p>

#copyright{
    user-select: none; 
}
```

### 2、禁止选择网页所有文字

```css
body{
    user-select: none; 
}
```