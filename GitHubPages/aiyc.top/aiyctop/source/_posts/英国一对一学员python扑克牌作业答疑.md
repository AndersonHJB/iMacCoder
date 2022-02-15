---
title: 英国一对一学员Python扑克牌作业答疑
tags: []
id: '2094'
categories:
  - - liujiahuiNotebook
date: 2021-12-15 09:09:18
---

你好，我是悦创。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/63c092cdaf6949f6a414ab32eac2ae0b.png) ![在这里插入图片描述](https://img-blog.csdnimg.cn/cc6eb80312354b58a1dc322240216e6b.png) 代码：[https://www.aiycoj.cn/?id=bc5e0e0d-d732-4a46-a2b8-8449f624542e](https://www.aiycoj.cn/?id=bc5e0e0d-d732-4a46-a2b8-8449f624542e)

## 作业内容

编写一个程序，接受用户的输入，描述一张扑克牌（使用下面的速记符号 Short-hand），并打印出 Description。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/dfbaa6806d6a47a7a7fd66be26ee3c89.png)

## 要求

*   用户输入只能是 2 或者 3 个字符，不要空格。例如 10H，3D。
*   第一个字符（或者头两个字符，如果卡牌为 10）要在 Ranks 里，最后一个字符要在 Suits 里。
*   无论用户输入大小写字母，程序都应该能顺利运行
*   如果用户输入了不合规格的字符或者字符不存在与 Ranks 和 Suits，则应该报 Invalid Card Entered。

## Input & Output 的例子

![在这里插入图片描述](https://img-blog.csdnimg.cn/2fa3913a5df7443ba147bb272631121c.png) 她写的代码是对的，所以我就直接放她写的代码：

```python
shorthand = input("Enter the card notation: ").upper()
length = len(shorthand)
ranks = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', 'A': 'Ace', 'J': 'Jack', 'Q': 'Queens', 'K': 'King'}
suits = {'H': 'Hearts', 'D': 'Diamond', 'S': 'Spades', 'C': 'Clubs'}

if length == 3:
    if shorthand[0:2] == '10' and shorthand[-1] in suits:
        print('Ten of ' + suits[shorthand[-1]])

    else:
        print('Invalid Card Entered')

elif length == 2:

    if shorthand[0] in ranks and shorthand[-1] in suits:
        print(ranks[shorthand[0]] + ' of ' + suits[shorthand[-1]])

    else:
        print('Invalid Card Entered')

else:
    print('Invalid Card Entered')
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/59ad0e2085c64a8184f5464a4a8501b5.png) 好，就到这里。下课！

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/d066a4d2a5ed422c804597101a451e79.png)