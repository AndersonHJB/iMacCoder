---
title: Django 快速入门课程「搭建个人博客」
tags: []
id: '1009'
categories:
  - - Django
date: 2020-09-13 14:03:36
---

## 1\. 初探 Django

### 1\. Why Django?

*   免费开源
*   功能丰富
*   开发迅速
*   可扩展性强
*   模版系统
*   后台管理

### 2\. 新建 Python 虚拟环境

1.  在桌面新建项目文件夹，比如名为 **website**
    
2.  在命令行里利用 **cd** 命令进入到 **website** 文件夹
    
3.  输入
    

```python
python3 -m venv djangoenv
```

4.  在 **website** 文件夹内会出现一个 **djangoenv** 文件夹
    
5.  Windows 用户继续输入
    

```python
djangoenv\Scripts\activate
```

6.  Mac 用户继续输入

```python
source djangoenv/bin/activate
```

命令行开头会出现( djangoenv )字样，如图： ![image-20200905182852466](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130429.png) 在命令行里输入

```python
pip3 install django
```

> Mac 在虚拟环境之中，直接输入 python 就是 python3 的版本。

![image-20200906191701119](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130440.png)

### 3\. 安装 Django 并新建项目

安装完成输入

```python
django-admin startproject my_blog .
# django-admin.py startproject my_blog
```

其中 **my\_blog** 是 **Django** 网站项目名称，根据自己需求更改 **注意：不要取 django 或者test之类容易产生冲突的名称** 然后就会在 **website** 文件夹中出现 **my\_blog** 文件夹 里面内容如图 ![image-20200905184324551](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130453.png)

### 4\. 初始化生成文件用途

文件名称

用途

manage.py

一个在命令行中可以调用的网站管理工具

在 my\_blog 文件夹里：

\_\_init\_\_.py

告诉 Python 这个文件夹是一个模块

settings.py

my\_blog 项目的一些配置

urls.py

网站内的各个网址声明

wsgi.py

web 服务器与 Django 项目的接口

### 5\. 检测 Django 项目是否安装成功

在命令行里输入

```python
python3 manage.py runserver
```

![image-20200905190822157](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130525.png)

### 6\. 检测 Django 项目是否安装成功

在浏览器中输入网址：127.0.0.1:8000 ![image-20200905191032862](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130548.png)

### 7\. 在命令行中快速用 cd 打开文件夹

在命令行中输入 **cd+空格 然后将文件夹拖进来**

### 8\. 学习资源

1.  MDN

