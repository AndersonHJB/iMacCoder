---
title: 03-Java 中的基本数据类型
tags: []
id: '1047'
categories:
  - - Java核心技术与实战
date: 2020-09-18 16:37:00
---

## 目录

*   认识二进制
*   数字的基本数据类型
*   布尔和字符数据类型
*   使用各种基本数据类型

你好，我是悦创。 上一章，我们如果 int 赋值的值超过 int 的最大限度，那我们要如何操作呢？

```java
public class BigNumber {
    public static void main(String[] args){
        int BigNum = 9999999999;//错误代码
        long Number= 9999999999L;//解决方法
    }
}
```

如果你使用的是 Ide ， 那在编写的时候，还没运行就会出现红色的波浪线，如下： ![image-20200914194030991](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200918163533.png)

## 1\. 认识二进制

*   **十进制**：每一位可以是 0~9 这 10 个值，到 10 进位。一百用十进制表示就是 100 ，十就是 10。
*   **二进制**：每一位可以是 0 和 1 这两个值，到 2 进位。一百用二进制表示就是 1100100，十就是 1010。
*   **十六进制**：每一位可以是 0~F 这 15 个值，到 16 进位。一百用十六进制表示就是 64，十就是 A。
*   **bit 和 byte**：
    *   一个二进制的位叫做一个 bit。俗称小 b。网络宽带中的单位，都是小 b「bit」
    *   八个二进制的位，组成一个byte，俗称大B。硬盘等存储的单位，都是大 B「byte」「1 byte = 8 bit」
    *   Byte 是计算机中基本的衡量存储的单位，计算机在对外使用时不会用小 b 作为划分存储的单位。

## 2\. 数字的基本数据类型

*   **整数类型**
    *   byte 占用 1 个 byte，值域是 -128 ~ 127
    *   short 占用 2 个byte，值域是 -32768~32767
    *   int 占用 4 个 byte，值域是 -2147483648~2147483647。Java 中整数缺省是 int 类型「缺省，即系统默认状态，意思与“默认”相同。」
    *   long 占用 8 个 byte，值域是 -9223372036854774808~9223372036854774807
*   **浮点(小数)类型**
    *   float – 有精度，值域复杂 ±340282346638528859811704183484516925440
    *   double–精度是 float 的一倍，占用 8 个 byte。Java 中浮点数缺省是 double 类型。
*   **符号位**
    

* * *

精度，下面代码可知计算机并不能把无限循环的小数表示出来，这样我们就能对精度有个直观的认识。

```java
public class FloatCalc {
    public static void main(String[] args) {
        System.out.println(1 / 3);
        System.out.println(1 / 3.0);
        System.out.println(1.0 / 3);
    }
}
```

## 3\. 布尔和字符数据类型

*   **布尔和字符数据类型**
    *   boolean占用 4 个 byte ，值域是 true,false 。
    *   char 占用 2 个 byte，值域是所有字符(最多 65535 个)「字符是单引号」

```java
public class BooleanAndChar {
    public static void main(String[] agrs) {
//        Boolean
        System.out.println(1 < 2); // true
        System.out.println(1 > 2); // false
//        Char
        System.out.println("ABC"); // 双引号是字符串 // ABC
        System.out.println('A'); // char 是单引号 // A 
    }
}
```

## 4\. 使用各种基本数据类型

*   例程
*   L 后缀
*   感受浮点数精度
*   整数缺省是 int 类型，浮点数缺省是 double 类型
*   编译错误的定位和修正

```java
import java.math.BigDecimal;

public class PrimaryTypes {
    public static void main(String[] args) {
        byte byteVar = 100;
        System.out.println(byteVar); // 100

        short shortVar = 30000;
        System.out.println(shortVar); // 30000

        int intVar = 1000000000;
        System.out.println(intVar); // 1000000000

        long longVar = 80000000000L; // 为了方便区分 l 和 1 ，所以这里我们用大写的 L。
        System.out.println(longVar); // 80000000000

        float floatVar = 100.0000000666F; // 大 F 和 小 f 都是可以容易区分的。f 其实就是 float。 
        System.out.println(floatVar); // 100.0

        double doubleVar = 100.0000000666;
        System.out.println(doubleVar); // 100.0000000666

        boolean booleanVar = true;
        // boolean booleanVar = false;
        System.out.println(booleanVar); // true

        char charVar = 'a';
        System.out.println(charVar); // a

    }
}
```

补充，我们知道 float 的精度会比 double 少，我用观察上面代码可知，我特意的把 float 和 double 的字面值设置为同一个，从输出结果可知，double 精度大于 float。