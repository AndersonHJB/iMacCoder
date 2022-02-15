---
title: Python一对一题目辅导「PTA 题目讲解·难度系数：基础」
tags: []
id: '1337'
categories:
  - - Python一对一
date: 2021-01-07 15:10:12
---

点击此链接获得完整文章阅读： [Python一对一题目辅导「PTA 题目讲解·难度系数：基础」](https://mp.weixin.qq.com/s/kinioqMIX1ufuRePMY5pvAhttp:// "Python一对一题目辅导「PTA 题目讲解·难度系数：基础」")

# 题目范围

# 作业 7:

## 6-2 编写函数计算一个或不特定多个数的乘积（高教社，《Python编程基础及应用》习题8-6） (4分)

### 1、函数接口定义：

```python
def caculate(*t)
```

打 \* 号的参数 t 接受多个参数成员，参数成员预期为整数或浮点数类型。 知识点讲解 Linke：[https://www.aiyc.top/126.html](https://www.aiyc.top/126.html)

#### \*args 的用法

`*args` 和 `**kwargs` 主要用于函数定义。 你可以将不定数量的**参数**传递给一个函数。 **这里的不定的意思是：**预先并不知道，函数使用者会传递多少个参数给你，所以在这个场景下使用这两个关键字。 `*args` 是用来发送一个**非键值**对的可变数量的参数列表给一个函数。 这里有个例子帮你理解这个概念：

```python
def test_var_args(*args):
    print(args)
    print(type(args))

test_var_args('yasoob', 'python', 'eggs', 'test')

# 输出
('yasoob', 'python', 'eggs', 'test')
<class 'tuple'>
```

我们可以发现，拿到的数据的数据类型是元组（tuple）

```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

# 输出
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

> \*args：可以自行换成别的名称，不过我们约定俗成写成：args

我希望这解决了你所有的困惑. 那接下来让我们谈谈 `**kwargs`

#### \*\*kwargs 的用法

`**kwargs` 允许你将不定长度的**键值对**, 作为参数传递给一个函数。 如果你想要在一个函数里处理**带名字的参数**, 你应该使用`**kwargs`。

```python
def greet_me(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))
        # print("{1} == {0}".format(key, value)) # 第二个主要用来让同学们了解 format

greet_me(name="yasoob", gzh='aiyuechuang', the_public='AI悦创')

# 输出
{'name': 'yasoob', 'gzh': 'aiyuechuang', 'the_public': 'AI悦创'}
<class 'dict'>
name == yasoob
gzh == aiyuechuang
the_public == AI悦创
```

现在你可以看出我们怎样在一个函数里, 处理了一个**键值对**参数了。 这就是 `**kwargs` 的基础, 而且你可以看出它有多么管用。 接下来让我们谈谈，你怎样使用 `*args` 和 `**kwargs` 来调用一个参数为列表或者字典的函数。

#### 使用 `*args` 和 `**kwargs` 来调用函数

那现在我们将看到怎样使用`*args`和`**kwargs` 来调用一个函数。 假设，你有这样一个小函数：

```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
```

可以联想如果参数很多的话，这样就代码就不是非常的简洁。你可以使用 `*args` 或 `**kwargs` 来给这个小函数传递参数。 下面是怎样做：

```python
# 首先使用 *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# 现在使用 **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

#### 标准参数与 `*args、**kwargs` 在使用时的顺序

那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：

```python
some_func(fargs, *args, **kwargs)
```

#### 什么时候使用它们？

这还真的要看你的需求而定。 最常见的用例是在写函数装饰器的时候。 此外它也可以用来做猴子补丁(monkey patching)。猴子补丁的意思是在程序运行时(runtime)修改某些代码。 打个比方，你有一个类，里面有个叫 `get_info` 的函数会调用一个 API 并返回相应的数据。如果我们想测试它，可以把 API 调用替换成一些测试数据。例如：

```python
import someclass

def get_info(self, *args):
    return "Test data"

someclass.get_info = get_info
```

我敢肯定你也可以想象到一些其他的用例。

### 2、裁判测试程序样例：

```python
s = input().split()            #接受输入字符串并按空格分拆，存入列表，列表成员为字符串类型
t = [float(x) for x in s]    #使用列表推导将列表s中的成员全部转换成浮点数，存入另一个列表t
print("%.4f" % caculate(*t))
```

### 3、输入样例：

```python
3 2 1
```

### 4、输出样例：

```python
6.0000
```

### 5、Coder

```python
def caculate(*t):
    product = 1
    for value in t:
        product *= value
    return product
```

## 6-3 打印指定范围内的全部回文素数（高教社，《Python编程基础及应用》习题8-7） (6分)

**知识点：** 回文素数是指一个数既是**素数**又是**回文数**，例如 131 既是素数又是回文数。 请实现下述两个函数，帮助测试程序完成如下功能：从键盘输入正整数 N， 打印从 1 ~ N (包含 N )的全部**回文素数**，一行一个。

> 回文素数是指，对一个整数 n（n≥11）**从左向右**和**从右向左读：其结果值相同且是素数「质数」**，即称 n 为回文素数。**「1、实现方法」** 除了 11，**偶数位的数不存在回文质数**。4位，6位，8位……数不存在回文质数。因为四位及四位以上的偶数位的回文数都可以被 11 整除，故不存在偶数位的回文质数。**「2、判断输入数的位数」** 最初几个回文素数：11，101，131，151，181，191，313，353，373，383，727，757，787，797，919，929……两位回文素数1个，三位回文素数15个，五位回文素数93个，七位回文素数668个，九位回文素数 5172个。

### 1、函数接口定义：

```python
def isPrime(num):

def reverseNumber(num):

```

isPrime() 用于判断整数 num 是否是素数，是返回 True , 否则返回 False。 reverseNumber() 用于返回整数 num 的反向数，321 的反向数为 123， 320 的反向数为 23。

### 2、裁判测试程序样例：

```python
N = int(input()) # 获取数字并转为整数，并且这个 N 是一个范围
for n in range(1, N+1): # range 是左闭右开，不会提取到结尾的那个数所以需要 + 1，然后以这个范围做循环。
    if isPrime(n) and reverseNumber(n) == n:
        print(n)
```

### 3、输入样例：

```python
400
```

### 4、输出样例：

```python
2
3
5
7
11
101
131
151
181
191
313
353
373
383
```

### 5、Coder

#### 1、质数的判断方法：

一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。 **方法一：**

```python
# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
   # 查看因子
   for i in range(2, num):
       if (num % i) == 0: # 肯定是除于比 num 小的数来检测是否能被整除
           print(num,"不是质数")
           print(i, "乘于", num//i, "是", num) # 如果能被整除那直接用 // 也是可以的。
           break
   else:
       print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
   print(num, "不是质数")
```

**方法二：**

```python
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
```

\*\*方法三：

```python
def isPrime(num):
    if num == 1:
        return 0
    elif num == 2:
        return 2
    else :
        from math import sqrt
        active = True
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                active = False
        if active:
            return num
        else:
            return 0
```

#### 2、整数反转

**解题思路：** 首先我们想一下，怎么去反转一个整数？——用栈？ 或者把整数变成字符串，再去反转这个字符串？ 这两种方式是可以，但并不好。实际上我们只要能拿到这个整数的末尾数字就可以了。 以 12345 为例，先拿到 5，再拿到 4，之后是 3，2，1，我们按这样的顺序就可以反向拼接处一个数字了，也就能达到 **反转** 的效果。 怎么拿末尾数字呢？好办，用取模运算就可以了。**「取余运算即可」** 1、将 12345 % 10 得到 5，之后将12345 / 10 2、将1234 % 10 得到4，再将1234 / 10 3、将123 % 10 得到3，再将123 / 10 4、将12 % 10 得到2，再将12 / 10 5、将1 % 10 得到1，再将1 / 10 这么看起来，一个循环就搞定了，循环的判断条件是 x>0 但这样不对，因为忽略了 **负数** 循环的判断条件应该是 while(x!=0)，无论正数还是负数，按照上面不断的 /10 这样的操作，最后都会变成0，所以判断终止条件就是 !=0 有了取模和除法操作，对于像 12300 这样的数字，也可以完美的解决掉了。

* * *

看起来这道题就这么解决了：

```python
def reverseNumber(num):
    res = 0
    while (num != 0):
        tmp = num % 10
        res = res * 10 + tmp
        num = int(num / 10)
    return res


if __name__ == '__main__':
    print(reverseNumber(3456))
```

## **6-4 整数数位和（高教社，《Python编程基础及应用》习题8-3） (4分)**

编写一个函数，该函数接受一个正整数作为参数，返回该整数的各位数字之和。

### 1、函数接口定义：

```python
def digitSum(v)
```

v 为输入整数（正整数）； 函数返回一个整数，其值为 v 的各位数字之和。

### 2、裁判测试程序样例：

```python
a = int(input())
print(digitSum(a))
```

### 3、输入样例：

```python
291
```

### 4、输出样例：

```python
12
```

### 5、Coder

```python
def digitSum(a):
    num_list = list(str(a))
    tmp = 0
    for i in num_list:
        # tmp = tmp + int(i)
        tmp += int(i)
    return tmp
```

```python
def digitSum(v):
    num_list = list(str(v))
    a = 0
    for i in range(0,len(num_list)):
        a += int(num_list[i])
    return a
```

题目已经给定了这个数字，如果是在实际的开发当中，是需要对输入的数字是不是纯数字进行判断的。

## **6-5 编写函数计算f(i) = 1/2 + 2/3 + 3/4 + ... + i/(i+1) （高教社，《Python编程基础及应用》习题8-4） (4分)**

编写函数计算f(i) = 1/2 + 2/3 + 3/4 + ... + i/(i+1) 。

### 1、函数接口定义：

```python
def f(i):
```

i 为正整数，返回结果浮点数。

### 2、裁判测试程序样例：

```python
v=int(input())
print("%.4f" % f(v))
```

### 3、输入样例：

```python
5
```

### 4、输出样例：

```python
3.5500
```

### 5、Coder

```python
def f(i) :
    result = 0
    for x in range(i+1):
        current_num = x / (x + 1)
        result += current_num
    return result
```

# 作业 8:

## 6-1 定义并实现身体质量指数类（高教社，《Python编程基础及应用》习题9-3） (4分)

按图施工，设计下述 BMI 「**Body Mass Index」**类，用于计算身体质量指数。该指数等于体重（kg) 除以身高 (米) 的平方。 相应的判定标准如下图所示。

