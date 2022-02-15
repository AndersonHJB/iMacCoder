---
title: C++路径中“./”、“../”、“/”代表的含义
tags: []
id: '1916'
categories:
  - - C++一对一辅导
date: 2021-09-26 15:53:31
---

[![在这里插入图片描述](https://img-blog.csdnimg.cn/2710ffc3bcf341e6b8fd69ac2af877ff.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQUnmgqbliJs=,size_20,color_FFFFFF,t_70,g_se,x_16)](https://img-blog.csdnimg.cn/2710ffc3bcf341e6b8fd69ac2af877ff.png) 你好，我是悦创。 最近，在为 Python 办公自动化课程备课，故需要整理一波这样的笔记。 **"./"：代表目前所在的目录。** **" . ./"代表上一层目录。** **"/"：代表根目录。**

## 举个栗子：

在读取文件时，路径的写法有如下方式

### 1\. 文件在当前目录（以图像文件为例，当前项目文件为中心）

```python
"./1.jpg" 或 "1.jpg"
```

### 2\. 文件在上层目录

1.  在上层目录下

```python
"../1.jpg"
```

2.  在上层目录下的一个 Image 文件夹下

```python
"../Image/1.jpg"
```

3.  在上上层目录下

```python
"../../1.jpg"
```

### 3\. 文件在下一层目录

1.  在下一层目录 Image1 文件夹下

```python
"./Image1/1.jpg"
```

2.  根目录表示法，任何页面访问 Image 下的 `Image.jpg` 图片

```python
"C:/Image/1.jpg"
```

## 代码示例：

```python
/**
 *Copyright (c) 2018 Young Fan.All Right Reserved.
 *Filename: 8 路径符号的剖析
 *Author: Young Fan
 *Date: 2018.4.30
 *OpenCV version: 3.4.1
 *IDE: Visual Studio 2017
 *Description: “./”、“ ../”、“/”
 */

#include<opencv2/opencv.hpp>
using namespace cv;

int main()
{
    Mat Image = imread("./1.jpg");//文件在当前目录
    imshow("Test", Image);

    Mat Image1 = imread("../1.jpg");//文件在上一层目录下
    imshow("Test1", Image1);


    Mat Image2 = imread("./Image1/1.jpg");//文件在下一层目录(Image1文件夹)
    imshow("Test2", Image2);

    Mat Image3 = imread("../../1.jpg"); //文件在上上层目录下
    imshow("Test3", Image3);


    waitKey();

    return 0;
}
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/fc6874429ed64501ab03c12fbbefd2a3.png)