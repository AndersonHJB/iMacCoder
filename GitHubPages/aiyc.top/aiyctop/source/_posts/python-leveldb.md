---
title: Python leveldb
tags: []
id: '1677'
categories:
  - - leveldb
date: 2021-05-17 11:24:37
---

你好，我是悦创。 leveldb 是 google 实现的一种非常高效的 key-value 数据库。key-value 数据库中，redis 是比较知名且好用的，但它是一个内存数据库，而 leveldb 只需要少量的内存，但速度依然很快，美中不足的是，没有网络服务封装，这样一来就只能单机使用，如果你实力足够强，也可以自己封装一个。 python 版本的 leveldb 安装很简单：

```python
pip install leveldb
```

接下来重点介绍使用方法。

## 一 、 读写

```python
def single_operate():
    db = leveldb.LevelDB('./data')
    db.Put('foo','东升')
    print db.Get('foo')
    db.Delete('foo')
    print db.Get('foo')
```

新建数据库很方便，如果这个目录已经存在就会直接打开，没有的话就会新建。示例中给出了添加，删除，和获取的方法，注意，是没有修改操作的。

## 二 、 遍历

如何遍历数据呢，也非常方便，你可以指定开始的 key 和结束的 key ，也可以指定顺序，是否带 value

```python
def test_iter():
    db = leveldb.LevelDB('./data')
    for i in xrange(10):
        db.Put(str(i), 'string_%s' % i)
    print list(db.RangeIter(key_from = '2', key_to = '5'))
    print list(db.RangeIter(key_from = '2', key_to = '5',reverse=True))
```

```python
def iter_key_values():
    db = leveldb.LevelDB('./data')
    for i in xrange(10):
        db.Put(str(i), 'string_%s' % i)
    keys = list(db.RangeIter(include_value = False))
    print keys

    keys_values = list(db.RangeIter())
    print keys_values
```

## 三、 批量操作

如果我对数据库有一大批操作，每一次都和数据库进行交互，其实挺浪费性能的，因此像 mongodb，redis 都提供了批量操作的方法，leveldb 也是如此。下面是一个清空数据库的例子：

```python
def clear_db():
    db = leveldb.LevelDB('./data')
    b = leveldb.WriteBatch()
    for k in db.RangeIter(include_value = False, reverse = True):
        b.Delete(k)
    db.Write(b)
```

`b.Delete(k)` 并没有真正的删除数据，而是在 `db.Write(b)` 时执行所有的操作

## 四、 快照

创建快照非常简单，美中不足的是，再次加载数据库以后，没有方法找到之前创建的快照，难道已关闭这些快照就都不见了，这这样的快照还有什么意思呢，也许只有 python 版本的快照是这样的吧：

```python
def test_snapshot():
    db = leveldb.LevelDB('./data')
    db.Put('foo','s1')
    s1 = db.CreateSnapshot()
    db.Put('foo','s2')
    s2 = db.CreateSnapshot()

    print db.Get('foo')
    print s1.Get('foo')
    print s2.Get('foo')
```