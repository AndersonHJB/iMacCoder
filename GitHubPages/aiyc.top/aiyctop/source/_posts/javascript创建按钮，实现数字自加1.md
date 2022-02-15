---
title: JavaScript创建按钮，实现数字自加1
tags: []
id: '2032'
categories:
  - - 技术杂谈
date: 2021-11-29 19:50:07
---

你好，我是悦创。 最近跆拳道内部比赛需要一个比赛倒计时和加分扣分的功能。 所以，我们使用 HTML 先实现。 大致步骤： 1、写一个 p 标签，指定一个 id 选择器，输入数字！ 2、写一个 input 标签，指定type属性的属性值为 button，创建一个按钮，加入 onclick 事件！ 3、为 p 标签和 input 标签指定相关的 CSS 样式（可以省略） 4、用 js 创建一个自加的函数，在函数中用 document 对象的 `getElementById()` 方法，选中 p 标签。 5、通过 innerHTML 获取 p 标签的内容，实现自加！！ 实现代码如下：

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>自加</title>
    <style>
            body {
                text-align: center;
            }
            p,#ipt,#btn {
                font-size: 50px;
            }
            #ipt {
                width: 100px;
                margin-bottom: 10px;
            }
            #ipt,#btn {
                height: 100px;
                padding: 0px 20px;
            }
        </style>
        <script>
           function numPlus() {
                var p = document.getElementById('num');
                p.innerHTML++;
           }
        </script>
</head>
<body>
        <p id="num">1</p>
        <input type="button" id="btn" value="click +1" onclick="numPlus()" />
</body>
</html>
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/0c9b9818a8df4c34adb289ec39b60f9b.png)