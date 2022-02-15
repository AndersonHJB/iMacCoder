---
title: Lesson 6 Notes/Projects
tags: []
id: '1863'
categories:
  - - Alex Homework
date: 2021-08-26 03:45:28
---

Functions are basically a warehouse that takes input, and outputs something with a certain rule applied to the input, (the rule of a function is typically specified in the function, and is typically specific to that function.) There are functions in mathematics, and also in python. In python, there are two main types of functions. Built-in functions, and third-party or self-defined ones. Built-in functions are basically functions that come with python after you install it onto your computer. Third-party functions, or self-defined functions, are basically functions that you defined or created in your own code to be used. Some examples of built-in functions in python, is the sum() function, or the eval() function. Here is an example of the sum() function being used, as well as eval():

```python
list1 = [1, 2, 3, 46, 7, 8, 4, 3]
result = sum(list1)
print(result) # prints 74
```

```python
user_string = input("Please input a equation for python to solve!")
result = eval(user_string) # evaluates (solves) the equation or mathematical problem that the user inputted.
print(result) # prints out the evaluated equation.
```

The built-in function sum() in python basically returns the sum of all items in a iterable datatype, such as a with a list full of numbers, the sum() function will return the sum of everything in the list. The built-in function eval() returns a evaluated version of a string. For example, if you passed a string containing a mathematical equattion to the eval() function, the function will basically solve the equation for you, or evaluate it. Apart from built-in functions, and third-party or self-defined ones, there are also "functions" that are parts of built-in python modules, or part of third-party modules. Some "functions" require a "." before the function, and it has to follow a class object, or a object of that module, which technically means that the "function" is not really a function, but rather a method of the module. A good example of a method of a module or a module's object, would be the .randint() method of the random module. What it does, is it basically picks a random integer value from a given range that you input as it's parameters to the method. Here is an example of how it is used:

```python
ask_range = int(input("Please input the highest number in a range that you would like to generate a random number in: "))
random_number = random.randint(0, ask_range) # generates number from 0 to the number that the user specified. .randint() is a method of the "random" object
print(f"The number generated for you is {random_number}.")
```

If you want to define your own function, you can use the "def" keyword, which allows a user to define their own function, by putting the name and parentheses following the name of their function, putting that after the "def" keyword, and putting a colon after all that, and you can put the function's rules, or the "change" that you want it to apply to the input it is given, inside of the function. Here is an example:

```python
def add(a, b):
    sum = a + b
    print(sum)
add(3, 4) # prints 7
```

You do not have to specify or require any parameters to be even entered into the function. You could have a function that simply carries a task out that doesn't require an input to be entered and it will execute that task out just fine. For example:

```python
def hello_world():
    print("Hello World!")
hello_world() # prints "Hello World!"
```

In the example given above, you do not have to input anything into the function, and you can simply call it, and it will output "Hello World!" which is what we wanted it to do. If you do not call a function, then the purpose or the action of the function will not be carried out, even if you have a return statement or a print statement, since the function is not active, as it is not being called. There is a helpful if conditional check:

```python
if __name__ == "__main__":
    # do something
```

Basically, the code above checks to see if the name of the file that is being run is equal to "**main**", and if it is, that means that the file is being run directly, and it will execute the code inside the if conditional statement. This is especially useful if you are writing code that other people will use, since if they import some functions from your code file, and you've already called your own functions that you made, and they import the functions into their code, and they call your functions, that could result in some problems such as the function calls overlapping each other, and since another person imported your functions from your code, if you have called your functions in your own code, and they call it again from their code, it could print out the result of the call from your code, as well as their call, which would essentially be overlapping. That is why it is helpful in certain scnearios to use that conditional check, this way it can prevent some issues that may arise from other people using your code. If there is a certain scenario where you are calling a function and inputting the parameters of the function that you are calling, and you are not sure the position of what you are inputting might be in the function's parameter fields, and whatever the function returns is order-sensitive, but you know the parameters that the function takes, then you can set each of the parameters equal to a value that is specific to that parameter, and call the function like that. That will make the order in which you set the parameters' values whilst calling the function irrelevant, since you already are specifically defining them to a certain value. For example, this is how you could do this:

```python
def description(name, age):
    print(f"Hi {name}! I heard you are {age} years old.")
description(age="25", "joe") # prints "Hi joe! I heard you are 25 years old."
```

There are two statements that are most frequently seen inside of functions, the print() function, and the "return" keyword. There is a difference between the two, the main one being that the print() function returns a None value if you assign a function call that has a print() function in it, to a variable, and you try printing that variable, then the print value will result in None being printed. However if you change that print() function in the function that you called and assigned to a variable, and you try printing the variable, then it will actually call the function that you assigned the function call to a variable, and it will essentially be the same as if you simply just called the function. This is because the "return" keyword actually puts the returned value in place of where the function was called, which means that if you assigned a function call to a variable, and you printed that variable, then it would put in place of the variable, which was where the function was called, the returned value. The print() function simply only outputs a value for the user to see, but doesn't actually store the value into the place where the function was called, hence why printing the variable "storing" the function call, will only return None, since there is no value actually there, as the function call returned/stored no value. There are three things that are most commonly seen in the syntax of writing functions, "modifying" a global variable in a local namespace and calling that variable, calling a global variable directly from a local namespace, and trying to "modify" or redefine a global variable after calling it inside of a function. Here are these three most commonly seen things in the syntax of writing functions, listed out in actual code examples:

```python
a = 1
def test():
    a = 2
    print(a)
test() # outputs 2
print(a) # outputs 1
```

In the example above, the reason why the function call returns 2, and the print() statement that prints the "a" variable returns 1, is because when you try to "change" the value of a global variable by redefining it in a local namespace, and calling it in that local namespace, it's actually not modifying that global variable, but it's actually creating an entirely new variable stored in a local namespace, and not a global one.

```python
a = 1
def test():
    print(a)
test() # outputs 1
print(a) # outputs 1
```

In this second example, the reason why both the function call and the print() statement both return 1, is because when you try to call/reference a variable from inside a local namespace (in a function), python will first look for that variable locally, and if it doesn't find any references of it locally, it will look for it globally, and if the variable is found, then it will print that variable out, and if not, it will return an error. The "a" variable in this case is a global variable, and since we didn't redefine another "a" variable locally, python simply prints out the value of the global variable "a", hence why both the function call and the print() statement both return 1, since that is the value of the global variable "a".

```python
a = 1
def test():
    print(a)
    a = 2
test()
print(a)
```

In the third example displayed above, python returns an error stating that the variable "a" was referenced before it was assigned. This is because python will first look for the variable that is being called in a local namespace, and if it is not found, then it will look for it in a global namespace. Since the variable "a" in a local namespace was defined after the print() statement called it and was going to print it, python doesn't recognize that there are any variables to be called and printed, hence why it returns an error explaining that. Basic fortune telling program:

```python
class InvalidInputException(Exception):
    pass

ask_gender = input("Please enter your gender: M/F")
while ask_gender in ["M", "m", "Male", "F", "f", "Female", "female"]:
    try:
        ask_age = int(input("Please enter your age: "))
        if isinstance(ask_age, int):
            if ask_gender in ["M", "m", "Male", "male"]:
                print("*************Here is your fortune*************")
                print("You will get into Stanford University and find great success!")
                break
            elif ask_gender in ["F", "f", "Female", "female"]:
                print("*************Here is your fortune*************")
                print("You will get into Harvard University and find great success!")
    except ValueError:
        raise InvalidInputException("Please input a valid age!")

else:
    print("Please enter a valid gender!")
```