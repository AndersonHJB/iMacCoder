---
title: Python自动化办公之数据库「上」
tags: []
id: '1466'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-14 15:06:08
---

你好，我是悦创。这一篇我们继续来学习 Python 办公自动化之数据的学习。

## 一：数据库和 sqlite 介绍

### 1、什么是数据库

数据库是“**按照数据结构来组织、存储和管理数据的仓库**”，是一个长期存储在计算机内的、有组织的、有共享的、统一管理的数据集合。 数据库是以一定方式储存在一起、能与多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合，可视为电子化的文件柜。

### 2、有哪些数据库

**数据库类型**

*   大型数据库：[甲骨文Oracle](https://baike.baidu.com/item/%E7%94%B2%E9%AA%A8%E6%96%87%E5%85%AC%E5%8F%B8/430115?fromtitle=Oracle&fromid=301207&fr=aladdin)。
*   分布式数据库：[HBase](https://baike.baidu.com/item/HBase/7670213?fr=aladdin)。
*   中型数据库：[SqlServer](https://baike.baidu.com/item/SqlServer/463101?fr=aladdin)、[Mysql](https://baike.baidu.com/item/MySQL/471251)、[MariaDB](https://baike.baidu.com/item/mariaDB/6466119?fr=aladdin)、[PostgreSQL](https://baike.baidu.com/item/PostgreSQL/530240?fr=aladdin)、[Redis](https://baike.baidu.com/item/Redis/6549233) 等。
*   小型数据库：[Sqlite](https://baike.baidu.com/item/SQLite/375020?fr=aladdin)、[Access](https://baike.baidu.com/item/Microsoft%20Office%20Access/7748166?fromtitle=access&fromid=10275&fr=aladdin)。

**如何选择**

*   大集团：Oracle、HBase。
*   发展中公司：PostgreSQL、Mysql。
*   app的临时数据库：Sqlite。

### 3、Sqlite

*   方便携带、易于操作、随时创建、Python 原生支持的小型数据库文件。
*   轻型的数据库，遵守 ACID 的关系型数据库管理系统，它包含在一个相对小的 C 库中。
*   D.RichardHipp 建立的公有领域项目。
*   设计目标是嵌入式\]的，而且已经在很多嵌入式产品中使用了它，它占用资源非常的低，在嵌入式设备中，可能只需要几百 K 的内存就够了。
*   支持 Windows/Linux/Unix. 等等主流的操作系统。
*   能够跟很多程序语言相结合，比如 Tcl、C#、PHP、Java. 等，还有 ODBC 接口。
*   比起. Mysql、PostgreSQL 这两款开源的世界著名数据库管理系统来讲，它的处理速度比他们都快。
*   第一个 Alpha 版本诞生于2000年5月。 至2015年已经有15个年头，SQLite. 也迎来了一个版本 SQLite 3已经发布。
*   Python 自带 sqlite3 这个库，方便且直接的创建和读取 sqlite3 数据库。

## 二：sqlite 创建表格

### 1、sqlitestudio 介绍

本节内容的目的，是教大家如何在非代码的情况下，创建 sqlite3 数据库文件和表格编辑操作。 既然不写代码，就肯定需要借助软件来操作。本节课对应的源码中，准备好了 windows、macos、linux 三个系统的 sqlitestudio 软件，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/498261f0423d2a55a92d4294021a26ed.png)

> windows 使用 zip；macos 使用 dmg；linux 使用tar.xz； AI悦创公众号后台回复：20210214，进行获取

sqlitestudio 是一款绿色软件，安装你的操作系统所对应的 sqlitestudio 软件，然后执行，就可以得到启动界面。 ![image.png](https://img-blog.csdnimg.cn/img_convert/fc6958617a7fca312e320fce2f3f156d.png)

### 2、新建 sqlite 数据库文件

点击左上角的数据库，选择添加数据库，则会弹框，让你选择某个数据库文件，或者创建一个新的 sqlite 文件 ![image.png](https://img-blog.csdnimg.cn/img_convert/1ca5884b7a7698ccfb0393ba5b4506d6.png) 点击黄色的文件夹，是指打开某个存在的 sqlite 文件。 点击绿色的+，是新建一个 sqlite 文件，并且你也需要指定存储的具体位置。 选择在三个 sqlitestudio 安装包旁边，新建一个名为 first.db 的文件，如下截图 ![image.png](https://img-blog.csdnimg.cn/img_convert/bb0bbf2f05aa5bb8be1ddd43907d7379.png) 并且，文件也有对应的生成。【最左侧的文件夹，是我解压并使用的 sqlitestudio 。你们拿到的源码中，没有这个文件夹，因为被我删除了】 ![image.png](https://img-blog.csdnimg.cn/img_convert/ced2fb969627bd69375896453e0743c9.png)

### 3、新增数据

回到 sqlitestudio 软件界面，打开刚新建的 first.db ，里面什么都没有，表格是空的，现在来新建一个表格。 鼠标右键点击 Tables ，然后选择新建表格，在新出的界面中，写表格名、字段名和字段类型，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/db3025263586501404e26b3791aa994a.png) Table Name 表格名，输入具体名称。最上方框中的那个按钮，是增列字段的按钮，点击按钮弹出中间的字段信息，输入字段名、类型、大小等。 这里写了 id title content author 四个字段信息，然后点击绿色的勾，保存表格即可。 保存了文件，重新刷新页面，就可以查看数据栏，如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/77e5f7089e62df359a387a59ee9d93c7.png) 点击绿色的+号，然后增加几条数据，方便我们下节课的代码练习。图中有三条。 sqlitestudio 也要保留，方便我们下一篇操作，查看代码练习的数据变化结果。