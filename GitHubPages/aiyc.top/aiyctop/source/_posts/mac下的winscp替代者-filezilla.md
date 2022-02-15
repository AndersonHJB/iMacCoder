---
title: Mac下的winscp替代者 FileZilla
tags: []
id: '1482'
categories:
  - - 杂谈
date: 2021-02-21 10:00:04
---

# 前言

Windows下做开发运维的小伙伴，应该有一部分像我这样喜欢 用 [winscp](https://winscp.net/eng/docs/lang:chs)去管理远程服务器的文件吧。图形化管理确时好用，界面布局也符合操作习惯。刚用Mac 不知道用sftp软件好。

## 方式一： Mac 下推荐使用 FileZilla

我找了一圈感觉用的比较舒服的就是这款软件了。 https://www.filezilla.cn/ 特点：

*   易于使用
*   多协议支持 FileZilla支持FTP、FTPS、SFTP等文件传输协议
*   支持中文
*   免费使用
*   跨平台Windows下也可以用

### 使用简介

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221095505586.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221095520229.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221095529197.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 方式二： Intellj IDEA 自带

如果你电脑上已经安装 IDEA 那么可以使用这种方式。我偶尔也会用，多一种选择。如果你也是 coder 可以用这个，功能也很强大，甚至可以自动上传，自动部署项目。这里就不展开了，有兴趣自己研究吧，这里只是告诉大家 idea 有这个功能。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221095558476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 具体功能在 Tools =》 Start SSH Session 之中，可以远程管理文件，也可以远程shell。也是挺不错的。