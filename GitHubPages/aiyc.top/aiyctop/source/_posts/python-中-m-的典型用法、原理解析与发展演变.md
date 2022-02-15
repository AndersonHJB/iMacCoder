---
title: Python 中 -m 的典型用法、原理解析与发展演变
tags: []
id: '1652'
categories:
  - - 技术杂谈
date: 2021-05-06 14:47:05
---

> 这篇文章主要介绍了 Python 中 -m 的典型用法、原理解析与发展演变,需要的朋友可以参考下

我们可以使用，Python -h 来查看 option。 我呢，想要聊聊比较特殊的 “-m” 选项： 关于它的典型用法、原理解析与发展演变的过程。 首先，让我们用“-help”来看看它的解释：

```python
➜  ~ Python3 -h
usage: /usr/local/bin/Python3 [option] ... [-c cmd  -m mod  file  -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
```

我把其中 -m 的解析提取出来：

```python
-m mod : run library module as a script (terminates option list)
```

*   mod 是 module 的缩写，**即 -m 选项后面的内容是 module（模块），其作用是把模块当成脚本来运行。**
    
*   terminates option list：意味着 -m 之后的其它选项不起作用，在这点上它跟 -c 是一样的，都是 “**终极选项**”。官方把它们定义为 “**接口选项**”（Interface options），需要区别于其它的普通选项或通用选项。
    

## 1\. -m 选项的五个典型用法

### 1\. 1 第一种「http.server」

Python 中有很多使用 -m 选项的场景，相信大家可能会用到或者看见过，我在这里想分享 5 个。 在 Python3 中，只需一行命令就能实现一个简单的 HTTP 服务：

```python
python -m http.server 8000

# 注:在 Python2 中是这样
python -m SimpleHTTPServer 8000
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210501153936199.png) 执行后，在本机打开 **http://localhost:8000** ，或者在局域网内的其它机器上打开 **http://本机ip:8000** ，就能访问到执行目录下的内容，例如下图就是我本机的内容： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210501154037875.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 比如，**这样传输数据或者文件，即可不用 QQ、微信之类的东西了。**每台电脑的 IP 地址不一样，具体查看方法，可以自行谷歌。不过我简单提两个命令行命令，老手一看就懂，非老手直接谷歌吧。

#### Mac ip 地址

```cmd
ifconfig
```

可看到这里的 en0 这个网卡的 ip 地址了。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210501154927460.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 当然，如果你觉得使用命令行太复杂，我们还是可以使用之前介绍的，在网络设置窗口上查看 ip 吧。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210501155025333.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

#### Windows ip

```cmd
ipconfig -all
```

我们找到 iPv4 字样的那一行就是我们想要的 ip 地址了。

### 1.2 第二种「pydoc」

与此类似，我们只需要一行命令：

```python
python -m pydoc -p xxx
```

就能生成 HTML 格式的官方帮助文档，可以在浏览器中访问。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210501162733819.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 上面的命令执行了 pydoc 模块，会在 9000 端口启动一个 http 服务，在浏览器中打开，我的结果如下： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210504101602552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 1.3 第三种「pdb」

它的第三个常见用法是执行 pdb 的调试命令 `python -m pdb xxx.py` ，以调试模式来执行 `xxx.py` 脚本： **test.py**

```python
print("Hello AI悦创。")
print("Life is short, You need Python!")
```

接下来使用命令行来使用： 代码版：

```cmd
➜  0504 git:(master) ✗ ls
test.py
➜  0504 git:(master) ✗ python3 -m pdb test.py
> /Users/apple/Desktop/GitHub/PyCharm_Coder/Personal_Practice_Code/2021/05/0504/test.py(8)<module>()
-> print("Hello AI悦创。")
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) run
Restarting test.py with arguments:
    test.py
