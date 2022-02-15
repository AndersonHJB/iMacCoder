---
title: 10-程序循环之 for 语句
tags: []
id: '1192'
categories:
  - - Java核心技术与实战
date: 2020-10-02 18:42:27
---

## 目录

*   简化输出连续 26 个字符的程序
*   简化并增强找整除数的程序
*   break 语句
*   continue 语句

## 1\. 简化输出连续 26 个字符的程序

*   **for 语句**
    *   让程序在满足某条件时，重复执行某个代码块。for 是 Java 中的关键字
    *   for 语句语法和简单的示例程
    *   初始语句在 for 循环开始前执行一次，以后不再执行；循环体条件表达式在每次循环体执行前会执行，如果为 true，则执行循环体，否则循环结束；循环体后语句会在每次循环执行后被执行;

```java
for (初始语句; 循环体条件表达式; 循环体后语句) { 
    for 循环体
}
```

*   **使用 for 简化输出连续26个字符的程序**

```java
public class SimpleFor {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.println("i的值是：" + i);
        }
    }
}
```

```java
i的值是：0
i的值是：1
i的值是：2
i的值是：3
i的值是：4
i的值是：5
i的值是：6
i的值是：7
i的值是：8
i的值是：9
```

```java
public class PrintChars {
    public static void main(String[] args) {
        char ch = '我';
        int startNum = ch;
        for (int i = 0; i < 26; i++) {
            int newNum = startNum + i;
            System.out.println(newNum + "\t" + ((char) newNum));
        }
    }
}
```

```java
25105   我
25106   戒
25107   戓
25108   戔
25109   戕
25110   或
25111   戗
25112   战
25113   戙
25114   戚
25115   戛
25116   戜
25117   戝
25118   戞
25119   戟
25120   戠
25121   戡
25122   戢
25123   戣
25124   戤
25125   戥
25126   戦
25127   戧
25128   戨
25129   戩
25130   截
```

**补充：多运行几次感受感受**

```java
/*
* @Author: AI悦创
* @Date:   2020-09-27 10:09:59
* @Last Modified by:   aiyuechuang
* @Last Modified time: 2020-09-27 10:48:30
*/
public class Example {
    public static void main(String[] args) {
        char ch = '我';
        int startNum = ch;
        for (int i = 0; i < 26; i++) {
            // System.out.println(((int) startNum ++) + "\t" + (char) startNum); // 错误结果
            System.out.println((char) startNum + "\t" + (int) startNum ++); // 正确结果
        }

    }
}
```

> 当然，我们还可以吧 startNum 单独提取出来写，也是可以的。不过写在哪呢？留个思考给同学们！实在想不出来的可以留言哦，我看到会回复你的。

## 2\. 简化并增强找整除数的程序

*   **简化和增强找整除数的程序**
    *   使用 for 语句让程序简洁
    *   增加新功能，输出最多10个可以整除的数
    *   条件布尔表达式可以用 for 语句外部的变量
    *   循环体执行后的语句可以有多个表达式，用逗号分开

**1\. 使用 for 语句让程序简洁**

```java
public class CalcDivFor {
    public static void main(String[] args) {
        int divided = 100;
        int divisor = 3;

        for (int i = 0; i < 100; i++) {
            if (divided % divisor == 0) {
                System.out.println(divided + "可以整除" + divisor + "。商为" + divided / divisor);
            }
            divided++;

        }


    }
}
```

**2\. 增加新功能，输出最多10个可以整除的数**

```java
public class CalcDivFor {
    public static void main(String[] args) {
        int divided = 100;
        int divisor = 3;

        int found = 0;
        for (int i = 0; i < 100 && found < 10; i++) {
            if (divided % divisor == 0) {
                System.out.println(divided + "可以整除" + divisor + "。商为" + divided / divisor);
                found++;
            }
            divided++;

        }


    }
}
```

**3\. 条件布尔表达式可以用 for 语句外部的变量**

```java
public class CalcDivForWithLimit {
    public static void main(String[] args) {
        int dividend = 100;
        int divisor = 3;

        int foundCount = 0;
        int toBeFound = 5;
        for (int i = 0; i < 100 && toBeFound > foundCount; i++) {
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商为" + dividend / divisor);
                foundCount++;
            }
            dividend++;
        }
        System.out.println("总共找到" + foundCount + "个可以整除" + divisor + "的数。");
    }
}
```

```java
public class CalcDivForWithLimit2 {
    public static void main(String[] args) {
        int dividend = 100;
        int divisor = 3;

        int foundCount = 0;
        int toBeFound = 5;
        for (int i = 0; i < 100 && toBeFound > foundCount; i++, foundCount++) {
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商为" + dividend / divisor);
            }
            dividend++;
        }
        System.out.println("总共找到" + foundCount + "个可以整除" + divisor + "的数。");
    }
}
```

**4\. 循环体执行后的语句可以有多个表达式，用逗号分开**

```java
public class CalcDivFor {
    public static void main(String[] args) {
        int divided = 100;
        int divisor = 3;

        int found = 0;
        for (int i = 0; i < 100 && found < 10; i++, divided++) {
            if (divided % divisor == 0) {
                System.out.println(divided + "可以整除" + divisor + "。商为" + divided / divisor);
                found++;
            }
            // divided++;

        }


    }
}
```

## 3\. Break 语句

*   **结束循环**
    *   break 语句可以结束循环
    *   在求整除程序中使用 break 提前结束循环

```java
public class CalcDivBreak {
    public static void main(String[] args) {
        int dividend = 100;
        int divisor = 3;

        int foundCount = 0;
        int toBeFound = 5;
        for (int i = 0; i < 100; i++) {
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商为" + dividend / divisor);
                foundCount++;
            }
            dividend++;

            if (foundCount >= toBeFound) {
                break;
            }
        }
        System.out.println("总共找到" + foundCount + "个可以整除" + divisor + "的数。");
    }
}
```

```java
102可以整除3。商为34
105可以整除3。商为35
108可以整除3。商为36
111可以整除3。商为37
114可以整除3。商为38
总共找到5个可以整除3的数。
```

## 4\. continue 语句

*   **跳过不符合条件的循环**
    *   continue 语句可以结束当次循环的执行，开始下一次循环体的执行

```java
public class CalcDivBreakAndContinue {
    public static void main(String[] args) {
        int dividend = 10;
        int divisor = 21;

        int foundCount = 0;
        int toBeFound = 5;
        for (int i = 0; i < 200; i++, dividend++) {
            if (divisor > dividend) {
                System.out.println("跳过" + dividend + ", 因为它比除数" + divisor + "小。");
                continue;
            }
            if (dividend % divisor == 0) {
                System.out.println(dividend + "可以整除" + divisor + "。商为" + dividend / divisor);
                foundCount++;
            }

            if (foundCount >= toBeFound) {
                break;
            }
        }
        System.out.println("总共找到" + foundCount + "个可以整除" + divisor + "的数。");
    }
}
```

```java
跳过10, 因为它比除数21小。
跳过11, 因为它比除数21小。
跳过12, 因为它比除数21小。
跳过13, 因为它比除数21小。
跳过14, 因为它比除数21小。
跳过15, 因为它比除数21小。
跳过16, 因为它比除数21小。
跳过17, 因为它比除数21小。
跳过18, 因为它比除数21小。
跳过19, 因为它比除数21小。
跳过20, 因为它比除数21小。
21可以整除21。商为1
42可以整除21。商为2
63可以整除21。商为3
84可以整除21。商为4
105可以整除21。商为5
总共找到5个可以整除21的数。
```