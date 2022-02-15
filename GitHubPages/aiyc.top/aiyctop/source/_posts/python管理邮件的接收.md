---
title: Python管理邮件的接收
tags: []
id: '1523'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-26 21:57:50
---

## 库的安装

你好，我是悦创。既然可以发送邮件，就一定可以接收邮件，这两者是相互的。接收邮件，这里介绍 zmail 库，安装命令：

```bash
pip install zmail
```

zmail 支持邮件的发送和接收，操作的类型是字典。

## 准备初始化

接收邮件，同样是先初始化，如下代码：

```bash
import zmail
server = zmail.server('1432803776@qq.com','*************')
```

这里的 server 类似于一个邮箱客户端，可以通过 server 来取邮箱中收到的邮件，例如：

```bash
mail = server.get_latest()
```

这是获取邮箱中最后一个邮件，也就是最新的邮件。

## 接收邮件并展示

**mail 变量里面放着一封邮件，如何查看邮件内容？** 使用如下代码：

```bash
zmail.show(mail)
```

展示邮件的全部内容，输出如下：

```bash
-------------------------
Subject  [AI悦创] 请审核：“02 环境准备：在各系统中快速安装 Git 环境”
Id  134
From  AI悦创 <1432803776@qq.com>
To  1432803776@qq.com
Date  2021-02-25 09:56:04+00:00
Content_text  ['在《02 环境准备：在各系统中快速安装 Git 环境》中有一条评论等待您的审核\r\nhttps://www.aiyc.top/1514.html\r\n\r\n作者：22（IP地址：121.205.195.226，226.195.205.121.broad.pt.fj.dynamic.163data.com.cn）\r\n电子邮箱：2273947745@qq.com\r\nURL：http://2\r\n评论：\r\n11\r\n\r\n批准：https://www.aiyc.top/wp-admin/comment.php?action=approve&c=195#wpbody-content\r\n移至回收站：https://www.aiyc.top/wp-admin/comment.php?action=trash&c=195#wpbody-content\r\n标记为垃圾评论：https://www.aiyc.top/wp-admin/comment.php?action=spam&c=195#wpbody-content\r\n当前有1条评论等待审核。请移步审核页面来查看：\r\nhttps://www.aiyc.top/wp-admin/edit-comments.php?comment_status=moderated#wpbody-content\r\n']
Content_html  []
Attachments  
```

我的邮件内容如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/db2db3af7726860cfb98f17f23d55fc9.png) 这里的内容都是成对出现的，例如 Subject \[AI悦创\] 请审核：“02 环境准备：在各系统中快速安装 Git 环境”，都是一对一对的，所以这里的内容也是列表格式。 如果你直接输出 mail 的内容，如下截图： ![image.png](https://img-blog.csdnimg.cn/img_convert/a1eedcb0b722491f40a40924b36897e2.png) 这里的展示更明显，而且内容更直观，有大括号，是列表格式。既然是字典格式，取出单个内容，就可以用字典的取值方式，如下：

```bash
print(mail['subject'], mail['from'], mail['date'], sep='\n')
''' 下面是输出内容
[AI悦创] 请审核：“02 环境准备：在各系统中快速安装 Git 环境”
AI悦创 <1432803776@qq.com>
2021-02-25 09:56:04+00:00
'''
```

读取了邮件的标题、发送者、发送时间这三个信息。 下面来展示下邮件对象，所有的键，如下代码：

```bash
tmail = server.get_mail(1)
for m in tmail:
    print(m)

''' 下面是输出
content_text # 文本内容
content_html # HTML格式内容
attachments # 附件
headers # 头部信息，字典格式
raw_headers # 头部信息，列表中嵌套元组格式
charsets # 文字编码
subject # 邮件标题
date # 发送日期
from # 发送者
to # 接受者
id # id值，代表第几封邮件
raw # 头部信息，列表中嵌套字节字符串格式
'''
```

接收邮件，可以一封一封的接收，还可以按标题、日期、发送者等信息过滤并接收，下面展示一下按标题信息过滤并接收一批邮件，如下代码：

```bash
tmails = server.get_mails(subject='测试邮件的标题')
len(tmails)
for t in tmails:
    print(t['subject'], t['from'])
'''
19
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题【无HTML】 "1432803776@qq.com" <1432803776@qq.com>
测试邮件的标题【有HTML】 "1432803776@qq.com" <1432803776@qq.com>
'''
```

首先是 get\_emails 函数，这是获取一批邮件，函数中指定邮件标题 subject，必须包含了“测试邮件的标题”字段。 得到的邮件列表，存放在 tmails 变量中，一共有 19 封邮件。 然后循环取出每个邮件的标题和发信人，就得到一大串的信息输出。