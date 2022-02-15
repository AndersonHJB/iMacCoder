---
title: Python中重要、常用的科学计算库
tags:
  - 数据分析
id: '1445'
categories:
  - - 人人都能学数据分析
date: 2021-02-09 09:28:04
---

## Numpy

Numpy 是Python科学计算的一个基础包，后期大部分项目都会基于Numpy以及构建于其上的库。

#### Numpy所提供的的功能

*   快速高效的多位数组对象
*   用于计算的函数
*   读写硬盘上基于数组的数据集工具
*   线性代数运算，傅里叶变换，以及随机数生成
*   用于把C,C++,Fortran代码集成到Python中的工具

除了为Python提供快速的数组处理能力，NumPy在数据分析方面还有另外一个主要作用，即作为在算法之间传递数据的容器。对于数值型数据，NumPy数组在存储和处理数据时要比内置的Python数据结构高效得多。此外，由低级语言（比如C和Fortran)编写的库可以直接操作NumPy数组中的数据，无需进行任何数据复制工作。

## Pandas

pandas提供了使我们能够快速便捷地处理结构化数据的大量数据结构和函数。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。用得最多的pandas对象是DataFrame，它是一个面向列（column-oriented)的二维表结构，且含有行标和列标： such as: ![image-20210209111737161](https://img-blog.csdnimg.cn/img_convert/04552a211d8363553ab09efe6d9f0e7d.png) `pandas`兼具NumPy高性能的数组计算功能以及电子表格和关系型数据库（如SQL）灵活的数据处理功能。它提供了复杂精细的索引功能，以便更为便捷地完成重塑、切片和切块、聚合以及选取数据子集等操作。 对于金融行业的用户，pandas提供了大量适用于金融数据的高性能时间序列功能和工具。事实上，我一开始就是想把pandas设计为一款适用于金融数据分析应用的工具。 对于使用R语言进行统计计算的用户，肯定不会对DataFrame这个名字感到陌生，因为它源自于R的data.frame对象。但是这两个对象并不相同。R的data.frame对象所提供的功能只是DataFrame对象所提供的功能的一个子集。虽然讲的是Python，但我偶尔还是会用R做对比，因为它毕竟是最流行的开源数据分析环境，而且很多读者都对它很熟悉。 pandas这个名字本身源自于panel data（面板数据，这是计量经济学中关于多维结构化数据集的一个术语）以及Python data analysis（Python数据分析），毕竟如果想学好数据分析只学Python之不够的。

## matplotlib

> 图表工具

matplotlib是最流行的用于绘制数据图表的Python库。它跟IPython结合得很好，因而提供了一种非常好用的交互数据绘图环境。绘制的图表也是交互式的，你可以利用绘图窗口中的工具栏放大图表中的某个区域或对整个图表进行平移浏览。可以更直观的看到数据的变化情况！

## Ipython

IPython是Python科学计算标准工具集的组成部分，它将其他所有的东西联系到了一起。 它为交互式和探索式计算提供了一个强健而高效的环境。它是一个增强的Python shell，目的是提高编写、测试、调试Python代码的速度。它主要用于交互式数据处理和利用matplotlib对数据进行可视化处理。在用Python编程时，经常会用到IPython，包括运行、调试和测试代码。 除标准的基于终端的IPython shell外，Ipython还支持：

*   一个类似于Mathematica的HTML笔记本（通过Web浏览器连接IPython，稍后将对此进行详细介绍）。
*   一个基于Qt框架的GUI控制台，其中含有绘图、多行编辑以及语法高亮显示等功能。
*   可用于交互式并行和分布式计算的基础架构。强烈建议使用Ipython

![image-20210209112319930](https://img-blog.csdnimg.cn/img_convert/0a54d2023881531f1c63252b5871a12c.png)

## SciPy

```
SciPy是一组专门解决科学计算中各种标准问题域的包的集合，主要包括下面这些包：
· scipy.integrate：数值积分例程和微分方程求解器。
· scipy.linalg：扩展了由numpy.1inalg提供的线性代数例程和矩阵分解功能。
· scipy.optimize：函数优化器（最小化器）以及根查找算法。
· scipy.signal：信号处理工具。
· scipy.sparse：稀疏矩阵和稀疏线性系统求解器。
· scipy.special：SPECFUN(这是一个实现了许多常用数学函数（如伽玛函数）的Fortran库）的包装器。
· scipy.stats:标准连续和离散概率分布（如密度函数、采样器、连续分布函数等)、各种统计检验方法，以及更好的描述统计法。
· scipy.weave：利用内联C++代码加速数组计算的工具。
```

NumPy跟SciPy的有机结合完全可以替代MATLAB的计算功能(包括其插件工具箱）。

* * *

想安装的自行使用pip install 进行安装