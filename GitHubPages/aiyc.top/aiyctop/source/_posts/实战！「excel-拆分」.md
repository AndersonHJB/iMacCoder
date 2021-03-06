---
title: 实战！「Excel 拆分」
tags: []
id: '1447'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-09 19:43:54
---

你好，我是悦创。上面一篇，我在 [Excel 合并](https://www.aiyc.top/1439.html) 中留下一个 Excel 拆分的实战问题，接下来我们来解决一下。 **我来重新分享一下题目：**

*   **批量拆分。**
*   **问题：**假设你是公司的财务人员，你需要使用 Excel 对员工工资进行核算，之后再打印出来。但是公司要求员工薪水保密，所以每个员工的工资需要拆分成一个独立的文件，最后还需要打印出来。

## 如何实现 Excel 拆分？

对于批量操作 Excel，还有一种情况是批量拆分。比如很多公司会用 Excel 记录和统计员工的薪水、记录货物信息、记录客户情况等数据。这些数据越来越多之后，文件会越来越大，打开文件和查找速度就会变得很慢，最后只好按照某些列进行 Excel 的拆分。 接下来，我就为你讲解一下如何进行 Excel 的批量拆分。让我们来看一个工资条的案例。 例如我在一个 Excel 中存放了工资信息，需要把第一行的表头和员工工资拆分成一个以员工名字命名的 Excel 文件。我来带你看下具体该怎么操作：

员工编号

姓名

出勤

工资

奖金

职务工资

全勤奖

实发工资

1001

韩梅梅

30

2000

1000

1000

100

4100

1002

李雷

30

2500

1000

500

100

4100

会发现，逐行读取可以使用循环功能批量操作，对每一行的内容处理，如果能使用 Python 进行自动化的话，一个 Excel 拆分的工作就全部能使用 Python 自动化实现了。所以，我打算设计一个 for 循环语句用于遍历所有的行，在 for 循环语句当中实现对每一行具体内容的处理。 我把文件拆分的关键代码写了出来，你可以参考一下：

```python
for line in range(1,employee_number):
    content = table.row_values(rowx=line, start_colx=0, end_colx=None)
    # 将表头和员工数量重新组成一个新的文件 
    new_content = []
    # 增加表头到要写入的内容中
    new_content.append(salary_header)
    # 增加员工工资到要写入的内容中
    new_content.append(content)
    # 调用自定义函数write_to_file()写入新的文件
    write_to_file(filename = content[1], cnt = new_content)
```

在这段代码的第一行，我使用了一个 range 函数，它会生成从 1 到员工总数的数字范围。你可能会问，为什么没有直接写出 Excel 中总员工的数量，而是使用 employee\_number 这样一个变量呢？ 这是因为，如果直接写出员工数量，一旦遇到员工入职或员工离职等情况，你就需要根据 Excel 中的行数重新编写 Python 代码，而我现在使用的方式是每次打开 Excel 文件，会自动统计员工的数量（即行数），这种编写代码的方式能够让你的程序有更好的扩展性，一般这种方式用于处理文件内容经常变动的情况。 文件的批量拆分也是通过循环来实现逐行处理的功能的，但是你需要注意拆分以后的要保存的文件名称不要重复，不然很容易导致 Excel 中只有最后一次循环写入的内容。