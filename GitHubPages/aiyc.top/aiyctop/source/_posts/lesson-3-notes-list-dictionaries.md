---
title: Lesson 3 Notes List/Dictionaries
tags: []
id: '1851'
categories:
  - - Alex Homework
date: 2021-08-14 23:35:20
---

Lists and dictionaries in python are very useful in each of their own ways. Lists are great if you want a simple, easy way to store data and you would like to add new items or values to it, and dictionaries are very useful in storing key:value specific items, such as a person and their phone number. Some things lists can do better than dictionaries, such as storing values that can be quickly modified, or values that could change at any time, and dictionaries are not as good on that, but they are better than lists for storing key-specific items that can be accessed easily. For example, storing a list of names of people, and the person's phone number, would not be very efficient, since you would manually have to create a rule for accessing the indexes where the phone numbers dedicated to a person would be stored. If you create a dictionary, you don't have to do all that, such as only putting phone numbers at odd indexes, and calling them like this:

```python
name_numbers = ["Bob", 1243123, "Jeff", 123213556, "Billy", 123123]
print(name_numbers[name_numbers.index("Bob") + 1])
```

If you wanted to use two lists, and put the names of people in one list, and each person's phone number in another list, and you wanted to print out a person's phone number, you can also use .index() to get the value, (this only works if the index of the phone number matches the person that the phone number belongs to.) You can achieve that like this:

```python
people = ["Bob", "Jeff", "Joe"]
phone_numbers = [4324324, 23424234, 2342342132]
print(phone_numbers[phone_numbers.index("Bob")]) # gets phone number in the index of "Bob".
```

The code above basically means that since you already know what the approximate indexes of the phone numbers are, you can simply add 1 to the index, since you know that the phone numbers must be one index after the name of the person with that phone number, and you call the index of the person, and add 1 to the index, this way you can get the phone number associated with the person. This is clearly not very efficient as you have to keep doing this for every phone number, and this is why dictionaries exist. With a dictionary, you can create one to store a person and their phone number like this, and get the person's phone number very easily with either one of two methods:

```python
person_number = {
    "Bob": 12312312,
    "Jeff": 123122312,
    "Billy": 12312135646,
}
print(person_number['Bob']) # first method
print(person_number.get("Bob")) # second method, not as widely used for dictionaries that you created yourself, since you should already know what is inside your own dictionary.
```

You can also use multiple layers of calling with keys to call values from dictionaries very specifically. This works very well especially if you have nested dictionaries within dictionaries, or any nested datatypes inside of a dictionary, such as a list as a value to a key in a dictionary, etc. This can be done like:

```python
my_dict = {
    "1": [1424321, 12414],
    "2": [12312321, 123],
    "3": [12313, 463476],
}
print(my_dict["1"][0]) # accesses value stored in the key "1", and gets the value at the first index of the value that's stored in "1".
```

There are two main ways to create a dictionary:

```python
my_dict = dict("Jeff" = 231231)
my_dict = {"Jeff": 123123132}
```

Since dictionary keys must be immutable, you cannot pass a list to a dictionary to be a key, since the key must be immutable, and a list is a mutable datatype. However since a tuple is a immutable data type, you can pass a tuple to be a key in a dictionary. You can also define multiple variables at once, if you want them all to equal the same thing. You can do this by defining the three variables with a comma in between each one, and set them equal to the value you want them all to be equal to. Here is an example:

```python
a, b, c = 100
print(a, b, c)
```

You can also print multiple variables at once, just like how you would define them at once. Speaking of defining variables, there is a special format in python directly related to variable definition. You must follow the correct format, otherwise python will return an error stating that the format in which you used to define a variable, was not valid. Trying to define a variable using either of these two formats: the variable starting with numbers, or foreshadowing a built in keyword, will automatically make python return an error when you go to run your program:

```python
1myvar = 1
as = 5
print(1myvar)
print(as)
 output:
         SyntaxError: Invalid syntax
```

Python cannot accept any variable definition that conflict with it's built-in keywords, hence the reason why the "as" keyword cannot be used as a variable, or the "or" keyword, or any built-in python keyword. In list slicing the start value means the index where you want to start the slice, and the stop value means the index where you want to stop the slice. There is another value called the "step" parameter, and it means how many indexes you move each time the slicing occurs. So if you want to start from index 0, and stop at index 7, stepping by two, python will output every value in the index range between 0 -7, jumping by 2 indexes each time, without printing the stop value. Python never prints the stop value, but always prints the starting value. For example:

```python
list1 = [1, 2, 3, 4, 5]
print(list1[0:2]) # prints [1, 2]
print(list1[0:4:2]) # prints [1, 3]
```

