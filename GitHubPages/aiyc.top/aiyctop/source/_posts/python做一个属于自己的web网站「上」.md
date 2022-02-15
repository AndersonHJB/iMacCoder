---
title: Python做一个属于自己的web网站「上」
tags: []
id: '1542'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-04 14:28:35
---

## 目录

1、掌握前端技术开发精髓 2、Django 的安装和基础使用 3、理解 MTV 模型 4、制作首页

## 1、掌握前端技术开发精髓

网页内容，由三部分组成，分别是 html、css 和 javascript 。

*   html 是网页面部分
*   css 是美化网页的操作
*   javascript 是让网页可以交互起来

前端内容，html 是必须的，css 可以交给前端框架，js 也可以交给框架。 所以本问课这里主要介绍 html 部分和认识一个前端框架。html 是一种标记语言，结构是这样的的 内容 ，一个尖括号的起始标签，一个尖括号带 / 的结束标签。并且这种成对的标签，是可以嵌套的。

### HTML 基础

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

### BootStrap 是什么

以上是 html 的基础结构，接下来了解下前端框架，这里要介绍的是 Bootstrap 。 Bootstrap 是非常著名的前端框架之一，也是最早的前端框架。

> **一个小疑问：为什么会有前端框架的出现？**做网站，费时费力，网站难的是后台的服务搭建，这部分是用户看不到的，用户看到的地方是网页内容。及时你的后台在强大，前端效果不好看，用户也会觉得你这个站很low。 但并不是所有的人都懂如何美化网页，所有一个现成的前端框架就非常有必要的。使用前端框架，可以快速的实现你要的内容，并且配合上具体的使用文档，及时没有网页开发经验，也可以按照说明，快速的完成一个还算美观的前端页面。