链接：[https://developer.mozilla.org/zh-CN/docs/Learn](https://developer.mozilla.org/zh-CN/docs/Learn) ![image-20200905192222058](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130613.png)

2.  配色参考

链接：[https://coolors.co/palettes/trending](https://coolors.co/palettes/trending) ![image-20200905192644704](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130741.png)

### 9\. 作业

创建一个 Django 网站及你的博客首页，在自己电脑上搭建一个 Django 项目，制作一个网站首页页面。

## 2\. Django 视图与网址

### 1\. python manage.py migrate

前面我们运行 Django 的时候，命令行提示我们如下内容： ![image-20200905211801306](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130803.png) 您有18个未应用的迁移。你的项目可能不会正常工作，直到你应用程序的迁移: admin, auth, contenttype, session。 运行 “python manager.py migrate” 来应用它们。 你可以理解为创建数据库，一帮我们在做这种比较完善的项目的时候，它的提示一般是比较全的。所以，有时候你翻译一下就知道要做什么事情。

### 2\. 新建一个 Django App

在命令行中进入到 Django 项目文件夹下，也就是和 `manage.py` 同一个路径：

```python
python3 manage.py startapp blog
```

**完成后多出来一个 blog 文件夹，内容如下** ![image-20200905213917961](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130821.png) **App 的作用：** 比如一个网站留言板块功能是一个 App，或者是用户登陆功能，这样也是一个 App。而这个 App 是可以注册的，注册之后网站就可以使用了。也就是把这个 App 拷贝到其他的 Django 网站也是可以直接使用的。 这里目前只是创建了 App 我们还未注册到网站之中，所以我们需要注册到网站之中。

### 3\. 将 App 添加到 settings.py 里

在 Django 项目文件夹中有一个和当前项目同名的文件夹，里面有一个 **settings.py** 文件，在 **INSTALLED\_APPS** 里添加一个 blog 项目 ![image-20200905220405845](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130845.png) ![image-20200905221821160](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130900.png)

### 4\. Django 的 MTV 模式

![Page 112, object 2743](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130924.jpg)

*   Browser：浏览器
*   URL：网址
*   View：视图
*   Model ：模型
*   Database：数据库
*   Template：模板

![image-20200906155724301](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913130943.png)

### 5\. 编写视图函数

打开 **blog/views.py** 文件 默认界面如下 ![image-20200906161258300](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131004.png) ![image-20200906161359523](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131028.png)

### 6\. 编写 views.py

添加如下语句

```python
from django.shortcuts import render
from django.http import HttpResponse # 从 django 的 http 模块引入 HttpResponse 函数
# from 某某模块的某某子模块 import 某个函数

def index(request):
    # 定义一个 index 函数处理主页的访问请求 Request 包含了用户浏览器传来的 HTTP 请求内容
    return HttpResponse("欢迎来到 AI悦创博客！") # 用 HttpResponse 函数直接返回一段文字给用户
```

### 7\. 创建 urls.py

在 **blog** 文件夹下创建一个新的文件，保存为 **urls.py** 「这里的 bolg 就是我们上面创建的 App」 用于处理网址的解析 填入以下内容 ![Kapture 2020-09-06 at 16.26.08](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131115.gif)

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index')
    # path(route, view)
    # path(route, view, name="'index'")
]

# 单词 route
"""
n. 路线，航线；道路，公路；（交通工具的）固定路线；巡访；途径，渠道；（北美）递送路线；用于美国干线公路号码前
v. 按特定路线发送，为……规定路线
"""
```

### 8\. 注意！

在 **my\_blog** 文件夹下本来就有 **urls.py** 文件 和我们刚刚创建的 **urls.py** 不是同一个

### 9\. 配置项目的 urls.py

打开 **my\_blog** 文件夹里的 **urls.py**，看到如下内容 ![image-20200906171610725](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131254.png) ![image-20200906171644196](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131359.png)

### 10\. 默认存在一个 admin 网址

在命令行运行

```python
python3 manage.py runserver
```

然后在浏览器打开网址: **127.0.0.1:8000/admin** ![image-20200906193305372](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131516.png)

### 11\. 创建一个管理员账号

在命令行中输入下面内容

```python
python manage.py createsuperuser
```

![image-20200906193950615](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131625.png)

### 12\. 用管理员账户登录后台

在命令行运行

```python
python manage.py runserver
```

然后在浏览器打开网址: **127.0.0.1:8000/admin** 如果你的服务没有关闭，你可以刷新页面，访问本地链接。admin 链接，进行登录。 ![image-20200906194224546](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131731.png) ![image-20200906194255217](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131837.png) 当然，我们也可以在后台创建用户，这是完全没有问题的。

### 13\. 配置项目的 urls.py

修改 **my\_blog** 文件夹里的 **urls.py** ![image-20200906194749487](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913131935.png) 添加两处内容

```python
from django.contrib import admin
from django.urls import path, include # 添加一个 include

urlpatterns = [
    path('admin/', admin.site.urls), # 这个就是你在浏览器中输入的 url
    path('blog/', include('blog.urls'), name='aiyc'),  # 地址结尾需要添加 /
]
```

这个时候你的主页链接变成了：[http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) 直接访问：[http://127.0.0.1:8000/](http://127.0.0.1:8000/) 会出现如下页面： ![image-20200906200954757](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132142.png) 以上页面默认是开启 `DEBUG = True` 才显示的，如果你关闭了则和下面页面类似： ![image-20200906201146223](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132245.png)

### 14\. 如果修改 urls.py

如果修改 **blog** 里 **urls.py** 的网址会发生什么 原本现在的代码：

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index')
    # path(route, view, name="'index'")
]
```

修改之后的代码：

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index, name='index')
    # path(route, view, name="'index'")
]
```

这个时候，你访问 blog 页面就不能直接 blog 访问，还需要加上 index，也就是此链接：[http://127.0.0.1:8000/blog/index/](http://127.0.0.1:8000/blog/index/) 如果这个时候，blog app 里面又加了一行代码：`path('', views.index, name='index')` 则如果 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) 后面什么都不接上，那就使用该新增的语句。如果是接了则查找匹配的。比如 index，则匹配 index 包含的页面 view 。

### 15\. 更复杂的网址处理

修改 **blog** 文件夹里的 **urls.py** 添加一行： ![image-20200906202359337](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132329.png)

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    # path(route, view, name="'index'")
    path('<int:blog_id>', views.blog_detail, name='blog_detail')
]
```

