---
title: Python 实现 Excel 的读写操作「写入Excel文件」
tags: []
id: '1429'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-06 17:57:32
---

你好，我是悦创。前面给你讲解了什么是办公自动化，和环境安装，接下来我们来实际操作教学。 本文课，我们来熟悉下 Excel 的读和写操作。 首先来学习下，随机生成数据，写入一个 Excel 文件并保存，所使用到的库，是 xlwt，安装命令 `pip install xlwt` ，安装简单方便，无依赖，很快。 然后打开一个 jupyter 网页文件，第一个代码块，先导入 xlwt 这个库，并新建一个 WorkBook 对象。

```python
import xlwt
wb = xlwt.Workbook() # 新建一个workbook对象、工作簿
```

Excel 的每个文件，里面可以有很多 sheet，所以有了 workbook ，还需要新建 sheet

```python
sheet = wb.add_sheet('第一个sheet')
```

有了sheet，就可以开始写入数据了。sheet 里面是一个二维的表格，并且索引是从 0 开始的，所以第一步，先写头部数据。

```python
head_data = ['姓名', '地址', '手机号', '城市']
for head in head_data:
    sheet.write(0, head_data.index(head), head)
```

write 函数写入，分别是 x 行 x 列数据。

*   头部数据永远是第一行，所以第 0 行。
*   数据的列，则是当前数据所在列表的索引，直接使用 index 函数即可。

有了头部数据，现在就开始写入内容了，分别是：随机姓名、随机地址、随机号码、随机城市，数据的来源都是 faker 库，一个专门创建虚假数据用来测试的库，安装命令：`pip install faker`。 因为头部信息已经写好，所以接下来是从第1行开始写数据，每行四个数据，准备写 99 个用户数据，所以用循环，循环99次，代码如下：

```python
import faker
fake = faker.Faker()
for i in range(1,100):
    sheet.write(i,0,fake.first_name() + ' ' + fake.last_name())
    sheet.write(i,1,fake.address())
    sheet.write(i,2,fake.phone_number())
    sheet.write(i,3,fake.city())
```

数据全部写好了，但是此时数据保存在 wb 这个对象中，wb 就是最开始的 Workbook。 **但是 wb 中的数据，不是永久的；保存成文件，才是永久的。** Workbook 对象，提供 save 函数，可以直接保存成 xls 文件，代码如下：

```python
wb.save('虚假用户数据.xls')
```

然后找到文件，文件的位置就是这个 jupyter 文件的旁边。使用 office 或者 wps 打开这个 xls 文件，如下截图： ![image.png](https://img-blog.csdnimg.cn/img_convert/4545d33118b71170e2d05c0423153e64.png) 一共有100行，其中头部一行，虚假用户信息 99 行。 **完整代码：**

```python
import xlwt
import faker
wb = xlwt.Workbook()
sheet = wb.add_sheet("第一个 sheet")

head_data = ['姓名', '地址', '手机号', '城市']
for head in head_data:
    sheet.write(0, head_data.index(head), head)
# sheet.write(x行, y列, head)

fake = faker.Faker()
for i in range(1, 100):
    sheet.write(i, 0, fake.first_name() + ' ' + fake.last_name())
    sheet.write(i, 1, fake.address())
    sheet.write(i, 2, fake.phone_number())
    sheet.write(i, 3, fake.city())

wb.save('虚假用户数据.xls')
```