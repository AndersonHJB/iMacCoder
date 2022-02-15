---
title: python基础第三课
tags: []
id: '1996'
categories:
  - - Python一对一
date: 2022-01-30 11:05:28
---

## 一、字符串的格式化

name = input() sex = input() age = input() template\_Str = 'dear{} , you are a {} , you are{} years old'.format(name , sex , age) 注意：此时.format()中的变量顺序和名称必须与前方完全对应 这里给出另外一种方法： template\_str = f' dear{name} , you are a {sex} , you are {age} years old '  

## 二、列表（list）

*   列表用\[ \]来表示，列表里的元素用英文逗号来隔开，列表内元素都是可变的
*   列表的切片与字符串完全相同，这里不再赘述。
*   列表的赋值：列表内元素可改变，可直接用\[ \]进行赋值（注意：若a\[x : x \] = ..... ，此时我们添加元素到x与x-1之中）
*   列表元素的添加：直接用.append('需要加入的元素')
*   列表的索引与字符串不同：.index()，而字符串为.find()
*   列表的删除：del a\[所删除元素的下标\]   del a\[\]  删除整个列表a
*   判断某个元素是否在列表内：使用if ’元素‘ in 列表 进行判断

  

## 三、元组（tuple）

元组是有序的，但是不可变的，其内容与字符串大致相同，但是元组用（）来表示