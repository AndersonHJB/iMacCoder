---
title: 魔性，用 Python 实现火爆全网的「蚂蚁呀嘿」视频特效！
tags: []
id: '1555'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-07 16:15:09
---

##### 完整文章、资料阅读公众号文章还有视频：[https://mp.weixin.qq.com/s/RsJWPWKE0YCebelxHr-KaA](https://mp.weixin.qq.com/s/RsJWPWKE0YCebelxHr-KaA)

![](https://img-blog.csdnimg.cn/img_convert/5508bb739075a6c388ffd4a28ce26712.gif) 你好，我是悦创。这篇文章搞了前后两天，至于为什么搞，后面会说。写到这个文章的生时候，我估计我后面还会写 Python 处理视频的自动化文章，也敬请期待！**期待的同时希望你们的转发分享，这样我会更有动力，如果可以也可以赞赏来一些，我们来一个众筹写作好吗？——后面我写一篇这样的文章，希望大家支持我哈。** 最近悦创在抖音上看到很多「蚂蚁呀嘿」的魔性视频，各方大佬齐齐上阵。其实把真正开始去发现是从我女朋友那里发现的，她做了一个有趣的视频，第一遍播放的时候，倒是没那么大的兴趣。但虽知道后面就一发不可收拾，那我就想：**能不能用 Python 实现呢？** 不过在开始之前呢，我还是要说的，**如果使用网上的软件制作蚂蚁呀嘿，是有风险的。把个人清晰的正面照发布上网络，是有巨大的风险的。但是小悦本人安全意识较高，又想做怎么办呢？——Python** 然后就开始找资料啥的，进行研究。刚好看到百度的开源项目，基于 PaddleGAN 实现表情迁移，于是也来玩一把！ 但我看抖音上的大部分是这样的，不知道选什么视频比较好的。我就选择点赞量比较大的： ![蚂蚁呀黑.mp4](https://img-blog.csdnimg.cn/img_convert/7f2f55e32159afeaa752aaa4983cc03b.png) 那悦创就想，做些程序员的合集或者是油画合集。但网络上的教程都不好用，所以我就整理并写了一篇。本文的逻辑将会是：先实现单人，然后再实现多人。

# 1\. \[单人版\]蚂蚁呀嘿

我们先来看看单人版的效果： ![](https://img-blog.csdnimg.cn/img_convert/206ccb1c9b1407af2bb47ea8c3660579.gif) **没配音，感觉不是很精彩，后面上视频。** 那么需要如何实现呢，接下来就是教学时间。冲冲冲！

## 1.1 准备

本教程是基于 [PaddleGAN](https://github.com/PaddlePaddle/PaddleGAN) 实现的 First Order Motion model ，实现让任何人唱起「蚂蚁呀嘿」的旋律，若是大家喜欢这个教程，请到 [Github PaddleGAN](https://github.com/PaddlePaddle/PaddleGAN) 主页点击 star 呀！下面就让我们一起动手实现吧！\*\* **整体实现只有三步：**

1.  下载 PaddleGAN 代码
2.  运行 First Order Motion model 的命令
3.  给视频加上声音

看 是不是相当简单！！接下来让我们一步步开始吧！

### 1.1.1 下载 PaddleGAN 代码

```python
# 从github上克隆PaddleGAN代码
# git clone https://github.com/PaddlePaddle/PaddleGAN
git clone https://gitee.com/paddlepaddle/PaddleGAN.git
```

**如果有人没有安装 git 可以在公众号：AI悦创，后台回复：「padd」，就可以获取到文件。** **PS：如果无法实现相同效果，还是希望你用 git，关于 git 如何安装，可以查看此文章：**[Git 安装与本地创建 Git 仓库](https://mp.weixin.qq.com/s/GPbMmHjBK3pl9mFXpHEcDA)

### 1.1.2 First Order Motion model 原理

在玩的同时，还是要说说，原理。 First Order Motion model 的任务是 image animation，给定一张源图片，给定一个驱动视频，生成一段视频，其中主角是源图片，动作是驱动视频中的动作，源图像通常包含一个主体，驱动视频包含一系列动作。 通俗来说，First Order Motion 能够将给定的驱动视频中的人物 A 的动作迁移至给定的源图片中的人物 B 身上，生成全新的以人物 B 的脸演绎人物A的表情的视频。 以人脸表情迁移为例，给定一个源人物，给定一个驱动视频，可以生成一个视频，其中主体是源人物，视频中源人物的表情是由驱动视频中的表情所确定的。通常情况下，我们需要对源人物进行人脸关键点标注、进行表情迁移的模型训练。 但是这篇文章提出的方法只需要在同类别物体的数据集上进行训练即可，比如实现太极动作迁移就用太极视频数据集进行训练，想要达到表情迁移的效果就使用人脸视频数据集 voxceleb 进行训练。训练好后，我们使用对应的预训练模型就可以达到前言中实时 image animation 的操作。

## 1.2 开发环境准备

### 1.2.1 建立虚拟环境

我个人比较喜欢对每个项目建立虚拟环境，如果你不需要可以跳过这步。我这里新建一个项目文件夹： **The\_ant\_ah\_black**

```python
# 进入项目文件夹
cd The_ant_ah_black

# 创建虚拟环境 antvenv
python3 -m venv antvenv

# Windows 进入虚拟环境，命令：
antvenv\Scripts\activate

# Mac 进入虚拟环境，命令：
source antvenv/bin/activate
```

开头出现如下图，即为创建成功： ![image.png](https://img-blog.csdnimg.cn/img_convert/3a6c5b7220796d41633981d07016a435.png) 把我们下载的 PaddleGAN 代码，放进 \*\*The\_ant\_ah\_black \*\*文件夹下。 ![image.png](https://img-blog.csdnimg.cn/img_convert/f09f352224c3d8606b6df361789fd7fe.png)

### 1.2.2 安装所需安装包

#### 方法一：

按下面的命令一步一步执行即可。

```python
# 安装所需安装包
cd PaddleGAN/
pip install -r requirements.txt
pip install imageio-ffmpeg
cd applications/
mkdir output
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install paddlehub -i https://mirror.baidu.com/pypi/simple
```

#### 方法二：

我是给我的 Python 换过源的，所以没换过且有可能安装失败的可以使用下面的命令。

```python
# 终端打开文件夹
cd PaddleGAN

# 安装相关依赖
pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple
pip install imageio-ffmpeg -i https://mirror.baidu.com/pypi/simple
```

终端打开文件夹，安装所需要的依赖。 毕竟是百度的开源项目，所以使用了百度的 pip 源，速度真的很快。 下面再创建一个输出文件夹，生成的视频会保存在这里。

```python
# 打开文件夹
cd applications/

# 新建文件夹
mkdir output
```

最后还需要安装百度的 paddlepaddle 和 paddlehub。 paddlepaddle 是基础，而 paddlehub 则是用来检测人脸用的。 将「输入图片」中的所有人脸检测出来，然后使用 PaddleGAN 对每个人脸进行表情迁移，最后生成视频。

```python
# 安装库
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install paddlehub -i https://mirror.baidu.com/pypi/simple
```

### 1.2.3 命令解析

```python
export PYTHONPATH=$PYTHONPATH:/home/aistudio/PaddleGAN && python -u tools/first-order-demo.py  --driving_video ~/work/fullbody.MP4  --source_image ~/work/aiyuechuang.png --relative --adapt_scale
```

大家可以上传自己准备的视频和图片，并将如上命令中的 **source\_image** 参数和 **driving\_video** 参数分别换成自己的图片和视频路径，然后运行如下命令，就可以完成动作表情迁移，程序运行成功后，会在 **ouput** 文件夹生成名为 **result.mp4** 的视频文件，该文件即为动作迁移后的视频。**/home/aistudio/PaddleGAN** 为你的 **PaddleGAN 路径** 。 **本项目中提供了原始图片和驱动视频供展示使用。具体的各参数使用说明如下**

*   driving\_video： 驱动视频，视频中人物的表情动作作为待迁移的对象
*   source\_image： 原始图片，视频中人物的表情动作将迁移到该原始图片中的人物上
*   relative： 指示程序中使用视频和图片中人物关键点的相对坐标还是绝对坐标，建议使用相对坐标，若使用绝对坐标，会导致迁移后人物扭曲变形
*   adapt\_scale： 根据关键点凸包自适应运动尺度

#### 命令总结

```python
export PYTHONPATH=$PYTHONPATH:PaddleGAN路径 && python -u tools中first-order-demo.py的路径  --driving_video 视频路径  --source_image 图片路径 --relative --adapt_scale
```

## 1.3 具体操作实操

此处，大家可以使用自己设计的图片，生成你想要的视频。比如我的原始图片 **秃头乔哥.png**，就是编程创始人集合照，如下图。 ![image.png](https://img-blog.csdnimg.cn/img_convert/ec742a2103c4c9926a02407468851b6e.png) 对于其他的视频特效，就需要更改驱动视频，即修改 driving\_video 。

### 1.3.1 我的文件路径

图片：**/Users/apple/Desktop/GitHub/The\_ant\_ah\_black/aiyc\_work/秃头乔哥.png** 视频：**/Users/apple/Desktop/GitHub/The\_ant\_ah\_black/aiyc\_work/fullbody.MP4** PaddleGAN：**/Users/apple/Desktop/GitHub/The\_ant\_ah\_black/PaddleGAN** first-order-demo.py 路径：**/Users/apple/Desktop/GitHub/The\_ant\_ah\_black/PaddleGAN/applications/tools/first-order-demo.py** 所以我的写出来的路径是：

```python
export PYTHONPATH=$PYTHONPATH:/Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN && python -u /Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN/applications/tools/first-order-demo.py  --driving_video /Users/apple/Desktop/GitHub/The_ant_ah_black/aiyc_work/fullbody.MP4  --source_image /Users/apple/Desktop/GitHub/The_ant_ah_black/aiyc_work/秃头乔哥.png --relative --adapt_scale
```

> **PS：这里我为了让小白理解，都用了绝对路径。大佬可以自行使用相对路径，我也会把相对路径写出来。**

**为了让小白明白，我再重复一下。** **绝对路径：**

```python
export PYTHONPATH=$PYTHONPATH:/Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN && python -u /Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN/applications/tools/first-order-demo.py  --driving_video /Users/apple/Desktop/GitHub/The_ant_ah_black/aiyc_work/fullbody.MP4  --source_image /Users/apple/Desktop/GitHub/The_ant_ah_black/aiyc_work/秃头乔哥.png --relative --adapt_scale
```

**相对路径：**

```python
export PYTHONPATH=$PYTHONPATH:/Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN && python -u tools/first-order-demo.py  --driving_video ../../aiyc_work/fullbody.MP4  --source_image ../../aiyc_work/秃头乔哥.png --relative --adapt_scale
```

使用相对路径的话，上面命令写完之后，需要在终端进入到文件夹：applications 下，不然找不到：first-order-demo.py，这里面：first-order-demo.py 我用的是相对路径。 所以我不管输入的是绝对路径还是相对路径，结果是类似的。 ![image.png](https://img-blog.csdnimg.cn/img_convert/3b1dea219273607e39da8908702c1893.png) 我们可以在下图路径中找到生成的视频： ![image.png](https://img-blog.csdnimg.cn/img_convert/f82c95d653e5e374fffe6fdde64f0896.png) ![result1.mp4](https://img-blog.csdnimg.cn/img_convert/7f2f55e32159afeaa752aaa4983cc03b.png) 另外生成的视频是不带声音的，所以需要使用 FFmpeg 将视频与音频进行合并。

### 1.3.2 使用 moviepy 为生成的视频加上音乐

#### 方法一

```python
# add audio
pip install moviepy
```

```python
#为生成的视频加上音乐
from moviepy.editor import *

videoclip_1 = VideoFileClip("/Users/apple/Desktop/GitHub/The_ant_ah_black/aiyc_work/fullbody.MP4")
videoclip_2 = VideoFileClip("/Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN/applications/output/result.mp4")

audio_1 = videoclip_1.audio

videoclip_3 = videoclip_2.set_audio(audio_1)

videoclip_3.write_videofile("/Users/apple/Desktop/GitHub/The_ant_ah_black/PaddleGAN/applications/output/qiaoge.mp4", audio_codec="aac")
```

![image.png](https://img-blog.csdnimg.cn/img_convert/9a2856414f1e9040d4ad7695d241574e.png) 效果视频： ![qiaoge.mp4](https://img-blog.csdnimg.cn/img_convert/7f2f55e32159afeaa752aaa4983cc03b.png)

#### 方法二

使用 FFmpeg 将视频与音频进行合并，那就需要安装 FFmpeg ，Windows 、 Mac 如何安装自行搜索。

```python
# 视频和音频合并
ffmpeg -i myyh.mp4 -i MYYH.mp3 -vcodec copy -acodec copy result.mp4
```

**目前该方法适合在 Windows 和 Linux 上操作，Mac 在调用 ffmpeg 这一步会出错。** 不知道是不是和 mac 不支持 gpu 安装 paddlepaddle 有关系。 如果你想生成 GIF，分享给其他人，比如整蛊你的好朋友。同样可以使用 FFmpeg 生成 GIF。

```python
# 生成GIF
ffmpeg -ss 0 -t 8 -i result.mp4 -s 600*400 -r 15 result.gif
```

需要设定视频截取时间及 GIF 图像大小。Python 也可以操作，但这里就不写了。有兴趣期待后面的文章吧。 **哟吼，有音乐了。不错吧！接下来，来多个视频。**

# 2\. \[多人版\]蚂蚁呀嘿

**接下来，我们来让百年前油画中的人物一起「蚂蚁呀嘿」吧~** PaddleGAN 施魔法前： ![](https://img-blog.csdnimg.cn/img_convert/6054c0614d1777c76a09f6e1a4e0ef32.png) PaddleGAN 施魔法后： ![](https://img-blog.csdnimg.cn/img_convert/ff5e963d24d9fa08d32097720b64002b.gif)

## 2.1 流程

整体流程分为三步：

1.  将照片中的多人脸使用人脸检测模型 S3FD 框出并抠出
2.  对抠出的人脸用 First Order Motion 进行脸部表情迁移
3.  将迁移好的人脸放回对应的原位置

**注意，由于人脸检测后，需要确定位置将人脸框出来并抠出，如果人脸太近，会框到除了其他的脸，导致效果较差，如下图** ![image.png](https://img-blog.csdnimg.cn/img_convert/231beac6eca6716567417f2ffdd28564.png) **所以尽量选取人脸间距较大的照片，同时，框的大小需要根据照片中人脸间距情况进行调节（参数--ratio）**

## 2.2 下载 PaddleGAN

```python
# 从github上克隆PaddleGAN代码
# git clone https://github.com/PaddlePaddle/PaddleGAN
git clone https://gitee.com/paddlepaddle/PaddleGAN.git
```

很显然，上面一步是可以跳过了。第一个单人版，就需要环境。我们已经弄好。 可是接下来的步骤就不能省略了，必须执行哦！

```python
cd PaddleGAN
git checkout develop
```

接下来的命令也是，如果安装过，则不用执行。不过对于不确定的小白来说，也是可以再执行一遍，也是没问题的。

```python
# 安装所需安装包
pip install -r requirements.txt
pip install imageio-ffmpeg
cd applications/
```

## 2.3 执行命令

大家可以上传自己准备的视频和图片，并在如下命令中的 source\_image 参数和 driving\_video 参数分别换成自己的图片和视频路径，然后运行如下命令，就可以完成动作表情迁移，程序运行成功后，会在 ouput 文件夹生成名为 result.mp4 的视频文件，该文件即为动作迁移后的视频。 同时，根据自己上传的照片中人脸的间距，本项目中提供了原始图片和驱动视频供展示使用。具体的各参数使用说明如下：

*   driving\_video：驱动视频，视频中人物的表情动作作为待迁移的对象
*   source\_image：原始图片，视频中人物的表情动作将迁移到该原始图片中的人物上
*   relative：指示程序中使用视频和图片中人物关键点的相对坐标还是绝对坐标，建议使用相对坐标，若使用绝对坐标，会导致迁移后人物扭曲变形
*   adapt\_scale： 根据关键点凸包自适应运动尺度
*   ratio：将框出来的人脸贴回原图时的区域占宽高的比例，默认为 0.4，范围为【0.4，0.5】

```python
export PYTHONPATH=$PYTHONPATH:/Users/apple/Desktop/GitHub/Test/PaddleGAN && python -u tools/first-order-demo.py  --driving_video ../../aiyc_work/fullbody.MP4  --source_image ../../aiyc_work/油画3.jpg --ratio 0.4 --relative --adapt_scale 
```

对于如何加音频，上面已经写到了，这里就不提了。 上效果： ![油画.mp4](https://img-blog.csdnimg.cn/img_convert/7f2f55e32159afeaa752aaa4983cc03b.png) 我为我的办公自动化系列创建了一个知识星球，目的在于给那些自学或者想要我答疑的小伙伴创建的，因为号主也需要恰饭，但又想不能太贵。 所以就设置了：50元一年的，希望小伙伴多多支持一下。「50元还不全部是我的，有一部分是知识星球的钱，害......所以如果你想加入，我还是推荐先加我微信：Jiabcdefh，然后转账给我，我拉你进去。如果觉得麻烦，那就直接扫码吧，希望我们在知识星球相见！」 **用最便宜的价钱，学最优质的内容，悦创等你！** ![image.png](https://img-blog.csdnimg.cn/img_convert/985c8a41c55a95a592ff4abcff465fdf.png)