---
title: 买不起MacBook，使用Windows 10配置zsh命令行做开发
tags: []
id: '1976'
categories:
  - - 技术杂谈
date: 2021-10-11 08:24:51
---

你好，我是悦创。 从苹果转过来的开发都会感觉 Windows 下的命令行真是难用，接下来就跟着我来把 zsh 搬过来吧买不起 MacBook ，使用 Windows 10 配置 zsh 命令行做开发。![在这里插入图片描述](https://img-blog.csdnimg.cn/5544a37708994620850b7af0dcdf0ad1.png)

1.  必须是 Windows10，在程序和功能里面开启“适用于Linux的Windows子系统”

微软+R 启动运行，输入：control 回车即可： ![在这里插入图片描述](https://img-blog.csdnimg.cn/2f26922f23994217b6cf777e6de94eea.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/16c4a599fc304134ad0cfe3d42233d75.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/b71a695389c741f283d5fb97933b8ee3.png) ![开启这个功能](https://img-blog.csdnimg.cn/20e85a637c0b45568d8b73392d3f6f35.png)

2.  在应用商店里搜索 Linux ，选一个自己喜欢的 Linux 版本就好了，我以 Ubuntu 示意：

![在这里插入图片描述](https://img-blog.csdnimg.cn/4c5b9795437b4a0bb4065e68bf815029.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/dbd51a5de2ea4840b3c6ac31e980fa97.png)

3.  安装完成后打开，需要配置一会儿。然后设置用户名密码，我这里设置用户名为 user

![在这里插入图片描述](https://img-blog.csdnimg.cn/41057acfc2dd41458eb0b5886afa5b93.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/f5b34ba9f8534009876bfcd946c7c4ca.png) 然后配置一下 Ubuntu 下的用户名和密码： ![在这里插入图片描述](https://img-blog.csdnimg.cn/de1ce9e18b8a47dd9066a342e36d4a9f.png)

4.  配置好以后发现 Windows 下的命令提示符终端真的是难用，也没法复制粘贴快捷键。换一个 Conemu

这个可以像 Linux 下或者 mac 下的 iTerm2 一样进行快捷操作：[https://conemu.github.io/](https://conemu.github.io/) ![在这里插入图片描述](https://img-blog.csdnimg.cn/2aac52c82d004db2946d402b205522ba.png) [https://www.fosshub.com/ConEmu.html](https://www.fosshub.com/ConEmu.html) ![在这里插入图片描述](https://img-blog.csdnimg.cn/806958959e79440f9b6bc43ee75e93d0.png) 安装好以后初始化，设为默认启动 Bash，就可以直接进入 Ubuntu 的命令行了： ![在这里插入图片描述](https://img-blog.csdnimg.cn/9da2a3e14d2b4c1c90d432902f54c768.png) 好了，接下来我们来看一下会发生什么，当点击 ConEmu 启动的时候，就会进入到一个默认的路径里，这个路径是外面 Windows 用户的目录，C 盘被挂载到 /mnt/c 下面了，可以直接实现文件共享了。这个时候如果你还不知道在干什么要干什么的话，就可以先这么用了买不起 MacBook，使用 Windows 10 配置 zsh 命令行做开发![在这里插入图片描述](https://img-blog.csdnimg.cn/716fef054c9f4e029e63b70ba1a91e94.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/d329b46661004403944c39ebcc562f77.png)

5.  默认的 bash 还是有点弱，上个 oh my zsh

直接看官网怎么安装运行就行啦：[https://ohmyz.sh/#install](https://ohmyz.sh/#install) ![在这里插入图片描述](https://img-blog.csdnimg.cn/a45f1416478c4b978a140e15f646be7f.png) **Mac 安装 zsh** 使用 mac 系统的读者相信大部分都安装了 homebrew，因此建议直接使用 brew 的方式来安装 zsh，命令如下所示：

```cmd
brew install zsh
```

安装过程中，终端会出现如下信息：

```cmd
==> Installing zsh
==> Downloading https://homebrew.bintray.com/bottles/zsh-5.7.1.mojave.bottle.tar
==> Downloading from https://akamai.bintray.com/79/793d87f67e64a5e01dfdea890af21
######################################################################## 100.0%
==> Pouring zsh-5.7.1.mojave.bottle.tar.gz
?  /usr/local/Cellar/zsh/5.7.1: 1,515 files, 13.3MB
```

**Linux 安装 zsh** Linux 中安装 zsh 同样非常简单，只需要一条命令即可完成安装，考虑到 Linux 多个版本，不同版本的安装方式不同，这里以常用的 Ubuntu 和 centos 为例： Ubuntu 安装 zsh 命令：

```cmd
apt install zsh
```

centos 安装 zsh 命令：

```cmd
yum install zsh
```

下面我以 Ubuntu 为例，执行安装命令之后可以看到返回如下信息： ![在这里插入图片描述](https://img-blog.csdnimg.cn/c47e4f8273a24c1e9c719918cbc7cf22.png) **安装 oh-my-zsh** 安装 oh-my-zsh 的目的是为了让大家可以更快速的学习 Git 的命令行操作，它能够给我们在输入一些 Git 命令时候提供很大的方便。 因为 oh-my-zsh 是基于 zsh，它的安装方式和系统本身有关联关系，因此统一的安装命令如下：

```cmd
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

执行安装命令完成之后，可以看到终端如下信息：

```cmd
         __                                     __
  ____  / /_     ____ ___  __  __   ____  _____/ /_
 / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \
/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /
\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/
                        /____/                       ....is now installed!

Please look over the ~/.zshrc file to select plugins, themes, and options.
p.s. Follow us on https://twitter.com/ohmyzsh
p.p.s. Get stickers, shirts, and coffee mugs at https://shop.planetargon.com/collections/oh-my-zsh
➜  ~
```

**测试验证** 安装成功之后，会看到终端发现明显的变化，当你输入命令的一部分再按下 tab 键时，它会给你一些相应的提示或者自动补全，比如当你输入：

```cmd
git st
```

再按下 tab 键，在终端会看到如下效果：

```cmd
➜  ~ git st
stash      -- stash away changes to dirty working directory
status     -- show working-tree status
stripspace -- filter out empty lines
```

除了自动补全和命令提示外，还可以给你纠错，比如当你输入命令：

```cmd
git statsu
```

它会告诉你 git 没有这个命令，并提示你相对应正确的命令，如下所示：

```cmd
➜  ~ git statsu
git: 'statsu' is not a git command. See 'git --help'.

The most similar command is
    status
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/99d1ceb0cfb74697979c6ab989c070f4.png)