### 1、BMI 类接口定义：

```python
class BMI:
    ...
```

其中，name 为姓名，age 为年龄，height 为身高，单位为米，weight 为体重，单位为 kg。 getBMI() 函数返应计算所得的身体质量指数； getStatus() 返回评价结果，其值应为超轻/标准/超重/肥胖之一。

### 2、裁判测试程序样例：

```python
>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> n=81
>>> eval("n + 4")
85
```

```python
sName = input()  #输入姓名
iAge = int(input()) #输入年龄
fHeight = eval(input())  #输入身高，预期为浮点数，单位米
fWeight = eval(input())  #输入体重，预期为浮点数，单位千克
bmi=BMI(sName,iAge,fHeight,fWeight) #实例化BMI类
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())
```

### 3、输入样例：

```python
Alex
27
1.75
68
```

### 4、输出样例：

```python
Name: Alex
Age: 27
BMI = 22.204
Result = 标准
```

### 5、Coder

```python
class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getStatus(self):
        m=fWeight/(fHeight**2)
        if m<18:
            return ("超轻")
        elif m>=18 and m<25:
            return ("标准")
        elif m>=25 and m<27:
            return ("超重")
        else:
            return ("肥胖")
    def getBMI(self):
        n=fWeight/(fHeight**2)
        return n
```

