---
title: MacOS怎么安装ChromeDriver「2020安装教程」
tags: []
id: '824'
categories:
  - - 环境搭建
date: 2020-08-27 22:43:10
---

你好，我是悦创。 如果你觉得教程过时可以关注微信公众号：AI悦创，加小编好友。群友为你提供技术帮组。 由于我用的 MAC 电脑，所以不同于 Windows 系统，ChromeDriver 的安装方式也会不一样。 首先，对于 Windows 而言，只要把下载下来的 ChromeDriver 二进制执行文件存放在 python3 的安装根目录下，并添加 Path 即可。 但是，对于 MacOS 而言，直接放在 python3 的安装根目录下是没用的，因为我就犯过这样的错，然后在执行下面的代码的时候报了 找不到 ChromeDriver 的错，于是根据报错信息，我上网查了一下对于 Mac 安装 ChromeDriver 的正确打开方式，嗯，方式如下：

1.  对了，先提供一个安装 ChromeDriver 的链接：
    *   https://npm.taobao.org/mirrors/chromedriver/
    *   官网：[https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
2.  找到跟你的 Chrome 浏览器版本一致的安装包，下载并存放到 /usr/local 这个目录下
    

查看浏览器版本的方法如下： ![image-20200827223149210](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200827224102.png) ![image-20200827223248170](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200827224057.png) 请看上图，我的浏览器的版本是：版本 85.0.4183.83（正式版本） （64 位），那么我就要下载的 ChromeDriver 的版本是 85.0.4183.83 的，就是如下这个啦： ![image-20200827223441091](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200827224047.png) ![image-20200827223459773](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200827224041.png) Windows 系统其实也是类似的，可以直接选择 Windows 即可。

3.  下载到指定安装目录之后，我们通过终端命令来解压，要解压到 bin 目录下哦，否则也是不可行的，所以一开始其实也可以把安装包直接下载丢到 /usr/local/bin 这个目录下，省得解压的时候再指定目录。anyway，你喜欢哪种方法都行，只要最后保证把chromedriver.exe 这个执行文件存放到 /usr/local/bin 这个目录就行：

```cmake
sudo unzip chromedriver_mac64.zip /usr/local/bin
```

4.  接着你就可以写下这两行代码校验一下啦，对了我用的 python 语言：

```python
from selenium.webdriver import Chrome

webdriver_obj = Chrome()
```

5.  执行上述代码，如果出现如下页面，就说明安装成功啦！

![image-20200827224033246](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200827224037.png)