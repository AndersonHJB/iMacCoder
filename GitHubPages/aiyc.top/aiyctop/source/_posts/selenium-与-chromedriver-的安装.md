---
title: Selenium 与 ChromeDriver 的安装
tags: []
id: '1869'
categories:
  - - Python3 网络爬虫系统教学
date: 2021-09-03 12:45:02
---

你好，我是悦创。

## Selenium 的安装

Selenium 是一个自动化测试工具，利用它我们可以驱动浏览器执行特定的动作，如点击、下拉等操作。对于一些 JavaScript 渲染的页面来说，这种抓取方式非常有效。下面我们来看看 Selenium 的安装过程。

### 1\. 相关链接

*   官方网站：[http://www.seleniumhq.org](http://www.seleniumhq.org/)
*   GitHub：[https://github.com/SeleniumHQ/selenium/tree/trunk/py](https://github.com/SeleniumHQ/selenium/tree/trunk/py)
*   PyPI：[https://pypi.org/project/selenium/](https://pypi.org/project/selenium/)
*   官方文档：[http://selenium-python.readthedocs.io](http://selenium-python.readthedocs.io/)
*   中文文档：[http://selenium-python-zh.readthedocs.io](http://selenium-python-zh.readthedocs.io/)

### 2\. pip 安装

这里推荐直接使用 pip 安装，执行如下命令即可：

```cmd
pip3 install selenium
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/5ae59233864645f58a9ee3764edc1ad1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

### 3\. wheel 安装

此外，也可以到 PyPI 下载对应的 wheel 文件进行安装（下载地址：[https://pypi.org/project/selenium/#files](https://pypi.org/project/selenium/#files)），如最新版本为 `3.141.0` ，则下载 : ![在这里插入图片描述](https://img-blog.csdnimg.cn/a622a292a72c493fb61e10f130c2e848.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 然后进入 wheel 文件目录，使用 pip 安装：

```
pip3 install selenium-3.141.0-py2.py3-none-any.whl
```

### 4\. 验证安装

进入 Python 命令行交互模式，导入 Selenium 包，如果没有报错，则证明安装成功：

```cmd
$ python3
>>> import selenium
```

但这样做还不够，因为我们还需要用浏览器（如 Chrome、Firefox 等）来配合 Selenium 工作。 后面我们会介绍 Chrome、Firefox、PhantomJS 三种浏览器的配置方式。有了浏览器，我们才可以配合 Selenium 进行页面的抓取。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/e6803759dd284fc69e612bc2396e8fd1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## ChromeDriver 的安装

前面我们成功安装好了 Selenium 库，但是它是一个自动化测试工具，需要浏览器来配合使用，本节中我们就介绍一下 Chrome 浏览器及 ChromeDriver 驱动的配置。 首先，下载 Chrome 浏览器，方法有很多，在此不再赘述。 随后安装 ChromeDriver。因为只有安装 ChromeDriver，才能驱动 Chrome 浏览器完成相应的操作。下面我们来介绍下怎样安装 ChromeDriver。

### 1\. 相关链接

*   官方网站：[https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
*   下载地址：[https://chromedriver.storage.googleapis.com/index.html](https://chromedriver.storage.googleapis.com/index.html)

### 2\. 准备工作

在这之前请确保已经正确安装好了 Chrome 浏览器并可以正常运行，安装过程不再赘述。

### 3\. 查看版本

点击 Chrome 菜单 “帮助”→“关于 Google Chrome”，即可查看 Chrome 的版本号： ![在这里插入图片描述](https://img-blog.csdnimg.cn/c39d618e59ae439eb7e90340c5915ad2.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 这里我的 Chrome 版本是 `92.0`。 请记住 Chrome 版本号，因为选择 ChromeDriver 版本时需要用到。

### 4\. 下载 ChromeDriver

打开 ChromeDriver 的官方网站：

1.  [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
2.  [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
3.  [https://chromedriver.storage.googleapis.com/index.html](https://chromedriver.storage.googleapis.com/index.html)

上面两个链接都是可以的。

### 5\. 环境变量配置

下载完成后，将 ChromeDriver 的可执行文件配置到环境变量下。 在 Windows 下，建议直接将 chromedriver.exe 文件拖到 Python 的 Scripts 目录下，如图： ![在这里插入图片描述](https://img-blog.csdnimg.cn/1dfd2e0697b94b3e8caca8c98b5de328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 此外，也可以单独将其所在路径配置到环境变量。 在 Linux 和 Mac 下，需要将可执行文件配置到环境变量或将文件移动到属于环境变量的目录里。 例如，要移动文件到 /usr/bin 目录。首先，需要在命令行模式下进入其所在路径，然后将其移动到 /usr/bin：

```cmd
sudo mv chromedriver /usr/bin
```

当然，也可以将 ChromeDriver 配置到 `$PATH`。首先，可以将可执行文件放到某一目录，目录可以任意选择，例如将当前可执行文件放在 `/usr/local/chromedriver` 目录下，接下来可以修改 `～/.profile` 文件，相关命令如下：

```cmd
export PATH="$PATH:/usr/local/chromedriver"
```

保存后执行如下命令：

```cmd
source ~/.profile
```

即可完成环境变量的添加。

### 6\. 验证安装

配置完成后，就可以在命令行下直接执行 chromedriver 命令了：`chromedriver` 如果输入控制台有类似下图所示的输出，则证明 ChromeDriver 的环境变量配置好了。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/9bd20593374e4093aaa1b9cb2bc62c86.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 随后再在程序中测试，执行如下 Python 代码：

```python
from selenium import webdriver
browser = webdriver.Chrome()
```

运行之后，如果弹出一个空白的 Chrome 浏览器，则证明所有的配置都没有问题。如果没有弹出，请检查之前的每一步配置。 如果弹出后闪退，则可能是 ChromeDriver 版本和 Chrome 版本不兼容，请更换 ChromeDriver 版本。 如果没有问题，接下来就可以利用 Chrome 来做网页抓取了。

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/baa4e9fa26404df987ddcdc2baad7a36.png)