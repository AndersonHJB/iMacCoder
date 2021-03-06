---
title: 01-Python3 环境搭建（Python+SublimeText3+Pycharm+Mac）
tags: []
id: '578'
categories:
  - - Python3 网络爬虫系统教学
date: 2020-07-12 17:58:50
---

你好，我是悦创。 当你看见此视频的时候，表面你已经正式准备步入学习 Python 的阶段，这里我先祝贺你，你选择是正确的。对于此环境安装呢，主要可以直接看下面的视频操作讲解，以及后文的简单文字介绍。

#### 1.1 Python 安装

下载方法

> 进入官网：[https://www.python.org](https://www.python.org)

![在这里插入图片描述](https://images.gitbook.cn/2ed79940-33b5-11ea-9ca4-83fe0a60672f) **如图：**

1.  选择上方 Downloads 选项
2.  在弹出的选项框中选择自己对应的系统（注：若直接点击右边的灰色按钮，将下载的是 32 位）

![在这里插入图片描述](https://images.gitbook.cn/5f5fea40-33b5-11ea-ae9a-73a78fc9c1c1) 进入下载页面，如图：

1.  为 64 位文件下载
2.  为 32 位文件下载

**选择您对应的文件下载。** 安装注意事项： ![在这里插入图片描述](https://images.gitbook.cn/769031c0-33b5-11ea-9ca4-83fe0a60672f) （图片来源于网络） 自定义选项，可以选择文件存放位置等，使得 Python 更符合我们的操作习惯。 默认安装：一路 Next 到底，安装更方便、更快速。

> 特别注意：图中箭头指向处一定要记得勾选上。否则得手动配置环境变量了哦。

**Q：如何配置环境变量呢？**

> A：控制面板—系统与安全—系统—高级系统设置—环境变量—系统变量—双击 path—进入编辑环境变量窗口后在空白处填入 Python 所在路径—一路确定。

**检查** 安装完 Python 后，Win+R 打开运行窗口输入 cmd，进入命令行模式，输入 python。若如下图显示 Python 版本号及其他指令则表示 Python 安装成功。 ![在这里插入图片描述](https://images.gitbook.cn/a2df1ed0-33b5-11ea-99bc-c7daf55fc07a)

#### 1.2 Python 编译器 Sublime

> 官网：http://www.sublimetext.com/

![在这里插入图片描述](https://images.gitbook.cn/df153e70-33b5-11ea-be28-8d6dbc98de70) 选择该编辑器的原因：

1.  不需要过多的编程基础，快速上手
2.  启动运行速度快
3.  最关键的原因——免费

**常见问题** 使用快捷键 Ctrl+B 无法运行结果，可以尝试 Ctrl+Shift+P，在弹出的窗口中选择 `Bulid With: Python`。 ![在这里插入图片描述](https://images.gitbook.cn/f9808cb0-33b5-11ea-ae9a-73a78fc9c1c1) 或选择上方的 Tool 选项中的 Build With 选项，在弹出的窗口中选择 Python。