![image-20200906203314920](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132412.png)

### 16\. 在 views.py 添加函数

```python
from django.shortcuts import render
from django.http import HttpResponse # 从 django 的 http 模块引入 HttpResponse 函数
# from 某某模块的某某子模块 import 某个函数

def index(request):
    # 定义一个 index 函数处理主页的访问请求 Request 包含了用户浏览器传来的 HTTP 请求内容
    return HttpResponse("欢迎来到 AI悦创博客！") # 用 HttpResponse 函数直接返回一段文字给用户

def blog_detail(request, blog_id):
    return HttpResponse("这是第「{}」篇博客".format(blog_id))
```

![image-20200906203459933](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132456.png) ![image-20200906203821231](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132536.png)

### 17\. 通过网址实现一个加法器

如果我们想要通过 **/blog/123/456** 这样的网址实现一个加法器， 得到 **123+456** 的结果，该如何设计 **urls.py**

1.  Blog 中的 **urls.py**

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    # path(route, view, name="'index'")
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('<int:blog_id1>/<int:blog_id2>', views.blog_sum, name='blog_sum'),
]
```

2.  Blog 中的 **views.py**

```python
from django.shortcuts import render
from django.http import HttpResponse # 从 django 的 http 模块引入 HttpResponse 函数
# from 某某模块的某某子模块 import 某个函数

def index(request):
    # 定义一个 index 函数处理主页的访问请求 Request 包含了用户浏览器传来的 HTTP 请求内容
    return HttpResponse("欢迎来到 AI悦创博客！") # 用 HttpResponse 函数直接返回一段文字给用户

def blog_detail(request, blog_id):
    return HttpResponse("这是第「{}」篇博客".format(blog_id))

def blog_sum(request, blog_id1, blog_id2):
    return HttpResponse("Result:{blog_id1} + {blog_id2} = {result_sum}".format(blog_id1=blog_id1, blog_id2=blog_id2, result_sum=blog_id1 + blog_id2))
