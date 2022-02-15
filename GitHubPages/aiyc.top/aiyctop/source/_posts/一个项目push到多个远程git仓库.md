---
title: 一个项目push到多个远程Git仓库
tags: []
id: '1973'
categories:
  - - Git
date: 2021-10-09 16:29:18
---

你好，我是悦创。 我创建了一个项目，然后通过下面的命令 push 到了 GitHub 上。如何再将这个项目 push 到其他远程仓库呢？ 首先在项目控制台执行：

```cmd
git remote -v
```

查看到当前项目的远程仓库地址如下：

```cmd
$ git remote -v
origin  git@gitee.com:huangjiabaoaiyc/quicksandteam.git (fetch)
origin  git@gitee.com:huangjiabaoaiyc/quicksandteam.git (push)
```

那么接下来就需要将该项目同时添加到 gitee 仓库：

```cmd
git remote add gitee https://gitee.com/huangjiabaoaiyc/image.git
```

推送到远程仓库：

```cmd
git push -u gitee
```

这样就将项目也推送到 gitee 仓库，后续代码有更新的时候，先提交艾玛，然后使用下面两个命令分别提交到 github 和 gitee：

```cmd
git push -u origin
git push -u gitee
```

如你所见，上面的方式我们需要推送两次，那么能不能推送一次就可以同时推送到 github 和 gitee 呢，答案是当然可以。 首先删除刚才添加的 gitee 远程仓库地址：

```cmd
git remote rm gitee
```

然后用下面命令添加：

```cmd
git remote set-url --add origin https://gitee.com/huangjiabaoaiyc/image.git
```

最后再查看远程仓库地址信息：

```cmd
$ git remote -v
origin  git@gitee.com:huangjiabaoaiyc/quicksandteam.git (fetch)
origin  git@gitee.com:huangjiabaoaiyc/quicksandteam.git (push)
origin  https://gitee.com/huangjiabaoaiyc/image.git (push)
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![](https://img-blog.csdnimg.cn/df74b093fd8f4297b83e4eeda4ccfa59.png)