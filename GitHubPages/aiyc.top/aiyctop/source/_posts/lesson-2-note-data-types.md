---
title: 'Lesson 2 note: Data Types'
tags: []
id: '2035'
categories:
  - - liujiahuiNotebook
date: 2021-12-01 05:05:11
---

# Data Types

**\- String** **\- Numeric** **\- Boolean** **\- List** **\- Tuple** **\- Dictionary** **\- Set** ![](https://www.aiyc.top/wp-content/uploads/2021/12/1638303179-ed1243881c13e56.png?x-oss-process=image/resize,m_fill,w_300,h_162#)

## String 字符串

**`str()`** - 有序 - 不可变 （不能被修改） - 可以放任何数据类型 （会变成字符串）

## Numeric 数字型

**`int()` 整数 `float()` 浮点数** - 无序

## Boolean 布尔型

**`bool()`** - 只有True和False；也可用1代表True，0代表False

## List 列表

**`list()`** - 有序 - 可变 - 可放任意数据类型 - 应用场景：访问记录

## Tuple 元组

**`tuple()`** - 有序 - 不可变 - 可放任意数据类型 - 占用空间小（跟列表相比） - 应有场景：经纬度

## Dictionary 字典

**`dict()`** - 由key和value组成（key不可变；value可变，可放任意数据类型） - 在Python 3.7之前是无序的；在Python3.7之后是有序的（小白可暂时理解为无序的）

## Set 集合

**`set()`** - 确定性（不可变） - 互异性（自动删除掉重复的value） - 无序性

## 查看数据

**`type()`**

```python
type(str(123))
```

> \>>str

## 转换数据类型

```python
# 从字符串转换成数字类型
type(int(str(123)))
```

> \>>int

```python
从字符串转换成列表
type(list(str('LKW')))
```

> \>>list

## P.S.

有序：从左到右，由0号位开始，依次递进；从右到左，由-1号位开始，依次递减，这些数字叫“下标”