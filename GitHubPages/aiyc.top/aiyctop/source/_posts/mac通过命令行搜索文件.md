---
title: Mac通过命令行搜索文件
tags: []
id: '1544'
categories:
  - - Mac 实用技巧
date: 2021-03-05 11:21:09
---

你好，我是悦创 。 最近在做 Python 简单的图像识别 ，需要用到某些库和软件，有时候需要查找路径。所以就有了如下内容。 通过 Find 命令搜索文件 find 命令非常高效，并且使用简单。find 命令来自 unix，OS X 和 Linux 系统同样支持该命令。find 最基本的操作就是：

```bash
find 文件路径 参数
```

比如你可以通过以下命令在用户文件夹中搜索名字中包含 screen 的文件

```bash
find ~ -iname  "screen*"
```

你也可以在特定的文件夹中寻找特定的文件，比如：

```bash
find ~/Library/ -iname "com.apple.syncedpreferences.plist"
```

这个命令可以在Library文件夹中寻找com.apple.syncedpreferences.plist文件 通过 mdfind 命令搜索文件 mdfind 命令就是 Spotlight 功能的终端界面，这意味着如果 Spotlight 被禁用，mdfind 命令也将无法工作。mdfind 命令非常迅速、高效。最基本的使用方法是：

```bash
mdfind -name 文件名字
```

比如你可以通过下面的命令寻找 Photo 1.PNG 文件

```bash
mdfind -name "Photo 1.PNG"
```

因为 mdfind 就是 Spotlight 功能的终端界面，你还可以使用 mdfind 寻找文件和文件夹的内容，比如通过以下命令寻找所有包含 Will Pearson 文字的文件：

```bash
mdfind "Will Pearson"
```

mdfind 命令还可以通过 -onlyin 参数搜索特定文件夹的内容，比如

```bash
mdfind -onlyin ~/Library plist
```

这条命令可以搜索 Library 文件夹中所有 plist 文件。 还有一个查找某软件的安装路径 which ，比如我要查找 tesseract 软件的安装路径，就可以使用如下命令。

```bash
which tesseract
```