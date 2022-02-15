---
title: python password encryptor
tags: []
id: '1840'
categories:
  - - Alex Homework
date: 2021-08-11 22:06:11
---

```python
from cryptography.fernet import Fernet
import pyinputplus as pyip

print("Welcome to this basic password encryptor!")

key = Fernet.generate_key()
ask_action = pyip.inputStr("Please enter what action you would like to do: Encrypt/Decrypt, type 'stop' at any time to stop.")
while ask_action not in ['stop', 'Stop', 'STOP']:
    if ask_action in ['Encrypt', 'encrypt', 'ENCRYPT']:
        crypter = Fernet(key)
        user_pw = pyip.inputStr("Please enter the password you would like to encrypt:")
        bytes_pw = str.encode(user_pw)
        encrypted_pw = crypter.encrypt(bytes_pw)
        print("Here is your encrypted password: {}".format(encrypted_pw))
        ask_action = pyip.inputStr("Please enter what action you would like to do: Encrypt/Decrypt, type 'stop' at any time to stop.")

    elif ask_action in ['decrypt', 'Decrypt', 'DECRYPT']:
        decrypted_pw = crypter.decrypt(encrypted_pw)
        print("This is your decrypted pw: {}".format(decrypted_pw))
        ask_action = pyip.inputStr("Please enter what you would like to do: Encrypt/Decrypt, type 'stop' at any time to stop.")

print("Thank you for using this password encryptor!")
```