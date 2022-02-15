---
title: Python删除list里的重复元素有几种方法？
tags: []
id: '1468'
categories:
  - - Python
date: 2021-02-16 11:08:35
---

**问：说说Python删除list里的重复元素有几种方法？** **答：** 在 Python 中主要有 5 种方式，还没看答案，你能想起几种呢，面试笔试题经常碰到的一道题 。

### 1、使用 set 函数

set 是定义集合的，无序，非重复，也就是：确定性、互异性、无序性

```python
numList = [1,1,2,3,4,5,4]
print(list(set(numList)))
#[1, 2, 3, 4, 5]
```

### 2、先把 list 重新排序，然后从 list 的最后开始扫描

```python
a = [1, 2, 4, 2, 4, 5,]
a.sort()
last = a[-1]
for i in range(len(a) - 2, -1, -1):
    if last == a[i]:
        del a[i]
    else:
        last = a[i]
print(a) #[1, 2, 4, 5]
```

### 3、使用字典函数

```python
a=[1,2,4,2,4,]

b={}

b=b.fromkeys(a)

c=list(b.keys())

print(c) #[1, 2, 4]

```

### 4、append 方式

```python
def delList(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1
print(delList([1, 2, 2, 3, 3, 4, 5])) #[1, 2, 3, 4, 5]
```

### 5、count + remove方式

```python
def delList(L):
    for i in L:
        if L.count(i) != 1:
            for x in range((L.count(i) - 1)):
                L.remove(i)
    return L
print(delList([1, 2, 2, 3, 3, 4]))#[1, 2, 3, 4]
```