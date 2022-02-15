---
title: Lesson 4 Notes/Projects
tags: []
id: '1855'
categories:
  - - Alex Homework
date: 2021-08-19 10:08:27
---

The following code is for a basic login username/password checker for a user to sign into a application or website, using first if-elif-else statements, and the variant of it, will use a while loop to make things more clean looking and more efficient. 以下代码是用于用户登录应用程序或网站的基本登录用户名/密码检查器，使用第一个 if-elif-else 语句及其变体，将使用 while 循环使事情看起来更干净， 更高效。 Variant 1: 变体 1:

```python
import logging

logging.basicConfig(filename="loginlogs.txt", filemode="w")
logger = logging.getLogger(__name__)

dict_data = {"aiyc": 1234, "bob": 1245}
username = input("Please enter your account name: ")
password = input("Please enter your password: ")
if (username in dict_data) and (password == dict_data.get(username, "password incorrect!")):
    logger.warning("Login successful!")
else:
    logger.warning("Login unsuccessful!! Adding logs to logging file... ")
    print("Login failed, adding fail message to logs file...")
```

Variant 2: 变体 2：

```python
import logging

dict_data = {"aiyc": 1234, "bob": 1245}
logging.basicConfig(filename="loginlogs2.txt", filemode="w")
logger = logging.getLogger(__name__)
run = False
username = input("Please enter your username: ")
password = int(input("Please enter your password: "))
while not run:
    if (username in dict_data) and (password == dict_data.get(username, "password error!")):
        logger.warning("Login successful! Adding logs to logging file...")
        print("Login successful! Adding logs to logging file...")
        run = True
    else:
        logger.error("Login unsuccessful. ")
        print("Login unsuccessful. Please try again...")
        username = input("PLease enter your username: ")
        password = int(input("Please enter your password: "))
```

The second variant works better, since while loops make it much easier to keep asking for user input no matter how many times their input is invalid under our circumstances. While loops help a lot with something that requires a user to input something, since they are not like if or else statements, where you can only use them to check indefinitely once. While loops can be used to check for something until that circumstance or condition is met. This means that using them with user inputs, and defining a special condition for the while loop, and nesting logic statements such as if-elif-else statements in while loops, make it extremely easy and efficient to repeatedly ask or do something if a certain condition is not met. 第二种变体效果更好，因为无论在我们的情况下输入无效多少次，while 循环都可以更容易地继续询问用户输入。 While 循环对需要用户输入的东西有很大帮助，因为它们不像 if 或 else 语句，你只能使用它们无限期地检查一次。 While 循环可用于检查某事，直到满足该情况或条件。 这意味着将它们与用户输入一起使用，并为 while 循环定义一个特殊条件，并在 while 循环中嵌套诸如 if-elif-else 语句之类的逻辑语句，使得重复询问或执行某些操作变得非常容易和高效。 条件不满足。 Speaking of using all these loops and conditional statements, it is easy to trip over something really basic or easy to fix, such as a indentation problem. If you use two different methods of indenting a nested statement, or a statement that is meant to be inside of a codeblock, then python will return a IndentationError when you try running your code. There are two methods to indent code in python, using the "tab" key on your keyboard, or hitting the space key on your keyboard 4 times. You must use one method of indenting in all of your code, otherwise python will return an error stating something is wrong with your indentation. Copying a code with indents in it, from a website- most websites use the 4 spaces to indent their code, rather than using tabs, so you must keep this in mind when implementing outside code into your own code, as it could potentially cause a lot of problems especially in an IDE, such as pycharm, and it could drive you crazy trying to debug your code, while the simple issue is simply just to format the indentations in your code correctly. 说到使用所有这些循环和条件语句，很容易被一些非常基本或易于修复的东西绊倒，例如缩进问题。如果您使用两种不同的方法来缩进嵌套语句或打算位于代码块内的语句，那么当您尝试运行代码时，python 将返回 IndentationError。在python中有两种缩进代码的方法，使用键盘上的“tab”键，或者敲击键盘上的空格键4次。您必须在所有代码中使用一种缩进方法，否则 python 将返回一个错误，说明您的缩进有问题。从网站复制带有缩进的代码 - 大多数网站使用 4 个空格来缩进他们的代码，而不是使用制表符，因此在将外部代码实施到您自己的代码中时必须牢记这一点，因为它可能会导致很多问题，尤其是在 IDE 中，例如 pycharm，它可能会让您在尝试调试代码时发疯，而简单的问题只是正确格式化代码中的缩进。 If you nest a loop within a loop, such as a for loop nested within a while loop, and you try to use the "break" keyword to end the main loop, nothing will happen, since python cannot kill both loops with one keyword. This is where boolean flags come into play in python, since you can set a variable equal to a boolean value, and use a while loop to loop through certain actions while a certain boolean value is not being met. This results in a forever loop if you were never to set the boolean value to whatever meets the while loop's constraints, since the variable you compared it to, is predefined. This means that you have to manually set the boolean variable to whatever meets the while loop's constraints, then use the "break" keyword to kill the second loop. Otherwise, the program will be stuck in a forever loop, which is something you don't want. This is an example of a forever loop that will occur if you only try to use the break keyword to stop a forever loop, without any boolean flags: 如果在循环中嵌套循环，例如嵌套在 while 循环中的 for 循环，并且尝试使用“break”关键字结束主循环，则不会发生任何事情，因为 python 无法使用一个关键字终止两个循环。这就是布尔标志在 Python 中发挥作用的地方，因为您可以设置一个等于布尔值的变量，并在未满足某个布尔值时使用 while 循环来循环执行某些操作。如果您从未将布尔值设置为满足 while 循环约束的任何值，则会导致永远循环，因为您与之比较的变量是预定义的。这意味着您必须手动将布尔变量设置为满足 while 循环约束的任何值，然后使用“break”关键字终止第二个循环。否则，程序将陷入永远循环，这是您不想要的。这是一个永远循环的例子，如果你只尝试使用 break 关键字来停止一个永远循环，而没有任何布尔标志，就会发生这种循环：

