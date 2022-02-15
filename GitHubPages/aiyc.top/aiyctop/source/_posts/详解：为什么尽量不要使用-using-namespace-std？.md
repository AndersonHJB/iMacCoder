---
title: 详解：为什么尽量不要使用 using namespace std？
tags: []
id: '1799'
categories:
  - - C++一对一辅导
date: 2021-07-15 09:43:49
---

你好，我是悦创。 Q1：为什么尽量不要使用 using namespace std？为什么我看到很多资料都写着能不用就不用，能在大括号里面用就不要在外面用。我刚刚开始学 c++ 所以不太明白

## A：

*   需要保证的是尽量不要在头文件里 using 任何东西尤其是 namespace，要不然 include 进来的时候很容易莫名其妙产生命名冲突。
*   有条件的话，所有引入的符号都定义在自己的 namespace 里。任何情况下都不要 `using namespace std` 从理论上来说也是有道理的：因为系统库可能会升级，这样升级编译使用的 C++ 版本的时候有可能因为引入了新的符号跟自己代码里的命名冲突。
*   但一般来说，升级 C++ 版本最多几年也就做一次，冲突的可能性也并不大，而升级 C++ 版本本来也不一定能保证编译成功，为了这种特殊时候省一点时间让平时的编码和阅读都变费劲并没有什么道理。

## B：

其实底线就一条：如果你的头文件（`*.h、*.hpp`）有被外部使用，则不要使用任何 using 语句引入其他命名空间或其他命名空间中的标识符。 因为这可能会给使用你的头文件的人添麻烦。更何况头文件之间都是相互套的，假如人人都在头文件里包含若干个命名空间，到了第 N 层以后突然出现了一个命名冲突，这得往前回溯多少层才能找到冲突啊。而这个冲突本来是可以避免的。 其实在源文件（`*.cpp`）里面怎么 using 都是没关系的，因为 cpp 里的代码不影响到他人。甚至如果你的头文件（`*.h、*.hpp`）只是自己用，那 using 也是没事的。但为了养成良好的习惯，很多人仍然建议不要随便 using，以防写顺手，届时在共享的头文件里也顺手 using 了，造成人祸。

## C：

**举一个简单的例子：** 我们原来的代码一直没问题，但如果要使用 C++17 标准就报一个错，这个错影响还挺多的。具体原因是，C++17 添加了一种新类似 `std::byte` ，而 Windows 头文件里自带一种类型 `byte`。 这两种类型本身并不冲突，因为一个是 `std::byte`，另一个是 `byte`。 **但是！！！**，如果代码里广泛使用了using namspace std;再遇到 byte 的时候，编译器就不知道它是 Windows 的 byte 还是 `std:byte` 省略了 std。所以，尽量少在工程里包含这种"大杀器"。你如果想省事，可以在自己的 `.cpp` 文件里使用（`.cpp` 不暴露声明）。实在想在 `.h` 里用（为省事），尽量使用诸如 `using std::vector;` 之类的，用哪个暴露哪个，而不是一次性全部暴露。

## D：

这就跟 python 里你写

```python
from numpy import *
from pandas import *
from tensorflow import *
```

一样的。很容易就有冲突的。。。 看来论据不够充分 那我加下 《C++ Primer Plus (第六版 中文版 人民邮电出版社)》第九章： 内存模型和名称空间 第 328 页: "有关 using 编译命令和 using 声明，需要记住的一点是，他们 **增加了名称冲突的可能性**。" 《C++ Primer Plus (第六版 中文版 人民邮电出版社)》第九章: 内存模型和名称空间 第329页:

> 一般说来，**使用 using 命令** 比 **使用 using 编译命令** 更 **安全** ，这是由于它只导入了制定的名称。 如果该名称与局部名称发生冲突，编译器将发出指示。using 编译命令导入所有的名称，包括可能并不需要的名称。如果与局部名称发生冲突，则 **局部名称将覆盖名称空间版本** ，而编译器并不会发出警告。 另外，名称空间的开放性意味着名称空间的名称可能分散在多个地方，这使得难以准确知道添加了哪些名称。 ... 然而名称空间的支持者希望有更多的选择，既可以使用解析运算符面也可以使用 using 声明，也就是说，不要这样做：

```cpp
using namespace std; // avoid as too indiscriminate(随意)
```

而应这样做

```cpp
int x;
std::cin >> x ;
std::cout << x << std::endl;
```

或者这样做

```cpp
using std::cin;
using std::cout;
using std::endl;
int x;
cin >> x;
cout << x << endl;
```

所以，总之：头文件里不要用 using namespace。因为头文件内容相当于一段代码的公开部分，会在预处理阶段被替换进引用者的源文件里。 具体命令操作查看： ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021071509414775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 使用 using namespace 会对引用者产生侵入性，使得引用你的头文件有很多未知的副作用。不仅 using namespace，任何 using 都是要尽量避免的。任何类型函数都应该写全名。 如果在源文件中用 using namespace 就是个人的选择了。特别是项目小没有很多重名的时候。如果你看到 Google c++ style guide 上说不要用 using namespace std，更多是因为代码库里有很多 std 的补充替代品，比如 absl。使用时注明用的是哪个可读性比较好。

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210715094248557.png)