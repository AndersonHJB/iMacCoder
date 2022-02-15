---
title: Python 万能代码模版：自动办公，提升 X10 倍工作效率
tags: []
id: '1913'
categories:
  - - 技术杂谈
date: 2021-09-24 13:35:57
---

你好，我是悦创。 前面我写了：

1.  [Python 万能代码模版：爬虫代码篇](https://mp.weixin.qq.com/s/jj8srwUPF9wJOHG7YrQvcA)
2.  [Python 万能代码模版：数据可视化篇](https://mp.weixin.qq.com/s/I3vGziMTRTi7yNJAVmr8Mw)

然后，也是终于赶上一周一篇推文啦，差点就鸽了。最近厦门疫情比较严重，连续做了五次核酸，希望快点过去吧！厦门加油！ **然后，正文之前，我碎碎念念几句**：除了教学要教学的浅显易懂，我还是要达到文章也是对小白或者初学者非常实用的。之前有个做公众号的朋友跟我说，你这样的内容没有内涵。 但是一味追求内涵，对读者不能立刻取来使用，那又有何作用呢？ 当然啦，我后面会实用的+深度的，所以尽量做到全面的内容，也希望大家多多转发分享，做了四年干货的公众号，现在关注量才 1500+，感谢支持！

## 使用 Python 实现批量重命名文件

使用 Python 进行批量的文件重命名是比较简单的。比如我们要把一批图片导入到 PS 中编辑，或者导致一批视频文件到 PR 中操作，如果资源的文件名杂乱的话会严重影响效率。所以一般情况下我们都需要首先将相关的文件批量的按照某个规则重命名。 这里我们以前面爬虫示例的 3 小节中批量下载的图片文件夹为例，批量把该文件夹中的所有图片名字重命名为 “`aiyc_0x.jpg` ”的形式，其中 x 是图片的序号，逐一递增。 代码如下：

```python
# -*- coding: utf-8 -*-
# @Author: AI悦创
# @Date:   2021-09-24 10:52:01
# @Last Modified by:   aiyc
# @Last Modified time: 2021-09-24 12:50:02
import os

root, dirs, files = next(os.walk("tips_3/"))

idx = 0

for item in files:
    old_file_path = os.path.join(root,item)
    new_file_path = os.path.join(root, f"aiyc_{idx}.jpg")
    os.rename(old_file_path, new_file_path)
    idx = idx + 1
```

运行之前： ![image.png](https://img-blog.csdnimg.cn/img_convert/17419f26867f1bcfcdb8e973aba3b237.png) 执行过后，重新查看 tips\_3 文件夹，可以看到下面的图片均已变成我们希望的格式。 ![image.png](https://img-blog.csdnimg.cn/img_convert/c08278c5d24183e0932a6bc215d7596f.png) 当你希望批量重命名一批文件时，可以首先将这些文件放到某个文件夹中，然后按照下述方法进行批量重命名。 ![image.png](https://img-blog.csdnimg.cn/img_convert/227ea7fffac6b02606c7a47d78e2618d.png)

1.  替换为希望批量重命名的文件夹；
2.  文件的格式。其中 `{idx}` 部分需要保留，代码执行时会被替换为序号。

代码：[https://github.com/AndersonHJB/AIYC\_DATA/tree/main/03.%20自动办公，提升%20X10%20倍工作效率/3.1%20使用%20Python%20实现批量重命名文件](https://github.com/AndersonHJB/AIYC_DATA/tree/main/03.%20自动办公，提升%20X10%20倍工作效率/3.1%20使用%20Python%20实现批量重命名文件)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/b70a1aed66e44d43aa1410f266193128.png)