---
title: 实战！「Excel 合并」
tags: []
id: '1439'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-08 22:37:58
---

你好，我是悦创。今天是咱们来研究 Excel 的拆分和合并。 工作中，如果我们需要同时操作多个 Excel 文件，就是一件非常耗时的事情了。 在工作场景中，需要同时操作多个 Excel 的情况主要有 2 种：批量合并和批量拆分。我来带你看 2 个场景。

*   **批量合并。**
    *   **问题：**假设你需要对某些工作内容进行问卷调查，这时你用 Excel 做了调查问卷模版。
    *   **操作：**我想你会这样做：先把 Excel 通过工作群分发给所有员工，再把群里收集到的反馈附件汇总成一个文件。
    *   我画个流程图你会更清晰：

![](https://img-blog.csdnimg.cn/img_convert/5d3deff5e21a803a04096efb8adc1e29.png) - **批量拆分。**

*   **问题：** 假设你是公司的财务人员，你需要使用 Excel 对员工工资进行核算，之后再打印出来。但是公司要求员工薪水保密，所以每个员工的工资需要拆分成一个独立的文件，最后还需要打印出来。

无论是合并，还是拆分，我们都面临着一个困境：没有现成的软件可以实现多个 Excel 文件的合并和拆分操作，所以你只好对每一个 Excel 文件都进行“**打开 - 复制粘贴 - 保存**”的工作。 很多人在面对这样的工作需求时，都**忍不住立马去做，却很少停下来分析问题。其实，这三步是很简单的工作，不过也是无意义的重复工作，既浪费了时间，又没有真正产生价值。**

## 问题

刚刚我们说到批量处理，其实也就是逐一处理多个文件。如果我们想要提升这类工作的效率，就可以先借助 Python 把每一次处理都自动化。之前我已经讲解了如何使用 Python 操作EXcel 了。

*   [Python 实现 Excel 的读写操作「写入Excel文件」](https://www.aiyc.top/1429.html)
    
*   [Python 实现 Excel 的读写操作「读取 Excel 文件」](https://www.aiyc.top/1431.html)
    

试想一下，如果能够使用 Python 替代全部的手工操作，大批量的文件就可以使用 Python 的循环功能自动化完成对每一个文件的自动处理工作了。 对于编程语言来说，文件合并的步骤可以分解为： 1、读取第一个文件，读取第二个文件； 2、将第一个文件的内容追加到第二个文件下方。 **但是这里有个问题，如果按如下写入 Excel 文件有什么问题？**

```python
import xlwt

dst_file = 'Tester.xls'

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果")

# 写入内容,假设取出的内容是value
xlsheet.write(0, 0, value)

# 保存文件
workbook.save(dst_file)
```

在指出问题前，我先再次解析一下：写入文件的时候，我们使用了一个叫做 write 的函数。它的前两个参数代表的写入位置，分别是指定写入的行和列坐标。 无需多言，这个写入位置非常重要。**如果按照上面的代码方式写入，也就是前两个参数均指定为 0，就会覆盖这个 Excel 文件中的现有内容了。** **所以，你如果想完成合并操作的话，就要实现对现有 Excel 内容进行追加写入。通常我们会先获取现有的内容一共有多少行、多少列，然后向后移动一个位置，再进行写入。**

## 如何把 Excel 合并？

我们还是用前面提到的做调查问卷模板的场景，来具体讲一讲怎么实现 Excel 的合并。这里，我们就要用到一个重要功能了：**循环功能。** 循环功能的核心代码是：

```python
from pathlib import Path, PurePath

# 指定要合并excel的路径
src_path = '/Users/aiyuechuang/Desktop/文章1/调查问卷'

# 取得该目录下所有的xls格式文件
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xls')]
# 我可以依次获取 src_path 变量指向的路径下所有的文件。
# 避免这个目录里的文件类型过多，使用一个 if 语句用于条件判断，只提取 .xls 结尾的文件。
```

现在，用 Excel 实现调查问卷自动化的主要功能已经都实现了。接下来，我们看看怎样实现整个工作过程。我把它们的工作流程定义为三个步骤： 1、找到整个工作过程当中重复操作的部分； 2、将重复操作的部分需要哪些手工操作找出来，使用 Python 编写程序代替手工操作的部分； 3、对重复的部分，使用循环语句进行批量处理。 我来模拟这样的场景：当我们回收了调查问卷之后，每份问卷的格式是完全相同的，刚好可以利用上面提到的循环功能处理每份问卷。而问卷的选项则是我们需要提取出来用于汇总的，所以我们要使用 Python 实现读取 Excel 调查问卷的功能，最后再写入到一个新的 Excel 中。

```python
import xlrd
import xlwt
from pathlib import Path, PurePath
# 导入excel和文件操作库

# 指定要合并excel的路径
src_path = '/Users/aiyuechuang/Desktop/文章1/调查问卷'
# 指定合并完成的路径
dst_file = '/Users/aiyuechuang/Desktop/文章1/result/结果.xlsx'

# 取得该目录下所有的xlsx格式文件
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]

# 准备一个列表存放读取结果
content = []

# 对每一个文件进行重复处理
for file in files:
    # 用文件名作为每个用户的标识
    username = file.stem
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    # 取得每一项的结果
    answer1 = table.cell_value(rowx=4, colx=4)
    answer2 = table.cell_value(rowx=10, colx=4)
    temp = f'{username},{answer1},{answer2}'
    # 合并为一行先存储起来
    content.append(temp.split(','))
    print(temp)
    # 输出
    # 韩梅梅,D,B
    # 李雷,D,C

# 准备写入文件的表头
table_header = ['员工姓名', '第一题', '第二题']

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果")

# 写入表头
row = 0
col = 0
for cell_header in table_header:
    xlsheet.write(row, col, cell_header)
    col += 1 

# 向下移动一行
row += 1
# 取出每一行内容
for line in content:
    col = 0
    # 取出每个单元格内容
    for cell in line:
        # 写入内容
        xlsheet.write(row, col, cell)
        # 向右移动一个单元格
        col += 1
    # 向下移动一行
    row += 1
# 保存最终结果
workbook.save(dst_file)
```

在这段代码中，Excel 的读取和写入操作、for 循环操作都派上了用场，它的整个工作过程就像我画的时序图一样：**先打开用来汇总的 Excel 文件，依次对多个调查问卷进行读取，最后逐行写入到新建立的汇总文件中。** 下一篇文章带你学，如何把 Excel 拆分。