## **6-2 定义并实现 Book 类及其\_\_del\_\_函数（高教社，《Python编程基础及应用》习题9-4） (3分)**

图书馆里有很多的书， 请定义一个名为 Book 的类。 该类的属性包括书名（字符串），书号（字符串），单价（浮点数）； 该类的构造函数接受书名，书号及单价三个参数并参成对象初始化； 该类的 **del**() 函数则向终端打印如下信息：Book destroyed-书名,书号,单价 注意：单价保留两位小数。

### 1、类接口定义：

```python
class Book:
    ...
```

### 2、裁判测试程序样例：

```python
sName = input()  #输入书名
sNo = input() #输入书号
fPrice = float(input())   #输入单价
b = Book(sName,sNo,fPrice)
b = None   #触发b对象的__del__方法的执行
```

### 3、输入样例：

```python
Python编程基础及应用
888-999
43.678
```

### 4、输出样例：

```python
Book destroyed-Python编程基础及应用,888-999,43.68
```

### 5、Coder

```python
class Book:
    def __init__(self,name,No,price):
        self.sName=name
        self.sNo=No
        self.fPrice=price
    def name(self):
        return self.sName
    def number(self):
        return self.sNo
    def price(self):
        return self.fPrice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f" %(self.sName,self.sNo,self.fPrice))
```

