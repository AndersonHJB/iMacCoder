---
title: 基础的Linux命令
tags: []
id: '1487'
categories:
  - - Django
  - - Linux
  - - 在线编程搭建
date: 2021-02-21 10:28:00
---

## Linux系统基础命令

两个常用安装命令

```cmd
apt-get install + 软件名称（安装到系统里）  
pip3 install + 软件名称（安装Python模块）
```

*   `sudo` ：管理员身份授权运行
*   `cd` ：打开文件夹
*   `ls` ：浏览当前文件夹所有文件名

## 更新系统

```cmd
sudo apt-get update  
```

```cmd
sudo apt-get upgrade
```

```cmd
sudo apt-get update
sudo apt install python3-pip  
pip3 install mezzanine  
mezzanine-project makerbean  
cd makerbean
python3 manage.py createdb
sudo python3 manage.py runserver 0.0.0.0:80
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221102553781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221102546781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 安装Screen

```cmd
sudo apt install screen
```

安装完成后输入指令screen就可以打开一个新screen 继续运行Django服务器，成功后可关掉命令行窗口