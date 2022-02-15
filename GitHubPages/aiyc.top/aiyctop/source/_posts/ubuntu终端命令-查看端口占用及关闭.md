---
title: Ubuntu终端命令--查看端口占用及关闭
tags: []
id: '1495'
categories:
  - - Linux
date: 2021-02-22 09:55:34
---

你好，我是悦创。Ubuntu 查看端口使用情况，使用 netstat 命令：

## 1、查看已经连接的服务端口（ESTABLISHED）

```cmd
netstat -a
```

## 2、查看所有的服务端口（LISTEN，ESTABLISHED）

```cmd
netstat -ap
```

## 3、查看指定端口，可以结合 grep 命令：

```cmd
netstat -ap  grep 8080
```

也可以使用 lsof 命令：

```cmd
lsof -i:8888
```

## 4、若要关闭使用这个端口的程序，使用kill + 对应的pid

```cmd
kill -9 PID号
```

> Ps：kill 就是给某个进程 id 发送了一个信号。 默认发送的信号是 SIGTERM，而 kill -9 发送的信号是 SIGKILL，即 exit。 exit 信号不会被系统阻塞，所以 kill -9 能顺利杀掉进程。