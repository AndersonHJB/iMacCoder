---
title: 自动在Windows中运行Python脚本并定时触发作业|编程一对一教学学员答疑帖
tags: []
id: '2084'
categories:
  - - uncategorized
date: 2021-12-13 11:52:03
---

你好，我是悦创。 以下是一对一学员的需求： ![在这里插入图片描述](https://img-blog.csdnimg.cn/915b1e19ec4d406f90b089f9a91b28cb.png) 开整！

# 简介

讲一下在 Python 中写好了一个脚本之后，怎么自动双击一个程序自动就跑起来。 以及，怎么在 Windows 10 中设计定期定时触发并跑脚本。

# 环境介绍

系统环境：Windows 10 Python版本：Python 3.8 必备包：无

## 运行 Python 脚本：.bat 文件

在 Windows 中，`.bat` 文件是批处理文件，是与 Linux 中 `.sh`（shell）文件很像的东西。 如果，我们想在 Windows 中运行一个 Python 脚本，我们可以通过 CMD ，首先进入 python 文件所在的目录，之后运行。 但是这样很麻烦，每次都要打开 CMD，进入文件夹，运行文件。 所以，我们为了不每次都重复输入，建议把这些代码统一写在一个 txt 文件中，写完之后只要把 `.txt` 文件的后缀改为 `.bat` ，然后双击运行就行啦。

## 举例：

假设我们在 `cd D:\Curriculum-development\AI悦创编程一对一\Python 办公自动化\Tester_Coder`目录中有一个名为 `demo.py` 的脚本。 我们希望能有一个类似 exe 一样的东西，每次一双击，自动就会跑出结果。 那么，我们可以进行下面几个步骤： 在任意文件夹中，创建一个记事本文件（后缀 `.txt`），打开文件 在文件夹中输入如下内容：(第一句是用来切换文件夹路径的，第二句是用来运行 python 脚本的)

```python
C:\Users\clela\Desktop\demo
python demo.py
```

保存退出，将记事本的后缀由 `.txt` 改为 `.bat` 这时，双击 `.bat` 文件，就会发现，自己跑 Python 的结果啦~

## 定时在 Windows 中触发 .bat 文件

在 Windows 中，依照如下步骤触发作业：

1.  右键单击“我的电脑”
    
2.  选择 “管理”，弹出如下窗口
    

![在这里插入图片描述](https://img-blog.csdnimg.cn/eb34af9712874fcb94b6f09fd090d484.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/5d41cc5bb03848cbb14b8b72bc89ddc1.png)

3.  在右边Action一栏点击“Create Basic Task”，创建一个基本任务 ![在这里插入图片描述](https://img-blog.csdnimg.cn/8a8304694ee24169a8d816b0a3d34954.png)
    
4.  填写任务名称与描述，随便写就好了。单击下一步
    

![在这里插入图片描述](https://img-blog.csdnimg.cn/91bc691500734cdeb149bea5dd6d6dd5.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/ba740d7e92f14efa9a8d05717f20e51a.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/04a62a22a3144c8fbeeb16385dac8d4e.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/006f7a6c8efe4966b45ef8f704ef8364.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/79adf27cb52d4918accb1b9e093262de.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/bb2b51d15c534cd1b0e9f18907514b6a.png)

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh，公众号：AI悦创

![在这里插入图片描述](https://img-blog.csdnimg.cn/dca3cbc0be964603b79b09ce353a0173.png)