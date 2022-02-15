---
title: django中models里面__str__有什么作用？
tags: []
id: '1547'
categories:
  - - Django
date: 2021-03-05 16:34:29
---

\_\_str\_\_是 Python 的 object 基类的一个方法，也就是说 Python 所有的类都有，当然 django 的 modle 类也有，我们平常创建一个类的对象，print 这个对象时一般会是

```python
<__main__.TestClass object at 0x10f1e5670>
```

即这个对象的所属类和内存地址。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305162400368.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

```python
# 一般情况
class TestClass:
    def __init__(self):
        self.name = 'paomo'
t = TestClass()
print(t)
# <__main__.TestClass object at 0x10f1e5670>
```

我们改写类中的 \_\_str\_\_方法后可以在 print 时得到想要的易于人阅读的对象的信息，以下是实例：

```python
# 改写 __str__ 方法
class TestClass:
    def __init__(self):
        self.name = 'paomo'

    def __str__(self):
        return self.name
t = TestClass()
print(t)
```

聚合：

```python
# 一般情况
class TestClass:
    def __init__(self):
        self.name = 'paomo'
t = TestClass()
print(t)
# <__main__.TestClass object at 0x10f1e5670>


# 改写 __str__ 方法
class TestClass:
    def __init__(self):
        self.name = 'paomo'

    def __str__(self):
        return self.name
t = TestClass()
print(t)
```