---
title: Python Homework 1 Projects
tags: []
id: '1837'
categories:
  - - Alex Homework
date: 2021-08-11 22:06:43
---

```python
import pyinputplus as pyip
ask_name = pyip.inputStr("Please enter your name: ")
ask_gender = pyip.inputStr("Please enter your gender: ")
ask_age = int(input("Please enter your age:"))
ask_school = pyip.inputStr("Please enter the name of the school you go to: ")
print("-----------------------")
print(ask_name)
print(ask_gender)
print(ask_age)
print(ask_school)
```

```python
import pyinputplus as pyip
import random
print("Welcome to this random number guessing game!")
ask_range = int(input("Please enter the highest number you want to possibly guess to: "))
random_number = random.randint(0, ask_range)
ask_guess = int(input("Please enter your guess:"))
while ask_guess != random_number:
    if ask_guess < random_number:
        print("Your guess is too low, try again!")
    elif ask_guess > random_number:
        print("Your guess is too high, try again!")
    else:
        break
```

```python
import pyinputplus as pyip
ask_number = pyip.inputStr("Please enter the number you want to split: ")
digits = [int(a) for a in str(ask_number)]
print(digits)
```

I didn't really save the video that I recorded after the class, so I don't really know how you want me to write this problem where I split a number into it's digits, so I just solved this problem using list comprehension. I apologize for my mistake.