---
title: Jquery实现京东右侧固定层
tags: []
id: '1312'
categories:
  - - JavaScript
date: 2020-12-24 17:14:22
---

## 页面代码如下

```markup
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>京东首页右侧固定层</title>
    <link href="css/nav.css" rel="stylesheet">
    <script src="js/jquery-1.12.4.js"></script>
    <script src="js/js.js"></script>
</head>
<body>
<nav id="nav">
    <li><span></span>
        <p>就东会员</p></li>
    <li><span></span>
        <p>购物车</p></li>
    <li><span></span>
        <p>我的关注</p></li>
    <li><span></span>
        <p>我的足迹</p></li>
    <li><span></span>
        <p>我的消息</p></li>
    <li><span></span>
        <p>咨询JIMI</p></li>
</nav>
</body>
</html>
```

## css 代码如下

```css
*{margin: 0; padding:0; font-size: 12px;}
ul,ol,li{list-style: none;}
#nav{width: 100px; margin: 0 auto;}
#nav li{height:36px;}
#nav li span{
    display: block;
    float: right;
    width: 35px;
    height: 35px;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
    background: #7a6e6e url("../images/toolbars.png") no-repeat;
}

#nav li span:hover{ background-color: red;}
#nav li:nth-of-type(1) span{background-position: 0px -15px;}
#nav li:nth-of-type(2) span{background-position: 0px -57px;}
#nav li:nth-of-type(3) span{background-position: 1px -106px;}
#nav li:nth-of-type(4) span{background-position: 0px -156px;}
#nav li:nth-of-type(5) span{background-position: 0px -200px;}
#nav li:nth-of-type(6) span{background-position: 2px -265px;}
#nav li p{

    height: 35px;
    text-align: left;
    background: red;
    color: #ffffff;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
    line-height: 35px;
    padding-left: 10px;
    display: none;
}
```

## js 代码如下

```JavaScript
$(document).ready(function () {
    var index=-1;
    $("#nav li>span").mouseover(function () {
index=$("#nav li>span").index($(this));
$("#nav li:eq("+index+") span~p").show();
}).mouseout(function () {
    $("#nav li:eq("+index+") span~p").hide();
});
})
```