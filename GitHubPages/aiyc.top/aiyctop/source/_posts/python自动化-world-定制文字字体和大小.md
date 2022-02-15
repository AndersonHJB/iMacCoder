---
title: Python自动化 world 定制文字字体和大小
tags: []
id: '1615'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-03-28 09:55:19
---

# 导入定制所需库

上节课已经完成了使用 Python 创建一个 docx 文档，内容是朱自清的《背影》。 word 文档是有格式的，上次没有使用任何的格式，所以这节课来学习下，如何定制文字的字体和大小。 首先第一个，导入 docx 和样式类，如下：

```python
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
```

# 标题定制化大小和字体

然后新建 Document，以及添加一个标题，如下：

```python
document = Document()
document.styles['Normal'].font.name = u"宋体"
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')

title = document.add_heading(0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('背影')
run.font.name = u"宋体"
run.font.size = Pt(22)
run._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
run.font.bold = True
run.font.color.rgb = RGBColor(0,0,0)
```

对比以前的两行代码，这里的代码量就很多了，详细介绍下：

*   新建 document 后，给 style\['Normal'\] 设置整体的字体格式，第一行是英文字体，第二行是中文字体
*   从 title 的定义开始，title 是添加了一个空标题
*   title 第二行，设置居中对齐。默认是左对齐
*   然后设置 title，添加文字对象“背影”，对象保存到 run 参数
*   设置文字对象的字体，设置成宋体
*   字体大小是 22 磅，对应二号
*   为了安全起见，在设置一个中文的字体，也是宋体
*   然后字体加粗，为真
*   设置字体颜色，黑色

这段内容比较多，但是难度不大，字体的样式设置。

# 设置段落字体和大小

接下来就是段落的添加，内容都是添加一样的，就是要给每个段落的字体，设置宋体和 12 磅，以及前后的段落间距，如下代码：

```python
paragraphs = []
paragraphs.append(document.add_paragraph('文字太多，略'))
paragraphs.append(document.add_paragraph('文字太多，略'))
paragraphs.append(document.add_paragraph('文字太多，略'))
paragraphs.append(document.add_paragraph('文字太多，略'))
paragraphs.append(document.add_paragraph('文字太多，略'))
paragraphs.append(document.add_paragraph('文字太多，略'))
paragraphs.append(document.add_paragraph('文字太多，略'))
for para in paragraphs:
    para.space_after = Pt(5)
    para.space_before = Pt(5)
    for run in para.runs:
        run.font.name = u"宋体"
        run.font.size = Pt(12)
        run._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
```

这里代码用了循环，就是我们前面添加内容的对象，统一放到了列表 paragraphs 中，然后循环处理每个对象。 paragraphs 列表中的每个对象，都是一个段落 paragraph，段落里面有具体的文字 run。具体的代码解释如下：

*   循环取出每一个段落
*   设置段落的前后间距，都是5磅
*   然后取出段落的 runs，也就是文字，这个是列表，所以需要 for 循环
*   取出文字，设置英文宋体，中文宋体，以及文字大小12磅

完了，内容就是这么简单，循环的批量处理。

# 新增生成日期

编辑完内容，最后来加一个段落，这个段落比较特殊，内容是“此文档生成于xxxx年xx月xx日”，并且向右对齐，其中年月日是运行时的日子，字体大小 13 磅，略大一点，其余的没什么变化。 上代码：

```python
import datetime
paragraph = document.add_paragraph()
paragraph.space_after = Pt(5)
paragraph.space_before = Pt(5)
paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
paragraph.add_run("此文档生成于")

today = datetime.datetime.now()
today = today.strftime(" %Y{}%m{}%d{} ").format('年','月','日')
timerun = paragraph.add_run(today)
timerun.font.name = u"宋体"
timerun.font.size = Pt(13)
timerun._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
```

代码解释如下：

*   导入时间库，需要他生成时间
*   添加一个段落
*   段落前后 5 磅间距
*   段落设置右对齐
*   段落添加一段文字，内容是“此文档生成于”，这个字符串是一个 run
*   然后空格，接下来是当前时间对象，保存到 today 参数中
*   有了当前的时间对象，导出字符串。因为导出的字符串中不能有中文，所以中文采用 format 的形式进行二次拼接
*   然后将生成后的时间字符串，插入到段落中，这个字符串是一个新的 run
*   设置 run 的英文字体、中文字体、字体大小13磅

# 最终效果

全部操作完成，最后保存文件：

```python
document.save('背影-style.docx')
```

保存完毕，最后用办公软件，看下具体的文档效果，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/e95ef7a8498176fb760e6ebaf342db27.png) 生成的文件也在源码文件夹中，可以去查看下文字的字体类型和文字的大小磅数，以及最后的年月日是不是13磅