You can basically pass every datatype to be a value to a key in a dictionary however, which means you can pass a integer value as a value, or a string, or a list, or a tuple, etc, without python returning any errors. Trying to set a mutable datatype as a key in a dictionary, will result in python returning a TypeError stating that a mutable datatype is unhashable, which basically means that passing mutable datatypes to dictionaries as keys, is unsupported. You can use the "del" keyword to specify a value stored in a certain key to delete it from the dictionary, or if you don't specify any value and you just use the "del" keyword and you pass the dictionary to it, it will delete the entire dictionary's existence, meaning that if you try calling the dictionary again, python will return a ValueError, stating that there is no value under that variable, since you just wiped that dictionary's existence.

```python
my_dict = {
    "1": [12312]
    "2": [547547234]
    "3": [5423445587]
}
del my_dict["3"] # deletes value that is stored in the key "3"
del my_dict # wipes  the dictionary "my_dict" clean from existence.
```

There is a built-in function in python that can clear out a dictionary for you, but unlike the result if you were to use the del keyword, and not specify an index in the dictionary, with the .clear() function, it will not wipe the entire dictionary's existence, rather just empty it out. So if you were to try calling it after you used the function, python would not return an error, since the dictionary still exists, it's just empty. For example, it would look something like this:

```python
my_dict = {
    "1": [31414]
    "2": [12323]
    "3": [12313]
}
my_dict.clear()
print(my_dict)
output: 
{}
```

You can have other datatypes to be keys or values of keys in a dictionary. You do not have to only use strings as values for keys, or integers for values of keys, you can have lists as values of keys, tuples as values of keys, you can have tuples as keys, etc. SETS ----- Python has integrated many efficient ways for a user to work with sets, such as the ability to join two sets together using the "" symbol, or the ability to find the difference between two sets, which basically means that you are finding the values that are not duplicates between two sets, but you ultimately print out only the non-duplicate values from the set that the "-" sign is following, even if the other set has values that are non-duplilcates as well. There is also the ability to use the "&" symbol to get the repeating values in two sets compared to each other, put into a set, and printed out for the user to see, if they were to print the result of that statement out. You can also use the "^" symbol to compare the values of two sets with each other, and for every comparison of values in the two sets, where the values don't match up, or aren't the same, python will put the values into a list, and if you were to print the results of that statement out, you would see that python returns a list containing the values that aren't the same or matching with each other in the two sets that you compared. Here's how all of these statements would look printed out:

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 9, 0}
print(set1 & set2) # prints {1, 2, 3} which are the repeating values between the two sets compared.
print(set1  set2) # prints. out {0, 1, 2, 3, 4, 5, 9}
print(set1 - set 2) # prints out {4, 5}
print(set1 ^ set2) # prints out {0, 4, 5, 9}
```

You can also use certain key symbols in special ways to achieve the purpose of what a designated symbol for that purpose could achieve. For example, you can get the non-repeating values between two sets and put them into a set, without using the "^" symbol:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
res1 = set1 -  set 2 # gets the non-repeating values from comparing the two sets, but only returns for set1
res2 = set2 - set1 # gets the non-repeating values from comparing the two sets, but only returns for set2
res3 = res1  res2 # joins together the non-repeating values from both sets that we got. 
```

There are some important built-in keywords in python that represent a special purpose that they fulfill. These keywords are the "and", "or" and "not" keywords. The "and" keyword basically checks to see if more than one conditions are met. It is most commonly used when using conditional statements to check to see if two conditions are fulfilled. If even one condition is fulfilled but the other is not, then the entire conditional statement will evaluate to False. The "or" keyword basically does the same thing, it has the capability to check/evaluate multiple conditions, but if one condition evaluates to False, but the other evaluates to True, it will return True. This is because the "or" keyword only requires one condition to be met, and if that condition is met, then it just ignores the results of every other condition that is to be evaluated. The "not" keyword doesn't really fulfill any of the purposes that those two keywords fulfill, rather the "not" keyword is typically used with the "in" keyword to check to see if something is NOT in something else or not. This is particularly useful if you want to check something for multiple different versions of itself, or just to be case-sensitive with something that could potentially cause issues with other parts of your code, such as asking for a user input. You can also pair the "not in " statement with a while loop, which will basically keep asking for input, unless the input is in the object you passed to the "not in" statement. If a statement evaluates to None, it can also be considered False, since None is an instance of the boolean value "False". So why do lists and dictionaries both exist if they both satisfy similar purposes? They both satisfy similar purposes in certain conditions, but not all conditions. Dictionaries are great for storing information that is specific to something, such as a person's phone number is to a certain person. Lists are good for storing more generic information, maybe the colors of a cake, or anything that needs to be easily accessed and changed. Lists are useful in their own ways, and so are dictionaries. Lists are not efficient with storing something specific to something else, such as a dictionary, since it doesn't have the "key:value" format like a dictionary, but lists generally are more useful when you need to store more generic information. That is the reason why both lists and dictionaries exist, and how they are useful in their own ways, and in what ways they are specifically more useful than one another.