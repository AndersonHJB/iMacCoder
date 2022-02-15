---
title: Python发送携带附件的邮件
tags: []
id: '1513'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-25 15:50:01
---

## 准备阶段

你好，我是悦创。以往的邮件发送形式，通常都会带上附件，例如工作中的文件发给领导、将小组作业发给老师等等。Python 中使用 yagmail 发送含附件的邮件，非常的简单，且方便。 首先是准备代码部分：

```python
import yagmail
yag = yagmail.SMTP(user='1432803776@qq.com', password='****************',host='smtp.qq.com')
```

发送附件，就要准备附件文件。源码文件夹中准备了三个文件，分别是 "GCD.py"、"python.png"、"django.png"。

## 发送单个附件邮件

先发第一个邮件，放上 py 文件，代码如下：

```python
subject = '测试邮件的标题'
body = '测试邮件的内容部分,看下方，看下方，看下方'

h1 = '<h1>AI悦创</h1>'
a_link = '点击<a href="https://www.aiyc.top/">链接</a>，前往 AI悦创 网站'
py_source = "GCD.py"

yag.send(to='1432803776@qq.com', subject=subject, contents=[body, h1, a_link, py_source])
```

发送邮件时增加附件，只需要在 contents 列表中，放上文件的路径。这里放的是 py\_source ，也就是“GCD.py”名称，文件和发送邮件的 ipynb 文件放在一起。 邮件效果图如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/0845c050d3e58f1d6d85ea074407c6a5.png)

## 多附件的邮件

接着发送多个附件，除了 py 文件，将两个 png 图片也一并发送出去，如下代码：

```python
subject = '测试邮件的标题'
body = '测试邮件的内容部分,看下方，看下方，看下方'

h1 = '<h1>AI悦创</h1>'
a_link = '点击<a href="https://www.aiyc.top">链接</a>，前往AI悦创网站'

py_source = "GCD.py"
django_img = "django.png"
python3_img = "python3.png"

yag.send(to='1432803776@qq.com', subject=subject, contents=[body, h1, a_link, py_source, django_img, python3_img])
```

发送多个附件的邮件，只需要将文件的路径，直接放到 contents 列表中去即可，代码和上面的单附件代码一致。邮件效果截图： ![image.png](https://img-blog.csdnimg.cn/img_convert/10d61cd06b44549009d89a58f2b86659.png)

## 【选词填空】小练习

使用 yagmail 库发送邮件，附件放在 参数中； contents 可以是字符串，也可以是 ；

*   \[ \] 字符串
*   \[ \] subject
*   \[ \] 列表
*   \[ \] contents
*   \[ \] 字典