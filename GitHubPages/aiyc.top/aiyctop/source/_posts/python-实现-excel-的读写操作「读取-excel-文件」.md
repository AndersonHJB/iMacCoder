---
title: Python 实现 Excel 的读写操作「读取 Excel 文件」
tags: []
id: '1431'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-07 12:57:32
---

你好，我是悦创。写文件已经搞定，接下来就要学习下 Excel 的读操作。 写入 Excel 的库是 xlwt ，对应 write ；读取 Excel 的库是 xlrd ，对应r ead ；xlrd 的安装命令：`pip install xlrd` 首先导入 xlrd，然后打开前面写好的 “虚假用户数据.xls”，代码如下：

```python
import xlrd

wb = xlrd.open_workbook('虚假用户数据.xls')
```

打开了文件之后，wb 代表当前文件。读取数据，需要指定具体的 sheet，有两种方式，分别是通过索引和名称，如下代码：

```python
sheets = wb.sheets()                     # 获取文件中全部的sheet，返回结构是list。
sheet = sheets[0]                        # 通过索引顺序获取。

sheet = wb.sheet_by_index(0)             # 直接通过索引顺序获取。

sheet = wb.sheet_by_name('第一个sheet')   # 通过名称获取。
```

此时获取到了 sheet 对象，然后从这里取出数据就可以。 sheet 的内容是二维表格，取数据全靠行数和列数，定位具体的格子，然后拿到格子里面的内容。 **如果我们要取出全部的内容咋办？** 获取 sheet 的总行数和列数，然后循环就行。 取出总行数和列数的代码如下：

```python
rows = sheet.nrows
cols = sheet.ncols
```

rows就是总行数，cols是总列数。有这两值，然后两层循环，取数据就行。 那我们需要把 Excel 的每一行数据提取出来，而且我们一行有四列数据。四列数据变化的是：**列数**，不变的是： **行数** —— 所以率先循环的就是 **行** 后循环的是 **列** 。 **Ps：第一层循环后会等待第二层循环全部循环完毕，后再继续循环外层循环「第一层」。** 如下代码：

```python
for row in range(rows):
    for col in range(cols):
        print(sheet.cell(row, col).value, end=' , ')
    print('\n')
```

**效果图【只截图头部】：** ![image.png](https://img-blog.csdnimg.cn/img_convert/b0e811f14830de31c50b6b41e2b06193.png) 读数据，指定某行某列，定位到具体方格，取出里面的值即可，代码是 sheet.cell(row,col).value 。 **总结方法代码「共三种」** **1、方法一：**

```python
import xlrd

wb = xlrd.open_workbook('虚假用户数据.xls')
sheet = wb.sheet_by_name('第一个 sheet')  # 通过名称获取。
rows = sheet.nrows  # 获取总行数
cols = sheet.ncols  # 或许总列数
for row in range(rows):
    for col in range(cols):
        print(sheet.cell(row, col).value, end=' , ')
    print('\n')
```

**2、方法二：**

```python
import xlrd

wb = xlrd.open_workbook('虚假用户数据.xls')
sheets = wb.sheets()  # wb.sheets() 得到的数据类型是列表
sheet = sheets[0]
rows = sheet.nrows  # 获取总行数
cols = sheet.ncols  # 或许总列数
# print(rows, cols)
for row in range(rows):
    for col in range(cols):
        print(sheet.cell(row, col).value, end=' , ')
    print('\n')
```

**2、方法二：**

```python
import xlrd

wb = xlrd.open_workbook('虚假用户数据.xls')
sheet = wb.sheet_by_index(0)
rows = sheet.nrows  # 获取总行数
cols = sheet.ncols  # 或许总列数
# print(rows, cols)
for row in range(rows):
    for col in range(cols):
        print(sheet.cell(row, col).value, end=' , ')
    print('\n')
```