---
title: Mac下使用VScode编译配置C/C++程序详细图文教程
tags: []
id: '1358'
categories:
  - - VScode
date: 2021-01-16 09:34:50
---

> 微软提供一个跨平台的编辑器Visual studio code，这个编辑器很轻量级，插件也多，适合在Mac上编写一些C 或者 C++的代码，下面就详情来看看具体的操作步骤，希望对大家有所帮助

在Mac上有时候需要编写一些C 或者 C++的代码，如果使用 xcode，有时候就显得很笨重，而且运行起来很不方便。而微软提供了一个跨平台的编辑器Visual studio code ,这个编辑器很轻量级，而且插件超多，你几乎可以在这个编辑器里运行所有的软件。

## 操作步骤

### 1、安装软件

下载Mac系统适用VScode安装包；下载完成后，将zip安装包解压到桌面即可。

### 2、安装插件

打开VScode后，按下组合键“⇧⌘X”，打开扩展，输入“C/C++”，安装“C/C++”、“C/C++ Clang Command Adapter”，安装完成后，重启VScode让插件生效。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116092806960.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 3、“Hello World”

重启VScode后打开新建好的文件夹， ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116092826149.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

#### （1）依次点击“打开文件夹”，--->“新建文件”，

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116092847763.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

#### （2）添加.launch.json文件

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116092918457.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116092924933.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

#### （3）添加tasks.json文件：

按下组合键“⇧⌘B”，如下图操作： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116092950189.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116093006641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116093014254.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

#### （4）再次按下组合键“⇧⌘B”，编译cpp文件，待编译完成后，“F5”调试执行，运行后结果在终端显示：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210116093034527.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)