```python
while True:
    for i in range(10):
        print(i)
        break
    print("Loop is done!")
```

The loop above will never stop running because you only use the "break" keyword, and you do not set a boolean flag to completely force kill the while loop. The example below is a proper code that will stop after printing every value starting from 0 and going to 10, without printing out 10: 上面的循环永远不会停止运行，因为您只使用了“break”关键字，并且您没有设置布尔标志来完全强制终止 while 循环。 下面的示例是一个正确的代码，它将在打印从 0 开始到 10 的每个值后停止，而不打印出 10：

```python
run = False
while not run:
    for i in range(10):
        print(i)
        if i == 9:
            run = True
    print("Loop is done!")
```

The code given as an example above actually prints out everything from 0 - 10 ignoring the print statement for 10, (due to range()), and it prints out "Loop is done!", since this time it actually exits the for loop, and runs that statement, and then the code is finished executing. The reason why you cannot set a boolean flag after the "break" statement or put any code after the "break" statement, is because nothing after the break statement will run, since it's immediately skipped over. 上面作为示例给出的代码实际上打印了从 0 到 10 的所有内容，忽略了 10 的打印语句（由于 range()），并且它打印出“Loop is done!”，因为这次它实际上退出了 for 循环 , 并运行该语句，然后代码完成执行。 您不能在“break”语句之后设置布尔标志或在“break”语句之后放置任何代码的原因是因为break语句之后的任何内容都不会运行，因为它会立即被跳过。 Here is the line-by-line explanation of what each line in the code with the nested loop actually does:

```python
run = False # sets a run flag, using a boolean value. 使用布尔值设置运行标志。
while not run: # runs code within loop if boolean flag is equal to False. 如果布尔标志等于 False，则在循环内运行代码.
    for i in range(10): # loops through numbers in range 0 - 10. 循环遍历 0 - 10 范围内的数字
        print(i) # prints number that is being looped through the range of 0 - 10, without printing 10. 打印在 0 - 10 范围内循环的数字，而不打印 10。
        if i == 9: # checks to see if number being looped is equal to 9. 检查循环中的数字是否等于 9。
            run = True # if number being looped is equal to 9, then set boolean flag value to be equal to True, thus ending the while loop, and stopping the program. 如果被循环的数字等于 9，则将布尔标志值设置为等于 True，从而结束 while 循环，并停止程序。
    print("Loop is finished!") # after while loop is exited, print a mesasge stating that the loop is finished. 在 while 循环被激发后，打印一条消息，说明循环已完成。
```

If you want to make sure 100% that both loops are killed, then you should add the "break" keyword after you set your boolean flag's value to True, this way it will not only kill the while loop if the number that's being looped through is equal to 9, but it will also kill the for loop, thus guaranteeing that the program will 100% be finished running, if the number that is being looped through is equal to 9. 如果您想确保 100% 两个循环都被终止，那么您应该在将布尔标志的值设置为 True 后添加“break”关键字，这样它不仅会在循环的数字中终止 while 循环 等于 9，但它也会终止 for 循环，从而保证程序将 100% 完成运行，如果正在循环的数字等于 9。 The easiest way to determine the output of a while loop, is to acquire a "reverse thought process". A typical person would try to go step by step, and try to visualize in their head, step by step from the starting point, what the output of a code would be. This is not very efficient as it takes a while for you to go step by step. Instead, what you could do is, you could immediately start visualizing from the most likely point where the program's next step, would be to return False, and kill the while loop, and once you are sure that is what the program will do, then you could be sure that the pattern from the starting point will be the pattern for output, all the way until the point where you determined the program's next step would be to return False, which means your program will output every value/output in that pattern all the way from the starting point to that value. For example, if you wrote this code: 确定 while 循环输出的最简单方法是获得“反向思维过程”。 一个典型的人会一步一步地尝试，并尝试在他们的脑海中从起点一步一步地想象代码的输出是什么。 这不是很有效，因为您需要一段时间才能逐步进行。 相反，您可以做的是，您可以立即从程序下一步最有可能的点开始进行可视化，即返回 False，并终止 while 循环，一旦您确定这就是程序将执行的操作，那么 您可以确定从起点开始的模式将是输出模式，一直到您确定程序的下一步将返回 False 的点，这意味着您的程序将输出该模式中的每个值/输出 从起点到那个值。 例如，如果您编写了以下代码：

```python
run = False
while not run:
    for i in range(10):
        print(i)
        if i == 9:
            run = True
            break
    print("Loop is finished!")
```

You could start your thought process from 9, since that is that last number where the next step for the program, would be to return False, since 10 = 10, and the while loop only runs when the number being looped through is less than 10. This means that you know that the program will only output every value from the starting point, 0, to 9, and print the message that is supposed to be run when the program exits, since the next step for the value 9, would be to return False, which would stop the loop, which means that nothing is outputted after 9, and the program immediately prints out the exiting message. 您可以从 9 开始您的思考过程，因为这是程序下一步将返回 False 的最后一个数字，因为 10 = 10，并且 while 循环仅在循环的数字小于 10 时运行 . 这意味着您知道程序将只输出从起点 0 到 9 的每个值，并打印程序退出时应该运行的消息，因为值 9 的下一步将是 返回 False，这将停止循环，这意味着在 9 之后没有任何输出，并且程序立即打印出退出消息。