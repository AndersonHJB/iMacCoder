---
title: Python发送网页格式邮件
tags: []
id: '1504'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-23 20:01:16
---

## 邮件初始化

邮件的内容，可以是简单的几个文字，也可以是丰富的 HTML 页面。 但是刚上手是无法做出精美的 HTML 网页邮件的，先来做个基础的 HTML 格式邮件。 首先同样是将 yagmail 初始化成对象，如下代码：

```python
import yagmail
yag = yagmail.SMTP(user='1432803776@qq.com', password='****************',host='smtp.qq.com')
```

依旧是使用 qq。邮箱，密码记得获取授权码。

## 复习纯文字邮件

然后是准备 subject，以及内容和 html 内容，如下：

```python
subject = '测试邮件的标题【无HTML】'
body = '测试邮件的内容部分,看下方，看下方，看下方'

yag.send(to = '1432803776@qq.com',subject =subject,contents = body)
```

先发送一个没有 HTML 格式的文字邮件。

## 发送 HTML 格式邮件

然后再发送一个含有 HTML 的邮件，如下代码：

```python
subject = '测试邮件的标题【有HTML】'
body = '测试邮件的内容部分,看下方，看下方，看下方'
h1 = '<h1>Spbeen</h1>'
a_link = '点击<a href="http://www.spbeen.com">链接</a>，前往Spbeen网站'

yag.send(to = '1432803776@qq.com',subject =subject,contents = [body,h1,a_link])
```

结果如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/aaa995b34e10f6f06cbd9464fdbd8f64.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/f0c7876376e0da6063a10f1b9d58484c.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/595f7f3f81e5ef1a9dc7620e4fd854ca.png)

## 【选词填空】练习

QQ 的邮箱服务，使用的是协议。

*   \[ \] http
*   \[ \] sql
*   \[ \] p2p
*   \[ \] smtp

## 视频学习