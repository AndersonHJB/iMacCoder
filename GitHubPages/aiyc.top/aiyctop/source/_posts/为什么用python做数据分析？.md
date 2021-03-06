---
title: 为什么用Python做数据分析？
tags: []
id: '769'
categories:
  - - 数据分析
date: 2020-07-31 00:30:52
---

![img](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200731002708.jpg)

> 生活的理想，就是为了理想的生活。 ——张闻天

你好，我是悦创。 21世纪的企业竞争是数据的竞争，谁掌握数据，谁就掌握未来。 我们每个人都处于数据洪流之中，大数据可以帮助我们分析数据背后的价值。数据整合分析后得到的信息，是数据背后的价值，大数据实现了数据到信息的转化，掌握了大数据时代下的数据，就能够指导世界发展。 正所谓 **“工欲善其事 必先利其器”** ，在时代的大背景下，选择最有前景的工具去完成手头的工作，是值得我们每个人去停下来思考的问题。 最近几年，大数据、人工智能、机器学习等概念异常火爆，以至于普通人对此均有所耳闻。而 Python 语法简单灵活易学，拥有庞大的外部库可扩展自己的应用领域，尤其是许多与大数据内容相关的库，如 `Matplotlib`、`Numpy`、`Pandas`、`SciPy`、`TensorFlow` 等，因此 Python 成为了大数据、人工智能、机器学习的首选语言而备受关注。所以我们说，**用 `python` 做数据分析，再合适不过了**！

## 1\. Python 语法简单易学

如果你不是科班出身的程序猿，那么 Python 对你来讲应该是最好的编程语言了，没有之一。如果你是科班程序员，再掌握一门 `Python` 语言，绝对是如虎添翼的事情。 **`Python` 语言非常的简洁，并且可读性非常强。** 所以，`Python` 的程序对于新手朋友们非常友好，只要你按部就班地学习，并辅之以一定的练习与实战，进入这个领域并且能够用 `Python` 工作完成日常工作，3个月足矣。并且这会导致一个良性循环，`Python` 在日常工作中打开局面，会进一步激发你的学习兴趣，进而促使你有更多的信心去更加深入地学习这门语言。

```python
# Python 打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}×{}={}".format(i, j, i*j), end='  ')
    print("")
```

运行结果：

```python
1×1=1  
2×1=2  2×2=4  
3×1=3  3×2=6  3×3=9  
4×1=4  4×2=8  4×3=12  4×4=16  
5×1=5  5×2=10  5×3=15  5×4=20  5×5=25  
6×1=6  6×2=12  6×3=18  6×4=24  6×5=30  6×6=36  
7×1=7  7×2=14  7×3=21  7×4=28  7×5=35  7×6=42  7×7=49  
8×1=8  8×2=16  8×3=24  8×4=32  8×5=40  8×6=48  8×7=56  8×8=64  
9×1=9  9×2=18  9×3=27  9×4=36  9×5=45  9×6=54  9×7=63  9×8=72  9×9=81  
```

单从 Python 语法角度来说，其基础语法非常简单，非常注重用少量的代码构造出很多功能。简单 4行代码，就可以打印出 99乘法表，简约而不简单。**移动互联时代，快人一步，则抢夺先机。** 简洁的语法，则是更高开发效率的代名词。

## 2\. Python 还是一门脚本语言

脚本语言的 “优势”，其实在于它不需要事先 “编译”。而 Python 不仅仅是一门高级语言，它还有脚本语言的特征。这就能拿来做很多事情了。 例如做数据清洗的时候，我们迫切地需要看到每一步的执行效果，以此来判断下一步的行动，而这是其它高级语言所不能提供的能力。 `Python` 提供了很多交互式编程环境，比如 `Ipython`，还有最近大名鼎鼎的 `Jupyter`。这对我们的数据分析场景尤为重要。 **试想这样一个情况：** 我有很多封装为函数的小段可视化代码，为了避免代码过于分散，我将封装好后全部放进一个文件中。如果我希望同时执行其中的数段代码可视化功能，以比较不同的代码执行的效果。那我可要抓狂了，因为在同一个集成编辑环境中，我只能显示一个可视化效果，除非我将它们分别下载下来一一比较。 在交互式编程环境中，比如 `Jupyter`，则完全没有这样的烦恼。每段代码可以在同一个页面中分开运行，并交互式的展现，执行完成后，结果会以文本文件的格式写入到当前页面中。当你执行一整套流程，`Jupyter` 结果会像一篇笔记一样让你赏心悦目。而这正是 Python 作为一门脚本语言带来的独特魅力。 ![图片描述](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200731002714.jpg) 从这个角度说，选择用 Python 做数据分析，是理所当然的选择。事实上，我们可以用先用 Python 脚本语言的特性做数据处理，再用高级语言的特性对数据能力进行封装。甚至于可以在封装阶段调用 C 语言的接口，提供额外的扩展功能，而这又是 Python 作为“胶水语言”的特性了。

## 3\. Python语言是人工智能的首选