```

更多参考链接：[https://docs.djangoproject.com/zh-hans/3.1/topics/http/urls/](https://docs.djangoproject.com/zh-hans/3.1/topics/http/urls/) **系统讲解：**

#### 例如

下面是一个简单的 URLconf:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

注意：

*   要从 URL 中取值，使用尖括号。
*   捕获的值可以选择性地包含转换器类型。比如，使用 `<int:name>` 来捕获整型参数。如果不包含转换器，则会匹配除了 `/` 外的任何字符。
*   这里不需要添加反斜杠，因为每个 URL 都有。比如，应该是 `articles` 而不是 `/articles` 。

一些请求的例子：

*   `/articles/2005/03/` 会匹配 URL 列表中的第三项。Django 会调用函数 `views.month_archive(request, year=2005, month=3)` 。
*   `/articles/2003/` would match the first pattern in the list, not the second one, because the patterns are tested in order, and the first one is the first test to pass. Feel free to exploit the ordering to insert special cases like this. Here, Django would call the function `views.special_case_2003(request)`
*   `/articles/2003` would not match any of these patterns, because each pattern requires that the URL end with a slash.
*   `/articles/2003/03/building-a-django-site/` 会匹配 URL 列表中的最后一项。Django 会调用函数 `views.article_detail(request, year=2003, month=3, slug="building-a-django-site")` 。

#### 路径转换器

下面的路径转换器在默认情况下是有效的：

*   `str` - 匹配除了 `'/'` 之外的非空字符串。如果表达式内不包含转换器，则会默认匹配字符串。
*   `int` - 匹配 0 或任何正整数。返回一个 `int` 。
*   `slug` - 匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签。比如，`building-your-1st-django-site` 。
*   `uuid` - 匹配一个格式化的 UUID 。为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写。比如，`075194d3-6885-417e-a8a8-6c931e272f00`。返回一个 [`UUID`](https://docs.python.org/3/library/uuid.html#uuid.UUID) 实例。
*   `path` - 匹配非空字段，包括路径分隔符 `'/'` 。它允许你匹配完整的 URL 路径而不是像 `str` 那样匹配 URL 的一部分。

### 18\. 整体逻辑图

![Django视图中的逻辑](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132709.png) 我们到这里就直接使用了如下流程： ![image-20200907093903101](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132804.png) 之后我们添加个模版，这样使得我们的网站更加美观。

### 19\. 作业

创建一个 Blog App ，能处理博客首页的访问请求，能处理不同的博客数字 id。

## 3\. Django 模板

### 1\. 建立 templates 文件夹

在 **blog** 文件夹中新建一个 **templates** 文件夹，结构如下 ![image-20200907100039171](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913132940.png)

### 2\. 添加博客首页 HTML

在刚才新建的 templates 文件夹中新建一个 **blog\_index.html** 文件， **blog\_index.html** 中填写简单的首页欢迎内容 ![image-20200907105343126](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913133053.png)

```markup
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>AI悦创博客</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
    </head>
    <body>
        <h1>欢迎来到AI悦创博客首页</h1>
        <p id="welcome-line">欢迎来到AI悦创教育</p>
        <a class="link" href="https://www.aiyc.top">AII悦创</a>
        <a class="link" href="https://www.aiyc.top/python3spiderlearn">Python爬虫系统教程</a>
        <ol>
            <li>Python</li>
            <li>Java</li>
            <li>C++</li>
        </ol>
    </body>
</html>
```

目标:输入 **127.0.0.1:8000/blog/** 网址后打开下面的 HTML ，上一节课我们使用 view 直接返回结果，这节课我们使用 view 去使用我们的 templates 。

### 3\. 修改 views.py

原本的内容：

```python
def index(request):
    # 定义一个 index 函数处理主页的访问请求 Request 包含了用户浏览器传来的 HTTP 请求内容
    return HttpResponse("欢迎来到 AI悦创博客！") # 用 HttpResponse 函数直接返回一段文字给用户
```

修改为：

```python
def index(request):
    return render(request, 'blog_index.html')
```

### 4\. 运行 Django 服务器

在命令行运行

```python
python manage.py runserver
```

然后在浏览器打开网址：[http://localhost:8000/blog/index/](http://localhost:8000/blog/index/) ![image-20200907142943184](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913133210.png)

### 5\. 理解一下模板系统

在 **views.py** 中指定渲染某个模板 ![image-20200907143156756](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913133448.png) Django 会自动搜寻各个 App 的 templates 文件夹，然后在 **blog/templates/blog\_index.html**

### 6\. 问题?

不同的 App 中可能存在同名的 html 文件，容易产生冲突怎么办？

### 7\. 解决方案

在 templates 文件夹中再建立和当前 App 同名的文件夹，html 文件放到该文件夹中。 即原来是：**blog/templates/blog\_index.html** 改成：**blog/templates/blog/blog\_index.html** ![image-20200907152321092](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913134157.png) 修改 **views.py** 内容为

```python
def index(request):
    return render(request, 'blog/blog_index.html')
