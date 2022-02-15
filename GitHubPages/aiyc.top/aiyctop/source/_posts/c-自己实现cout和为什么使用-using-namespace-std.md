---
title: C++ 自己实现cout和为什么使用 using namespace std;
tags: []
id: '1787'
categories:
  - - C++一对一辅导
date: 2021-07-09 17:16:11
---

你好，我是悦创。

> 前排提示：阅读本篇文章需要至少学过类和对象以及重载运算符的概念。

接触这么久 C++ 了，我想尝试写一个自己的 cout 了。在实现之前，先扯扯几个概念：

## 一、cout 是谁？

**不就是输出语句嘛？！这个答案太浅显。** **正确答案：** cout 是类 ostream 的一个对象，而这个对象有一个成员重载运算符函数：`operator <<`。顺便一说，类 ostream 又属于 iostream 库中，iostream 是标准的 C++ 头文件。既然如此，那么这个头文件里应该是这样写的：

```cpp
//iostream
class ostream
{
    public:
        ostream operator << (int n){输出n}
        ostream operator << (double n){输出n}
        ...
}
ostream cout;
```

这个 `ostream::operator <<` 有多个重载版本，所以形参什么类型都有，包括 int，double，char 等等。当我们写 `cout<<a` 时，其实也可以写成 `cout.operator<<(a)` 。 cout 的语句格式是：`cout<<表达式1<<表达式2<<……<<表达式n;` ，那么如果按照以上的写法，我们只能写诸如 `cout<<a;` 的语句，而不能写成 `cout<<a<<b<<c;` 这样连起来的形式，可是 C++ 里面却能实现这样的写法，这是为什么呢？ 原来在 `ostream::operator <<` 里还有一句 `return *this` 。当执行语句 `cout<<a<<b<<c;` 时，先执行 `cout.operator<<(a)` ，然后这个函数会返回 cout，其实就是返回自己本身，然后再去执行 `cout.operator<<(b)` ，然后又会去执行下一个函数，以此类推。 因此可以这样实现：

```cpp
ostream &operator << (int n)
{
    输出n;
    return *this;
}
```

## 二、什么是namespace？

我们经常在程序开头写 `using namespace std;` ，**但有没有想过是干什么用的？** 顾名思义，namespace 的意思是 **命名空间**，它是用来组织和重用代码的。那这个到底有什么用呢？ 好，我们在脑中想这么一种情况：**你写了一个库文件，里面有个名字叫 fun 的函数，很不幸你另外一个人写的库文件也有个名字叫 fun 的函数，这样就冲突了。**

```cpp
//你的库文件里：
void fun();

//别人的库文件里：
void fun();

//有人想用fun()
fun(); //究竟该用哪个？冲突了！
```

这时，我们就想了一个办法： - 把你写的 fun 函数放到一个你命名的空间里，把另外一个人写的 fun 函数放到另一个命名空间里。 - 只要有人说要用你的空间，那么他用的 fun 函数肯定是你写的 fun 函数，不会是另外一个人的。 - 如果那个人说要用另一个人的空间，那么他用的 fun 函数肯定是另一个人写的 fun 函数，不会是你的。

```cpp
//你的库文件里：
namespace you{void fun();}

//别人的库文件里：
namespace other{void fun();}

//当有人用你的函数时：
you::fun();

//当有人用另外一个人的函数时：
other::fun();

//如果有人说要用你的空间，像这样：
using namespace you;
fun();//这个其实是you::fun();，不会是other::fun();
```

> 如果，你直接使用 cout 而不使用 namespace ，那系统不知道你在用的是谁的 cout （没准有多个 cout 呢？）

扯了这么多，其实这里面表达的意思是：**为了解决名字冲突问题，引入了名字空间这个概念**，通过使用 `namespace xxx；` 你所使用的库函数或变量就是在该名字空间中定义的，这样一来就不会引起不必要的冲突了。 那我们为什么要写 `using namespace std;` ？早期的 C 将标准库功能定义在全局空间里，声明在带 `.h` 后缀的头文件里。

*   C++ 标准为了和 C 区别开，也为了正确使用命名空间，规定头文件不使用后缀 `.h` 。因此，当使用 `<iostream.h>` 时，相当于在 C 中调用库函数，使用的是全局命名空间，这也是早期的 C++ 实现；
    
*   当使用 `<iostream>` 的时候，该头文件没有定义全局命名空间，必须使用 `namespace std；` 这样才能正确使用 cout。
    

假如不写 `using namespace std;`，那就要写成 `std::cout<<` 了。每一句都这么写**很烦**，于是干脆在程序开头直接来一句 `using namespace std;`。 好了，其实这个 iostream 库大概是这么写的：

```cpp
//iostream
namespace std{
class ostream
{
    public:
        ostream operator << (int n){输出n}
        ostream operator << (double n){输出n}
        ...
}
}
std::ostream cout;
```

## 三、自己实现 cout

以上两个已经讲得很清楚了，下面上实现 cout 的代码：

```cpp
#include<stdio.h>

namespace Mystd{ //命名空间
class MyOstream{
    public:
        const MyOstream& operator<<(const int integer) const
        {
            printf("%d", integer);
            return *this;
        }
        const MyOstream& operator<<(const char *s) const
        {
            printf("%s", s);
            return *this;
        }
};
}

void Print()
{
    Mystd::MyOstream MyAnothercout;
    MyAnothercout<<"Print";
}

int main()
{
    Mystd::MyOstream Mycout;
    int a = 30, b = 20;
    Mycout<<"number:"<<a<<" "<<b<<"\n";
    Print();
    return 0;
}

```

本代码已经通过编译，并且能正确输出。对于C++的这些特性，当我们学得深入了以后，就很有必要弄懂了。

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210709171526142.png)