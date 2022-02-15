---
title: Python 追加 Excel 数据
tags: []
id: '1449'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-10 20:57:18
---

你好，我是悦创。这篇文章，我再来分享一个库：xlutils。 我们的目标：往“**虚假用户数据.xls**”里面，追加额外的 50 条用户数据，就是标题+数据，达到 150 条。 **那我的思路是什么呢？**

*   xlrd 是读取 Excel 文件的库
*   xlwt 是写入 Excel 的库

如果使用以上两个库，可以一边读取，一边写入新文件。 不过在此，有另一个方便使用的库，库名是 xlutils，安装命令：`pip install xlutils`。 安装好之后，开始写代码，完成追加 50 条数据的需求。

## 代码编写

（1）导入所需的库，分别是 xlrd 和 xlutils

```python
import xlrd
from xlutils.copy import copy
```

（2）使用 xlrd 打开文件，然后 xlutils 赋值打开后的 workbook，如下代码：

```python
wb = xlrd.open_workbook('虚假用户数据.xls',formatting_info=True)
xwb = copy(wb)
```

wb 对象是 workbook ，xwb 也是 workbook ，但是后者可以写操作，前者不可以。 （3）有了 workbook 之后，就开始指定 sheet，并获取这个 sheet 的总行数。

```python
sheet = xwb.get_sheet('第一个sheet')
rows = sheet.get_rows()
len(rows) # 输出100
```

指定名称为“第一个sheet”的 sheet ，然后获取全部的行，并输出总量，就得到了 sheet 中有 100 行。 （4）有了具体的行数，然后保证原有数据不变动的情况下，从第 101 行写数据。101 行的索引是 100，索引循环的起始数值是 100。

```python
import faker

fake = faker.Faker()
for i in range(len(rows), 150):
    sheet.write(i, 0, fake.first_name() + ' ' + fake.last_name())
    sheet.write(i, 1, fake.address())
    sheet.write(i, 2, fake.phone_number())
    sheet.write(i, 3, fake.city())
```

range 函数，从 len(rows) 开始，到 150-1结束，共 50 条。 faker 库是制造虚假数据的，这个在前面写数据有用过，循环写入了 50 条。 （5）最后保存就可以了

```python
xwb.save('虚假用户数据.xls')
```

使用 xwb，也就是操作之后的 workbook 对象，直接保存原来的文件名就可以了。

## Office 办公软件查看数据结果

最后使用 Excel 软件打开这个 xls 文件，查看数据有多少行，如下代码： ![image.png](https://img-blog.csdnimg.cn/img_convert/0ebded265a8e24232b8dbaef00ab4a59.png) 总共 150 行，原有数据 100 行，加上新写入的 50 行，数据没问题。 将以上的代码，合并起来多次运行，“**虚假用户数据.xls**” 的数据量会逐步增加，运行一次增加 50 行。 xlutils 是 **xlrd+xlwt** 的操作合集，但又不等于他们相加。库不一样，完成的操作不一样，所需的场景也不同，不同的需求用不同的库。