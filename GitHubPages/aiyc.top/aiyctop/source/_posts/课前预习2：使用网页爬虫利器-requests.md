---
title: 课前预习2：使用网页爬虫利器—Requests
tags: []
id: '807'
categories:
  - - Python3 网络爬虫系统教学
date: 2020-08-13 08:55:27
---

上篇文章我们讲解了使用 Python 自带的 urllib 模块来爬取我们的第一个页面。但事实上，urllib 在现在的互联网公司应用的并不是最多的。今天，我们就来介绍一下目前最为流行，也是最为方便的网络爬虫框架之一：Requests 。

## 1\. 为什么要学习 Requests

在回答这个问题之前，我们先介绍一下 Requests：

> Requests 允许你发送**纯天然，植物饲养**的 HTTP/1.1 请求，无需手工劳动。你不需要手动为 URL 添加查询字串，也不需要对 POST 数据进行表单编码。Keep-alive 和 HTTP 连接池的功能是 100% 自动化的，一切动力都来自于根植在 Requests 内部的 [urllib3](https://github.com/shazow/urllib3)。

这是节选自 [Requests 官方文档](http://cn.python-requests.org/zh_CN/latest/)的一段话，看上去像是在自卖自夸。事实上，Requests 的确极大地减少了我们的开发和配置工作。其 [GitHub 主页](https://github.com/requests/requests/)上多达 32K 的 star 也在宣告着它的成功与优秀基因。 为什么要学习 Requests 呢？对于初学者来说，主要原因是：

*   Requests 在互联网上拥有丰富的学习资源。在百度上搜索“Requests 爬虫”关键字，一共有16万多条搜索结果。这意味着 Requests 的相关技术已经比较成熟。特别对于初学者而言，一个具有丰富学习材料的内容，能够减少学习中的“挖坑”次数和“掉坑”次数；
*   Requests 官方提供中文文档。这对于新人，尤其是英语能力还不是很好的新人来说，是最好的资源。官网文档提供了详细而且非常准确的函数定义与说明。如果开发过程中出现了问题，百度、Google、Stack Overflow……所有的搜索方法都试过，但是都不能解决问题的时候，翻阅官方文档是最稳妥，而且是最快捷的解决方案。

## 2\. Requests 初体验

1.  安装 Requests Requests 是第三方库，因此我们需要手动安装。在 CMD 控制台中输入：
    
    ```python
    pip install requests
    ```
    
2.  当控制台提示安装成功后，我们进入 Python 中，导入 Requests，验证是否安装成功。 ![图2-验证requests是否安装](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200813085337.png)
    

（请原谅我这里的图用的是 Linux 系统下的截图。当我写到这部分的时候，我的 Windows 电脑“悲剧”了。）

## 3\. 重写 urllib 访问页面的代码

使用 Requests 爬取网页只需要几行代码，复杂程度远远小于 urllib。

```python
import requests
url = "http://gitbook.cn/"
web_data = requests.get(url)
web_info = web_data.text
print(web_info)
```

让我们运行这个小程序，打印出运行结果：

```python
......
<p>GitChat 是一款基于微信平台的知识分享产品。通过这款产品我们希望改变IT知识的学习方式.</p>
......
```

Amazing！Requests 自动帮我们检测编码，并且正常的显示了中文！ 让我们详细的讲解一下这段代码。

```python
import requests
url = "http://gitbook.cn/"
web_data = requests.get(url)
```

上述代码很好理解。第一行代码导入了 Requests 这个库，第二行代码定义了我们要爬取的 URL，第三行，我们直接调用 Requests 中的 get() 方法，即通过 GET 访问一个网页：

```python
 web_info = web_data.text
```

当我们发出 GET 请求后，Requests 会基于 HTTP 头部对相应的编码做出有根据的推测，所以当我们访问 web\_data.text 之前，Requests 会使用它推测的文本编码进行解析。

## 4\. 定制请求头

什么是请求头呢？HTTP 请求头，HTTP 客户程序（例如浏览器），向服务器发送请求的时候必须指明请求类型（一般是 GET 或者 POST）。如有必要，客户程序还可以选择发送其他的请求头。 还记得我们上一篇文章中提到的“模拟浏览器”的行为吗？没错，浏览器的标志也在请求头中。 ![图3-请求头](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200813085345.png) 上图就是一个典型的请求头。在 Request 中，我们可以很方便的构造自己需要的请求头：

```python
header = {             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,   */*;q=0.8',
   'Accept-Language':'zh-CN,zh;q=0.9',
   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
   }
r = requests.get("http://gitbook.cn/", headers=headers)
```

## 5\. Cookie 的用处

> 平时上网时都是使用无状态的 HTTP 协议传输出数据，这意味着客户端与服务端在数据传送完成后就会中断连接。这时我们就需要一个一直保持会话连接的机制。在 Session 出现前，Cookie 就完全充当了这种角色。也就是，Cookie 的小量信息能帮助我们跟踪会话。一般该信息记录用户身份。

什么是 Cookie？简单的说，就是记录你用户名和密码，让你可以直接进入自己账户空间的一组数据。多说无益，我们来亲自实践一下。 这次我们尝试访问 CSDN，首先这是我已经登录之后，显示的个人页面。 ![图4-个人页面](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200813085348.png) 在没有加入 Cookie 之前，我们尝试访问一下这个页面。

```python
import requests
url = "https://my.csdn.net/"
web_data = requests.get(url)
web_info = web_data.text
print(web_info)
```

运行结果为： ![图5-未登录页面](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200813085352.png) 结果显示——你要么登录，要么注册。 那么，如果加入了 Cookie 呢？我们首先获取自己的 Cookie，如果你使用的是 Chrome 浏览器，只需要：右击 -> 查看 -> network，然后刷新一下页面，就可以看到请求头中相对应的 Cookie。 ![图6-自己的Cookie](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200813085356.png) **注意**：Cookie 数据是十分隐私的个人数据！如果被他人获取到，采用一些常规手段，就可以登录你的相关账号，因此，请不要随意将自己的 Cookie 信息展示给他人！ 让我们再重新修改一下代码

```python
import requests
url = 'https://my.csdn.net/'
header = {
    'Cookie':'此处隐藏个人Cookie',
    'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
web_data = requests.get(url,headers=header)
web_info = web_data.text
print(web_info)
```

运行一下，查看结果 ![图7-带COokie爬取的页面](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200813085400.png) 我们看到，最终爬取的结果中，已经包含了登录时收藏的相关文章！Cookie设置成功！

## 6\. 内容总结

*   使用 Requests 能够将大量原本复杂的开发过程进行简化，方便了我们更关注网页爬取技术本身；
*   对于请求头，我们可以直接定制，你可以参考[《HTTP 请求行、请求头、请求体详解》](https://blog.csdn.net/u010256388/article/details/68491509)这篇文章详细了解请求头和请求体；
*   **Cookie 是十分重要的隐私数据，带上 Cookie，可以爬取相关账户的信息。不要轻易地将自己的账户 Cookie 展示给其他人看。**