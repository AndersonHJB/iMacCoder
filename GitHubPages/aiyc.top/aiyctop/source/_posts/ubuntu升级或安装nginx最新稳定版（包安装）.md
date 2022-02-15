---
title: Ubuntu升级或安装Nginx最新稳定版（包安装）
tags: []
id: '1496'
categories:
  - - Linux
date: 2021-02-22 10:31:00
---

## 说明

1）如果你之前安装过 Nginx，你可以输入

```cmd
sudo apt-get --purge remove nginx
```

将 Ngxin 的配置文件和程序全都卸载，然后按照下面的方式安装即可。 2）如果你不想卸载之前的，仍然可以按照下面的方式进行安装升级，但是 `/etc/nginx` 目录下可能会有你之前版本的一些配置文件，比如 `sites-enabled` 文件夹和 `sites-available` 文件夹等等，但1.14.0稳定版本不需要这些文件夹了，所以最好是卸载了重新安装。

## Nginx 版本介绍

Nginx 官网下载：https://nginx.org/en/download.html ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222101835719.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

*   Mainline version：正在开发阶段的版本，可能会有漏洞。
*   Stable version：稳定版
*   Legacy versions： 历史版本
    
*   本次安装1.18.0的稳定版本
    

## 实际操作

安装或升级，需要添加源才能下载 Nginx 的稳定版本，首先输入以下两条命令：

```cmd
 sudo wget http://nginx.org/keys/nginx_signing.key
 sudo apt-key add nginx_signing.key
```

在 \`\`/etc/apt/sources.list\` 文件中加入下面两行：

```cmd
deb http://nginx.org/packages/ubuntu/ codename nginx
deb-src http://nginx.org/packages/ubuntu/ codename nginx
```

注意 codename 要根据系统来选择可以点击查看详细说明：http://nginx.org/en/linux\_packages.html#stable ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222102338446.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

```cmd
sudo vim /etc/apt/sources.list
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222102608419.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) Ubuntu 其他版本和系统平台更换 codename 即可最后输入：

```cmd
sudo apt-get update
sudo apt-get install nginx
```

输入完成之后，如果你看见这句话： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222105728738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 输入 `nginx -v` 查看安装版本：

```cmd
root@iZ8vb1o9x5vmr6vy4go7tsZ:~# nginx -v
nginx version: nginx/1.18.0
```

此外，`/etc/nginx/` 下的目录结构： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222103032623.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)