```

### 8\. Django 模板进阶

#### 1\. 强大的模板系统

比方说我希望我们的数据不要写在 HTML 文件当中，就相当于我们的 HTML 相当于填空「类似考试试卷那种」，答案使用 view 来填。 修改 **blog\_index.html** 文件 ![image-20200907153552311](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913134332.png)

#### 2\. 修改 views.py

添加如下语句： ![image-20200907183719987](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913134424.png) ![image-20200907184018428](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913134502.png) 启动服务之后，即可访问该页面： ![image-20200907205255960](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135202.png)

#### 3\. 渲染列表

**views.py** 中添加如下语句

```python
def index(request):
    language_list = ['Python', 'Java', 'C++', 'JavaScript', 'C', 'C#']
    return render(request, 'blog/blog_index.html',
        {"title": "欢迎来到AI悦创的博客站点", 'language_list': language_list})
```

#### 4\. 循环语句

修改 **blog\_index.html** 文件 ![image-20200907212353308](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135210.png) ![image-20200907213911942](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135218.png) 刷新页面之后的结果： ![image-20200907213733119](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135317.png)

#### 5\. 获取循环数字

![image-20200908085823509](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135324.png)

```markup
<!-- --snip-- -->
        <ol>
            {% for item in language_list %}
            <li>{{forloop.counter}}---{{item}}</li>
            {% endfor %}
        </ol>
```

#### 6\. 渲染字典

![image-20200908095749311](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135334.png) 修改 **blog\_index.html** 文件 ![image-20200908100501798](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135342.png)

#### 7\. 模板中的条件判断

**views.py** 中添加如下语句 ![image-20200908100908614](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135356.png) 修改 **blog\_index.html** 文件 ![image-20200908172547832](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135404.png) **elif, else, and, or** 等关键词都可以使用

#### 8\. 判断用户是否登录

![image-20200908175346992](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135438.png) ![image-20200908175429005](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135441.png)

#### 9\. 使用现成的博客模板

![image-20200908194350990](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135447.png)

#### 10\. index.html

![image-20200908194957585](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135458.png) 原本代码：

```python
def index(request):
    language_list = ['Python', 'Java', 'C++', 'JavaScript', 'C', 'C#']
    link_dict = {'AI悦创博客': 'https://www.aiyc.top', 'FP创客空间': 'https://www.fpmakerspace.com'}
    flag = False
    return render(request, 'blog/blog_index.html',
        {
        "title": "欢迎来到AI悦创的博客站点",
        "language_list": language_list,
        "link_dict": link_dict,
        "flag": flag,
        })
```

修改之后：

```python
def index(request):
    language_list = ['Python', 'Java', 'C++', 'JavaScript', 'C', 'C#']
    link_dict = {'AI悦创博客': 'https://www.aiyc.top', 'FP创客空间': 'https://www.fpmakerspace.com'}
    flag = False
    return render(request, 'blog/index.html',
        {
        "title": "欢迎来到AI悦创的博客站点",
        "language_list": language_list,
        "link_dict": link_dict,
        "flag": flag,
        })
