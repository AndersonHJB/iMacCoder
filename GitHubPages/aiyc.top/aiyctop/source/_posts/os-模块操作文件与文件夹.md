---
title: os 模块操作文件与文件夹
tags: []
id: '1670'
categories:
  - - Python os库
  - - 技术杂谈
date: 2021-05-13 17:19:10
---

你好，我是悦创。 在日常工作中，我们经常会和文件、文件夹打交道，比如将服务器上指定目录下文件进行归档，或将爬虫爬取的数据根据时间创建对应的文件夹 / 文件，如果这些还依靠手动来进行操作，无疑是费时费力的，这时候 Python 中的 os 模块就必不可少了。本小节将围绕 os 模块的使用进行介绍。

## 1\. os 模块介绍

os 模块是 Python 中的内置模块，无需安装即可使用，os 模块提供非常丰富的方法用来处理文件和目录。 os 模块的使用步骤如下。

### 步骤 1：导入 os 模块

```python
import os
```

### 步骤 2：操作文件或者文件夹

通过 os 模块提供的方法对文件、文件夹进行操作。

## 2\. os 模块操作文件与文件夹

os 模块是 Python 中操作文件与文件夹时常用的模块，os 模块中常用方法见下表。

方法名

描述

getcwd()

获取当前工作目录

listdir(path)

获取指定的文件夹包含的文件或文件夹的名字的列表

rename(src,dst)

用于文件或文件夹重命名

makedirs(path)

用于递归创建文件夹

removedirs(path)

用于递归删除文件夹

remove(path)

删除指定路径的文件

open(file, flags\[, mode\])

打开文件

read(fd,n)

读取指定文件

wirte(fd,str)

写入内容

walk(dir)

文件、目录遍历器

**os.path 模块中常用方法见下表。**

方法名

描述

os.path.exists(path)

如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False

os.path.join(path1\[, path2\[, …\]\])

把目录和文件名合成一个路径

下面来具体看下每个方法的使用：

### 1\. getcwd() 使用：

```python
import os
print(os.getcwd()) #输出：D:\code
```

**代码解释：** 当前代码文件存放在 `D:\code` 下，导入 OS 模块，使用 `getcwd()` 方法，获取当前工作目录，打印结果为 `D:\code`，如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513155258286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 2\. listdir() 使用：

```python
import os
print(os.listdir('.'))
# 输出：['dingding.py', 'image', 'index.py', 'writeppt.py', 'writeword.py']
```

**代码解释：** `listdir()` 方法可以 **获取指定的文件夹包含的文件或文件夹的名字的列表** ，目前 `D:\code` 目录下文件结构如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513160332345.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 通过 `listdir()` 方法传递指定目录，代码中传递 “`.`” 表示当前目录，输出结果：`['dingding.py', 'image', 'index.py', 'writeppt.py', 'writeword.py']`，如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513160610517.png)

### 3\. rename() 使用：

```python
import os

os.rename("image", "newimage")
os.rename("dingding.py", "newdingding.py")
```

**代码解释 ：** `rename()` 方法为重命名文件或文件夹，第一个参数为要重命名的文件名或文件夹名，第二个参数为修改后的名称，上述代码中将文件夹 `image` 重名为 `newimage` ，将文件 `dingding.py` 重名为 `newdingding.py` ，代码执行完成后，`D:\code` 目录下效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513162210882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 4\. makedirs() 使用：

```python
import os
os.makedirs("dist/src/code")
```

**代码解释：** `makedirs()` 方法用于递归创建目录，参数即为需要递归创建的目录，上述代码指定 `dist/src/code` ，即表示创建一个 `dist` 文件夹，其中包含 `src` 文件夹，在 `src` 下包含 code 文件夹。代码执行完成后，`D:\code` 目录下效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513163114350.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 5\. removedirs() 使用：

```python
import os
os.removedirs("dist/src/code")
print(os.listdir('.'))
# 输出：['newdingding.py', 'newimage', 'index.py', 'writeppt.py', 'writeword.py']
```

**代码解释 ：** `removedirs()` 方法用于递归删除目录，参数为要递归删除的目录，上述代码指定 `dist/src/code` ，即将 `dist` 文件夹下 `src` 文件夹下 `code` 文件夹一并进行删除。 执行完删除后，通过 `listdir()` 方法查看当前目录下文件结构，输出 `['newdingding.py', 'newimage', 'index.py', 'writeppt.py', 'writeword.py']` ，可以看到已经完成删除操作。

### 6\. remove() 使用：

```python
import os
os.remove("newdingding.py")
print(os.listdir('.'))
# 输出：['newimage', 'index.py', 'writeppt.py', 'writeword.py']
```

**代码解释 ：** `remove()` 方法用于删除指定文件，上述代码中删除 `newdingding.py` 文件，删除完成后，通过 `listdir ()` 方法查看当前目录文件结构，输出 `['newimage', 'index.py', 'writeppt.py', 'writeword.py']`，可以看到已经完成删除操作。代码执行完成后，`D:\code` 目录下效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513164358371.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 7\. open() 使用：

```python
import os
os.open("writeppt.py", os.O_RDONLY)
```

**代码解释：** `open()` 方法用于打开指定文件，第一个参数为要打开的文件，第二个参数为打开的模式，可以取值如下所示：

