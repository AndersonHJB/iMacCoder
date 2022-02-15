---
title: '03 初识Git : 本地创建一个 Git 仓库'
tags: []
id: '1515'
categories:
  - - Git原理详解与实操指南
date: 2021-02-25 17:44:26
---

![image.png](https://img-blog.csdnimg.cn/img_convert/079a43b009674886825e652a4d541985.png)

> 宝剑锋从磨砺出，梅花香自苦寒来。——佚名

在上一节内容中，我们已经将 Git 环境安装好，从这一节开始我们开始正式接触 Git 的操作命令，从最简单的开始，循序渐进。在这一节中，我们通过本地创建一个 Git 版本库来初步认识 Git 版本库，以及 Git 的一些必要的配置。

## 3.1 创建版本库

我们首先创建文件夹 aiyc，这个文件夹用于版本管理的根目录。 如果在 Windows 下我们也可以单击鼠标右键，在菜单中选择新建文件夹，然后把文件夹名字改为 aiyc 就可以了。如果在 Linux 或者 Mac 系统下，可以通过命令 mkdir 创建文件夹，参考命令如下：

```bash
mkdir test && cd test
```

接下来不管什么系统，都打开终端，并在终端中通过`cd`命令的方式进入文件夹，然后就可以使用 git init 命令初始化一个仓库了，参考执行命令如下：

```bash
git init
```

执行命令之后，Git 会进行一系列的初始化操作，当你看到类似如下的提示：

```bash
➜  aiyc git init
已初始化空的 Git 仓库于 /Users/apple/Desktop/Git学习/aiyc/.git/
➜  aiyc git:(master)
```

说明已经成功创建一个版本库，同时你会发现光标左侧比之前多出几个字符 `git:(master)`，这是因为我们在第二节的时候安装了`oh-my-zsh`主题所导致。 当`oh-my-zsh`发现当前目录下存在`.git`文件夹，便会读取当前版本库的信息，并把当前版本库所在的分支名显示在光标左侧；而当你通过 `cd..` 命令跳出版本库的目录时候，光标左侧的`git:(master)`提示也会随着消失，如下图所示 ![image.png](https://img-blog.csdnimg.cn/img_convert/4e8ff82ac4591a4e719963e13e8845ea.png) 刚才说到初始化版本库会在当前目录中创建一个`.git`的文件夹，我们可以重新进入版本库根目录，然后通过命令 `ls -al` 进行查看，如下命令所示：

```bash
➜  .git git:(master) ls -al
total 24
drwxr-xr-x   9 apple  staff  288  2 25 16:54 .
drwxr-xr-x   3 apple  staff   96  2 25 16:54 ..
-rw-r--r--   1 apple  staff   23  2 25 16:54 HEAD
-rw-r--r--   1 apple  staff  137  2 25 16:54 config
-rw-r--r--   1 apple  staff   73  2 25 16:54 description
drwxr-xr-x  14 apple  staff  448  2 25 16:54 hooks
drwxr-xr-x   3 apple  staff   96  2 25 16:54 info
drwxr-xr-x   4 apple  staff  128  2 25 16:54 objects
drwxr-xr-x   4 apple  staff  128  2 25 16:54 refs
➜  .git git:(master)
```

这些目录可能我们会比较陌生，在后面的章节当中我们会略有涉及，因此，在这节当中先简单了解一下这些文件夹的作用：

*   HEAD：文件指示目前被检出的分支
*   branches：新版本已经废弃无须理会
*   description：用来显示对仓库的描述信息
*   config：文件包含项目特有的配置选项
*   info：目录包含一个全局性排除文件
*   hooks：目录包含客户端或服务端的钩子脚本
*   index：文件保存暂存区信息
*   objects：目录存储所有数据内容
*   refs：目录存储分支的提交对象的指针

## 3.2 基础配置

在建立完项目的版本库之后，后续对代码的管理操作都会要求要有一个身份，所以需要你在管理操作之前，配置一个昵称和邮箱，这个昵称和邮箱仅仅是在查看改动记录时候用的，和后面的鉴权没有关系。

### 3.2.1 查看配置信息

在设置昵称和邮箱之前，可以先检查一下之前有没有配置过昵称和邮箱 查看昵称的命令如下：

```bash
git config user.name
```

查看邮箱的命令如下：

```bash
git config user.email
```

### 3.2.2 设置配置信息

如果执行上面的命令没有返回相应的昵称和邮箱，说明你还没有配置昵称和邮箱。那么就需要进行配置 。 配置昵称的命令参考如下：

```bash
git config --global user.name "你的昵称"
```

配置邮箱的命令参考如下：

```bash
git config --global user.email "你的邮箱"
```

实际操作：

```bash
➜  aiyc git:(master) git config --global user.name "aiyuechuang"
➜  aiyc git:(master) git config --global user.email "1432803776@qq.com"
➜  aiyc git:(master) git config user.name
aiyuechuang
➜  aiyc git:(master) git config user.email
1432803776@qq.com
```

### 3.2.3 修改配置信息

在配置中如果不小心配置错了，或者后面想修改配置的时候，是不能通过重复执行上面的设置昵称命令，来修改昵称的，邮箱修改同理。如果你多次设置昵称，它会在命令执行后提示你无法重复配置或者可能不给你提示，但是这种情况会导致一个 key 配置了多个 value 的问题。 不过，修改的时候，可以通过特定的方式去修改，这里我介绍两种方法， 第一种是通过命令行，第二种是通过修改配置文件。

#### 命令行修改配置

通过命令行修改的方式比较简单，直接执行以下的命令即可。 修改昵称参考命令如下：

```bash
git config --global --replace-all user.name "your user name"
```

修改邮箱地址参考命令如下：

```bash
git config --global --replace-all user.email "your user email"
```

#### 修改配置文件

修改文件的方式，主要是修改位于主目录下 `.gitconfig` 文件。 在 Linux 和 Mac 中，可以通过 vim 命令进行直接编辑，比如 `vim ~/.gitconfig` ；

```bash
vim ~/.gitconfig
```

Windows 系统同样位于用户主目录下，假设你当前的用户是 `administrator`，那么对应的配置文件的路径应该是 `C:\Users\administrator\.gitconfig`，可以直接使用记事本修改里边的 name 或者 email。 如果之前已经配置过昵称和邮箱的情况下，当使用 vim 或者记事本打开配置文件之后，可以看到如下配置：

```bash
[user]
        name = aiyuechuang
        email = 1432803776@qq.com
```

在如果有重复的 name 或 email，可以将其删掉，只剩下一个就好。修改完，通过 git bash 输入 `git config –list`可以查看是否修改成功了。

## 3.3 小结

这一节中主要讲到了如何创建一个本地版本库、版本库的大体结构 、基础配置方法等。

1.  在空文件夹中，可以通过命令 `git init`创建一个本地版本库；
    
2.  每个版本库的根目录下，都存放着一个`.git`的隐藏文件夹，里面包含版本库的全部信息；
    
3.  管理版本库必须有一个身份，需要设置昵称和邮箱。