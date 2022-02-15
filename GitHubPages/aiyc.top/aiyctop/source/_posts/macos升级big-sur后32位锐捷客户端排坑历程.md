---
title: MacOS升级Big Sur后32位锐捷客户端排坑历程
tags: []
id: '1721'
categories:
  - - 技术杂谈
date: 2021-05-31 10:36:18
---

你好，我是悦创。 天哪！升级一时爽…搞了一晚上，因为10.15.2全面摒弃32位应用，所以校园网锐捷首当其冲，连打开都没得机会… 从学校的网站上面下载：http://www.xit.edu.cn/xit\_e/index.html 也是无法使用。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531101553541.png) 唉，都怪没有好好看升级警示，参考-—>https://support.apple.com/zh-cn/HT208436 那看看网上都有神马解决方法吧。 不删数据回退 Mojave，GG，必须重装 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531101623637.png) - 锐捷路由器，没钱且麻烦

*   替代客户端，如 mentohust，年代久远且折腾了很久都没成功…
    
*   64位锐捷客户端（最终解决方法）
    

## 客户端获取

在网上找了很多 Mac 版本能搜到的 v1.33 和 v1.34 都是 32 位的，而学校官网也没有放出新的客户端？？ **包括锐捷官网试着搜了一下 RG-SU 系列，也没有新软件？？？** 绝望了好久看到 B 站某 up 主说是客服给了新的 64 位包…天哪！为什么锐捷官网不放出来？？？无语死了… ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531101800713.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 当然，我现在的系统是： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531101859138.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

> [https://pan.baidu.com/s/1cB8kFnMNk\_tAJWPLDfEI5g](https://pan.baidu.com/s/1cB8kFnMNk_tAJWPLDfEI5g) 锐捷 for mac v1.35 大家可以到这个链接去下载，有两种版本，每个单位和学校不一样，都试一下，那个有用用哪个

## 踩坑

本以为下载完软件就完事打击了，但是还有几个坑点，很少人写，因此记录一下造福大家

*   首先先解压到桌面，然后，切记，**拉至应用程序文件夹**，否则会出现 `无法读取认证客户端系统配置信息，请重新安装客户端！` 惨兮兮

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531102021978.png) - 双击进行安装，会出现下图情况，`去设置—>安全性与隐私—>仍要打开` ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531102040621.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531102117801.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) - 连接不上最可能是网卡选错了，还是多试几个就可以了 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531102134497.png) 最最坑的是！！！即使你所有信息都对了，第一次配置的时候有可能是不成功的，再连一次，只要连上了后面就可以愉快地使用了！只要避开上面几个坑基本上没大问题~搞了一晚上，甚是辛酸，最后吐槽一下人间百态，某鱼v1.35客户端卖5块钱…这个钱都赚？？？