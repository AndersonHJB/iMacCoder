---
title: PicGo + GitHub 搭建个人图床工具
tags: []
id: '1557'
categories:
  - - GitHub
date: 2021-03-08 16:34:52
---

写在前面

> 我以前用的 七牛云 + Mpic 的组合，后来由于七牛云测试域名收回，我的图床就废了。以前的好多图片都埋藏在七牛云的服务器上，又气又难过。思考好一段时间，想自己搭服务，但成本有点高，备案的域名 + 服务器一年几百块。对于我这种不靠写字谋生的人而言没有必要，所以就停摆了一段时间。直到今天用 GitHub 搭起了图床，可以说非常开心了。所以跟大家分享一下。

*   方便程度：★★★★☆
*   配置难度：★★☆☆☆ 适用环境：win + mac + linux
*   需要工具：GitHub 账号 + PicGo 客户端
*   稳定性：背靠 GitHub 和微软，比自建服务器都稳
*   隐私性：这算是唯一缺点，你的图片别人可以访问

# 1\. GitHub 仓库设置

> 流程：新建 public 仓库 -> 创建 token -> 复制 token 备用

## 1.1 新建仓库

点击 git 主页右上角的 + 创建 New repository； ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308144803390.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 填写仓库信息，例如我就创建了一个 cloudimg 的仓库。 这里注意，仓库得设置为 Public 因为后面通过客户端访问算是外部访问，因此无法访问 Private ，这样的话图片传上来之后只能存储不能显示。所以要设置为 Public。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308145139253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 1.2 创建 token 并复制保存

此时仓库已经建立，点击 settings 进入设置： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161409646.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161616556.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161644398.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161725181.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161845173.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 然后复制生成一串字符 token，这个 token 只出现一次，所以要保存一下。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161923491.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308161945294.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

# 2\. PicGo 客户端配置

## 2.1 下载&安装

PicGo （目前 2.3.0）是一个开源的图床工具，非常优秀。可以到 git 上下载，但下载速度太慢，所以我放了一个云盘的链接，速度快很多。

*   github 地址：[PicGo](https://github.com/molunerfinn/picgo)：[https://github.com/molunerfinn/picgo](https://github.com/molunerfinn/picgo)
*   https://github.com/Molunerfinn/PicGo/releases
    
*   Win/Mac 版下载链接：[https://aiyc.lanzous.com/b00od7p5a](https://aiyc.lanzous.com/b00od7p5a)
    

密码:3oc6

## 2.2 配置

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308162928403.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

*   仓库名 即你的仓库名
*   分支名 默认 master，如果填测试上传图片出错则填 main
*   Token 就是刚刚复制的那一串字符
*   存储路径 这个可以填也可以不填，填了的话图片就上传到 git 中 blog 这个文件夹 域名 https://raw.githubusercontent.com/AndersonHJB/cloudimg/master 这个要改一下 格式 https://raw.githubusercontent.com/\[username\]/\[仓库名\]/master

然后点确定就可以了。 注：这里提供一个加速访问图片的方法：CDN加速，具体原理自行百度。 将上面的域名改为： 原 https://raw.githubusercontent.com/AndersonHJB/cloudimg/master 现 https://cdn.jsdelivr.net/gh/AndersonHJB/cloudimg@master 然后关于上传的快捷键设置。默认的是 Mac 按键，推荐改成 Ctrl + alt +c。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308163315216.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 综上，操作完成。 本方案唯一缺点，不能私人。但是考虑到 GitHub 上传的图在列表里没法预览，应该没人会闲着没事翻记录。