---
title: 03-word 中插入图片和表格
tags: []
id: '1625'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-04-04 16:48:54
---

# 准备图片及代码

word 文档，支持文字、图片、表格等内容格式，前面掌握了文字和样式，这节课来学习下图片和表格的添加。 首先是图片。之前的代码是自动生成《背影》，纯文字信息。现在要保证原来文件不变的前提下，来给他添加一张图片。 图片是网上找的一个插图： ![image.png](https://img-blog.csdnimg.cn/img_convert/511dea82c3befdff5a24163f36f1051f.png) 插入图片的代码，如下：

```python
# 插入图片
images = '1.jpg'
p_img = document.add_paragraph()
p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_run_img = p_img.add_run()
img_obj = p_run_img.add_picture(images, width=Inches(5))
```

对图片的代码进行详细的介绍：

*   这里不事使用 document.add\_picture()，因为这个函数不能调居中对齐，默认左对齐
*   这里的做法是添加一个段落，然后居中对齐
*   然后段落中添加一个 run【 run 里面可以文字，也可以是图片】
*   run 中添加进去图片，Inches 是设置图片的大小，调整一个适中的大小即可

# 图片的插入位置

图片的位置放在 “ 此文档生成于xxxx年xx月xx日” 的前面，所以顺序是 标题、正文内容、图片、结尾文字。如下代码：

```python
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt,RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

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

paragraphs = []
paragraphs.append(document.add_paragraph('略'))
paragraphs.append(document.add_paragraph('略'))
paragraphs.append(document.add_paragraph('略'))
paragraphs.append(document.add_paragraph('略'))
paragraphs.append(document.add_paragraph('略'))
paragraphs.append(document.add_paragraph('略'))
paragraphs.append(document.add_paragraph('略'))
for para in paragraphs:
    para.space_after = Pt(5)
    para.space_before = Pt(5)
    for run in para.runs:
        run.font.name = u"宋体"
        run.font.size = Pt(12)
        run._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')

# 插入图片
images = '1.jpg'
p_img = document.add_paragraph()
p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_run_img = p_img.add_run()
img_obj = p_run_img.add_picture(images, width=Inches(5))

import datetime
paragraph = document.add_paragraph()
paragraph.space_after = Pt(15)
paragraph.space_before = Pt(15)
paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
paragraph.add_run("此文档生成于")

today = datetime.datetime.now()
today = today.strftime(" %Y{}%m{}%d{} ").format('年','月','日')
timerun = paragraph.add_run(today)
timerun.font.name = u"宋体"
timerun.font.size = Pt(13)
timerun._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')

document.save('背影-images.docx')
```

文本效果如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/c4a1354ede6eff7a2d58870e00d0d7ae.png)

# 表格的内容定义

这是图片的内容，接下来是表格的插入。 这里准备将朱自清的个人信息，用表格进行展示。所以先准备朱自清的信息【信息来自百度百科】：

> 中文名 朱自清外文名 Zhu Ziqing别 名 原名自华国 籍 中国民 族 汉族出生地 江苏东海县出生日期 1898年11月22日逝世日期 1948年8月12日职 业 散文家、诗人、学者毕业院校 北京大学代表作品 《春》《绿》《背影》《荷塘月色》《匆匆》字 号 字佩弦，号秋实 将以上内容全部写入 python 的列表中，以二维列表存储，如下：

```python
info = [
    ['中文名','朱自清'],
    ['英文名','Zhu Ziqing'],
    ['原籍:','浙江绍兴'],
    ['别名','原名自华'],
    ['字号','字佩寇，号秋实'],
    ['国籍','中国'],
    ['民族','汉'],
    ['出生地','江苏东海县'],
    ['出生日期','1989年11月22日'],
    ['逝世日期','1948年8月12日'],
    ['职业','散文家、诗人、学者'],
    ['毕业院校','北京大学'],
    ['代表作','《春》《绿》《背影》'],
]
row = len(info)
col = len(info[0])
```

# 添加表格到文档中

通过 info，设定行和列的数量，然后就是用两个 for 循环，写入表格的内容，如下代码：

```python
document.add_page_break()

title = document.add_heading(0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('朱自清信息表格')
run.font.name = u"宋体"
run.font.size = Pt(22)
run._element.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
run.font.bold = True
run.font.color.rgb = RGBColor(0,0,0)


info = [
    ['中文名','朱自清'],
    ['英文名','Zhu Ziqing'],
    ['原籍:','浙江绍兴'],
    ['别名','原名自华'],
    ['字号','字佩寇，号秋实'],
    ['国籍','中国'],
    ['民族','汉'],
    ['出生地','江苏东海县'],
    ['出生日期','1989年11月22日'],
    ['逝世日期','1948年8月12日'],
    ['职业','散文家、诗人、学者'],
    ['毕业院校','北京大学'],
    ['代表作','《春》《绿》《背影》'],
]
row = len(info)
col = len(info[0])
table = document.add_table(rows=row,cols=col)
table.style = 'Light Shading'
for r in range(row):
    for c in range(col):
        table.cell(r,c).text = info[r][c]
```

这里的代码，info下面是表格的操作，设置样式是 Light Shading 格式，两个 for 循环写入表格每个 cell 文本中。 然后是 document.add\_page\_break() 这个内容，这是添加一个换页符，也就是现在从新的一页开始。 然后添加新页的标题，朱自清信息表格，和顶部的标题样式一样。最后结果，如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/2a757dd2d6b9b70242391739d74d1eed.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/a2647385716150042aa03bd8a6428a56.png)