---
title: 13-程序执行流程之 switch 语句
tags: []
id: '1218'
categories:
  - - Java核心技术与实战
date: 2020-10-07 21:06:24
---

## 目录

*   将阿拉伯数字转换为中文数字
*   使用 switch 语句简化程序
*   switch 语法中的 break
*   switch 语句语法点总结

## 1\. 将阿拉伯数字转换为中文数字

*   使用 if 可以完成，但是略显不够整洁
*   能够根据两个值相比较，进入某个代码块最适合这个情况

```java
public class IfElseNum {
    public static void main(String[] args) {

        int n = 1;

        String ret = n + "对应的汉字是";
        if (n == 0) {
            ret = ret + "零";
        } else if (n == 1) {
            ret = ret + "壹";
        } else if (n == 2) {
            ret = ret + "贰";
        } else if (n == 3) {
            ret = ret + "叁";
        } else if (n == 4) {
            ret = ret + "肆";
        } else if (n == 5) {
            ret = ret + "伍";
        } else if (n == 6) {
            ret = ret + "陆";
        } else if (n == 7) {
            ret = ret + "柒";
        } else if (n == 8) {
            ret = ret + "捌";
        } else if (n == 9) {
            ret = ret + "玖";
        } else {
            System.out.println("错误的值" + n + "。值需要在大于等于1，小于等于9。");
        }

        System.out.println(ret);
    }
}
```

```java
1对应的汉字是壹
```

## 2\. 使用 switch 语句简化程序

*   **switch 语句的语法**

```java
switch (用于比较的 int 值){
    case 目标值 1，对应一个 if else(xxx):
        匹配后可以执行的语句
    case 目标值 2，不可以与别的 case 字句重复 :
        匹配后可以执行的语句
    default (对应最后的 else，可选):
        default 语句 
}
```

```java
public class IfElseSwitch {
    public static void main(String[] args) {

        int n = 2;

        String ret = n + "对应的汉字是";

        switch (n) {
            case 1:
                ret = ret + "壹";
                break;
            case 2:
                ret = ret + "贰";
                break;
            case 3:
                ret = ret + "叁";
                break;
            case 4:
                ret = ret + "肆";
                break;
            case 5:
                ret = ret + "伍";
                break;
            case 6:
                ret = ret + "陆";
                break;
            case 7:
                ret = ret + "柒";
                break;
            case 8:
                ret = ret + "捌";
                break;
            case 9:
                ret = ret + "玖";
                break;
            default:
                System.out.println("错误的值" + n + "。值需要大于等于1，小于等于9。");
        }
        System.out.println(ret);
    }
}
```

```java
2对应的汉字是贰
```

为了方便演示，我把上面的代码写的简洁一些，改成如下：

```java
/*
* @Author: AI悦创
* @Date:   2020-10-07 20:24:46
* @Last Modified by:   aiyuechuang
* @Last Modified time: 2020-10-07 20:30:21
*/
public class Example {
    public static void main(String[] args) {
        int n = 1;

        String ret = n + "对应的汉字是：";

        switch (n) {
            case 1:
                ret = ret + "壹";
                // System.out.println(ret);
                break;

            case 2:
                ret = ret + "贰";

            default:
                System.out.println("错误的值" + n + "。值需要大于等于1，小于等于3。");
        }
        System.out.println(ret);

    }
}
```

```java
public class Example {
    public static void main(String[] args) {
        int n = 1;

        String ret = n + "对应的汉字是：";

        switch (n) {
            case 1:
                int a;
                ret = ret + "壹";
                break;

            case 2:
                int a;
                ret = ret + "贰";

            default:
                System.out.println("错误的值" + n + "。值需要大于等于1，小于等于3。");
        }
        System.out.println(ret);

    }
}
```

这样声明 a 变量是会报错的。 虽然，你有可能觉得，执行完 `case 1` 就不会执行 `case 2` ，但你需要知道的是，case 不是一个代码块，「并不是像有用 {} 括起来的代码一样」所以在它的作用域里面不能有重名的变量。

> Ps：同一个代码块是不能有重名的变量的。

## 3\. switch 语法中的 break

*   switch 语句如果没有遇到 break，会一直执行下去。
*   如果我们的例子没有 break 会怎么样
*   没有 break 的情况也有用武之地

```java
public class IfElseSwitchNoBreak {
    public static void main(String[] args) {

        int n = 5;

        String ret = n + "对应的汉字是";

        switch (n) {
            case 1:
                ret = ret + "壹";
            case 2:
                ret = ret + "贰";
            case 3:
                ret = ret + "叁";
            case 4:
                ret = ret + "肆";
            case 5:
                ret = ret + "伍";
            case 6:
                ret = ret + "陆";
            case 7:
                ret = ret + "柒";
            case 8:
                ret = ret + "捌";
            case 9:
                ret = ret + "玖";
            default:
                System.out.println("错误的值" + n + "。值需要大于等于1，小于等于9。");
        }
        System.out.println(ret);
    }
}
```

```java
错误的值5。值需要大于等于1，小于等于9。
5对应的汉字是伍陆柒捌玖
```

## 4\. switch 语句语法点总结

*   switch 语句中用于比较的值，必须是 int 类型
*   switch 语句适用于有固定多个目标值匹配，然后执行不同的逻辑的情况
*   必须使用 break 语句显示的结束一个 case 子句，否则 switch 语句会从 第一个 match 的 case 语句开始执行直到遇到 break 语句或者 switch 语句结束
*   default 子句是可选的，如果所有的 case 语句都没有匹配上，才会执行 default 中的代码

```java
public class IfElseSwitchNoBreak2 {
    public static void main(String[] args) {

        int n = 3;

        switch (n) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                System.out.println("n的值小于等于1大于等于5，为" + n);
            case 6:
            case 7:
            case 8:
            case 9:
                System.out.println("n的值小于等于6大于等于9，为" + n);
            default:
                System.out.println("错误的值" + n + "。值需要大于等于1，小于等于9。");
        }
    }
}
```

```java
n的值小于等于1大于等于5，为3
n的值小于等于6大于等于9，为3
错误的值3。值需要大于等于1，小于等于9。
```