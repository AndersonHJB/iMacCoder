---
title: python file renamer
tags: []
id: '1843'
categories:
  - - uncategorized
date: 2021-08-11 22:04:43
---

```python
import os
import pyinputplus as pyip

print("Welcome to this basic file renamer!")

user_action = pyip.inputStr("What do you want to do to a file: Rename/Delete/Create, type 'stop' at anytime to stop.")

while user_action not in ['stop', 'Stop', 'STOP']:
    if user_action in ['Rename', 'rename', 'RENAME']:
        try:
            user_rename = pyip.inputStr("What is the name of the file that you would like to rename?")
            new_name = pyip.inputStr("Please enter the name you would like to rename your file to: ")
            os.rename(user_rename, new_name)
            print("File successfully renamed!")
            user_action = pyip.inputStr("What do you want to do to a file: Rename/Delete/Create, type 'stop' at anytime to stop.")
        except IOError:
            print("The file you requested to rename doesn't exist!")
            user_action = pyip.inputStr("What do you want to do to a file: Rename/Delete/Create, type 'stop' at anytime to stop.")
    if user_action in ['Delete', 'delete', 'delete a file', 'Delete a file', 'DELETE']:
        try:
            user_delete = pyip.inputStr("Please enter the name of the file that you want to delete: ")
            os.remove(user_delete)
            print("File successfully deleted!")
            user_action = pyip.inputStr("What do you want to do to a file: Rename/Delete/Create, type 'stop' at anytime to stop.")
        except IOError:
            print("The file you requested to delete doesn't exist!")
            user_action = pyip.inputStr("What do you want to do to a file: Rename/Delete/Create, type 'stop' at anytime to stop.")

    if user_action in ['Create', 'create', 'CREATE', 'Create a file', 'create a file', 'CREATE A FILE']:
        user_file_name = pyip.inputStr("Please enter the name of the file that you want to create: ")
        open(user_file_name, 'a')
        print("File successfully opened!")
        user_action = pyip.inputStr("What do you want to do to a file: Rename/Delete/Create, type 'stop' at anytime to stop.")
```