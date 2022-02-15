---
title: Python3知识点：相对路径 ‘’，‘/’，'./'，'../'
tags: []
id: '1915'
categories:
  - - 技术杂谈
date: 2021-09-26 15:25:16
---

你好，我是悦创。 `''` ： 当前同级目录 `'/'` ：根目录 `'./'` ：当前同级目录 `'../'` ：上级目录 示例代码如下：

```python
f = open("aaa.txt","w")     #当前目录
f.write("在哪啊")
f.close()

f = open("/foo.txt","w")    #根目录下
f.write("Python是一个非常好的语言。\n是的，的确非常好！\n")
f.close()

f = open("/foo.txt","r")
message = f.readlines()
print(message)              #返回一个列表
str = f.read()
print(str)                  #返回文档的格式

f = open("./test.txt","w")  #当前目录
f.write("在哪啊?\n")
f.write("是当前目录！")
f.close()

f = open("../test.txt","w") #上级目录
f.write("在哪啊?\n")
f.write("是上级目录！")
f.close()
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/4713eda1ba0049a18562e200de65aaf2.png)