日前，Tiobe 发布了 2019年 6月编程语言排行榜，排名前五的分别是：Java、C、Python、C++、 Visual Basic。其中，Java 依旧稳居第一，Python 则升至第三位。 ![图片描述](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200731002718.png) Python 在统计、AI 编程、脚本编写、系统测试等领域均排名第一。此外，Python 还在 Web 编程和科学计算等领域处于领先地位，总之，Python 无处不在。目前的情况是，越来越多的开发者正在涌入这些领域，为这些领域带来强大的生命力。 **火热只是表象，深层次的原因则是强大的 AI 支持库。** NumPy 支持维度数组与矩阵运算，堪称 AI 数据神器，而各种算法，实际上处理的都是矩阵和向量。使用 NumPy，矩阵的转置、求逆、求和、叉乘、点乘……都可以轻松地用一行代码搞定，行、列可以轻易抽取，矩阵分解也不过是几行代码的问题。而且，NumPy 在实现层对矩阵运算做了大量的并行化处理，通过数学运算的精巧，而不是让用户自己写多线程程序，来提升程序效率。 ![图片描述](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200731002722.jpg) 对于 AI 模型，几十上百行代码就够了。当然你也可以选择采用成熟的模型而调用 `Scikit-Learn` 的接口，效果却轻而易举地超越前辈的规则模型，简直没有比这更让新入门的朋友如此开心的事情了。 对于深度神经模型，`Python` 也有现成的平台的可以选用，比如 `TensorFlow` ，是搭建深度神经网络的首选。 Python 生态的完善，让 Python 的学习曲线非常平缓。你可以选择先成为一名数据分析师，在完全驾驭这个领域之后，再学习经典算法，成为一名数据挖掘领域的专家。如果你对新技术充满虔诚与狂热，那么进入深度学习领域吧。数据分析能力将成为你在 AI 这个领域的奠基石，算法与数学的积累，会让你在 AI 的殿堂里走的更远，总之你的一切能力都不会浪费，他们都会因你的下一次选择而不断升华。 **而这源于你今天选择了 `Python` 这门工具，开启了数据分析的序幕**。

## 4\. 统计分析？数据可视化？Python 都擅长

如果说 Python 是基础的话，那么 Python 数据分析的三大工具（ `Numpy` ，`Pandas`，`Matplotlib` ）则是数据分析领域最为灿烂的三大明珠。正是这三大工具，把数据分析推向了另一个高潮。「我觉得添加上 Pyecharts」 `Numpy` 提供了一套高效操作数组的方法，是 Python 科学计算的基础包。 `Pandas` 是一个表格容器，它纳入了大量的标准化的数据模型，提供了高效地操作大型数据集所需的方法。这是成为强大而高效的数据分析环境的重要因素之一。 `Matplotlib` 则是提供了一套可视化的方法。初次接触大家可能会有这样的疑问，`Matplotlib` 和 `MATLAB` 的名字有些相似，它们是否有一定的相似性呢？ 可以这么说，`Matplotlib` 的诞生是源于模仿 `MATLAB`，但是依托 `Python` 强大的开发生态，解决 `MATLAB` 自身的局限性。`MATLAB` 是一款科学计算软件，在处理数据与程序的交互式场景中，就显得有些相形见绌。 而 `Python` 作为一款高级语言，在与应用层的交互性方面有着近乎降维打击的优势。并且 `Matplotlib` 继承了 `Python` 语法简洁优美、开源免费的特点，因此在学术界和工业节应用广泛。 特别是近几年，依托于 Python 建立的数据分析生态愈发完善，像基于 `Matplotlib` 更高级封装的 `Seaborn` ，以及依托百度 `Echarts` 而来的 `Pyecharts` 等等，这些越来越多的开发者贡献自己的智慧，把 `Python` 的数据开发生态搭建得越来越齐全。 所以说，选择用 `Python` 做数据分析，其实是选择了这个生态，依托于这个生态，就像是站在了巨人的肩上，只有站得高，才能看得远。

## 5\. 没有数据源？那自己写个爬虫好了

俗话常说 **“巧妇难为无米之炊”** ，我们学习数据分析，可能最大的阻碍不是语法知识，而是没有足够的数据源去实战。如果不在实际项目中，空学几句语法，那不成了花架子了？用 Python 则完全不用担心！ 网络爬虫通俗的讲就是通过程序去自动采集数据。世界上 80%的爬虫是基于 Python 开发的，学好爬虫技能，可为后续的大数据分析、挖掘、机器学习等提供重要的数据源。 Python 写爬虫，其实也很简单，只要你了解基础的 HTML 知识，那么也可以快速开发出自己的爬虫程序，这里我们简单看一个豆瓣电影清单的 demo，只要三十行的代码量，就可以自动从豆瓣上采集。在之后的教学上，我们会详细讲解这个 demo，包括爬虫的编写逻辑、`requests` 库的安装等等。

```python
#!/usr/bin/env python
# coding: utf-8
# Author：AI悦创
# 公众号：AI悦创

import json
import re
import requests
from requests import RequestException

# 获取网页的内容，以文本形式返回
def get_page(url):
    headers = {
        "Host":"movie.douban.com", 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 对网页文本内容进行解析
def parse_page(html):
    pattern = re.compile('<li.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'title': item[0],
            'score': item[1],
            'image': item[2],}

# 爬虫主程序，同时print效果
def main():
    url = "https://movie.douban.com/cinema/nowplaying/beijing/"
    html = get_page(url)
    print(html)
    for item in parse_page(html):
        print(item)
if __name__ == '__main__':
    main()
```

## 6\. 总结

总结来说，用 Python 做数据分析，再适合不过了！Python 是一个强有力的编程生态，通俗来说就是，`Python` 能力非常全面：`Numpy`，`Pandas` 是专门为数据分析打造的工具，而 `Matplotlib` 等工具则提供了可视化的捷径；如果没有数据，`Python` 还可以非常便捷地用来编写爬虫程序，解决数据来源的问题。 利用 `Python` 工具，可以在最短的时间内，打通数据获取、清洗、统计、到可视化的整个流程。并且 `Python` 语法简单易学，学习曲线平滑，非常适宜没有编程基础或者非科班出身的朋友学习。 特别需要指出的是，学会了这门课，不仅仅是多了一个技能，而是多了一个打开 AI大门的钥匙，一张 AI赛程的入场券！所以，你准备好了吗？