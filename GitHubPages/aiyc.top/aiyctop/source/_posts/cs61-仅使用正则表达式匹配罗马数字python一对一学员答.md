---
title: CS61-仅使用正则表达式匹配罗马数字|Python一对一学员答疑贴
tags: []
id: '1827'
categories:
  - - 技术杂谈
date: 2021-08-03 19:59:20
---

你好，我是悦创。 我的一个一对一学员的提问： ![](https://img-blog.csdnimg.cn/488d116ed7db4cefa3f375a15da35411.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 问题代码：

```
import re

def roman_numerals(text):
    """
    Finds any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M).

    >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    ['IIV', 'VI', 'IV']
    >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    ['I', 'II', 'IV']
    >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    ['I', 'II', 'III', 'IV', 'V']
    >>> roman_numerals("Let's play Civ VII")
    ['VII']
    >>> roman_numerals("i love vi so much more than emacs.")
    []
    >>> roman_numerals("she loves ALL editors equally.")
    []
    """
    return re.findall(__________, text)
```

最后写出如下正则表达式：

```python
b[IVXLCDM]+\b
```

```python
import re


def roman_numerals(text):
    """
    Finds any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M).

    # >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    ['IIV', 'VI', 'IV']
    # >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    ['I', 'II', 'IV']
    # >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    ['I', 'II', 'III', 'IV', 'V']
    # >>> roman_numerals("Let's play Civ VII")
    ['VII']
    # >>> roman_numerals("i love vi so much more than emacs.")
    []
    # >>> roman_numerals("she loves ALL editors equally.")
    []
    """
    pattern = r"\b[IVXLCDM]+\b"
    return re.findall(pattern, text)


if __name__ == '__main__':
    while True:
        a = roman_numerals(input(">>>"))
        print(a)
```

**加循环是为了方便测试**

```python
>>>Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?
['IIV', 'VI', 'IV']
>>>My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit
['I', 'II', 'IV']
>>>I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5Let's play Civ VII
['I', 'II', 'III', 'IV', 'V']
>>>Let's play Civ VII
['VII']
>>>i love vi so much more than emacs.
[]
>>>she loves ALL editors equally.
[]
>>>
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/216259de66954fd1a0962e219a36b404.png)