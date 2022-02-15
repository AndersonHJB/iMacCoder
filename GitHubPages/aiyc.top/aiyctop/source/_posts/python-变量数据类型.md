---
title: 2.python 变量&数据类型
tags: []
id: '2016'
categories:
  - - Python
date: 2021-11-07 21:53:55
---

# 变量

> 变量命名规范：可以是大写字母，小写字母，大小写字母数字混合，下划线，不能以数字开头

```python
A = 1
a = 1
user_name = '张三'
_a = 1
test1 = 1
```

> 错误命名如下：

```python
19a = 1
```

# 数据类型

#### 字符串型 str

*   有序性
*   任意数据类型
*   不可变

```python
username = '张三'
```

#### 数字型 int float

```python
num = 100 #整型
num = 1.2 #浮点型
```

#### 布尔型 bool

```python
is_right = True  #真
is_right = False #假
```

#### 元祖 tuple

*   有序性
*   任意数据类型
*   不可变

```python
a = (1,'two',3.0,'four')
```

#### 列表 list

*   有序性
*   任意数据类型
*   可变

```python
a = [1,'two',3.0,'four']
```

#### 字典 dict

*   无序性
*   任意数据类型
*   可变

```python
a = {1:'one',2:'two'}
```

#### 集合 set

```python
a = {1,2,2,2,2,2,3,4,5}
#结果
print(a) #{1,2,3,4,5}
```

*   无序性
*   确定性
*   互异性

# 小技巧

> #### 代码洁癖 自动加空格 Ctrl + Alt + L
> 
> #### 注释 Ctrl + /