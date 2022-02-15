---
title: Python pip换源所有方法
tags: []
id: '1658'
categories:
  - - 技术杂谈
date: 2021-05-08 20:09:58
---

你好，我是悦创。 我接下来，把所有 Python pip 换源的方法，都整理下来。

## 第一种方法

1.  打开 appdata 文件夹，在资源管理器的地址栏输入 `%appdata%` 后回车：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508192633540.png) 2. 新建一个 pip 文件夹，在 pip 文件夹里面新建一个配置文件 `pip.ini`： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508193011731.png) 3. 在配置文件中输入如下内容后保存即可：

```cmd
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

再次使用 pip，即会使用新源。 **一些常用的国内源：**

*   清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
    
*   阿里云：https://mirrors.aliyun.com/pypi/simple
    
*   中国科学技术大学 https://pypi.mirrors.ustc.edu.cn/simple
    
*   豆瓣：http://pypi.douban.com/simple
    

## 第二种方法

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508200241770.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 第三种方法

从 `pip10.0.0` 开始，有个 config 子命令可用来改配置，无需关心不同操作系统下配置文件路径。 详见讨论：[https://link.zhihu.com/?target=https%3A//github.com/pypa/pip/issues/1736](https://link.zhihu.com/?target=https%3A//github.com/pypa/pip/issues/1736) 实际使用例子：

```cmd
# 阿里源
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/

# 豆瓣源
pip config set global.index-url https://pypi.douban.com/simple

# 阿里云 http://mirrors.aliyun.com/pypi/simple/
# 科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣(douban) http://pypi.douban.com/simple/
# 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
# 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```

## 参考

1.  数据分析的环境不会搭？看这里准没错！：[https://www.aiyc.top/772.html](https://www.aiyc.top/772.html)
2.  Linux下pip使用国内源：[https://www.aiyc.top/153.html](https://www.aiyc.top/153.html)
3.  Windows下更换pip源为清华源：[https://www.aiyc.top/1657.html](https://www.aiyc.top/1657.html)