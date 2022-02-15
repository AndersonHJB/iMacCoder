---
title: Python 中两个 list 元素对比
tags: []
id: '1779'
categories:
  - - 技术杂谈
date: 2021-07-02 22:32:43
---

你好，我是悦创。 set 是一个无序不重复元素集，Python 数据类型的一种，由于是无序的，不能通过索引和切片来做一些操作。主要有添加、删除、交集、并集、差集、对称差集 五种操作。

## 1\. 添加

```python
a=set([1,2,3])
#方法1：添加1项
a.add(4)
#方法2:添加多项，update中的参数必须是迭代器
a.update([4,5,6])
```

## 2\. 删除

```python
a.remove(1)    #如果删除不存在的元素，产生KeyError
a.discard(2)   #如果存在元素2，则删除
c=a.pop()      #删除一个不确定的元素，并且赋给c，如果集合a为空则产生 KeyError
a.clear()      #删除集合中所有元素
```

## 3\. 交、并、差、对称差

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210702222905587.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

```python
a=set(range(1,11))             # a为{1,2,3,4,5,6,7,8,9,10}
b=set(range(0,10,2))           # b为10以内的偶数列{0,2,4,6,8}
"""
=====================方法一:运算符版本=========================
"""
union=list(ab)                # 并               
inter=list(a&b)                # 交 
diff=list(a-b)                 # 差
sys_diff=list(a^b)             # 对称差
"""
=====================方法二:非运算符版本======================
"""
tmp1=list(a.union(b))                   # 并
tmp2=list(a.intersection(b))            # 交
tmp3=list(a.difference(b))              # 差
tmp4=list(a.symmetric_difference(b))    # 对称差

print(tmp1)               # 输出集合的并：0,1,2,3,4,5,6,7,8,9,10
print(tmp2)               # 输出集合的交：2,4,6,8
print(tmp3)               # 输出集合的差：1,3,5,7,9,10 
print(tmp4)               # 输出对称差集：0,1,3,5,7,9,10
```