> /Users/apple/Desktop/GitHub/PyCharm_Coder/Personal_Practice_Code/2021/05/0504/test.py(8)<module>()
-> print("Hello AI悦创。")
(Pdb) next
Hello AI悦创。
> /Users/apple/Desktop/GitHub/PyCharm_Coder/Personal_Practice_Code/2021/05/0504/test.py(9)<module>()
-> print("Life is short, You need Python!")
(Pdb)
```

截图： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506112044429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 1.4 第四种「timeit」

第四个同样挺有用的场景是用 timeit 在命令行中测试一小段代码的运行时间。 以下的 3 段代码，用不同的方式拼接 “0-1-2-……-99” 数字串。可以直观地看出它们的效率差异：

```cmd
➜  0504 git:(master) ✗ python3 -m timeit "'-'.join(str(n) for n in range(100))"
10000 loops, best of 5: 22.8 usec per loop
➜  0504 git:(master) ✗ python3 -m timeit "'-'.join([str(n) for n in range(100)])"
10000 loops, best of 5: 21 usec per loop
➜  0504 git:(master) ✗ python3 -m timeit "'-'.join(map(str, range(100)))"
20000 loops, best of 5: 17.2 usec per loop
```

最后，还有一种常常被人忽略的场景：`python -m pip install xxx` 。我们可能会习惯性地使用 `pip install xxx` ，或者做了版本区分时用 `pip3 install xxx` ，总之不在前面用 `python -m` 做指定。但这种写法可能会出问题。 很巧合的是，在（2019.11.01），Python 的核心开发者、[第一届指导委员会 五人成员之一的 Brett Cannon](https://mp.weixin.qq.com/s/hjcVFaGgI_Ww--Ktv7XP9Q) 专门写了一篇博客 [《 Why you should use "python -m pip" 》](https://snarky.ca/why-you-should-use-python-m-pip/) ，提出应该使用 `python -m pip` 的方式，并做了详细的解释。

### \-m 选项的两种原理解析

看了前面的几种典型用法，你是否开始好奇： `-m` 是怎么运作的？它是怎么实现的？ 对于 `python -m name` ，一句话解释： Python 会检索 sys.path ，查找名字为 `name` 的模块或者包（含命名空间包），并将其内容当成 `__main__` 模块来执行。

#### 1、对于普通模块

以 `.py` 为后缀的文件就是一个模块，在 `-m` 之后使用时，只需要使用模块名，不需要写出后缀，但前提是该模块名是有效的，且不能是用 C 语言写成的模块。 在 `-m` 之后，如果是一个无效的模块名，则会报错 **No module named xxx**。 如果是一个带后缀的模块，则首先会导入该模块，然后可能报错：**Error while finding module specification for 'xxx.py' (AttributeError: module 'xxx' has no attribute '\_\_path\_\_'**。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506142021233.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 对于一个普通模块，有时候这两种写法表面看起来是等效的： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506142034781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 两种写法都会把定位到的模块脚本当成主程序入口来执行，即在执行时，该脚本的 `__name__` 都是 `__main__` ，跟 import 导入方式是不同的。 但它的前提是：在执行目录中存在着 `test.py` ，且只有唯一的 **test 模块**。对于本例，如果换一个目录执行的话，`python test.py` 当然会报找不到文件的错误，然而，`python -m test` 却不会报错，因为解释器在遍历 sys.path 时可以找到同名的 `test` 模块，并且执行： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506142543782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 由此差异，我们其实可以总结出 `-m` 的用法： **已知一个模块的名字，但不知道它的文件路径，那么使用 -m 就意味着交给解释器自行查找，若找到，则当成脚本执行。** 以前面的 `python -m http.server 8000` 为例，我们也可以找到 `server` 模块的绝对路径，然后执行，尽管这样会变得很麻烦。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506143452922.png)

#### 2\. 探究

那么，`-m` 方式与直接运行脚本相比，在实现上有什么不同呢？ 1、直接运行脚本时，相当于给出了脚本的完整路径（不管是绝对路径还是相对路径），解释器根据： **文件系统的查找机制**， 定位到该脚本，然后执行： 使用 `-m` 方式时。 解释器需要在不 import 的情况下，在 **所有模块命名空间** 中查找，定位到脚本的路径，然后执行。 为了实现这个过程，解释器会借助两个模块： pkgutil 和 runpy ，前者用来获取所有的模块列表，后者根据模块名来定位并执行脚本 2、对于包内模块，如果 `-m` 之后要执行的是一个包，那么解释器经过前面提到的查找过程，先定位到该包，然后会去执行它的 `__main__` 子模块，也就是说，在包目录下需要实现一个 `__main__.py` 文件。 换句话说，假设有个包的名称是 `pname` ，那么， `python -m pname` ，其实就等效于 `python -m pname.__main__`。 仍以前文创建 HTTP 服务为例，`http` 是 Python 内置的一个包，它没有`__main__.py` 文件，所以使用 `-m` 方式执行时，就会报错：**No module named http.\_\_main\_\_; 'http' is a package and cannot be directly executed。** ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506150301809.png) 作为对比，我们可以看看前文提到的 pip，它也是一个包，为什么`python -m pip` 的方式可以使用呢？当然是因为它有 `__main__.py` 文件： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210506150334197.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) `python -m pip` 实际上执行的就是这个 `__main__.py` 文件，它主要作为一个调用入口，调用了核心的 `pip._internal.main`。 http 包因为没有一个统一的入口模块，所以采用了 `python -m 包.模块` 的方式，而 pip 包因为有统一的入口模块，所以加了一个 `__main__.py` 文件，最后只需要写 `python -m 包`，简明直观。

#### 总结

以上所述是小编给大家介绍的 Python 中 `-m` 的典型用法、原理解析与发展演变，希望对大家有所帮助，如果大家有任何疑问请给我留言，小编会及时回复大家的。