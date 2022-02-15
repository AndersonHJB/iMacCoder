---
title: Python - OS Module
tags: []
id: '1925'
categories:
  - - os
  - - Python os库
date: 2021-09-30 00:02:59
---

Hello, My name is aiyuechuang. It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc. You first need to import the `os` module to interact with the underlying operating system. So, import it using the `import os` statement before using its functions.

## Getting Current Working Directory

The `getcwd()` function confirms returns the current working directory. **Example: Get Current Working Directory**

```python
>>> import os
>>> os.getcwd()
'C:\\Python37'
```

## Creating a Directory

We can create a new directory using the `os.mkdir()` function, as shown below. **Example: Create a Physical Directory**

```python
>>> import os
>>> os.mkdir("C:\MyPythonProject")
```

A new directory corresponding to the path in the string argument of the function will be created. If you open the `C:\` drive, then you will see the `MyPythonProject` folder has been created. By default, if you don't specify the whole path in the `mkdir()` function, it will create the specified directory in the current working directory or drive. The following will create `MyPythonProject` in the `C:\Python37` directory. **Example: Create a Physical Directory**

```python
>>> import os
>>> os.getcwd()
'C:\Python37'
>>> os.mkdir("MyPythonProject")
```

## Changing the Current Working Directory

We must first change the current working directory to a newly created one before doing any operations in it. This is done using the `chdir()` function. The following change current working directory to `C:\MyPythonProject`. **Example: Change Working Directory**

```python
>>> import os
>>> os.chdir("C:\MyPythonProject") # changing current workign directory
>>> os.getcwd()
'C:\MyPythonProject'
```

You can change the current working directory to a drive. The following makes the `C:\` drive as the current working directory. **Example: Change Directory to Drive**

```python
>>> os.chdir("C:\\")
>>> os.getcwd()
'C:\\'
```

In order to set the current directory to the parent directory use `".."` as the argument in the `chdir()` function. **Example: Change CWD to Parent**

```python
>>> os.chdir("C:\\MyPythonProject")
>>> os.getcwd()
'C:\\MyPythonProject'
>>> os.chdir("..")
>>> os.getcwd()
'C:\\'
```

## Removing a Directory

The `rmdir()` function in the OS module removes the specified directory either with an absolute or relative path. Note that, for a directory to be removed, it should be empty. **Example: Remove Directory**

```python
>>> import os
>>> os.rmdir("C:\\MyPythonProject")
```

However, you can not remove the current working directory. To remove it, you must change the current working directory, as shown below. **Example: Remove Directory**

```python
>>> import os
>>> os.getcwd()
'C:\\MyPythonProject'
>>> os.rmdir("C:\\MyPythonProject")
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\MyPythonProject'
>>> os.chdir("..")
>>> os.rmdir("MyPythonProject")
```

Above, the `MyPythonProject` will not be removed because it is the current directory. We changed the current working directory to the parent directory using `os.chdir("..")` and then remove it using the `rmdir()` function.

## List Files and Sub-directories

The `listdir()` function returns the list of all files and directories in the specified directory. **Example: List Directories**

```python
>>> import os
>>> os.listdir("c:\python37")
['DLLs', 'Doc', 'fantasy-1.py', 'fantasy.db', 'fantasy.py', 'frame.py', 
'gridexample.py', 'include', 'Lib', 'libs', 'LICENSE.txt', 'listbox.py', 'NEWS.txt',
'place.py', 'players.db', 'python.exe', 'python3.dll', 'python36.dll', 'pythonw.exe', 
'sclst.py', 'Scripts', 'tcl', 'test.py', 'Tools', 'tooltip.py', 'vcruntime140.dll', 
'virat.jpg', 'virat.py']
```

If we don't specify any directory, then list of files and directories in the current working directory will be returned. **Example: List Directories of CWD**

```python
>>> import os
>>>os.listdir()
['.config', '.dotnet', 'python']
```

Learn more about [OS modules in Python docs](https://docs.python.org/3/library/os.html)

> AI yuecuang launched a tutorial class, including "Python language tutorial class, C++ tutorial class, algorithm/data structure tutorial class, children's programming, pygame game development", all one-to-one teaching: one-to-one tutoring + one-to-one q&a + assignment + project practice, etc. QQ, wechat online, response at any time! V: Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/5299daef5aa8448d871a42da9f7f4a00.png)