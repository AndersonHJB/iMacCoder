---
title: 章节测试一答案「Python-变量和数据类型_详细答案解析」
tags: []
id: '583'
categories:
  - - 7 天零基础章节测试
date: 2020-07-12 21:32:08
---

你好，我是悦创。欢迎来到 Python 核心技术实战，这是你的第一次测试，加油！

1.  以下哪个变量可以做python的变量： A. 01a B. class C. a\_int D. b-int
    
    > ##### 答案解析
    > 
    > 正确答案：C 易错项：B 变量名命名规则必须是大小写英文、数字和\_的组合，不能用数字开头，且不能以python里的关键字作为变量名。其中B为python中关键字，可在命令行中进入交互环境输入help('keywords')来查看python关键字列表。
    
2.  以下哪个选项不是 Python 的基本数据类型关键字 A. int B.bool C. string D. dict
    
    > ##### 答案解析
    > 
    > 正确答案：C 易错项：B 字符串的关键字在 python 里是 str
    
3.  此题无需在线作答，请在纸上作答后查看答案解析 语句 x, y, z = 1, 2, 3执行后，变量y的值为\_\_\_\_\_\_\_\_\_\_。
    
    > 请在改文章下面留言，留下你的答案！
    > 
    > ##### 答案解析
    > 
    > 正确答案：2
    
4.  此题无需在线作答，请在纸上作答后查看答案解析 查看变量类型的 Python 内置函数是\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_。
    
    > ##### 答案解析
    > 
    > 正确答案：type() 记忆性知识点
    
5.  此题无需在线作答，请在纸上作答后查看答案解析 请写出该代码的输出结果\_\_\_\_\_\_\_\_\_\_\_\_\_。
    
    ```python
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)
    ```
    
    > ##### 答案解析
    > 
    > 正确答案：ABC 执行 a = 'ABC'，解释器创建了字符串 'ABC' 和变量 a，并把 a 指向 'ABC'： 执行 b = a，解释器创建了变量b，并把 b 指向 a 指向的字符串 'ABC'： 执行 a = 'XYZ'，解释器创建了字符串 'XYZ'，并把 a 的指向改为'XYZ'，但 b 并没有更改： 所以，最后打印变量 b 的结果自然是 'ABC' 了。
    

![在这里插入图片描述](https://images.gitbook.cn/ea07bfc0-6d02-11ea-9b0b-4bc64571574c)