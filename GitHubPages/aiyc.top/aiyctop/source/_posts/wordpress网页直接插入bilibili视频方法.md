---
title: Wordpress网页直接插入bilibili视频方法
tags: []
id: '1391'
categories:
  - - WordPress
date: 2021-01-28 10:21:57
---

## Wordpress 网页直接插入 bilibili 视频方法

先在视频页将鼠标移到分享按钮，复制下方的嵌入代码： ![在这里插入图片描述](https://images.gitbook.cn/2d9b7010-610e-11eb-bbd4-0996478cd7aa) 在文章编辑页，插入自定义 html 模块，如图： ![在这里插入图片描述](https://images.gitbook.cn/69620500-610e-11eb-bbd4-0996478cd7aa) ![在这里插入图片描述](https://images.gitbook.cn/815bb700-610e-11eb-81b4-8f1b543b0395) ![在这里插入图片描述](https://images.gitbook.cn/99ca4ae0-610e-11eb-a8aa-992450a0658d)

## 粘贴代码：

```markup
<iframe src="//player.bilibili.com/player.html?aid=839629572&bvid=BV1Y54y1m743&cid=237240818&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
```

再加上

```markup
style="width: 100%; height: 500px; max-width: 100%；align:center; padding:20px 0;"
```

到代码内，这里调整的是播放界面在网站中显示的大小，可以更改高度和宽度。

```markup
<iframe src="//player.bilibili.com/player.html?aid=839629572&bvid=BV1Y54y1m743&cid=237240818&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="width: 100%; height: 500px; max-width: 100%；align:center; padding:20px 0;"> </iframe>
```

添加以后的效果，如图： ![在这里插入图片描述](https://images.gitbook.cn/395dbba0-610f-11eb-842d-6da6a21c1104)