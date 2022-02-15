---
title: C++函数返回值介绍
tags: []
id: '1791'
categories:
  - - C++一对一辅导
date: 2021-07-11 13:44:13
---

你好，我是悦创。C++ 函数返回值介绍（含return 0 与 return 1 与 return -1介绍） 很多人在学习 C++ 的过程中应该会留意到返回值的问题，特别是习惯用：int main() 的猿类同伴们。我们需要在函数结尾写个返回值。

```cpp
int main(){


    return 0;
}
```

# 一、返回值类型

C++ 函数可以返回多种类型，大致可分4种：

1.  返回 void(无返回值)；
    
2.  返回对象(内置类型对象和自定义对象)；
    
3.  返回指针(普通指针和函数指针)；
    
4.  返回引用；
    

## 1、返回 void (无返回值)；

初学 C++ 用的就是 void ，如果没有特殊情况，写函数还是习惯用 void。

```cpp
void fun()
{
    //默认return;
}
```

## 2、返回对象(内置类型对象和自定义对象)

**比较常见的就是返回值为 int，因为 C++ 中 0 可以表示假，非零数可以表示真。** 我比较喜欢通过返回 int 作为判断语句。用起来比较方便。比如下面的 Legal(A)函数返回值为 int，全部代码在：[【数据结构周周练】003顺序栈与链栈](https://blog.csdn.net/shuiyixin/article/details/83042402) 这篇博客。

```cpp
#include<iostream>

char A[] = { 'I','I','I','I','O','O','O','O' };
char B[] = { 'I','O','I','O','I','O','I','O' };
char C[] = { 'I','I','O','O','O','I','O','I' };
char D[] = { 'I','I','I','O','O','I','O','O' };

int Legal(char * Arr) {
    int k = 0;
    int i = 0;
    while (i < 8 && k >= 0) {
        if (Arr[i] == 'I')
            k++;
        else
            k--;
        i++;
    }
    if(k<0)
    {
        return 0;
    }
    return 1;
}

void main() {

    if (Legal(A))
        std::cout << "A 序列合法" << std::endl;
    else
        std::cout << "A 序列不合法" << std::endl;

    if (Legal(B))
        std::cout << "B 序列合法" << std::endl;
    else
        std::cout << "B 序列不合法" << std::endl;

    if (Legal(C))
        std::cout << "C 序列合法" << std::endl;
    else
        std::cout << "C 序列不合法" << std::endl;

    if (Legal(D))
        std::cout << "D 序列合法" << std::endl;
    else
        std::cout << "D 序列不合法" << std::endl;
}

```

```cpp
if (Legal(A))
    std::cout << "A 序列合法" << std::endl;
else
    std::cout << "A 序列不合法" << std::endl;
```

也可以返回我们自定义的对象，含义与内置对象一样。

```cpp
Obj fun()
{
    Obj obj;
    ....
    return obj;
}
```

## 3、返回指针(普通指针和函数指针)

返回指针主要为返回普通指针和函数指针。 普通指针即函数声明的数据类型是内置对象，如 int，char等。返回的类型与函数类型相同，用一个同样返回类型的变量作为返回值。

```cpp
int * fun(int *p)
{
    return p;
}
```

函数指针即定义一个函数，并将其返回值作为指针类型返回。

```cpp
#include<iostream>
using namespace std;

int Max(int i, int j) {
    return i >= j ? i : j;
}
typedef int(*PFun)(int, int);

PFun fun(int a) {
    cout << a << endl;
    return Max;
}
int main() {
    PFun pf;
    pf = fun(100);
    int max = pf(5, 8);
    cout << "max : " << max << endl;
}
```

## 4、返回引用

```cpp
int& fun(int &i)
{
    return i;
}
```

# 二、return 0 与 return 1 与 return -1

## 1、return 0

第一个含义一般用在主函数结束时，按照程序开发的一般惯例，表示成功完成本函数。 第二个含义表示假，一般用于bool函数返回值。在C++中也可以直接用int，返回值为0时为假。宏定义ERROR 与FLASE一般为0。

## 2、return 1

与return 0 的第二个含义相对应，表示真，正确。宏定义TRUE，OK一般为1。

## 3、return -1

与 return 0 的第一个含义相对应，表示返回一个代数值，一般用在子函数结尾。按照程序开发的一般惯例，表示该函数失败，在数据结构中，一般指数据溢出，宏定义OVERFLOW 一般为-1。

## 4、返回值

有很多人跟我说，为什么我的返回值一般都是返回1，因为函数结束时，一般用返回 0 表示函数无错误。其实函数原本的返回值应该为宏定义的 TRUE 或者 OK，为了简化程序，将重点放在算法本身上，所以很多宏定义都没有使用，如果规范来写，数据结构中的很多类型应该是用 typedef 重新设置一个新名字，特别是结构体中的数据域。因为代码我最想体现，最希望大家了解到的是算法本身，所以在函数返回值中，返回 0 代表错误，返回 1 代表正确，希望大家注意。