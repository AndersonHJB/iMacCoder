---
title: 解决Python使用matplotlib绘图时出现的中文乱码问题
tags: []
id: '1897'
categories:
  - - 技术杂谈
date: 2021-09-15 12:57:17
---

## 前言

你好，我是悦创。 最近再写 Python 万能代码模板系列文章，公众号：AI悦创，首发。 然后，写到可视化部分的知识的，出现一些小问题。 Python 中使用 matplotlib 绘图时发现控制台报如下问题，可知是中文字体问题：

```python
runfile('E:/PycharmProjects/PythonScience/matplotlib/testPlot.py', wdir='E:/PycharmProjects/PythonScience/matplotlib')
F:\Anaconda3\lib\site-packages\matplotlib\backends\backend_agg.py:211: RuntimeWarning: Glyph 26102 missing from current font.
  font.set_text(s, 0.0, flags=flags)
F:\Anaconda3\lib\site-packages\matplotlib\backends\backend_agg.py:211: RuntimeWarning: Glyph 38388 missing from current font.
  font.set_text(s, 0.0, flags=flags)
```

## 解决方案一

只需设置下参数即可，设置代码如下：

```python
# 设置字体的属性
# plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False
```

### 例子

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.arange(1, 12)
y = x ** 2 + 4
plt.title("Matplotlib demo")
plt.xlabel("时间(分钟)")
plt.ylabel("金额($)")
plt.plot(x,y)
plt.show()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/bec63e44c4724c759317ec70630ad5fc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQUnmgqbliJs=,size_20,color_FFFFFF,t_70,g_se,x_16) 如果想阅读，Python 万能代码模板，请关注公众号：AI悦创，来获取。近期持续更新！

## 解决方法二

**原因：matplotlib 自带的字体库不支持中文** **解决办法：下载中文字体>放入 matplotlib 字体库路径>修改 matplotlibrc 文件** 仅此三步，不需要其他任何操作，不需要添加任何代码。

### 1\. 下载中文字体

网上常用的中文字体是 SimHei，提供三个下载地址，其他字体可自行搜索下载。

> https://github.com/StellarCN/scp\_zh/blob/master/fonts/SimHei.ttf http://www.xiazaiziti.com/210356.html https://www.wfonts.com/font/simhei

### 2\. 拷贝字体到 matplotlib 的字体库

1、查看 matplotlib 字体库路径，将 `SimHei.ttf` 文件放入其中 在当前 python 环境（所用 python 环境）下运行如下代码。

```python
import matplotlib

print(matplotlib.matplotlib_fname())   # 查找字体路径
```

输出如下：

```python
C:\Users\clela\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\mpl-data\matplotlibrc
```

在上述路径后，删除：matplotlibrc 添加 `/fonts/ttf`，即可得到 matplotlib 字体库的路径为：

```python
C:\Users\clela\AppData\Local\Programs\Python\Python38\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
```

将下载的 `SimHei.ttf` 文件放到字体库路径下即可。

### 3\. 修改 matplotlibrc 文件

```python
import matplotlib

print(matplotlib.matplotlib_fname())   # 查找字体路径
```

matplotlibrc 文件的路径即为上述代码的输出：

```python
C:\Users\clela\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\mpl-data\matplotlibrc
```

找到 `font.serif`，`font.sans-serif` 所在位置，如下如所示。在冒号后面加入 `SimHei` ，保存退出，大功告成。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/f46a93179295469e801ce60f85cc7510.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQUnmgqbliJs=,size_20,color_FFFFFF,t_70,g_se,x_16)

> 一般 matplotlib 会默认使用 "font.serif:" 后面的字体（排在第一位的），所以如果想换成其他字体，将其他字体名字放在 "font.serif:" 后面即可

**注：网上有的帖子讲需要删除这两行前面的“#”符号，在本人的测试中不需要删除，也不需要其他操作，只要按照上述流程操作即可解决中文显示乱码问题，good luck！如果真的解决不了，可关注留言。**

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/922caaecf7ca434b8636991ede15294c.png)