```

#### 11\. 打开 127.0.0.1:8000/blog/index

样式出问题，没有找到CSS，JS，图片等素材 ![image-20200908202907543](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135505.png)

#### 12\. 拷贝素材

把素材拷贝到项目里来 在项目根目录下新建 static 文件夹 在 static 文件夹中新建 blog 文件 ![image-20200908203158911](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135510.png) 把 **css、img、js、vendor** 四个素材拷贝到刚刚新建的 blog 文件夹里来 ![image-20200908203628459](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135515.png) ![image-20200908211813079](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135523.png)

#### 13\. 修改 settings.py

打开 **settings.py** 文件 在最后添加一行

```python
import os
STATICFILES_DIRS = [os.path.join('static'), ]
```

#### 14\. 修改 index.html

![image-20200908204902351](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135531.png)

#### 15\. 此时打开正常

![image-20200908213127513](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135540.png)

#### 16\. 修改 index.html，添加模板参数

找到 **index.html** 中和博文相关的内容 ![image-20200908213906927](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135551.png) 寻找规律，改成模板写法 ![image-20200909142421994](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135602.png) 找到 **index.html** 中和博文相关的内容 ![image-20200909153751553](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135607.png)

#### 17.修改 views.py

将 **views.py** 中的渲染参数按照模板设计的修改

```python
def index(request):
    post = {
        'link': 'http://www.aiyc.top',
        'title': '第一篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    }
    return render(request, 'blog/index.html',
        {
        "title": "悦创老师的博客",
        'post': post,
        })
```

![image-20200909153913808](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135616.png)

```python
def index(request):
    post_list = [
    {
        'link': 'http://www.aiyc.top',
        'title': '第一篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    },
    {
        'link': 'http://www.aiyc.top',
        'title': '第二篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    },
    ]
    return render(request, 'blog/index.html',
        {
        "title": "悦创老师的博客",
        "post_list": post_list,
        })
```

![image-20200909155248483](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135628.png) ![image-20200909155433567](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135636.png)

#### 18\. 博客详情页

把模版的 **post.html** 拷贝到项目 templates 里面的 blog。 ![image-20200909185119770](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135643.png) 修改 **views.py** 中的代码 修改前：

```python
def blog_detail(request, blog_id):
    return HttpResponse("这是第「{}」篇博客".format(blog_id))
```

修改后：

```python
def blog_detail(request, blog_id):
    return render(request, 'blog/post.html')
```

这里我的 url 定义是：

```python
urlpatterns = [
    path('index/', views.index, name='index'),
    # path(route, view, name="'index'")
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('<int:blog_id1>/<int:blog_id2>', views.blog_sum, name='blog_sum'),
]
```

所以，我们测试访问的网页为：

```python
http://localhost:8000/blog/1 # blog 后面跟随数字「我上面的 URL 定义是如此，按你的具体情况而定」
```

![image-20200909185815969](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135648.png) 拷贝素材「index 那一步已经导入所需要的素材」，修改所需要的素材的路径，和上面修改 **index.html** 是一个意思。 可以修改 **views.py** 中博文的详情页的连接，修改示例如下。 修改前：

```python
def index(request):
    post_list = [
    {
        'link': 'http://www.aiyc.top',
        'title': '第一篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    },
    {
        'link': 'http://www.aiyc.top',
        'title': '第二篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    },
    ]
    return render(request, 'blog/index.html',
        {
        "title": "悦创老师的博客",
        "post_list": post_list,
        })
```

修改后：

```python
def index(request):
    post_list = [
    {
        'link': '/blog/1',
        'title': '第一篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    },
    {
        'link': '/blog/2',
        'title': '第二篇博客',
        'subtitle': '这是副标题',
        'author': 'aiyuechuang',
        'date': '2020-09-09'
    },
    ]
    return render(request, 'blog/index.html',
        {
        "title": "悦创老师的博客",
        "post_list": post_list,
        })
```

就可以实现跳转到我们的详情页。 稍微的进阶，我们可以把详情页的标题换成我们访问的链接。 **views.py**

```python
def blog_detail(request, blog_id):
    return render(request, 'blog/post.html',
            {
                'title_link': request.path,
                'url_host': request.get_host(),
            }
        )
```

**post.html**

```markup
<h1>{{url_host}}{{title_link}}</h1>
```

### 9\. 作业

完善博客系统 完善博客系统的模板和对应的渲染函数 能通过 **views.py** 中的列表渲染博客首页

## 4\. Django 模型

### 1\. 认识数据库

存储数据的仓库 哪些是数据？ \*\*学生的姓名、性别、学号、成绩 \*\* **用户的银行卡号、余额、交易记录** \*\*网站登录账户、密码、报名的课程信息 \*\* **游戏中的用户名、装备、属性、等级** **……** 信息时代数据无处不在 ![image-20200910201655744](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135735.png) ![image-20200910202019442](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135740.png)

### 2\. Django 中的数据库

尝试一下，打开 blog 应用里的 models.py 文件 ![image-20200910203022713](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135746.png) 加入如下内容

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
```

### 3\. 同步数据库

在命令行运行：

```python
python manage.py makemigrations
```

得到如下提示，可以看到创建了 Post 模型「也就是生成一个 py 文件，py 文件的内容是如何修改数据库。——生成数据库同步脚本」 ![image-20200911084655065](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135750.png) 继续在命令行运行：

```python
python manage.py migrate
```

得到如下提示： ![image-20200911084949195](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135754.png)

### 4\. 利用 admin 后台系统管理数据

将我们创建的模型，注册到后台之中。 修改 blog 文件夹里的 **admin.py**

```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```

在命令行运行 `python manage.py runserver` 启动服务器 访问：[http://localhost:8000/admin/](http://localhost:8000/admin/) 登录后可以看到多出来一个新的栏目 ![image-20200911085550462](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135800.png)

### 5\. admin 后台系统管理

点击 Posts 进来可以看到还没有发过内容 点击 ADD POST + 后可直接添加一个 Post 的 Title ![image-20200911085838082](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135806.png) ![image-20200911085953284](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135815.png) 保存后内容如下，叫 Post object (1)，不直观 ![image-20200911090052268](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135821.png)

### 6\. 修改 models.py

修改 blog 文件夹里的 **models.py**

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title
```

刷新页面后可以看到变成以 title 为标题 ![image-20200911090513528](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135827.png)

### 7\. 设计博文模型

一篇博客相关的信息有如下：

1.  标题
    
2.  副标题
    
3.  作者
    
4.  发表日期
    
5.  标签
    
6.  分类
    
7.  博文内容
    
8.  博文链接
    
9.  （可选）点赞数
    
10.  （可选）阅读量
    

### 8\. Django 中可用的各类模型

*   AutoField
*   BigAutoField
*   BigIntegerField
*   BinaryField
*   BooleanField
*   **CharField**
*   DateField
*   **DateTimeField**
*   DecimalField
*   DurationField
*   EmailField
*   FileField
    
*   FileField and FieldFile
    
*   FilePathField
*   FloatField
    
*   ImageField
    
*   IntegerField
    
*   GenericIPAddressField
    
*   NullBooleanField
*   PositiveIntegerField
*   PositiveSmallIntegerField
*   SlugField SmallIntegerField
*   **TextField**
*   TimeField
*   URLField
*   UUIDField

### 9\. 设计博文模型——简易版

内容

模版

标题

CharField

副标题

CharField

作者

CharField

发表日期

DateTimeField

标签

CharField

分类

CharField

博文内容

TextField

博文链接

CharField

（可选）点赞数

IntegerField

（可选）阅读量

IntegerField

**这样设计有什么问题？** ![image-20200911091857025](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135833.png)

### 10\. 设计博文模型——进阶版

![image-20200911092052062](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135838.png)

### 11\. 博文基础模型

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    published_date = models.DateTimeField()
    content = models.TextField()
    link = models.CharField(max_length=100)


    def __str__(self):
        return self.title
```

### 12\. 关联作者模型

```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    published_date = models.DateTimeField()
    content = models.TextField()
    link = models.CharField(max_length=100)
    auth = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)  
    # 利用ForeignKey()即可关联另外一个模型
    # on_delete=models.CASCADE：代表如果把这个用户删除的话，就把和用户关联的表也删除

    def __str__(self):
        return self.title
```

ForeignKey 外键，一对多的意思，一个作者可以创建多个文章。 所以，作者对文章是一对多的关系，那我们就把作者放在多的这一边。没次检索表，我们都可以通过表来检索作者。

### 13\. 新建分类模型和标签模型

```python
class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True) # blank=True 可以为空

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tag_name
```

### 14\. 关联分类和标签模型

```python
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True) # 就是把这个分类删除，里面的文章也会被删除。
    tag = models.ManyToManyField(Tag, blank=True)
```

利用 **ManyToManyField()** 也可关联另外一个模型 **ForeignKey** 和 **ManyToManyField** 的区别在哪？

### 15\. 一对多

![image-20200911102038859](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135845.png)

### 16\. 多对多

![image-20200911102726269](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135848.png)

### 17\. 运行 Django 管理命令

在命令行运行 `python manage.py makemigrations` 注意：每次修改了 **models.py** 都需要运行上面这句 ![image-20200911105750266](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135855.png) ![image-20200911105815191](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135900.png)

### 18\. 完成 makemigrations

![image-20200911105910153](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135905.png)

### 19\. 运行 Django 管理命令

在命令行运行 `python manage.py migrate` **注意：makemigrations 完了以后要 migrate** ![image-20200911110209193](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135911.png)

### 20\. 重新运行 Django 服务器

运行 `python manage.py runserver` 登录 admin 后台查看 Post ![image-20200911110936013](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135916.png)

### 21\. 向 admin 后台添加模型

修改 blog 文件夹里的 **admin.py**

```python
from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
```

### 22\. 添加 Category

在后台添加一个 Python 分类 ![image-20200911111511338](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135922.png) 以后可以直接在新增 Post 时选择 Python 分类 自行添加文章内容、标签等，以供下面操作使用。

### 23\. 从数据库中提取真正的博文信息

```python
from .models import Post
def index(request):
    post_list = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html',
        {
        "title": "悦创老师的博客",
        "post_list": post_list,
        })
```

![image-20200911113534347](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135926.png)

### 24\. 设计博客详情页网址

每篇博文有一个英文的网址，如 https://www.aiyc/blog/django-lesson-1 **红色部分由数字、字母、短横线、下划线组成** 在后台发表时填 Link 只需要填红色部分 ![image-20200911142427779](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135931.png)

### 25\. 修改博客首页的详情页链接

链接设计为/blog/储存的链接 ![image-20200911143318146](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135935.png)

### 26\. 修改 urls.py

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    # path(route, view, name="'index'")
    # path('<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('<slug:blog_link>/', views.blog_detail, name='blog_detail'),
    # path('index/<sug:blog_id>', views.blog_detail, name='blog_detail')
    path('<int:blog_id1>/<int:blog_id2>', views.blog_sum, name='blog_sum'),
]
```

slug 表示是由字母、数字以及横杠、下划线组成的字符串 这样就能匹配形如 `/blog/django-lesson-1` 的网址 并将 `django-lesson-1` 提取出来存到变量 `blog_link` 里

### 27\. 修改 views.py

![image-20200913121701304](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135940.png)

```python
from django.shortcuts import get_object_or_404
def blog_detail(request, blog_link):
    post  = get_object_or_404(Post, link=blog_link)
    return HttpResponse(post.content)
```

**get\_object\_or\_404** 表示从某个模型根据关键词提取某段数据 找到就返回数据，找不到就返回404页面 ![image-20200913122531611](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135947.png) ![image-20200913122613060](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135952.png)

### 28\. 添加博客详情页模板

从博客模板中拷贝 `post.html` 到 `templates/blog/` 里 并修改 `views.py`

```python
def blog_detail(request, blog_link):
    post  = get_object_or_404(Post, link=blog_link)
    return render(request, 'blog/post.html', {'post': post})
```

### 29\. 修改 post.html 为模板格式

![image-20200913123451303](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913135956.png)

```markup
  <!-- Page Header -->
  <header class="masthead" style="background-image: url('{% static 'blog/img/post-bg.jpg' %}')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="post-heading">
            <h1>{{post.title}}</h1>
            <h2 class="subheading">{{post.subtitle}}</h2>
            <span class="meta">Posted by
              <a href="#">{{post.auth}}</a>
              on {{post.published_date}}</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Post Content -->
  <article>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <p>{{post.content}}</p>

          <p>Placeholder text by
            <a href="https://www.aiyc.top/">AIYC Blog</a>. Photographs by
            <a href="https://www.aiyc.top/">aiyuechuang</a>.</p>
        </div>
      </div>
    </div>
  </article>
```

### 30\. 更漂亮的排版

采用 Markdown 格式编写博文 ![image-20200913124628135](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913140001.png)

### 31\. 安装 markdown 模块

在命令行运行 `pip install markdown2` 修改 `views.py` ![image-20200913124826456](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913140009.png)

### 32\. 页面渲染情况

![image-20200913125101916](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913140016.png)

### 33\. 添加 safe 标签

Django 为了防止被攻击所开启的一个保护，我只需要添加一个 safe 即可。让他信任我所写的内容。 ![image-20200913125453842](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913140028.png)

### 34\. 调整 url

现在博客首页网址是 `/blog/` ，需要调整 `my_blog` 里的 `urls.py` ![image-20200913130046818](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913140032.png) **blog** 里的 **urls.py** ![image-20200913130144165](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200913140037.png)