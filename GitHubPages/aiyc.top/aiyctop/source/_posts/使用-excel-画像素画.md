---
title: 使用 Excel 画像素画
tags: []
id: '1498'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-22 20:55:13
---

## Excel 和图片类似

Excel 文件，单元格支持编辑内容和设置背景色。 一张图片，都是由密密麻麻的像素组成，且每个像素都是一个 rgb 的颜色值。 那是否可以读取图片每个像素的颜色，填充到 Excel 中，就可以做到 Excel 中画图。 这么想，是可以的。理论上也是可行的，那接下来就开始写代码。

## 打开文件和图片

第一步，导入所需库，分别是 xlsxwriter 和图片的 Image 库。使用 xlsxwriter 的理由，是 xls 内容有限，图片的像素可是很多的，所以最好是使用 xlsx 格式。

```python
import xlsxwriter
from PIL import Image
```

导入之后，准备图片，并读取图片的宽高，以及像素对象：

```python
path = '1.png'
img = Image.open(path)
imgL = img.convert("P").convert("RGB")
pix = imgL.load()
w, h = imgL.size
```

![image.png](https://img-blog.csdnimg.cn/img_convert/09adec287daa1a8100137ce6c3807658.png) 使用 Image 读取图片对象，获取宽和高，以及 pix 这像素对象，通过 pix\[1,1 \]拿到具体的颜色 RGB 值，然后转换成 16 进制的颜色值，进行背景色的写入。

## 准备一个特殊函数

现在打开一个 xlsx 文件，文件名任意，如下代码：

```python
wb = xlsxwriter.Workbook('demo2.xlsx')
ws = wb.add_worksheet('sheet1')
```

然后找一个 RGB 转 16 进制的函数，因为 RGB 是 10 进制的，方式就是通过 hex 函数转换成 16 进制，然后加上 x 和 0，并全部大写，就可以了。如下函数：

```python
def RGB_to_Hex(tmp):
    rgb = list(tmp)
    strs = '#'
    for i in rgb:
        num = int(i)
        strs += str(hex(num))[-2:].replace('x','0').upper()
    return strs
```

**为什么一定要 16 进制？** 因为 sheet 中，写入背景色时，颜色必须是 16 进制才可以。

## 读取和写入

下面就是循环的逐个单元格设置背景色，且不需要写入内容。如下代码：

```python
for i in range(w):
    for j in range(h):
        rgb = pix[i,j]
        color = RGB_to_Hex(rgb)
        style = wb.add_format({'bg_color': '{}'.format(color)})
        ws.write(j,i,'',style)
        ws.set_row(j,1)
ws.set_column(0,w-1,0.5)

wb.close()
```

代码思路：

*   循环读取宽和高，读取到全部的分辨率节点
*   然后通过 pix 读取指定 x,y 的 RGB 值，再转换成 16 进制的内容
*   设置 style 样式，颜色值就是转换之后的 16 进制
*   然后写入单元格，内容是空，颜色背景是 style
*   循环内也要设置当前单元格的行高
*   循环外，统一设置单元格的宽度

这是单元格的主要代码，写完后，关闭 workbook 即可。

## 查看像素画

读取图片的全部宽高，然后描绘到 Excel 中完成了。最后用图片的形式展示下文件的样子，如下图【使用 WPS 软件查看】： ![image.png](https://img-blog.csdnimg.cn/img_convert/92165eb3467045d83760e1e62a3a4cf6.png)