创建对象后，python 解释器默认调用**init**()方法。当删除一个对象时，python解释器也会默认调用一个方法，这个方法为**del**()方法。在python中，对于开发者来说很少会直接销毁对象(如果需要，应该使用del关键字销毁)。Python的内存管理机制能够很好的胜任这份工作。也就是说,不管是手动调用del还是由python自动回收都会触发**del**方法执行：

```python
import time


class Animal(object):
    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name

    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..." % self.__name)


# 创建对象
dog = Animal("哈皮狗")

# 删除对象
del dog
cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3
print("程序2秒钟后结束")
time.sleep(2)
```

## **6-3 设计一元二次方程求解类（高教社，《Python编程基础及应用》习题9-4） (4分)**

设计一个类 Root 来计算 ax+bx+c=0 的根。 该类包括：a、b、c 共 3 个属性表示方程的 3 个系数，getDiscriminant() 方法返回 b-4ac getRoot1() 和 getRoot2() 返回方程的两个根。 其中，getRoot1()返回的根对应：![image.png](https://cdn.nlark.com/yuque/0/2021/png/1359959/1609931011737-07817b4a-bd0e-4658-a69c-93ee42bf7807.png) getRoot2()返回的根对应： ![image.png](https://cdn.nlark.com/yuque/0/2021/png/1359959/1609931317894-7bfd3d7d-13d7-48b1-95c5-144e0f99f61e.png)

### 1、类接口定义：

```python
class Root:
    def __init__(self,a,b,c):
        ...
```

### 2、裁判测试程序样例：

```python
a=float(input()) #请输入二次项系数
b=float(input()) #请输入一次项系数
c=float(input()) #请输入常数项系数

root=Root(a,b,c)
if root.getDiscriminant()>0:
    print("{:.2f}".format(root.getRoot1()))
    print("{:.2f}".format(root.getRoot2()))
elif root.getDiscriminant()==0:
    print("{:.2f}".format(root.getRoot1()))
else:
    print("No Root!")
```

### 3、输入样例：

```python
2.1
10.2
3.0
```

### 4、输出样例：

```python
-0.31
-4.54
```

### 5、Coder

```python
from math import sqrt


class Root:
    def __init__(self, a, b, c):
        self.two = a
        self.one = b
        self.cs = c

    def getDiscriminant(self):
        return b ** 2 - 4 * a * c

    def getRoot1(self):
        m = b ** 2 - 4 * a * c
        n = b * (-1) + sqrt(m)
        return n / (2 * a)

    def getRoot2(self):
        m = b ** 2 - 4 * a * c
        n = b * (-1) - sqrt(m)
        return n / (2 * a)
```

## **6-4 设计一个股票类（高教社，《Python编程基础及应用》习题9-6） (4分)**

设计一个名为 Stock 的类来表示一个公司的股票，包括以下内容： 1）股票代码、股票名称、前一天股票价格、当天股票价格4个**私有**属性； 2）构造方法，需初始化代码、名称、前一天价格和当天价格等属性； 3）返回股票名字的 get 方法; 4）返回股票代码的 get 方法; 5）获取和设置股票前一天价格的get和set方法; 6）获取和设置股票当前价格的get和set方法; 7）名为getChangePercent()方法，返回前日收市价至当前价格的变化百分比； 8). 包括文档字符串，其内容为:"Stock Information Class" 说明：各方法的名称及参数要求请参见测试程序。

