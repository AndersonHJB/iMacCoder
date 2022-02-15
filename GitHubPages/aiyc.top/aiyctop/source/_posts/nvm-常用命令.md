---
title: NVM 常用命令
tags: []
id: '1946'
categories:
  - - GitBook开发笔记
  - - NodeJS
  - - 技术杂谈
date: 2021-10-08 12:44:22
---

你好，我是悦创。

## NVM 是什么？

NVM 是 NODE.JS 的版本管理工具，通过它可以安装和切换不同版本的NODE， 从 GitHub 或者其他网站下载一个项目，我们首先查看的是当前这个项目所需要的 NODE 版本，NDOE.JS 官方版本更新的非常快，而且每一次更新改动都比较大，正是因为这个需求，才需要频繁的切换 NODE 版本

## NVM 下载

### 1\. Window 版本

```link
https://github.com/coreybutler/nvm-windows/releases
```

### 2\. MAC 版本

```link
https://github.com/nvm-sh/nvm#install--update-script
```

## NVM， NODE， NPM 之间的区别

node 版本和 npm 包 兼容性越来越差，不同的 node 版本对应这不同的 npm 包版本。在使用 node 版本的过程中，版本之间的切换越来越重要。nvm 是一个很好的 node 版本管理工具

1.  node: node 开发环境，代码库
2.  npm: 安装 node 的时候，一起安装的，node 的包管理器
3.  nvm: node 的版本管理工具

## 输入 nvm 验证 nvm 是否安装成功

1.  输入 nvm 输出：Node Version Manager 代表安装成功
    
2.  查看 nvm 版本 nvm verison
    

## 常用的 nvm 命令

(0) `nvm version` ：查看 nvm 版本 (常用) (1) `nvm install stable`：安装最新稳定版 node (2) `nvm install <version>`：安装指定版本 For Example:

```cmd
nvm install v10.12.0
```

(3) `nvm ls-remote`：查看远程所有的版本，如果为 N/A,切换到外网，改变一下指向

```cmd
export NVM_NODEJS_ORG_MIRROR=http://nodejs.org/dist
```

(4) `nvm ls`：查看已经下载安装的 node 版本 (5) `nvm current`：查看当前使用的 node 版本 (6) `nvm use v10.13.0`：切换到 10.13.0node 版本 (7) `nvm alias default 10.12.0`：设置默认 node 版本

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

[![https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png "https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png")](https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png "https://img-blog.csdnimg.cn/5dbd5f53dcff4532a71c485b64932b0f.png")