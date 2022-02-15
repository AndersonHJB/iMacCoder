---
title: Lesson 5 Notes/Projects
tags: []
id: '1858'
categories:
  - - Alex Homework
date: 2021-08-22 05:54:29
---

In python, there are many ways to one thing. For example, there are three ways to easily and to let python handle putting every number in a certain range, into a list. The first way is: 在python中，一件事有很多方法。 例如，有三种方法可以轻松地让 python 处理将特定范围内的每个数字放入列表中。 第一种方式是：

```python
list1 = list(range(10))
print(list1) # outputs [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The second way is: 第二种方法是：

```python
list1 = [num for num in range(10)]
print(list1) # outputs [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The third way is: 第三种方式是：

```python
list1 = []
for num in range(10):
    list1.append(num)
print(list1) # outputs [0, 1, 2,3, 4, 5, 6, 7, 8, 9]
```

If you were to run these three different blocks of code, you will see that they all output the exact same thing. The first method simply force converts the numbers in the range of 0 - 10 into a list, which basically just splits the numbers up, and adds them to a list. The second method uses list comprenhension to add every item in the range of 0 - 10 to a list. The third method basically does basically what the second method does, except it takes more lines of code to write. The for loop assigns a new variable to each number in the range of 0 - 10, and adds that number to the list, and when the list is called, it simply outputs everything that is inside of itself. These three methods all work, and outputs the exact same result. 如果您要运行这三个不同的代码块，您将看到它们都输出完全相同的内容。 第一种方法只是将 0 - 10 范围内的数字强制转换为列表，这基本上只是将数字拆分，然后将它们添加到列表中。 第二种方法使用列表理解将 0 - 10 范围内的每个项目添加到列表中。 第三种方法基本上和第二种方法一样，只是需要编写更多行代码。 for 循环为 0 - 10 范围内的每个数字分配一个新变量，并将该数字添加到列表中，当列表被调用时，它只是输出其内部的所有内容。 这三种方法都有效，并输出完全相同的结果。 Now what if we wanted to keep track of what index of an element is what in a list? Or what if we wanted to see how the index position of something in a list, and not just blindly print the element out? Well, python has a awesome function called enumerate(). Basically, what enumerate() does, is it keeps track of the number of iterations something that is being iterated through has gone through. This means that enumerate() works especially well with something like a for loop, since a for loop works extremely well with iterations. Here is an example of how the enumerate() function works in a actual block of code:

```python
list1 = ["aiyc", 'bob', "joe", "jeff"]
for index, item in enumerate(list1):
    print((index, item))
```

The code above basically returns a tuple containing the index of where each item in the list "list1" is, and the value contained at the index position that was stated in the tuple before it. You could also not specify any other value other than the "item "variable to be defined in the for loop, and if you printed out the item variable, you will see that it will sort the index or count of the iterations from the for loop, however it might be better to actually define the count of the iterations from the enumerate() function, this way you know what it's enumerating and iterating through and counting, and not just counting something. 上面的代码基本上返回一个元组，其中包含列表“list1”中每个项目所在位置的索引，以及包含在它之前的元组中声明的索引位置的值。 除了要在 for 循环中定义的“item”变量之外，您也不能指定任何其他值，如果您打印出 item 变量，您将看到它将对 for 循环中的迭代的索引或计数进行排序 ，但是实际上从 enumerate() 函数定义迭代计数可能会更好，这样您就可以知道它正在枚举、迭代和计数的内容，而不仅仅是计算某些内容。 When using a conditional statement, and let's say you only need to print out one thing, or execute one line of code if that condition is met, then you don't necessarily have to put the line of code that you want to execute in a line inside of it, you could simply put it on the same line. This works fine when you use this syntax in terminal, but in a proper development environment such as pycharm, pycharm really doesn't like it when you use that kinda syntax in your code, and it will warn you saying that your code should be in the line inside and after the place where the condition is defined. 当使用条件语句时，假设您只需要打印一件事，或者如果满足该条件就执行一行代码，那么您不必将要执行的代码行放在 线里面，你可以简单地把它放在同一条线上。 当您在终端中使用这种语法时，这可以正常工作，但是在适当的开发环境（例如 pycharm）中，当您在代码中使用这种语法时，pycharm 真的不喜欢它，它会警告您说您的代码应该在 定义条件的位置内部和之后的行。 Again, the reverse thinking method really helps when you are trying to fully understand a code, when you are working line by line to comprehend exactly what each line of code does. For example, in this code:

```python
i = 0
while True:
    print(i)
    i = i + 1
    if i > 5:
        break
```

In this code, python first recognizes that the value of the variable "i" is equal to 0, and that as long as the program is being run, it should print out the value of i, and add 1 to the value of i each time after printing it. Then it checks to see if the value of i is equal to 5, and if it is, then it should exit the loop, and therefore stop the program. The reverse thinking method comes into play for these few lines:

```python
print(i) # outputs 0, 1, 2, 3, 4, 5
i = i + 1
if i > 5:
    break
```

We know that if the value of i is greater than 5, then python will exit the loop and stop the program. And we know that everytime the loop occurs, we add one to the value of i. We know that 5 > 5 = False, since 5 is not greater than 5, however the value of 6 is greater than 5, which means that i's value is False, which means that the loop stops, and it does not print out 5, which means it only prints 0, 1, 2, 3, 4, 5. 我们知道如果i的值大于5，那么python会退出循环并停止程序。 我们知道，每次循环发生时，我们都会给 i 的值加 1。 我们知道 5 > 5 = False，因为 5 不大于 5，但是 6 的值大于 5，这意味着 i 的值是 False，这意味着循环停止，并且不打印出 5， 这意味着它只打印 0、1、2、3、4、5。 Basic person information description program: 基本人物信息描述程序：

```python
name = input("Please enter your name: ")
gender = input("Please enter your gender: ")
age = input("Please enter your age: ")
school = input("Please enter the name of the school that you go to: ")
print("Getting basic information...")
print("************************************")
print(f"Hi! My name is {name}")
print(f"I am a {gender}.")
print(f"I am {age} years old.")
print(f"I go to {school}.")
```

```python
name = input("请输入您的名字： ")
gender = input("行输入您的性别：男/女 ")
age = input("请输入您的年龄： ")
school = input("请输入您去的学校：")
print("正在获取人员的基本信息...")
print("************************************")
print(f"你好！我的名字是{name}.")
print(f"我是一个{gender}人.")
print(f"我上{school}.")
```