### 1、类接口定义：

```python
class Stock:
    ...
```

### 2、裁判测试程序样例：

```python
# 股票代码、股票名称、前一天股票价格、当天股票价格 4 个私有属性；
sCode = input() #输入股票代码
sName = input() #输入股票名称
priceYesterday = float(input())  #输入前一天股票价格
priceToday = float(input())  #输入今日股票价格

# 类：Stock
s = Stock(sCode,sName,priceYesterday,priceToday) # 初始化代码

print("代码:", s.getCode())
print("名称:", s.getName())
print("昨日价格:%.2f\n今天价格:%.2f" % (s.getPriceYesterday(),s.getPriceToday()))
s.setPriceYesterday(50.25)
print("修正昨日价格为:%.2f" % 50.25)
print("价格变化百分比:%.2f%%" % (s.getChangePercent()*100))
print(Stock.__doc__)
```

### 3、输入样例：

```python
601318
中国平安
63.21
64.39
```

### 4、输出样例：

```python
代码: 601318
名称: 中国平安
昨日价格:63.21
今天价格:64.39
修正昨日价格为:50.25
价格变化百分比:28.14%
Stock Information Class
```

### 5、Coder

```python
class Stock:
    '''Stock Information Class'''

    def __init__(self, sCode, sName, priceYesterday, priceToday):
        self.sCode = sCode
        self.sName = sName
        self.priceYesterday = priceYesterday
        self.priceToday = priceToday

    def getCode(self):
        return self.sCode

    def getName(self):
        return self.sName

    def getPriceYesterday(self):
        return self.priceYesterday

    def getPriceToday(self):
        return self.priceToday

    def setPriceYesterday(self, new):
        self.priceYesterday = new

    def setPriceToday(self, new):
        self.priceToday = new

    def getChangePercent(self):
        return (self.priceToday - self.priceYesterday) / self.priceYesterday

```

## **6-5 设计Shape基类及Circle, Rectangle继承类（高教社，《Python编程基础及应用》习题9-7） (5分)**

设计一个基类 Shape，包括：

1.  名为 sName 的属性（图形名称）；
    
2.  构造函数应对 sName 属性进行初始化。
    

设计 Shape 的继承类 Rectangle , 包括：

1.  长，宽两个属性；
    
2.  构造函数调用 Shape 的构造函数，并初始化长，宽两个属性；
    
3.  getArea() 成员函数计算并返回矩形面积。
    

设计 Shape 的继承类 Circle, 包括：

1.  半径属性；
    
2.  构造函数调用 Shape 的构造函数，并初始化半径属性；
    
3.  getArea() 成员函数计算并返回圆形面积。
    

注意：请注意阅读测试样例程序以理解题目对类的接口的要求。

### 1、类接口定义：

```python
class Shape:
       ...

class Rectangle(Shape):
     ...

class Circle(Shape):
    ...
```

### 2、裁判测试程序样例：

```python
s1 = Shape("shape0")
s = input()  #矩形名称
w = float(input()) #矩形宽度
h = float(input()) #矩形高度
r1 = Rectangle(s,w,h)
s = input()  #圆的名称
r = float(input()) #圆的半径
c1 = Circle(s,r)

print(s1.sName)
print("矩形%s面积: %.2f" % (r1.sName,r1.getArea()))
print("圆形%s面积: %.2f" % (c1.sName,c1.getArea()))
```

### 3、输入样例：

```python
Jupyter
12.1
9.9
Moon
3.3
```

