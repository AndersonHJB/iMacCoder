---
title: 「转载」vaptcha 等手势验证码图像识别与轨迹提取（思路）
tags:
  - 深度学习
  - 验证码
id: '793'
categories:
  - - 深度学习
date: 2020-08-11 15:40:30
---

作者：文安哲 从博客重开以后就说要更文章，鸽了蛮久了，赶紧补上一篇嫖嫖各位老公的流量。 最近看群里面大家讨论研究手势验证码比较多，然后我也顺带研究做了一下，给各位老公们分享一下做的过程。 首先，一起来康康手势验证码长啥样！ ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154055.jpg) ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154058.png) 大概就是长这个样子，需要按照图像中的那条轨迹再图片上滑动，不得不说这类验证码确实体验感拉满，让人很想立马关掉这个网站。 那么言归正传，这类验证码该怎么做识别部分呢？ 按照我们正常的思维方式就是要提取出来图中轨迹的部分和形状。 之前我试验了通过 opencv 二值化然后提取物体轮廓等等方法，可能对单一一张图有用，但是拿到其他图上效果就不是很好了。 直到有一天我看到了一张图 ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154101.png) 瞬间就反应过来我们可以通过语义切割的方式去获取轨迹部分。 使用MaskRcnn即可相对准确的切割出我们想要的部分。 1、采集图像样本。 这里没啥好说的，通过不断地请求获取验证码得到原始的手势验证码的图像。这里我大概采集了100张左右。 ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154105.png) 2、标记样本 这里我们使用Labelme工具来标注。 [传送门](https://github.com/wkentaro/labelme) 标记出来的效果大概就这这个样子 ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154109.png) 3、训练样本 这里建议大家使用tensorflow自己的object\_detection来训练 [传送门](https://github.com/tensorflow/models/tree/v1.13.0/research/object_detection) 这里面有若干已经写好的有关目标检测的网络可以供我们调用，具体使用方法我会再单独开一篇文章来讲，如果本身就会的就可以跳过直接去玩耍辣。 4、处理训练结果 训练后他会返回一个由0和1组成的Ndarray的mask,在这里可能需要重新resize一下这个mask成为你原图的宽高（可能是因为我改了一下代码出现了点问题）， 然后直接对这个ndarray \* 255就会将这个Ndarray转成由0和255组成，再直接与使用opencv imshow就可以看到如下效果。 ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154113.png) 5、获取轨迹 获取轨迹这里就比较简单啦，直接使用skimage中的morphology直接对之前由0和1组成的Ndarray操作就可以抽取出白色部分的骨架。 抽取完骨架获取的是一个有True和False组成的Size和之前Ndarray一样的矩阵。直接在原图上操作，将对应为True点位的RGB改为\[0, 0, 0\] ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200811154116.png) 可以看到图中轨迹部分上画出了一条黑色的线~ 感谢各位老公的捧场，本篇文章到此结束啦~下一期更新一下基于object\_detection api的目标检测 转发一定要标注原作者和网址哦~

> 原文链接：[https://wenanzhe.com/2020/08/11/vaptcha%e7%ad%89%e6%89%8b%e5%8a%bf%e9%aa%8c%e8%af%81%e7%a0%81%e5%9b%be%e5%83%8f%e8%af%86%e5%88%ab%e4%b8%8e%e8%bd%a8%e8%bf%b9%e6%8f%90%e5%8f%96/](https://wenanzhe.com/2020/08/11/vaptcha等手势验证码图像识别与轨迹提取/) 作者：文安哲