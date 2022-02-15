---
title: openpyxl 追加 Excel 数据
tags: []
id: '1494'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-22 00:06:44
---

xlsxwriter 只能创建新的文件，不能对文件进行数据的追加和读取操作。 需要追加和读取 xlsx 文件，就需要用到 openpyxl 这个库了。安装命令：`pip install openpyxl`。 使用 openpyxl 完成这面这个需求：

*   读取上面创建好的 xlsxwriter 插入数据和折线图.xlsx 文件，复制一份，保存到 poenpyxl 插入数据和折线图\[copy xlsxwriter\].xlsx 复制的文件中
*   sheet1 保持和源文件的 sheet1 一致，折线图不画复制的文件中
*   创建一个 sheet2，sheet2 的数据从 sheet1 中拷贝过来
*   随机的增加 1 年的随机数据，也就是 2020年1月至12月的日期，数据1 和数据2 的 12 个数据随机生成
*   在 sheet2 中画一个折线图，统计数据1 和数据2

需求有四个，有难有易。

## 拷贝文件

#### 第一个是拷贝文件和 sheet1

其实拷贝了文件，自然就包含sheet1，最简单了，如下代码：

```python
import openpyxl
filename = 'xlsxwriter插入数据和折线图.xlsx'
wb = openpyxl.load_workbook(filename)
wb.save('poenpyxl插入数据和折线图[copy xlsxwriter].xlsx')
```

这样就得到了源文件和 sheet1 的复制品。

## 拷贝 sheet 内容

#### 第二个需求，拷贝sheet1，做成sheet2

也简单，如下代码：

```python
import openpyxl
filename = 'xlsxwriter插入数据和折线图.xlsx'
wb = openpyxl.load_workbook(filename)

sheet1 = wb['sheet1']
sheet2 = wb.copy_worksheet(sheet1)
sheet2.title = "sheet2"

wb.save('poenpyxl插入数据和折线图[copy xlsxwriter].xlsx')
```

获取 sheet1，复制一个给 sheet2 参数，然后改下 sheet2 的标题 title，这个 title 就是文件的 sheet2 的名字。

## 追加数据内容

#### 第三个需求，sheet2 中，数据1 和数据2 追加一年的数据，数据可以随意生成

貌似简单，但是年份时间不好计算，并且现在只有 2019 年的。如果之前数据是 2018 年，则追加一年，应该是 2019 年，所以要读取时间和月份追加。 这里的难点就是时间字符串的读取，以及字符串转时间，以及时间的相加。 如下实现代码：

```python
import openpyxl, random, datetime
from dateutil.relativedelta import relativedelta
filename = 'xlsxwriter插入数据和折线图.xlsx'
wb = openpyxl.load_workbook(filename)

sheet1 = wb['sheet1']
sheet2 = wb.copy_worksheet(sheet1)
sheet2.title = "sheet2"

rows = sheet2.max_row # 读取最后一行
prev_date_str = sheet2.cell(row=rows,column=1).value # 取出时间的字符串
prev_date = datetime.datetime.strptime(prev_date_str, "%Y-%m") # 时间字符串转时间对象
for i in range(1,13):
    tmp_date = prev_date + relativedelta(months=i) # 月份的计算，每次增加一个月，就得到了第二年的12个月
    tmp_num1 = random.randint(1,100)
    tmp_num2 = random.randint(1,100)
    sheet2.append([tmp_date.strftime("%Y-%m"), tmp_num1, tmp_num2])

wb.save('poenpyxl插入数据和折线图[copy xlsxwriter].xlsx')
```

实现思路：

*   读取出最后一行
*   取出时间字符串，然后转换成时间对象
*   一年 12 个月，循环 12 次，每次增加一个月，数值可以随机的生成，用 random 即可
*   数据的追加，是按每行，所以将【时间， 数据1， 数据2】通过 append 直接追加到数据最后即可

第三个需求搞定，下一个需求，sheet2 画折线图

## 使用 openpyxl 画图表

#### 第四个需求，在 sheet2 中对全部数据画折线图

这个难度不大，只要知道 openpyxl 的画图工具即可，如下代码：

```python
import openpyxl, random, datetime
from dateutil.relativedelta import relativedelta
filename = 'xlsxwriter插入数据和折线图.xlsx'
wb = openpyxl.load_workbook(filename)

sheet1 = wb['sheet1']
sheet2 = wb.copy_worksheet(sheet1)
sheet2.title = "sheet2"

rows = sheet2.max_row
prev_date_str = sheet2.cell(row=rows,column=1).value
prev_date = datetime.datetime.strptime(prev_date_str, "%Y-%m")
for i in range(1,13):
    tmp_date = prev_date + relativedelta(months=i)
    tmp_num1 = random.randint(1,100)
    tmp_num2 = random.randint(1,100)
    sheet2.append([tmp_date.strftime("%Y-%m"), tmp_num1, tmp_num2])

# 下面是画折线图的实现代码
from openpyxl.chart import Series,LineChart, Reference
chart = LineChart()  #图表对象
rows = sheet2.max_row

data1 = Reference(sheet2, min_col=2, min_row=1, max_col=2, max_row=rows) #涉及数据
title1 = sheet2.cell(row=1,column=2).value
seriesObj1 = Series(data1, title=title1)  #创建series对象

data2 = Reference(sheet2, min_col=3, min_row=1, max_col=3, max_row=rows) #涉及数据
title2 = sheet2.cell(row=1,column=3).value
seriesObj2 = Series(data2, title=title2)  #创建series对象

chart.append(seriesObj1)  #添加到chart中
chart.append(seriesObj2)  #添加到chart中

sheet2.add_chart(chart, "E3") #将图表添加到 sheet中


wb.save('poenpyxl插入数据和折线图[copy xlsxwriter].xlsx')
```

导入所需的画图工具，图表初始化，然后生成数据对象：

*   data1 的生成，因为索引从1 开始，所以标题是第一行第二列，数据是第二行第二列，一直到最后一行第二列
*   data2 的生成，因为索引从1开始，所以标题是第一行第三列，数据是第二行第三列，一直到第二行最后三列
*   将两个数据都放到图表内
*   然后图表的开始位置，设置成 E3，数据在 ABC，E 是空的，3 距离顶部有两格的位置

最后文件保存，大功告成。

## 查看最后的效果图

然后就是用 Office 打开 poenpyxl 插入数据和折线图 \[copy xlsxwriter\].xlsx，看下 sheet2 的样子，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/48b30e9c100a50af72a49b888ab9c2f4.png) 25 行数据，除了标题 24 行，刚好是 2019+2020 的 24 个月。折线图也一切正常。