### 4、输出样例：

```python
shape0
矩形Jupyter面积: 119.79
圆形Moon面积: 34.21
```

### 5、Coder

```python
from math import pi


# 设计一个基类Shape，包括：
class Shape:
    def __init__(self, sName=""):
        # 名为 sName 的属性（图形名称）；
        # 构造函数应对 sName 属性进行初始化。
        self.sName = sName


# 设计 Shape 的继承类 Rectangle , 包括：
class Rectangle(Shape):
    # 长，宽两个属性；
    # 构造函数调用 Shape 的构造函数，并初始化长，宽两个属性；
    def __init__(self, sName='', h=0.0, w=0.0):
        Shape.__init__(self, sName="")
        self.h = h
        self.w = h
        self.sName = sName

    # getArea() 成员函数计算并返回矩形面积。
    def getArea(self):
        return h * w

# 设计 Shape 的继承类 Circle ,包括：
class Circle(Rectangle):
    # 半径属性；
    # 构造函数调用 Shape 的构造函数，并初始化半径属性；
    def __init__(self, sName='', r=0.0):
        Shape.__init__(self, sName="")
        self.r = r
        self.sName = sName
    # getArea()成员函数计算并返回圆形面积。
    def getArea(self):
        area = pi * r ** 2
        return area
```

## **6-6 设计学生类，使用类对象属性来记录学生对象的数量**

设计一个名为 Student 的学生类：

1.  使用名为 count 的类对象属性来记录 Student 对象的个数；
    
2.  构造函数中初始化学号及姓名两个属性，并对 count 属性加 1；
    
3.  析构函数(**del**)中对类对象属性 count 减1。 说明：请阅读测试样例程序来理解题目对类的接口要求。
    

### 1、类接口定义：

```python
class Student
      ....
```

### 2、裁判测试程序样例：

```python
n = int(input())  #输入学生数量，数量大于1
s = []
for i in range(n):
    s.append(Student("Code"+str(i),"Name"+str(i)))
del s[0]  #删除一个学生，导致count减1
print("学生数量:",Student.count)
for x in s:
    print(x.code,x.name)
```

### 3、输入样例：

```python
3
```

### 4、输出样例：

```python
学生数量: 2
Code1 Name1
Code2 Name2
```

### 5、Coder

```python
# 设计一个名为 Student 的学生类：
class Student:
    # 使用名为 count 的类对象属性来记录 Student 对象的个数；
    count = 0

    def __init__(self, scode, sname):
        # 造函数中初始化学号及姓名两个属性，并对 count 属性加 1；
        self.code = scode
        self.name = sname
        Student.count += 1

    # 析构函数(__del__)中对类对象属性 count 减1。
    def __del__(self):
        Student.count = Student.count - 1
```

## 6-7 设计计数集合类，记录各元素加入集合的次数

从 set 类型继承，并设计一个名为 CountedSet 的子类型。通过重载 set 类型的某些函数，使得 CountedSet 对象 可以统计并记录各个元素被放入集合的总次数。请通过裁判测试程序了解该类的接口。

### 1、类接口定义：

```python
class CountedSet(set):
      ...
```

### 2、裁判测试程序样例：

```python
s = CountedSet()
while True:      #用q表示输入结束
    v = input()  #输入一个字符串
    if (v!="q"):
        s.add(v)
    else:
        break
#将集合转换成列表，排序递增输出
t = sorted(list(s))
print("元素值 次数")
for x in t:
    print(x,"-",s.getCount(x))
print("集合内元素个数:",len(s))
```

### 3、输入样例：

```python
a
b
a
q
```

### 4、输出样例：

在这里给出相应的输出。例如：

```python
元素值 次数
a - 2
b - 1
集合内元素个数: 2
```

## 5、Coder

```python
class CountedSet(set):
    def __init__(self):
        set.__init__(self)
        self.jishu = {}

    def add(self, x):
        set.add(self, x)
        self.jishu[x] = self.jishu.get(x, 0) + 1

    def getCount(self, x):
        return self.jishu[x]
```