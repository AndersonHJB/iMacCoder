---
title: 09-程序执行流程之 if-else 语句
tags: []
id: '1095'
categories:
  - - Java核心技术与实战
date: 2020-09-26 16:42:07
---

## 目录

*   顺序执行
*   怎么能多买几个热包子？用 if-else
*   增强寻找可以被整除的程序
*   if-else 的嵌套
*   if-else 的简化

## 1\. 顺序执行

*   代码块的执行是顺序执行
*   只要程序运行过程中不出错，就会一行行的向下顺序执行

## 2\. 怎么能多买几个热包子？用 if-else

*   **买包子的问题**
    *   买 3 个肉包子
    *   如果是刚出笼的热肉包子，就多买两个呢？
*   **if-else 语法**
    *   if-else 语法，只有一个语句块被执行
    *   if 和 else 都是 Java 中的关键字
    *   if 语法
    *   把 if-else 看做一个表达式，程序整体还是顺序执行的
    *   使用 if-else 来多买两个肉包子

```java
if (boolean 值) { if 语句块
} else {
else 语句块
}
```

```java
public class Baozi {
    public static void main(String[] args) {
        int baozi = 3;
        System.out.println("买了" + baozi + "个肉包子"); 
        // 买了3个肉包子
    }
}
```

```java
public class IfElseBaozi {
    public static void main(String[] args) {
        int baozi = 3;

        boolean baoziGangchuLong = true;

        if (baoziGangchuLong) {
            baozi = baozi + 2;
            System.out.println("包子刚刚出笼，买了" + baozi + "个肉包子"); 
            // 包子刚刚出笼，买了5个肉包子
        } else {
            System.out.println("买了" + baozi + "个肉包子");
        }
    }
}
```

## 3\. 增强寻找可以被整除的程序

*   **增强点**
    *   只输出可以整除的数
    *   输出商

```java
public class FindDiv {
    public static void main(String[] args) {
        int a = 35;
        int b = 9;

        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;
        if (a % b == 0) {
            System.out.println(a + "可以整除" + b + "。商为" + (a / b));
        }
        a++;


    }
}
```

```java
36可以整除9。商为4
45可以整除9。商为5
54可以整除9。商为6
63可以整除9。商为7
72可以整除9。商为8
81可以整除9。商为9
90可以整除9。商为10
99可以整除9。商为11
108可以整除9。商为12
117可以整除9。商为13
126可以整除9。商为14
```

## 4\. if-else 的嵌套

*   **求最大的数**
    *   if-else 就是一个语句，可以是另一个语句的一部分，也可以是 if-else 的一部 分，即嵌套。
    *   求 a，b 和 c 三个数的最大数。

```java
public class IfElseNest {

    public static void main(String[] args) {
        int a = 10;
        int b = 99;
        int c = 99;

        System.out.println("a=" + a + ". b=" + b + ". c=" + c);
        if (a == b && b == c) {
            System.out.println("a，b和c三个数等大。");
        } else {
            if (a > b) {
                if (a > c) {
                    System.out.println("a是最大的数。");
                } else {
                    if (a == c) {
                        System.out.printf("a和c等大。");
                    } else {
                        System.out.println("c是最大的数。");
                    }
                }
            } else {
                if (b > c) {
                    if (b == a) {
                        System.out.println("a和b是等大的数。");
                    } else {
                        System.out.println("b是最大的数。");
                    }
                } else {
                    if (b == c) {
                        System.out.println("b和c等大。");
                    } else {
                        System.out.println("c是最大的数。");
                    }
                }
            }
        }
    }
}
```

```java
a=10. b=99. c=99
b和c等大。
```

## 5\. if-else 的简化

*   **if-else 省略大括号**
    *   如果 if 或者 else 的语句块只有一个语句，可以省略大括号
    *   简化求最大数的程序

```java
if (boolean 值) 
    if 语句块
else
    else 语句块
```

```java
if (boolean 值) { 
    if 语句块
} else if () { 
    if 语句块
} else {
    else 语句块
}
```

```java
public class OneStatementIfEles {
    public static void main(String[] args) {

        int a = 10;

        System.out.println("省略大括号");
        if (a > 0)
            System.out.println("a大于0");
        else
            System.out.printf("a小于等于0");

        System.out.println("比较大小的完整的写法");
        if (a > 0) {
            System.out.println("a大于0");
        } else {
            if (a == 0) {
                System.out.println("a等于0");
            } else {
                System.out.println("a小于0");
            }
        }

        System.out.println("比较大小的省略所有大括号的方法");
        if (a > 0)
            System.out.println("a大于0");
        else if (a == 0)
            System.out.println("a等于0");
        else
            System.out.println("a小于0");


        System.out.println("比较大小的代码块有多个语句的最优写法");
        if (a > 0) {
            System.out.println("a大于0");
            System.out.printf("买" + a + "个肉包子");
        } else if (a == 0) {
            System.out.println("a等于0");
            System.out.printf("不买肉包子了！");
        } else {
            System.out.println("a小于0");
            System.out.println("肉包子吃多了！");
        }
    }
}
```

```java
省略大括号
a大于0
比较大小的完整的写法
a大于0
比较大小的省略所有大括号的方法
a大于0
比较大小的代码块有多个语句的最优写法
a大于0
```

```java
public class SimpleIfElse {

    public static void main(String[] args) {
        boolean condition = true;

        if (condition) {
            System.out.println("condition的值为真");
        } else {
            System.out.printf("condition的值为假");
        }

        int a = 10;
        int b = 20;
        if (a < b) {
            System.out.println("a的值为" + a + ", b的值为" + b + ". a<b是真的");
        }

        System.out.println("如论如何都会执行到");
    }

}
```

```java
condition的值为真
a的值为10, b的值为20. a<b是真的
如论如何都会执行到
```

## 6\. 补充

```java
/*
* @Author: AI悦创
* @Date:   2020-09-26 15:10:16
* @Last Modified by:   aiyuechuang
* @Last Modified time: 2020-09-26 15:26:25
*/
public class Example {
    public static void main(String[] args) {
        // int a = 10;
        // int b = 99;
        // int c = 99;
        int a, b, c = 10;
        System.out.println(a);
    }
}
```

```java
Example.java:13: 错误: 可能尚未初始化变量a
        System.out.println(a);
                           ^
1 个错误
```

你只能这样声明赋值：

```java
int a = 10, b = 99, c = 99;
```