关于 Bootstrap 的官方中文文档，官方链接：[Bootstrap官方中文](https://v3.bootcss.com/)

### 学习 Bootstrap

中文文档介绍很详细，看着就可以制作属于你自己的网页了。下面给出两个网页，一个是文章列表页，另一个是文章的详情页，源码文件夹中都有，如下截图【左侧效果，右侧源码】： ![image.png](https://img-blog.csdnimg.cn/img_convert/754c333e88aed05dbefbcb224f330eb9.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/d5d957965283f720dd57512ee3dcffa1.png) 这两个网页都是使用的 Bootstrap 框架做的，使用方式都是使用 cdn 链接的方式载入，比较快。 源码获取 ：[https://github.com/AndersonHJB/Play-with-office-automation/tree/main/专属的Web自动化处理/1.掌握前端网页精髓内容](https://github.com/AndersonHJB/Play-with-office-automation/tree/main/专属的Web自动化处理/1.掌握前端网页精髓内容) 如果获取失败，加我微信获取。

### 【选词填空】小练习

前端技术，主要是\_\_\_\_\_\_\_\_ 、\_\_\_\_\_\_\_\_和 \_\_\_\_\_\_\_\_。 \_\_\_\_\_\_\_\_是前端框架。

*   \[ \] JavaScript
*   \[ \] Django
*   \[ \] CSS
*   \[ \] HTML
*   \[ \] Bootstrap
*   \[ \] Python

## 2、Django 的安装和基础使用

Python 做 web 开发，非常的方便和快捷，这个优势，得益于 Python 的两个框架，一个 Flask ，一个 Django 。 Flask 小，微框架，只含有核心组件，其他的内容，都需要找库或者自行开发，适用进阶学习，以及高手使用，完全按着自己的思路，来使用 flask 搭建网站。 Django 大而全，开发迅速，组件完整，可以快速的搭建一个站起来，但是必须要安装Django的思路来搭建，所以适合新手学习。

> Django 与 Flask 个人观点： django 和 flask 是两种完全不同风格的框架。 django 是大而全， 就是 django 尽量帮你做好所有功能。 - 比如自动化的后台管理系统。 这些可以让你尽快熟悉 web 开发中需要用的知识点。 - flask 一个属于小强调开发灵活性的框架。就是尽量什么都不帮你做，自己去写或者集成第三方。 这些可以让你慢慢的理解原理。 从学习成本和开发成本上来讲 django 初期成本高一些，但是随着系统变大学习成本和开发成本会越来越小。 flask 则事随着系统的变大学习成本和开发成本会上升，因为你会发现你需要集成不少第三方库和第三方框架进入系统。这些会增加学习成本。 学习 restfulapi 的话，看个人熟悉的框架，因为 django 的生态比较丰富，所以 django rest framework 功能会相对完善些。如果个人熟悉 flask 也可以从 flask 入手。

接下来我们学习 Django 框架的安装和使用。首先是框架的安装，安装命令：

```markup
pip install django
```

目前 django 已经出到了 3 版本，django3 的目标是接入异步，就目前源码来看，并不是非常好用。

### 项目新建

#### 新建 Python 虚拟环境

*   在桌面新建项目文件夹，比如名为 **website**
*   在命令行里利用 **cd** 命令进入到 **website** 文件夹
*   输入

```markup
python3 -m venv djangoenv
```

*   在 **website** 文件夹内会出现一个 **djangoenv** 文件夹
*   Windows 用户继续输入

```bash
djangoenv\Scripts\activate
```

*   Mac 用户继续输入

```basic
source djangoenv/bin/activate
```

命令行开头会出现( djangoenv )字样，如图： ![](https://img-blog.csdnimg.cn/img_convert/1377bf1ad89053a171ecb861aee2e986.png) 在命令行里输入 安装好之后，使用命令提示符或者终端，就可以使用 django-admin 命令，来创建项目，如下效果图：

```markup
pip install django
```

> Mac 在虚拟环境之中，直接输入 python 就是 python3 的版本。

![image.png](https://img-blog.csdnimg.cn/img_convert/a64ae2248339bbb0349cadb1e304f100.png)

#### 安装 Django 并新建项目

安装完成输入：

```markup
django-admin startproject first .
# django-admin.py startproject first
```

![image.png](https://img-blog.csdnimg.cn/img_convert/a537e3c4a45d9b382d6100fc8fdba010.png) 项目新建成功，下面用你顺手的编辑器打开，这里推荐 pycharm、vscode、sublime，都可以。 其中 **my\_blog** 是 **Django** 网站项目名称，根据自己需求更改 **注意：不要取 django 或者test之类容易产生冲突的名称** 然后就会在 **website** 文件夹中出现 **my\_blog** 文件夹 里面内容如图 ![](https://img-blog.csdnimg.cn/img_convert/bd4ba1497fd503e38be04e57060930e9.png)

#### 初始化生成文件用途

文件名称

用途

manage.py

一个在命令行中可以调用的网站管理工具

在 my\_blog 文件夹里：

**init**.py

告诉 Python 这个文件夹是一个模块

settings.py

my\_blog 项目的一些配置

urls.py

网站内的各个网址声明

wsgi.py

web 服务器与 Django 项目的接口

#### 检测 Django 项目是否安装成功

在命令行里输入，输入 的时候要进入项目文件夹，里面要有 manage.py 这个文件。

```python
python3 manage.py runserver
```

![](https://img-blog.csdnimg.cn/img_convert/650f59a089afbe16cbf0d9100adec497.png) 在浏览器中输入网址：127.0.0.1:8000 ![](https://img-blog.csdnimg.cn/img_convert/6391e9473135610584a830283d94cd19.png) 使用编辑器打开项目文件夹，我这里用的是 Pycharm，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/57300596b9775d1fcd7be81bb0a8a268.png) 左侧是文件目录结构，下方是终端，打开方式：右侧上方是代码展示和编辑部分，目前没选择文件。 项目创建好了，还需要来创建 app 应用。

### 新建和注册 app

项目对应站，应用对应站的很多功能功能，所以 app 应用可以创建很多个。 如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/0d2455a69afc98a43845e2218457eb07.png)

> **Ps：注意，先不要填 blog 这个 app，等你运行完下面的命令再填。**

创建 app 的命令是：

```markup
python manage.py startapp blog
```

最后的 blog 是 app 名称。 创建好之后，打开 first 目录中的 settings.py ，找到 INSTALLED\_APPS ，将 app 名称，也就是 blog 放进去。到此，代码就全部准备好了，接下来是启动。

### 项目启动测试

启动命令是：

```markup
python manage.py runserver
```

如下效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/6414dc0e6d648afecff5ffd60b1554e7.png) 出现了 127.0.0.1:8000 就说明启动成功了，此时可以访问了，且终端下方，无法输入内容，也就是网站运行中。 下面是访问网站页面的效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/4fb43731cb84492ddad54efaf3b109d7.png) 说明：截图中，Django 版本是3.1.7，与 Django 2.2，虽然不同，但是没什么差别，都是基础内容的学习。 Django 大版本之后有语法差别，小版本之间没什么差别，都是一些细节上的优化和改动，所以你安装了django3，就可以正常的学习本课程。

### 【选词填空】小练习

1、如果指定版本安装 django 版本 2.2 库，命令是：  
2、新建 demo 项目，命令是：  
3、新建 app，app 名是 demos，命令是：  
4、启动 demo 项目，命令是：

*   \[ \] python manage.py startapp demos
*   \[ \] python manage.py runserver
*   \[ \] django-admin startproject demo
*   \[ \] pip install django==2.2

## 3、理解 MTV 模型

### MTV介绍

要掌握 Django，必须了解 Django 的 MTV 模型，这是非常重要的内容，不管是 Django1 还是 2 以及后面正在更新的 3 系列，MTV 模型是永远不会变的。 先来解释下 MTV 模型的意思，MTV 是三层关系，分别是：

*   M：「Model」 模型，数据管理
*   T：「Template」 模板，网页展示
*   V： 「View」 视图，逻辑控制

这三者是 Django 的网页的运行机制，下面单独介绍下 MTV 每个模板的功能。

### Model 模型介绍

Model 模型，是负责管理数据的。 每个网站都需要有数据库用于存储网站数据，网站需要展示数据时，也需要从数据库查询并读取数据。 Django 内置了 ORM 实现框架，支持多种数据库，默认的数据库是 Sqlite，当然也支持 Mysql 等关系型数据库。

### Template 介绍

Template 模板，指的就是网页模板。 真实给用户看的内容，**都是数据+网页模板的结合**。数据从数据库中查询出来，并渲染到模板中，得到单个的网页，再把网页返回给用户查看，这就是网页的渲染流程。 **那模板长什么样子？** 上节课程最好的静态网页，放到 django 项目的特定文件夹中，就是我们的模板，再简单的稍作修改，就得到了可以渲染数据的模板。

### View视图介绍

前面介绍了各种操作，例如查询并读取数据、数据渲染到网页，虽然有介绍，但并未介绍如何写，怎么写，写在哪。 这些逻辑代码，都是要写在 view 视图中的。View 视图，就是对应的逻辑代码存放的位置。 网站是要接收用户的请求，并返回给对应的响应，而 django 接受到的请求，发给指定的视图函数，视图函数做设定好的操作，再返回响应给用户，这样就完成了一次请求和响应操作。

### 图片展示

以上就是 MTV 模型的介绍，当然这里介绍的内容不难，只是对于模式的介绍，代码上具体的细节，还有很多，后面会逐一介绍。 下面看一个图，介绍 MTV 三者管理的模块，如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/78391d81679c302601454124f4af9272.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/d27d14a79459a026fe19443f8d0d8d7c.png) 介绍到此结束，后面会具体上手写代码，完成一个功能简单的文章网站。

### 【选词填空】练习

MTV，分别对应的三个单词是\_\_\_\_\_\_\_\_ 、\_\_\_\_\_\_\_\_ 、\_\_\_\_\_\_\_\_ 。

*   \[ \] Model
*   \[ \] View
*   \[ \] Template

## 4、制作首页

### 放入静态文件

django 项目准备好了，静态网页也准备好了，本文学习如何将网页接入到项目中。 第一步，在 blog 应用的目录下，创建一个名为 templates 的目录，注意不要写错。 ![image.png](https://img-blog.csdnimg.cn/img_convert/0791666e6c130ca85eea8cd644aeb8f0.png) 这个 templates 目录，就是存放模板的目录，名称不能错，因为这是 django 默认读取的目录。然后将两个 html 文件放进来。 ![image.png](https://img-blog.csdnimg.cn/img_convert/798a002369769d62addb1401accf74b1.png)

### 写一个函数

要完成网站首页，就必须定义首页的视图函数，这个函数放在 blog 目录下的 views.py 文件中。 打开了 views.py 文件，新建一个 index 函数，参数是 request，如下代码：

```python
def index(request):
    return render(request, 'index.html')
```

![image.png](https://img-blog.csdnimg.cn/img_convert/4fa441b3c2748063f2381a69c46d11ae.png) 这个就是视图函数的定义，代码解释：

*   第一行的 index 是函数名，request 是参数，必须要，因为函数在被调用时，请求会被传入，request 就是对应的参数。
*   第二行 return，这个是返回，函数必须有返回
*   render 是 django 内置的渲染函数，这里放入了两个值第一个是 request，默认的，需要加；第二个值是 index.html ，这个是放在 templates 目录中的首页
*   render() 函数的结果是一个 Response 响应，每个视图函数都必须返回一个响应。

以上是函数的介绍部分，那这个函数也就是简单的返回了一个载入 index.html 的响应。如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/c06a6b55f95568dd89c0784488b797aa.png)

### 准备URL

函数有了，那就给他分配一个 url，url 就是浏览器中访问的地址。 url 的配置，在 first 目录下的 urls.py 文件中，这里有一个 admin ，是默认的 django 后台配置，后面我们会用到这个。 既然是绑定首页，所以 url 的地址，应该是主域名，那在绑定的时候，代码如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/0b0b67e933a5d732f48d391f7d22af07.png) 视图函数绑定 url ，首先是从 blog.views 中导入 index 函数，然后在 urlpatterns 中进行设置就行。

### 启动服务

代码已经准备完毕，现在来启动项目。 打开命令行，输入命令：

```python
python manage.py runserver
```

截图和效果图如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/5c02010ce10c3bff65baf02b6390db1b.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/2e699c42119e2490bdb4e2e489e97b48.png) 如果你要绑定到 index路径上，只需要修改一下 urls.py 中的内容就可以。 ![image.png](https://img-blog.csdnimg.cn/img_convert/536f789b16cf7bcdbeebedabeb6921d1.png) 通常首页，是空 url 的默认路径，或者有 index 的 url 地址，都是可以的。

### 【多选题】小练习

制作网站首页，有哪些步骤？

*   \[ \] 准备网页，放进 teamplates
*   \[ \] Model 和数据库映射
*   \[ \] 写一条规则，将 url 和函数进行绑定
*   \[ \] 写一个函数，返回具体的 html 文件
*   \[ \] 写一个 Model