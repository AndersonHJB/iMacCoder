---
title: 04-Java 中的运算符
tags: []
id: '1051'
categories:
  - - Java核心技术与实战
date: 2020-09-19 17:10:33
---

## 目录

*   什么是运算符
*   取模运算符
*   整数的除法运算
*   比较运算符和布尔运算符
*   小括号运算符
*   运算符优先级
*   理解运算符优先级

## 1\. 什么是运算符

*   运算符对一个或者多个值进行运算，并得出一个运算结果。
*   运算符的运算结果类型有的是固定的，有时候会根据被计算的值变化。比如：两个 int 相加，结果的类型就是 int。两个 byte 相加，返回值的类型就是 byte。
*   混淆点：除赋值运算符外，运算符本身不会更改变量的值「代码 OprtNotChangeVariableValue」

```java
public class OprtNotChangeVariableValue {
    public static void main(String[] args) {
        int a = 100;

        System.out.println(a + 1);

        System.out.println(a);
    }
}
```

## 2\. 取模运算符 %「取余数」

*   用来计算余数
*   负数也可以被取模
*   负数也可以取模
*   小数也可以取模「很多时候是用不到的」

```java
public class ModCalc {
    public static void main(String[] args) {
        int num = 10;

        System.out.println(num % 2); // 0
        System.out.println(num % -3); // 1
        System.out.println(num % 4); // 2
        System.out.println(num % 5); // 0
        System.out.println(num % -6); // 4
    }
}
```

如果把 10 改成 -10 呢？

```java
public class ModCalc {
    public static void main(String[] args) {
        int num = -10;

        System.out.println(num % 2); // 0
        System.out.println(num % -3); // -1
        System.out.println(num % 4); // -2
        System.out.println(num % 5); // 0
        System.out.println(num % -6); // -4
    }
}
```

也就是说 num 是决定我们取摸结果的正负的。

## 3\. 整数的除法运算

int 除以 int 还是 int，不会变成浮点数「两个 int 相乘也是不会变成 double 的」

```java
public class IntegerDiv {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        System.out.println(a / b); // 3
        System.out.println(b / a); // 0
        float c = 3.0f; // 用 double 也是可以的
        System.out.println(a / c); // 3.3333333
        System.out.println(c / a); // 0.3

    }
}
```

这样就是前面为什么要在两个整数做除法的是，在其中一个要加 `.0` 原因。「任意一个数是浮点数就可以」

## 4\. 比较运算符和布尔运算符

*   **比较运算符**
    *   \>
    *   \>=
    *   <
    *   <=
    *   !=
    *   \==
*   **布尔运算符**
    *   ! 叫做 非 运算符，not 运算符。!true 是 false，!false 是 true。
    *   & 叫做 且 运算符，and 运算符。true & true 是 true，true & false 是 false。
    *   && 叫做 且且 运算符，andand 运算符。运算结果和 & 一样。
    *   叫做 或 运算符，or 运算符。true false 是 true，false false 是 false，true true 是 true。
    *   叫做 或或 运算符，oror 运算符。运算结果和 一样。

> 这里强调一点，根据一个具有实际开发十几年经验的前辈所得来的经验，能用 **且且、或或** 运算符，尽量使用 **且且、或或** ，具体原因先看如下代码：

```java
public class BooleanOprt {
    public static void main(String[] args) {
        // 我们也可以使用比较运算符生成的 boolean 来进行比较。
        boolean a = true; // 1 < 2
        boolean b = false; // 1 > 2

        // // &$ 且且 （andand）
        // & 且 （and）
        // //  或或 （oror）
        //  或 （or）


        System.out.println(a && b); // false 
        System.out.println(a & b); // false
        System.out.println(a  b); // true
        System.out.println(a  b); // true

        System.out.println(a  (10 / 0 > 1)); // true
        // 这个 或或运算，Java 会对它进行一个优化。
        // 就是说：或或左边一旦是符合条件为真「也就是可以决定这个表达式为真」
        // 那么它就不会对后面的表达式进行运算了。
        System.out.println(a  (10 / 0 > 1)); // true
        // 单个或，就是说：不管现在条件是否成立，都要给我判断右边的情况「运算它们」。
        // 它对结果没有影响，所以上面我尝试引入一个错误，这样我们就能知道这个表达式到底有没有执行。
        // 10 / 0 > 1 本身就是一个错误的表达式
    }
}
```

补充：[Java的布尔运算「专栏补充」](https://blog.csdn.net/qq_33254766/article/details/108682947)

## 5\. 小括号运算符

小括号运算符内可以包含任何运算符，决定运算符的顺序

```java
public class ParentOprt {
    public static void main(String[] args) {
        int a = 10;
        int b = 88;
        boolean c = ((a + b) * a - 9 * (a + b)) == (a + b);

        System.out.println(c);
    }
}
```

## 6\. 运算符优先级

*   **运算符优先级**
    *   ()
    *   !
    *   \*,/,%
    *   +,-
    *   \>,>=,<,<=
    *   \\==
    *   !=
    *   &,&&,,
    *   \\=

## 7\. 理解运算符优先级

*   **理解运算符，灵活记忆优先级**
    *   为什么等号的优先级最低？「等号是个赋值运算，肯定是要等都运算完了再进行赋值的」
    *   为什么布尔运算符的优先级低于比较运算符？「因为布尔运算符操作的是布尔值，除了你直接写 true 或 false 之外，布尔值就是从比较出来的」
    *   为什么比较运算符的优先级比算数运算符低？「有可能你要比较的这个数是比较运算符比较出来的」
*   **不要死记硬背，用括号让逻辑更清晰**