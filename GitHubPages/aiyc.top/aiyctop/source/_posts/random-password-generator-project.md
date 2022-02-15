---
title: random password generator project
tags: []
id: '1841'
categories:
  - - Alex Homework
date: 2021-08-11 22:06:28
---

```python
import pyinputplus as pyip 
import random
import string

print("Welcome to this random password generator!")
print("Type 'stop' at any time to quit the program!")
ask_range = pyip.inputNum("Please enter how long you want your password to be: ")


while ask_range not in ['stop', 'Stop', 'STOP']:
    result = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = ask_range))
    print("The password generated for you is: {}".format(result))
    ask_range = pyip.inputNum("Please enter how long you want your password to be:")
```