---
title: 在Pycharm中自动添加时间日期作者等信息
tags: []
id: '1474'
categories:
  - - Pycharm
date: 2021-02-17 19:57:31
---

你好，我是悦创。在 Pycharm 中自动添加时间日期作者等信息

## 1\. 按照下面路径以此打开

**File→Settings→Editor→File and code Templates** 右侧找到 Python Script, 如下图 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210217195222823.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 2\. 设置相关代码

```python
##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : AI悦创
# @FileName: ${NAME}.py
# @Software: ${PRODUCT_NAME}
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创

```

**设定的规则说明如下**

```python
（a）shebang行

#!/usr/bin/python3

（b）预定义的变量要扩展为格式为$ {<variable_name>}的相应值。

可用的预定义文件模板变量为：

$ {PROJECT_NAME} - 当前项目的名称。

$ {NAME} - 在文件创建过程中在“新建文件”对话框中指定的新文件的名称。

$ {USER} - 当前用户的登录名。

$ {DATE} - 当前的系统日期。

$ {TIME} - 当前系统时间。

$ {YEAR} - 今年。

$ {MONTH} - 当月。

$ {DAY} - 当月的当天。

$ {HOUR} - 目前的小时。

$ {MINUTE} - 当前分钟。

$ {PRODUCT_NAME} - 将在其中创建文件的IDE的名称。

$ {MONTH_NAME_SHORT} - 月份名称的前3个字母。 示例：1月，2月等

$ {MONTH_NAME_FULL} - 一个月的全名。 示例：1月，2月等
```