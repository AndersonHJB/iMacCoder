---
title: 12-程序循环之 while 语句
tags: []
id: '1215'
categories:
  - - Java核心技术与实战
date: 2020-10-05 19:29:36
---

## 目录

*   用 while 语句增强找整除数的程序
*   do-while 语句——至少执行一次
*   死循环(endless loop)
*   一个看似死循环却不是死循环的例子
*   使用 break 语句结束循环

## 1\. 用 while 语句增强找整除数的程序

*   **增强点:找出 n 个可以被整除的数**
*   **while 语句的语法**
    *   条件表达式的结果是一个 boolean 值，如果为 true，则执行循环体，如果为 false，则循 环结束。
    *   While 循环体是一个代码块。所以 while 循环也是可以嵌套别的语句的，包括 while 语句， for 语句，if-else 语句等。

```python
while (条件表达式){ 
    while 循环体
}
```

```java
public class FindNDiv {
    public static void main(String[] args) {
        int n = 10; // 我们要找 10 个

        int dividend = 100; // 被除数
        int divisor = 89; // 除数

        int found = 0;
        while (found < n) {
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商是" + dividend / divisor);
                found++;
            }
            dividend++;
        }

    }
}
```

```java
178可以整除89。商是2
267可以整除89。商是3
356可以整除89。商是4
445可以整除89。商是5
534可以整除89。商是6
623可以整除89。商是7
712可以整除89。商是8
801可以整除89。商是9
890可以整除89。商是10
979可以整除89。商是11
```

## 2\. do-while 语句——至少执行一次

*   do-while 语句语法
*   do-while 语句的循环体至少执行一次
*   像 for 循环、while 循环，条件一不成立就不会执行。
*   do-while 呢，就是首先不管条件成不成立，就会先做一遍循环体中的内容。

```python
do{
    while 循环体
} while (条件表达式);
```

```java
public class DoWhileExample {
    public static void main(String[] args) {

        do {
            System.out.println("会执行一次");
        } while (false);
    }
}
```

```java
会执行一次
```

在实际的开发中，其实 do-while 用到的比较少。

## 3\. 死循环(endless loop)

*   死循环：无法结束的循环( endless loop / infinite loop)
*   一个死循环的例子
*   死循环是因为没有设置好结束条件，循环的结束条件很重要，要充分考虑各种 边界情况。

```java
public class FindNDivEndless {
    public static void main(String[] args) {
        int n = 5;

        int dividend = 100;
        int divisor = 89;

        int found = 0;
        while (found < n) {
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商是" + dividend / divisor);
            }
            dividend++;
        }

    }
}
```

## 4\. 一个看似死循环却不是死循环的例子

*   用 while 找出 5个能被 2,000,000,000整除的数
*   程序最终还是结束了，但是结果并不是我们想要的

```java
public class FindNDivNotEndless {
    public static void main(String[] args) {
        int n = 5;

        int dividend = 100;
        int divisor = 2000000000;

        int found = 0;
        while (found < n) {
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商是" + dividend / divisor);
                found++;
            }
            dividend++;
        }

    }
}
```

```java
2000000000可以整除2000000000。商是1
-2000000000可以整除2000000000。商是-1
0可以整除2000000000。商是0
2000000000可以整除2000000000。商是1
-2000000000可以整除2000000000。商是-1
```

> Int 数据溢出的例子。这是计算机和数学的区别，数学是没有边界的问题，而计算机是有的。

## 5\. 使用 break 语句结束循环

*   break 语句可以结束任何循环
*   不考虑负数的情况，使用 break 改善程序
*   理解 String start 的内容，为什么不是“从 -2147483648 开始递增”「这个字符串在生成的时候调用的是 100，所以也就是 100」

```java
public class FindNDivBetter {
    public static void main(String[] args) {
        int n = 5;

        int dividend = 100;
        int divisor = 2000000000;

        String start = "从" + dividend + "开始递增，";

        int found = 0;
        while (found < n) {
            if (dividend < 0) {
                System.out.println("被除数溢出，未找到足够的数。循环结束。");
                break;
            }
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商是" + dividend / divisor);
                found++;
            }
            dividend++;
        }

        System.out.println(start + "共找到" + found + "个可以整除" + divisor + "的数。");

        System.out.println(dividend);
    }
}
```

```java
2000000000可以整除2000000000。商是1
被除数溢出，未找到足够的数。循环结束。
从100开始递增，共找到1个可以整除2000000000的数。
-2147483648
```