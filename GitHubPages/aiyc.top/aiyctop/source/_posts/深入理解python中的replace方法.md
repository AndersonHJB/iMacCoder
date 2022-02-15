---
title: 深入理解Python中的replace方法
tags: []
id: '602'
categories:
  - - 7 天零基础章节测试
date: 2020-07-13 10:53:28
---

先讨论一下它的用法：

> str = “abcdef” str.replace（old，new，\[max\]）方法用于字符串的修改，将字符串str中的字符old替换为 新的new字符串，max是可选参数，可以写也可以不写，不写的情况下，表示将str中所有的old替换为new，写之后表示最大替换次数。最后将修改后的字符串给返回，他是有返回值的 例如： str= “abcdef” print(str.replace(“abc”,’AAA’)) 运行结果： AAAdef

但是，字符串是不可以修改的类型，它并没有修改以前的str，可以看下列代码：

```python
str= "abcdef"
print(str.replace("abc",'AAA'))
print((str))
print(id(str))
print(id(str.replace("abc",'AAA')))
```

结果截图： ![这里写图片描述](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200713105159.png) 以前的还是以前的，他们的内存不一样，当你引用str这个变量的时候，并没有得到你想要的修改后的值，如果你想要通过str的引用得到修改后的值，那么，将str这个变量指向修改后的内存地址即可（目前我只知道这种方法，其他方法比较麻烦，不过都修改不了最初str内存里的值）：

```python
str= "abcdef"
print(str)
print(id(str))
str = str.replace("abc",'AAA')
print(str)
print(id(str))
```

运行截图： ![这里写图片描述](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200713105301.png) 仔细看看，转换前后str的内存地址发生了变化，这是因为将 str 变量指向了修改后的