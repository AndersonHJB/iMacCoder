---
title: Mac OS X在终端中打开文件夹窗口
tags: []
id: '823'
categories:
  - - Mac 实用技巧
date: 2020-08-27 15:18:10
---

你好，我是悦创。 最近在VMware中安装了两个虚拟机，很多命令还是在 Linux 下或者 UNIX 下比较爽。 使用 Mac OS X 的时候，因为习惯了在终端中用 VIM 编写代码，所以一般创建文件、编码都是用命令行操作的，但是偶尔还是需要用到 Finder ，比如可能需要查看以下素材图片的大小、想要把 HTML 文件拖到浏览器中看以下效果。这样的话，如果你的工作目录层次很深的话，就需要点击好多次才可以到达，很不方便。这个时候你可能就会想要下面这个小技巧了：

```cmake
open .
```

上面这个命令就是打开当前所在的文件夹，当然你也可以利用 open 命令打开其它的文件夹。 比如：

```cmake
open ~

open /home/

open ~/Downloads/
```

在 Ubuntu 下，使用终端打开 GNOME 文件夹的命令是：

```cmake
nautilus ~

nautilus /home/

nautilus ~/Downloads/
```

nautilus 又叫作鹦鹉螺，是Ubuntu下浏览文件的命令，很实用。