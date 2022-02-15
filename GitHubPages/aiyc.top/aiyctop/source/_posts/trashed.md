---
title: python基础第二课
tags: []
id: '1986'
categories:
  - - Python一对一
date: 2022-01-30 11:05:28
---

# 一、数字型

>  数字型分为整数（int）和浮点数（float）

①算术运算符：+,  -  ,  \* ,  / ,   % ,   \*\* ,  //

注意：其中/为除法运算符，除法运算符的结果一定是浮点数（float），%为取余字符，//为

取整字符。

②比较运算符： == , \>= ,<= ,> ,< !=

③赋值运算符：\= , \-= , += , \*= , /= , \*\*= , //=

# 二、字符串

> 字符串是由字母、数字和特殊字符来组成的序列，字符串是有序的，字符串可以用单引号、双引号和三引号来表示（当需要截取不同行的字符时，我们通常可以使用三引号直接进行截取，而单引号和双引号只可在单行进行截取进行截取）

①字符串的长度计算使用len函数

注意len函数是计算的字符串长度从1开始，而字符串的排序是从0开始，因此要和字符串的排序区分

②字符串字符的截取：\[\]，采取左闭右开的原则，取左不取右，\[::\]则默认从最左边取到最右边，\[:::\]，第三个冒号后面为间隔字符数，可为负（即从后往前取）

③字符串内置方法：.upper() , .lower() , .replace(‘old’, ‘new’) , .find(‘x’ ) , .count(‘x’) 

.isalpha() , .isdigit

注意：其中find函数寻找的仅为字符x第一次出现时的下标，count函数寻找的是字符x在字符串中一共出现的次数，.isalpha和.isdigit若正确则显示为True，错误显示为False

④字符串的不可变性

字符串时不可变的，若要改变字符串，则必须重新创建一个字符串

⑤字符串的转义：\\（转义符） ， \\t（制表符） ，\\n（换行符） ， \\b（退格） ，[\\\\（单斜杠符号](///\\（单斜杠符号)）

⑥字符串的连接：print(s1 + s2)组合形成了一个新的字符串 , print(s1 , s2)原来两个字符串的拼接 Normal 0 7.8 磅 0 2 false false false EN-US ZH-CN X-NONE /\* Style Definitions \*/ table.MsoNormalTable {mso-style-name:普通表格; mso-tstyle-rowband-size:0; mso-tstyle-colband-size:0; mso-style-noshow:yes; mso-style-priority:99; mso-style-parent:""; mso-padding-alt:0cm 5.4pt 0cm 5.4pt; mso-para-margin:0cm; mso-para-margin-bottom:.0001pt; mso-pagination:widow-orphan; font-size:10.5pt; mso-bidi-font-size:11.0pt; font-family:"Calibri","sans-serif"; mso-ascii-font-family:Calibri; mso-ascii-theme-font:minor-latin; mso-hansi-font-family:Calibri; mso-hansi-theme-font:minor-latin; mso-bidi-font-family:"Times New Roman"; mso-bidi-theme-font:minor-bidi; mso-font-kerning:1.0pt;}

< p class="MsoNormal">两种方式在形式上可能相同，但在本质上第一种方式形成了一个新的字符串，而第二周方式还是两个字符串的简单排列相加