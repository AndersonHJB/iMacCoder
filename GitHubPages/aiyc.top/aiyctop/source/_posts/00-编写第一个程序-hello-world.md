---
title: 00-编写第一个程序—— Hello World
tags: []
id: '997'
categories:
  - - Java核心技术与实战
date: 2020-09-12 17:31:07
---

## 目录

*   **编写程序**
*   **运行程序**

## 1\. 练习题

尝试用程序输出不同的字符出来，可以尝试不同的长度，中文等。

## 2\. 详解 HelloWorld 程序

*   类 (class) 语法元素
*   Main 方法语法元素
*   `System.out.println`
*   字符串

1.  **类(class)语法元素**

```java
public class HelloWorld{

}
```

*   public class 是类修饰符
*   HelloWorld 是类名，要与文件名一致
*   大括号内是类的内容

2.  **main 方法(main method)语法元素**

```java
public class HelloWorld{
    public static void main(String[] args){

    }
}
```

*   public static void 是方法修饰符
*   小括号内是方法的参数 (parameter)
*   String\[\] args 是方法参数
*   大括号内是方法的内容，又称方法体(method body)
*   Main 方法最为特殊的一点是，它是 Java 程序的入口。就好像游戏的开始按键。

3.  **System.out.println**

```java
public class HelloWorld{
    public static void main(String[] args){
        System.out.println()
    }
}
```

*   System.out.println 是 Java 平台提供的类库的内容。可以将内容输出到标注输出，在我们的例子里，就是命令行(command line)
*   小括号里的内容还是参数列表。
*   没有参数的情况下，System.out.println 会输出一行空行，也就是类似于我们敲下一个回车。

4.  **字符串**

```java
public class HelloWorld{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
```

*   在 Java 里，双引号引起来的内容叫做一个字符串。
*   字符串不是语法内容，可以写任意字符。

5.  运行编译

```cmake
207:java_code apple$ ls
HelloWorld.java
207:java_code apple$ javac HelloWorld.java
207:java_code apple$ ls
HelloWorld.class    HelloWorld.java
207:java_code apple$ java HelloWorld
Hello World
```

*   javac HelloWorld.java：进行编译
*   HelloWorld.java：给人看的 java 代码
*   HelloWorld.class：给机器看的字节码
*   java HelloWorld：运行我们编译出来的 Java 代码，不需要带 `.class`

**注意：**

1.  Java 的文件名称需要与 class 后面的名称一直，不一致则会在编译的时候出现报错。例如类似如下的报错：

```java
207:java_code apple$ javac HelloWorld.java
HelloWorld.java:7: 错误: 类 Helloworld 是公共的, 应在名为 Helloworld.java 的文件中声明
public class Helloworld{
       ^
1 个错误
```

2.  初识 Java 程序
    1.  **初识 class**
        *   Java 语言中的一等公民，Java 程序就是一个个的类组成的
        *   类由修饰符，类名和类的内容组成。
        *   类名必须与保存类源文件的文件名相同
    2.  **初识 main 方法**
        *   Main 方法是 Java 程序执行的入口。
        *   方法由方法修饰符，方法名，参数列表和方法体等组成。