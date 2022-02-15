---
title: Django 的安装和基础使用
tags: []
id: '1538'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-04 11:02:04
---

Python 做 web 开发，非常的方便和快捷，这个优势，得益于 Python 的两个框架，一个 Flask ，一个 Django 。 Flask 小，微框架，只含有核心组件，其他的内容，都需要找库或者自行开发，适用进阶学习，以及高手使用，完全按着自己的思路，来使用 flask 搭建网站。 Django 大而全，开发迅速，组件完整，可以快速的搭建一个站起来，但是必须要安装Django的思路来搭建，所以适合新手学习。

> Django 与 Flask 个人观点： django 和 flask 是两种完全不同风格的框架。 django 是大而全， 就是 django 尽量帮你做好所有功能。 - 比如自动化的后台管理系统。 这些可以让你尽快熟悉 web 开发中需要用的知识点。 - flask 一个属于小强调开发灵活性的框架。就是尽量什么都不帮你做，自己去写或者集成第三方。 这些可以让你慢慢的理解原理。 从学习成本和开发成本上来讲 django 初期成本高一些，但是随着系统变大学习成本和开发成本会越来越小。 flask 则事随着系统的变大学习成本和开发成本会上升，因为你会发现你需要集成不少第三方库和第三方框架进入系统。这些会增加学习成本。 学习 restfulapi 的话，看个人熟悉的框架，因为 django 的生态比较丰富，所以 django rest framework 功能会相对完善些。如果个人熟悉 flask 也可以从 flask 入手。

本节课程来学习 Django 框架的安装和使用。首先是框架的安装，安装命令：

```markup
pip install django
```

目前 django 已经出到了 3 版本，django3 的目标是接入异步，就目前源码来看，并不是非常好用。

## 项目新建

### 新建 Python 虚拟环境

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

### 安装 Django 并新建项目

安装完成输入：

```markup
django-admin startproject first .
# django-admin.py startproject first
```

![image.png](https://img-blog.csdnimg.cn/img_convert/a537e3c4a45d9b382d6100fc8fdba010.png) 项目新建成功，下面用你顺手的编辑器打开，这里推荐 pycharm、vscode、sublime，都可以。 其中 **my\_blog** 是 **Django** 网站项目名称，根据自己需求更改 **注意：不要取 django 或者test之类容易产生冲突的名称** 然后就会在 **website** 文件夹中出现 **my\_blog** 文件夹 里面内容如图 ![](https://img-blog.csdnimg.cn/img_convert/bd4ba1497fd503e38be04e57060930e9.png)

### 初始化生成文件用途

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

### 检测 Django 项目是否安装成功

在命令行里输入，输入 的时候要进入项目文件夹，里面要有 manage.py 这个文件。

```python
python3 manage.py runserver
```

![](https://img-blog.csdnimg.cn/img_convert/650f59a089afbe16cbf0d9100adec497.png) 在浏览器中输入网址：127.0.0.1:8000 ![](https://img-blog.csdnimg.cn/img_convert/6391e9473135610584a830283d94cd19.png) 使用编辑器打开项目文件夹，我这里用的是 Pycharm，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/57300596b9775d1fcd7be81bb0a8a268.png) 左侧是文件目录结构，下方是终端，打开方式：右侧上方是代码展示和编辑部分，目前没选择文件。 项目创建好了，还需要来创建 app 应用。

## 新建和注册 app

项目对应站，应用对应站的很多功能功能，所以 app 应用可以创建很多个。 如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/0d2455a69afc98a43845e2218457eb07.png)

> **Ps：注意，先不要填 blog 这个 app，等你运行完下面的命令再填。**

创建 app 的命令是：

```markup
python manage.py startapp blog
```

最后的 blog 是 app 名称。 创建好之后，打开 first 目录中的 settings.py ，找到 INSTALLED\_APPS ，将 app 名称，也就是 blog 放进去。到此，代码就全部准备好了，接下来是启动。

## 项目启动测试

启动命令是：

```markup
python manage.py runserver
```

如下效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/6414dc0e6d648afecff5ffd60b1554e7.png) 出现了 127.0.0.1:8000 就说明启动成功了，此时可以访问了，且终端下方，无法输入内容，也就是网站运行中。 下面是访问网站页面的效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/4fb43731cb84492ddad54efaf3b109d7.png) 说明：截图中，Django 版本是3.1.7，与 Django 2.2，虽然不同，但是没什么差别，都是基础内容的学习。 Django 大版本之后有语法差别，小版本之间没什么差别，都是一些细节上的优化和改动，所以你安装了django3，就可以正常的学习本课程。

## 【选词填空】小练习

1、如果指定版本安装 django 版本 2.2 库，命令是：  
2、新建 demo 项目，命令是：  
3、新建 app，app 名是 demos，命令是：  
4、启动 demo 项目，命令是：

*   \[ \] python manage.py startapp demos
*   \[ \] python manage.py runserver
*   \[ \] django-admin startproject demo
*   \[ \] pip install django==2.2