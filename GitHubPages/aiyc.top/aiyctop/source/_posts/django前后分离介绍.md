---
title: Django前后分离介绍
tags: []
id: '1550'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-05 20:27:40
---

## 制作API用于前后端分析结构

前后端分离，是个趋势，了解前后端分离，对我们的技术提升，也是有很大帮助的。 Django 的 MTV 模式，是数据库->后端->前端的一整套流程，所有的内容都是一套项目中。 前后端分离的思想，就是前端负责界面交互和美观，后端负责数据管理和数据输出。前端和后端的通信，完全基于 API 来处理。 **什么是 API？** 就是一个后端提供给前端拿数据的 url。 本节课的任务，就是做个 API 接口，访问这个接口，可以拿到数据库中的文章内容。 首先，说明下格式问题。前端找后端要数据，后端给数据，前端拿数据，都是有特定格式的，这种格式是前后端两个规则好的。 所以在这里，以 json 格式为例，json 也是前端编程语言 javascript 的对象结构。 ![image.png](https://img-blog.csdnimg.cn/img_convert/33091e6af31df1b1020d2f97aa8ebc12.png)

## 增加模型函数

django 的 Model 默认不能直接导出 json 的，所以在模型定义里面，预先准备一个函数，将对象转换成 json，如下代码：

```python
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name="标题")
    abstract = models.CharField(max_length=128, verbose_name="摘要")
    content = models.TextField(verbose_name="内容")

    def __str__(self):
        return "{}".format(self.title)

    @classmethod
    def articles_to_dict(cls, articles):
        arts = {}
        for article in articles:
            tmp = {}
            tmp['title'] = article.title
            tmp['abstract'] = article.abstract
            tmp['content'] = article.content
            arts[article.id] = tmp
        return arts
```

代码解释：

*   @classmethod 申明这个函数是个类函数
*   articles\_to\_dict 函数名，类函数参数必须有 cls，第二个 articles 是需要传入的值，文章列表
*   for 循环，循环获取每篇文章，做成一个临时的字典 tmp，将标题、摘要、内容做成字典内容
*   然后再把 tmp 字典放到循环外的 arts 大字典内，键值分别是文章的 id 和 tmp 临时字典
*   最后将 arts 字典进行返回
*   这样就可以把传入的对象列表，做成一个大的对象字典了

代码截图： ![image.png](https://img-blog.csdnimg.cn/img_convert/86a41244b0dbe1dffd71ac8834f95ee3.png)

## 对应的 API 函数

有了将对象转换成字典的函数，下面开始定义 api 函数。 api 和 view 不太一样，虽然操作是一样的，但是概念上不同，view 返回网页内容，api 返回纯数据，所以 api 函数放的位置，单独存放到一个 api.py 里面，这个文件需要新建，看上方的效果图。 新建了 api.py 文件后，打开这个文件，新建一个函数，代码如下：

```python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 8:08 下午
# @Author  : AI悦创
# @FileName: api.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
from django.http import JsonResponse
from .models import Article


def export_article(request, id=None):
    if id:
        articles = Article.objects.filter(id=id)
    else:
        articles = Article.objects.all()
    articles_json = Article.articles_to_dict(articles)
    print(articles_json)
    return JsonResponse(articles_json, json_dumps_params={'ensure_ascii': False})
```

对于新手来说，代码还有难度，在这里详细解释下：

*   导入 Article 和 JsonResponse。这个 JsonResponse 就是 json 格式的响应内容
*   然后是函数的定义，函数名是 export\_article，参数是 request 默认，以及一个 id，默认值是 None 为什么要 id，又设置成 None ？这里的思路是，这个函数可以返回特定的某篇文章，或者是返回默认所有文章。所以 id 的值，默认给个 None。等传入 id 时，None 会被覆盖
*   然后判断 id 的值，如果有值，就查询这个 id 所对应的的文章；`Article.objects.filter(id=id)` 是查询 id 匹配的文章，结果是文章列表
*   如果没有，则默认返回全部的文章
*   拿到了文章后，使用类函数 `articles_to_dict()` 将文章对象列表，转换成字典
*   通过 JsonResponse 将文章字典，做成响应直接返回
*   `json_dumps_params={'ensure_ascii':False}` 这个是不转换中文，视觉上看更直观

代码截图如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/caa7bf8c134222a34c96af4647d67bd8.png)

## 绑定 URL

api 函数准备好了，然后是注册和绑定 url，不要忘记了，这个也是需要绑定了，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/cb803beb8b38491e4b15063c4be962c5.png) 这里绑定了两个 url，一个是 article/json，这是匹配没有传入 id 时候的访问 url；另一个是 `article/json/<int:id>`，这个是匹配传入 id 时的 url。

## API 接口测试

一切准备就绪，看下访问效果，分别是访问无 id 的 url 和有 id 的 url，如下效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/016cb01cd5a79e39caad35b571128870.png) 网页中正常展示中文，打开浏览器的调试工具，切换到 Network 网络栏，这个 Json 格式就比较明显了，方便阅读。

## 【选词填空】练习

在 models.py 文件中，@classmethod 的意思\_\_\_\_\_\_\_\_\_是函数，也就是通过类可以直接调用的函数； 没有 @classmethod 的函数，是\_\_\_\_\_\_\_\_\_\_\_\_\_函数，不能通过类调用，只能通过实例调用。

*   \[ \] 实例
*   \[ \] 类