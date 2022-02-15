---
title: 05-Java 中的位运算符
tags: []
id: '1058'
categories:
  - - uncategorized
date: 2020-09-21 20:50:31
---

## 目录

*   字面值的八进制和十六进制
*   按位运算符
*   位移运算符
*   位运算符不会改变原变量的值
*   位运算符用处

## 1\. 字面值的八进制和十六进制

*   **以 0 开头的整数为八进制**
    *   05 就是十进制的 5
    *   011 就是十进制的 9
*   **以 0x 开头的整数位十六进制**
    *   0xF 就是十进制的 15
    *   0x11 就是十进制的 17

```java
public class LiteralNumber {
    public static void main(String[] args) {
        int a = 05;
        int b = 011;
        int c = 0xF;
        int d = 0x11;

        System.out.println(a); // 5
        System.out.println(b); // 9
        System.out.println(c); // 15
        System.out.println(d); // 17
    }
}
```

## 2\. 按位运算符

*   **按位运算符**
    
    *   按位并(AND):\\&
    *   按位或(OR):|
    *   按位异或(XOR):\\^ ：一句话，相异为真 ，运算规则是：两个数转为二进制，然后从高位开始比较，如果相同则为0，不相同则为1。
        
    *   按位取反:\\~
        
    
    > 储备知识：int 有 4 个字节，每个字节有 8 位，一共 32 位。也就是这样的形式： 00000000 00000000 00000000 00000000； 32 的二进制是：100000 ，把 32 的二进制放入上面储备知识中得出这样的效果：00000000 00000000 00000000 00100000。当然你也可以缩写成这样的效果：00100000。 接下来我们可以进行取反，取反之后为的结果为： 11011111；
    

> 操作的维度是 bit

```java
public class BitCalc {
    public static void main(String[] args) {
        // 二进制的 1111 1000
        int a = 0xF8;
        // 二进制的 1111 0100
        int b = 0xF4;
        // 二进制的 1111 1111
        int c = 0xFF;
        // int d = 0123; // 八进制
        // System.out.println(a);// 输出十进制的数 
        // System.out.println(d);
        System.out.println(a & b); // 与 // 240
        System.out.println(a  b); // 或 // 252
        System.out.println(a ^ b); // 异或 // 12

        System.out.println(~c); // -256
        // 按位取反，数的第一位是符号位，0 代表正数，1 代表负数； 
    }
}
/* 补充：
a   1111 1000
b   1111 0100
&   1111 0000
   1111 1100
^   0000 1100
C   255 > 11111111
～   -255
*/
```

补充：[二进制：不了解计算机的源头，你学什么编程](https://blog.csdn.net/qq_33254766/article/details/108702875) 在实际的工作中呢，按位运算其实用到的不多。并且在日后的工作中，我并不推荐大家有使用位运算符的倾向。「当你觉得这个问题可以用位运算符解决的时候，你应该也要思考一下，这个问题是不是还有可以让人更容易理解的解决方法。」

## 3\. 位移运算符

现代计算机是基于二进制的，我们就来看看，计算机语言中针对二进制的位操作。这里的**位操作**，也叫作**位运算**，就是直接对内存中的二进制位进行操作。常见的二进制位操作包括向左移位和向右移位的移位操作，以及“或”“与”“异或”的逻辑操作。「上面已经讲过与或非」下面我们来看位移运算符。

*   **位移运算符**
    *   \>>:符号位不动，其余位右移，符号位后边补 0，又称带符号右移「原本正数，那移动之后依然是正数。反之亦然。」
        *   换一种方法理解：num << 1,左移1位相当于 num 乘以 2 的 1 次方
    *   \>>>:符号位一起右移，左边补 0，又称无符号右移「原本正数，移动之后就变成了负数」
        
        *   只是对 32 位和 64 位的值有意义，例如： hashMap 中用到的 h >>> 16 ，举例 15 >>> 2 = 3
            *   因为在 Java 中，所有数据的表示方式都是以补码形式来表示，如果没有特别的说明，Java 中的数据类型默认为 int，int数据类型的长度为 4 个字节，就是 32bit 的意思
        *   15 转为二进制是 1111，向右无符号移动 2 位,空位补 0 为 0011 则
        
        ```java
        System.out.println(Integer.toBinaryString(15>>>2));
        ```
        
    *   \\<<:左移，右边补 0。左移没有带符号位一说，因为符号位在最左侧
        *   换一种方法理解：num >> 1,右移 1 位相当于 num 除以 2 的 1 次方

> 操作的维度是也是 bit

```java
public class BitShift {
    public static void main(String[] args) {
        int a = 0x400;
        System.out.println(a); // 1024
        System.out.println(a >> 1); // 512
        System.out.println(a >> 2); // 256

        System.out.println(a << 1); // 2048
        System.out.println(a << 2); // 4096

        int b = -0x400;
        System.out.println(b); // -1024
        System.out.println(b >> 1); // -512
        System.out.println(b >> 2); // -256

        System.out.println(b << 1); // -2048
        System.out.println(b << 2); // -4096

        System.out.println(b >>> 1); // 2147483136 补码的方式代表负数
        System.out.println(b >>> 2); // 1073741568 补码的方式代表负数


    }
}
```

左移乘，右移除

## 4\. 位运算符不会改变原变量的值

**按位运算符不会改变原本的变量的值** **位移运算符不会改变原本的变量的值**

```java
public class BitOprtNotChangeVariableValue {
    public static void main(String[] args) {
        int a = 0x400;
        int b = 0xF4;
        int c = 0xFF;

        System.out.println(a >> 2); // 256
        System.out.println(~a); // -1025
        System.out.println(a  0x8); // 1032

        System.out.println(a); // 1024

    }
}
```

## 5\. 位运算符用处

*   **按位运算符**
    *   掩码(MASK)
*   **位移运算符**
    *   高效除以 2

```java
public class BitOprtUsage {

    public static void main(String[] args) {
        int base = 1;
        int is_student_mask = base;
        int is_programmer_mask = base << 1;
        int is_driver_mask = base << 2;
        int is_painter_mask = base << 3;

        int data = 5; // 二进制是 101

        boolean isStudent = (data & is_student_mask) != 0;
        System.out.println(isStudent); // true

        boolean isProgrammer = (data & is_programmer_mask) != 0;
        System.out.println(isProgrammer); // false

        boolean isDriver = (data & is_driver_mask) != 0;
        System.out.println(isDriver); // true

        boolean isPainter = (data & is_painter_mask) != 0;
        System.out.println(isPainter); // false
    }
}
```