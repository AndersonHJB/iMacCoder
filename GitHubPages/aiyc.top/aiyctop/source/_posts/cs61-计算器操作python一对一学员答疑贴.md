---
title: CS61-计算器操作|Python一对一学员答疑贴
tags: []
id: '1828'
categories:
  - - 技术杂谈
date: 2021-08-03 20:31:18
---

你好，我是悦创。 我的一个一对一学员的提问：

## Q6: Calculator Ops

Write a regular expression that parses strings written in the 61A Calculator language and returns any expressions which have two numeric operands, leaving out the parentheses around them.

```python
import re

def calculator_ops(calc_str):
    """
    Finds expressions from the Calculator language that have two
    numeric operands and returns the expression without the parentheses.

    >>> calculator_ops("(* 2 4)")
    ['* 2 4']
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    ['* 2 4', '+ 3 5', '- 10 7']
    >>> calculator_ops("(* 2)")
    []
    """
    return re.findall(__________, calc_str)
```

## 答案

```python
import re


def calculator_ops(calc_str):
    """
    Finds expressions from the Calculator language that have two
    numeric operands and returns the expression without the parentheses.

    # >>> calculator_ops("(* 2 4)")
    ['* 2 4']
    # >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    ['* 2 4', '+ 3 5', '- 10 7']
    # >>> calculator_ops("(* 2)")
    []
    """
    pattern = r"[+,\-,*,/]\s\d+\s\d+"
    return re.findall(pattern, calc_str)


if __name__ == '__main__':
    while True:
        a = calculator_ops(input(">>>"))
        print(a)
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/3ecbada848ca4c90bc44a9a35b3d1719.png)