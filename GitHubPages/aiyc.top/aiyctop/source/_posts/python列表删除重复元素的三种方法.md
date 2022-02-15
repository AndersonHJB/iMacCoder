---
title: python列表删除重复元素的三种方法
tags: []
id: '1469'
categories:
  - - Python
date: 2021-02-16 11:55:13
---

给定一个列表，要求删除列表中重复元素。

```python
listA = ['python','语','言','是','一','门','动','态','语','言']
```

**方法1，** 对列表调用排序，从末尾依次比较相邻两个元素，遇重复元素则删除，否则指针左移一位重复上述过程：

```python
def deleteDuplicatedElementFromList(list):
        list.sort();
        print("sorted list:%s" % list)
        length = len(list)
        lastItem = list[length - 1]
        for i in range(length - 2,-1,-1):
                currentItem = list[i]
                if currentItem == lastItem:
                        list.remove(currentItem)
                else:
                        lastItem = currentItem
        return list
```

**方法2，** 设一临时列表保存结果，从头遍历原列表，如临时列表中没有当前元素则追加：

```python
def deleteDuplicatedElementFromList2(list):
        resultList = []
        for item in list:
                if not item in resultList:
                        resultList.append(item)
        return resultList
```

**方法3，** 利用python中集合元素惟一性特点，将列表转为集合，将转为列表返回：

```python
def deleteDuplicatedElementFromList3(listA):
        #return list(set(listA))
        return sorted(set(listA), key = listA.index)
```

执行结果：

```python
print(deleteDuplicatedElementFromList(listA))        
#sorted list:['python', '一', '动', '态', '是', '言', '言', '语', '语', '门']
#['python', '一', '动', '态', '是', '言', '语', '门']

print(deleteDuplicatedElementFromList2(listA))        
#['python', '语', '言', '是', '一', '门', '动', '态']

print(deleteDuplicatedElementFromList3(listA))        
#['python', '语', '言', '是', '一', '门', '动', '态']
```

分析： 方法1，逻辑复杂，临时变量保存值消耗内存，返回结果破坏了原列表顺序，效率最差 方法2，直接调用append方法原处修改列表，逻辑清晰，效率次之 方法3，极度简洁，使用python原生方法效率最高