*   **OS.O\_RDONLY**：以只读的方式打开；
*   **OS.O\_WRONLY**：以只写的方式打开；
*   **OS.O\_RDWR**：以读写的方式打开；
*   **OS.O\_NONBLOCK**：打开时不阻塞；
*   **OS.O\_APPEND**：以追加的方式打开；
*   **OS.O\_CREAT**：创建并打开一个新文件；
*   **OS.O\_TRUNC**：打开一个文件并截断它的长度为零（必须有写权限）；
*   **OS.O\_EXCL**：如果指定的文件存在，返回错误；
*   **OS.O\_SHLOCK**：自动获取共享锁；
*   **OS.O\_EXLOCK**：自动获取独立锁；
*   **OS.O\_DIRECT**：消除或减少缓存效果；
*   **OS.O\_FSYNC**：同步写入；
*   **OS.O\_NOFOLLOW**：不追踪软链接。

上述代码中，打开 `writeppt.py` 文件，以只读方式打开，返回新打开文件的描述符，可以进行后续的读取、写入操作。

### 8\. read() 使用：

```python
import OS
fs=os.open("writeppt.py",OS.O_RDONLY) # fs 就是 writeppt.py 的文件描述符
print(OS.read(fs,24))
```

**代码解释** ：read () 方法为从文件描述符中读取文件内容，第一个参数为 open () 方法打开文件返回的文件描述符，第二个参数为读取的字节数。上述代码中读取 `writeppt.py` 文件 24 个字节内容。

### 9\. write() 使用：

```python
import os
fs=os.open("test.txt", os.O_RDWR) # fs 就是 test.txt 的文件描述符，打开模式设置为以读写的方式打开
print(os.write(fs, "hello python")) #写入内容为 hello python
```

**代码解释**：`write()` 方法用于写入字符串到文件描述符 fs 中，第一个参数为文件描述符，第二个参数为写入的字符串内容。代码执行完成后，输出效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513165908653.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 10\. walk() 使用：

```python
import os
for dirpath, dirnames, filenames in os.walk("D:/code"):
    #输出：D:/code  ['newimage'] ['index.py','test.txt','writeppt.py','writeword.py']
    print(dirpath, dirnames, filenames)
```

**代码解释**：`os.walk()` 方法是一个简单易用的文件、目录遍历器，接收参数为要遍历的目录的地址，返回的是一个三元组 `(dirpath, dirnames, filenames)` ，分别表示当前正在遍历的这个文件夹的本身的地址、该文件夹中所有的目录的名字、该文件夹中所有的文件。代码中指定目录 `D:/code` ，执行时会遍历 D 盘 code 目录下所有文件和文件夹，输出效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513170104697.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 11\. os.path.exists() 使用：

```python
import os
print(os.path.exists("D:\\code\\index.py")) # 输出 true
print(os.path.exists("D:\\code\\test.py")) # 输出 False
```

**代码解释** ：`exists()` 方法判断路径是否存在，上面代码中在 D 盘 code 文件夹下存在 `index.py` ，所以输出 True，不存在 `test.py`，输出 False。代码执行完成后，输出效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513170330403.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 12\. os.path.join() 使用：

```python
import os
# 输出D:\code\2020\11
print(os.path.join("D:\\code\\", "2020\\","11"))
```

**代码解释：** `join()` 方法用于把目录和文件名合成一个路径。代码执行完成后，输出效果如下图所示。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513170602994.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 3\. os 模块实战

在开发中，程序遇到异常情况时需要记录错误日志文件，为便于程序员调试，通常错误日志文件的目录结构为：`当前年的文件夹下 / 当前月的文件夹下 / 当前日的文件夹 / 具体的 txt 错误日志文件` 。这时可以使用 Python 的 os 模块封装创建日志的公共方法，完成需求如下：

1.  根据传入的时间创建对应的年、月、日文件夹，在创建前需要判断文件夹是否存在，存在则不作操作
2.  根据传入的内容，创建 txt 错误日志文件，当重复调用时，txt 错误日志文件内容为追加

根据上述需求背景，封装后的代码如下：

```python
import os
import datetime

# 获取到当前年
year_time = datetime.datetime.now().year
# 获取到当前月
month_time = datetime.datetime.now().month
# 获取到当前日
daytime = datetime.datetime.now().day

# 生成错误日志文件
def createError(message):
    path = os.getcwd()+"\\"+str(year_time)+"\\"+str(month_time)+"\\"+str(daytime)
    # 文件路径是否存在
    ispath = os.path.exists(path)
    # 判断文件是否存在：不存在创建
    if not ispath:
        os.makedirs(path)
    # 写入异常到错误日志文件（log.txt）
    writeError(path, message)
# 写入异常到错误日志文件
def writeError(path, message):
    fs = os.open(path+"\\log.txt", os.O_RDWR  os.O_CREAT)
    os.write(fs, message.encode('utf-8'))
# 模拟调用
createError("SQL语句异常")

```

**代码解释**：代码中封装了两个方法分别为 `createError()` 方法和 `writeError()` 方法，用于生成错误日志存放文件夹及像 `log.txt` 写入错误日志内容。年月日文件夹使用 datetime 模块获取当前系统的年、月、日，使用 `exists()` 方法判断指定路径是否存在，返回布尔值，存在则返回 True。 如果不存在则通过 os 模块下的 `makedirs()` 方法进行创建。文件夹创建完成后，调用 `writeError()` 方法写入错误内容，首先使用 `open()` 方法打开 `log.txt` 文件，打开模式设置为读写和创建，通过 `write()` 方法写入错误内容到 `log.txt`。代码执行完成后，输出效果如下图所示： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513171656784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513171704240.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 4\. 小结

本节课程我们主要学习了 os 模块的使用。本节课程的重点如下： - 了解 os 模块作用及使用步骤； - 掌握 os 模块中操作文件与文件夹的使用方法。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513173500963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)