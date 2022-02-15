---
title: 02-寻找 VIP（上）-有福利|长期招收编程一对一
tags: []
id: '2152'
categories:
  - - Python 办公自动化
date: 2022-01-21 15:32:42
---

你好，我是悦创。 公众号原文：[https://mp.weixin.qq.com/s/iczDcPe22EoqzG0DjAeqSw](https://mp.weixin.qq.com/s/iczDcPe22EoqzG0DjAeqSw) 上一篇文章，距离这篇文章有点遥远呀，主要是这几个事情。注意看噢，没准就有你需要的。

1.  因为最近一对一学员有些多，所以公众号没有时间排版，这篇文章其实早已写完。
2.  在给我的一对一学员写文章，些什么文章？——**Python 基础入门文章**，这个系列文章我预估 28 篇，后期会考虑继续写进阶的 Python 或者结合现有的资源**免费**让大家看。对！免费，加我微信：Jiabcdefh，就可以免费阅读。（如果微信加不了，通过微信公众号：AI悦创，加我也可以噢！）

下图是文章编写进度（你们可以提前加我微信，我拉你进群。预期 ２月16日正式上线）： ![在这里插入图片描述](https://img-blog.csdnimg.cn/84793115911243288bd2f28077bc24cd.png)

3.  第三点，就是整理资源。和发布在知识星球中。知识星球进去要交钱噢，主要是为了赚点钱吧。加入星球后，后期全部课程资源免费获取。（具体啥资源不言而喻）

> PS：关注公众号：AI悦创，并且转发本文章：优惠价 60元（原件 365元）

# 1\. 导语

Excel 是 Windows 下最流行的电子表格处理工具，在大部分公司的办公过程中，它都扮演着举足轻重的作用。年度预算、财务报表、业务订单等等，大量的商业场景中都会有 Excel 的身影。 随着公司业务的不断开展，数据的不断累积，大量的数据处理也基于 Excel 进行。 Excel 本身支持用户通过菜单点选，进行数据处理工作。但设想这样的场景：

*   从几千行数据中挑选特殊的某些行，根据要求进行修改；
*   或者在不同表格之间进行拷贝粘贴。当由人力长期进行这样的操作时，是十分枯燥，而且极易出错的。

如我们在本课程开篇所说，对于繁琐、重复的劳动，我们可以借助编程语言来驱使计算机完成。 本篇我们着重学习使用 Python 对 Excel 文件进行读取的方法。 课程主要围绕 openpyxl 包展开描述，它可以处理最新的 Excel 文件格式（xlsx，Excel 2007及其之后的版本）。而对于老版本的 Excel 文件（xls），需要借助 xlrd、xlwt、xlutils 包，我们在后面的关卡再做描述。

# 2\. 知识结构

![image.png](https://img-blog.csdnimg.cn/img_convert/61496fefd9c3f9fb3a5923a93a2e21a0.png)

# 3\. 课程内容

## 3.1 基本概念

在进行具体的 Excel 文件处理之前，我们对 Excel 表格中的一些概念进行定义，以便在将来的描述中没有歧义。

## 3.2 工作簿

Excel 文件被称为工作簿，每个工作簿中，包含一个或者多个工作表。

## 3.3 工作表

包含在工作簿中，是数据单元存储的地方。当一个工作簿中有多张工作表时，可以在工作表底部看到不同表的名字，并通过点选完成表的切换： ![image.png](https://img-blog.csdnimg.cn/img_convert/88b63f910d9a896ee173432d31a3419c.png) 如上图这样，当选择的表是 **2009-04** 时，这张表称为活动表。

## 3.4 单元格

工作表，由行（索引从 1 开始的数字）跟列（索引从 A 开始的字母）组成，某个行与列的交叉处，就是一个单元格。在单元格中，可以放置文本或者数字内容。

# 4\. 场景描述

在本篇中，我们将尝试读取一份电商的销售数据。这份数据在上面定义工作表时你已经看到过。 数据存储在一个 Excel 文件中，其中由若干名称类似 `2009-01` 的工作表组成。每张工作表放置的是某个月份的用户交易情况。数据中的每一行，分别是一次用户消费的记录，在四个单元格中分别记录了这次消费的订单 ID、用户 ID、下单时间和交易额。 我们先尝试使用 Python 对文件中的内容进行读取。

# 5\. Excel读取

销售数据的 Excel 文件放置在 `relayfood.xlsx` 中，我们使用 Python 的 openpyxl 模块来打开这个文件：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')
print(type(wb))

# <class 'openpyxl.workbook.workbook.Workbook'>
```

这段代码，使用 openpyxl 模块的 `load_workbook()` 函数对 Excel 文件进行打开操作。 在代码的最后一行，输出了这个操作结果的类型，它是一个 `openpyxl.workbook.workbook.Workbook` 对象。文件内容并没有立刻读取出来，这步操作类似普通文件处理中的 `open()` 函数，在这之后，Python就可以通过操作 wb 变量来读取文件了。

## 5.1 读取工作表信息

在获取一个工作簿时，我们经常会关心这样的问题：**当前工作簿中都有哪些工作表？**通过 Python 代码，可以方便的完成这个操作：

```python
# 获取工作簿中所有的工作表名
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')
# print(type(wb))
print(wb.sheetnames)

# ['2009-01', '2009-02', '2009-03', '2009-04', '2009-05', '2009-06', '2009-07', '2009-08', '2009-09', '2009-10', '2009-11', '2009-12', '2010-01', '2010-02']
```

示例代码很简单，通过 Workbook 对象的 sheetnames 属性，我们可以直接获取一个列表，列表中的每个元素是工作簿中每个工作表的名字。

## 5.2 读取单元格内容

使用程序读取单元格内容，首先要定位到我们要访问的单元格，这个定位过程跟使用鼠标点选其实没有太大差别。 回忆一下我们通过鼠标选择某个单元格需要进行的操作：

1.  选择某个工作表。
2.  找到单元格所在的行跟列，点选。

程序实现使用的也是这两个步骤，比如我们希望定位如下截图中的单元格： ![image.png](https://img-blog.csdnimg.cn/img_convert/f8c8df7633277a569173910d855735d6.png) 这是 `2009-04` 这个工作表中第 11 行第 B 列的单元格。

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')
sheet = wb['2009-04']
print(type(sheet))
print(sheet['B11'])
print(sheet['B11'].value)
```

以上代码，先通过 openpyxl 的 `load_workbook()` 函数读取工作簿，并赋值给变量 wb，然后通过`wb['2009-04']` 指定到工作表 `2009-04`，得到工作表（Worksheet）对象，并赋值给变量 sheet。 最后通过 `sheet['B11'].value` 就获取到了单元格的值。这里方括号中的 `'B11'` 便表示要获取的值是第 B 列第 11 行的内容。请注意 Excel 定位单元格的时候，是先给出字母表示的列索引，再给出数字表示的行索引。这与我们 Python 其它内容中经常使用的先行后列的定位方式不太一样。 当然，若要代码更简洁，这个实现还可以简化成：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')
print(wb['2009-04']['B11'].value)
```

## 5.3 使用数字方式访问行列

![image.png](https://img-blog.csdnimg.cn/img_convert/01da0c25c03c59073373a69913bd4d9b.png) 在对列进行索引的时候，Excel 默认使用字母，当列数非常多时，会出现 AA、AB 这样两个字母甚至更多的三个字母组成的列索引。比起用数字来标识列编号，用字母的方式显得麻烦很多。 openpyxl 也为我们提供了使用数字来索引列的方法。比如可以通过下面的方式读取第 11 行第 2 列（B列）的内容：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-04']

print(sheet.cell(row=11, column=2))
print(sheet.cell(row=11, column=2).value)
```

通过 `sheet.cell(row=11, column=2)` 这样的方式，我们可以获取指向某个单元的 Cell 类对象。获取对象时指定的参数 row 和 column 就分别指定了单元格的行和列编号。 编号都使用数字，另外，你需要格外注意，这里的数字编号是从 1 开始的，这与 Python 列表、元组等数据结构中元素从 0 开始编号完全不同，老师提醒你一定要辨认清楚。在 sheet 中，当我们要访问第 11 行的时候，指定的 row 就是 11 而不是 10。 有了数字对行列进行索引的能力，我们要使用循环读取一定范围的单元格时，就方便多了。 请补全下面代码，尝试打印 `2009-04` 这个工作表中，第 10 行，第 2 到第 4 列的元素值：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-04']

# TODO，使用 for 循环打印 2009-04 这个工作表中，第 10 行，第2到第4列的元素值
```

看下老师的答案：

```python
# TODO，使用for循环打印2009-04这个工作表中，第10行，第2到第4列的元素值
for i in range(2, 5):
    print(sheet.cell(row=10, column=i).value)
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

## 5.4 Cell 的其它属性

我们在前面读取单元格的值时，访问的都是 Cell 对象的 value 属性。除了 value，Cell 对象还有 row、column、coordinate 这几个常用的属性，再看一段样例代码：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

print('row is ', wb['2009-04']['B11'].row)
print('column is ', wb['2009-04']['B11'].column)
print('coordinate is ',  wb['2009-04']['B11'].coordinate)
```

代码的执行结果非常直观

*   row 属性表示的就是单元格的行编号（数字）
*   column 属性标识的是单元格的列编号（数字）
*   而 coordinate 表示的是类似 B11 这样的，由字母和数字组成的单元格位置坐标。

## 5.5 表的尺寸

在 Python 的列表中，我们时常会使用 `len()` 获取列表的元素个数，这在遍历所有元素、计算列表尺寸等操作的时候经常会用到。 通过 openpyxl，也可以获取工作表的尺寸（最大列数和行数）。

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-04']

print('行数：', sheet.max_row)
print('列数：', sheet.max_column)
```

以上代码执行的结果中，可以看到，通过 Worksheet 类的对象 sheet 的 `max_row` 和 `max_column` 属性，就可以获取这张工作表的行数和列数。 有了这个方法，我们可以使用循环遍历的方式查询表中的所有单元格了。请在以下代码框中，使用 for 循环实现遍历 `2009-04` 这张工作表的每个单元格，并打印内容的功能。

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-04']

# TODO，遍历 2009-04 这张工作表的每个单元格，并打印内容
```

看一下老师的答案：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-04']

rows_num = sheet.max_row
columns_num = sheet.max_column

for i in range(1, rows_num+1):
    for j in range(1, columns_num+1):
        print(sheet.cell(row=i, column=j).value, end=' ')
    print()

# 副本
# 先 row 后 column
for row in range(1, rows_num+1):
    for column in range(1, columns_num + 1):
        print(sheet.cell(row=row, column=column).value, end=' ')
    print()
```

这段代码使用两层循环分别对行和列进行遍历，每遍历到一个单元格位置，就通过打印 `sheet.cell(row=i, column=j).value` 的值将单元格内容输出。这里的 i 和 j 就分别表明了当前的行编号跟列编号。 需要留意的是，由于 openpyxl 的行列编号都是从 1 开始（而不是从 0 开始），所以对于行的 for 循环 `for i in range(1, rows_num+1)`，需要从 1 开始，而最大值是 `rows_num`，就是之前通过`sheet.max_row` 获取到的最大的行编号；对于列的处理，也遵循同样的规则方法。

## 5.6 获取行列切片

获取工作表中某个区域的值，也是经常要进行的操作。比如获取 `2009-02` 工作表中，下图红色区域的内容： ![image.png](https://img-blog.csdnimg.cn/img_convert/ddca9b73e2e2d3ac301036a3f10bf216.png) 我们可以用类似操作列表切片的方式定义这块要切出来的区域。 回忆一下 Python 中获取列表切片的方法：列表元素`[开始坐标:结束坐标]`。这样的操作之后，就获取到了从**开始坐标**到**结束坐标**（不包含结束坐标）这个切片中的内容。 定义 Worksheet 中的切片，也是类似的方法：`Worksheet变量[左上角坐标:右下角坐标]`。因为我们这里要取的是一个矩形区域，定义起止位置便以矩形区域的角上单元格位置为标准。 上图红色的矩形区域，左上角的坐标是 B3，你仔细观察一下右下角的坐标是多少？补全以下代码获取这个区域吧：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-02']

# TODO，替换下面代码中的xxx，获取红色矩形区域的内容。
print(sheet['B3':xxx])
```

这是老师的答案：

```python
# TODO，替换下面代码中的xxx，获取红色矩形区域的内容。
print(sheet['B3':'D7'])
```

右下角的坐标是 D7，因此通过 `sheet['B3':'D7']` 获取到了图示的矩形区。代码通过 print 将这个Worksheet 变量被切片之后的结果进行打印。 可以看到结果是由 5 个元组（用圆括号包含的内容）元素组成，每个元组其实就是切片中的一行。而在元组中，每个元素其实就对应一个单元格 Cell。比如第一个元素 `<Cell '2009-02'.B3>`，它就是存储着 B3 这个单元格内容的 Cell。 之前已经提到过，如果要读取一个 Cell 的具体值，可以使用它的 value 属性。于是，老师可以通过以下代码将这个红色区域中的内容打印出来：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-02']

for row in sheet['B3':'D7']:
    for cell in row:
        print(cell.value, end=' ')
    print()
```

这里也是使用两层循环打印每个元素的内容。第一层循环 `for row in sheet['B3':'D7']`，会逐个遍历 `sheet['B3':'D7']` 中的每个元素，每个元素就是一行，这行内容放在一个元组类型的变量 row 里。 在内层循环中对 row 进行遍历，得到的每个元素变量 cell 就是类似前面看到的 `<Cell '2009-02'.B3>` 这样的 Cell 对象。 在循环内通过打印 cell 的 value 属性，就输出了单元格的内容。 当我们需要读出工作表完整的某一行或者某一列的时候，可以使用 Worksheet 的 rows 或 columns 属性。

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

比如，通过以下代码，获取第 2 行：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-02']
print(list(sheet.rows)[1])

# 补充
for r in sheet.rows:
    print(r)

# for c in sheet.columns:
#   print(c)
```

请留意 `list(sheet.rows)[1]` 这行代码，它包含了两步操作：

1.  将 `sheet.rows` 转换成列表（list）类型。
2.  通过 `[1]` 获取了列表的第 2 个元素（就是第 2 行）。

通过 `sheet.rows`，获取到一个工作表的所有行。 这里之所以进行类型转换操作，因为 `sheet.rows` 不是一个可以直接索引的类型，需要将它转换成列表，才能在这之后通过方括号加整数的形式取到具体指定的某一行。 而在第二步中，由于结果已经转换成了列表类型，元素的编号又遵守从 0 开始的规则了，所以要取第 2 行时，这里用的坐标索引是 `[1]`。 能取出某行或者列，通过循环获取每个 cell 并打印内容自然就不难了。尝试补全以下代码，打印 `2009-02` 这个工作表 D 列（第 4 列）的内容。

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-02']

# TODO, 打印第4列的所有单元格内容
```

以下是老师的答案供你参考：

```python
# TODO, 打印第4列的所有单元格内容
column = list(sheet.columns)[3]
for cell in column:
    print(cell.value)
```

跟 rows 属性类似的使用方法，通过 columns 属性获取某列并打印其中的单元格内容。

## 5.7 数据类型

Excel 文件单元格中的内容会有不同的类型，字符串、数字等。通过 openpyxl 读取这些内容的时候，读取到的变量在 Python 中也会拥有相应的类型。在进行计算的时候，数字可以做算术运算，而字符串不可以。类似这样的特点需要我们在处理 Excel 文件的内容时多加注意。 使用以下代码查看一下 `2009-02` 这个工作表中，第 2 行的每个单元格的内容，以及这个内容被读取到 Python 中之后它的类型：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-02']
for cell in list(sheet.rows)[1]:
    print('值：', cell.value)
    print('类型：', type(cell.value))
```

从输出结果中可以知道，第 1、2、4 三个元素都是整数类型。第 3 个元素是表示时间的 datetime 类型。 关于 datetime 类型变量的操作，有几个常用的属性可以让我们方便的获取时间中的年、月、日等信息，这里列举几个常用的以方便你查询：

**属性**

**作用**

year

获取年

month

获取月

day

获取日

比如我们获取 `2009-02` 工作表中，所有第 3 列时间中的月和日，可以用如下方式：

```python
import openpyxl
wb = openpyxl.load_workbook('relayfood.xlsx')

sheet = wb['2009-02']
for cell in list(sheet.columns)[2]:
    if cell.row > 1:
        print('{}月{}日'.format(cell.value.month, cell.value.day))
```

在这段代码中，通过 `for cell in list(sheet.columns)[2]` 遍历工作表的第3列，由于工作表的第 1行是表头，不包含年份信息，所以在循环的处理过程中，通过 `if cell.row > 1` 判断当行号大于 1 时，才打印月和日的信息。 在输出月日时，就直接读取了 datetime 类型的 month 和 day 属性。

# 4\. 寻找 VIP

那对于寻找 VIP 你会做吗？你可以先试一试。我们下一篇文章继续，加油！

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/3f2045d1f0e74cec8dd9cdc874221482.png)