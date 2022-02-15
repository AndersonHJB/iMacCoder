---
title: 爬取二次元插画「Pixiv」，这篇就够啦！
tags: []
id: '743'
categories:
  - - Python 爬虫
date: 2020-07-23 10:32:57
---

哈喽，大家好！我是 Sakura，在此借助这个 AI悦创平台来投稿。我呢，是爬虫圈一个小学生，会的不多，但是还是希望能给大家分享一些我在爬取的时候的经历。

## 目录

1.  环境配置
2.  抓取分析
3.  编写最初版本
4.  发现问题
5.  初步优化版本
6.  校验异步爬取速度— scrapy 试水
7.  利用线程池加快下载速度
8.  EXE 可运行程序
9.  后续更新思路
10.  源码分享

## 1\. 环境配置

### 1.1 编辑器版本

*   Python 3.6.8
*   PyCharm 2019.3.4

### 1.2 科学上网

经隔壁群推荐我发现了这个全球最大的二次元插画网站，无论是图片质量还是画风都是很棒的。 以前这个网站对大陆用户是很友好的，但是之前发生了一些事需要科学上网才能访问。知道方法的同学忽略，如果不知道的同学在AI悦创公众号回复「swff」即可获取

## 2\. 抓取分析

### 2.1 程序内容

这次要做的是一个实现通过已知作品id进行图片下载功能的程序

### 2.2 登录

首先这个网站一进去就需要登录，而解决这个问题有两种方法，一个是请求携带自己的 cookie ，另一种就是进行模拟登录。很明显第一种最简单，并且在我后续的实验中证实了这种方法可行，而且 cookie 不会失效(我测试了一个礼拜了 cookie 还可以用) ![image-pixivlogin](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090012.png) 这个网站包含了许多标签，也可以通过搜索栏进行搜索。 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090033.png)

> 注意：这个网站同时也包括一些 r-18 这类血腥，暴力等插画，未满 18 岁请在父母陪同下观看！！！

### 2.3 分析

随机从排行榜上选取了插画，按 F12 抓包。 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090103.png) 发现图片下边有个查看全部的按钮，说明他的图片并不是一次全部加载完成的，所以为了更好的确定图片的包，我们需要清空数据，再点查看图片按钮，这样就可以确保新加载的数据就是我们想要的所有图片的数据包。 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090121.png) nice ，新出现的只有一个，点开以后发现是一个类似于字典的数据，而且数量正好是提示框里的数量。 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090129.png) 然后我们点开每张图片的具体信息，发现里边给出了四种图片 url 地址，分别是 original，regular，small，thumb\_mini。 small 和 mini 一看是小的意思，应该是压缩过的；而 regular 有正式，合格的意思， original 是本来原来的意思，所以这里边应该选择 original 的下载地址。 我这里选的是 original 的地址，如果有想尝试另外三种的可在我后续源码中修改。 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090136.png) PS: 只有单张图片的作品依旧可以通过这个数据包拿到图片下载地址 现在，我们知道了如何找到图片的下载地址，那就可以编写程序了。

## 3\. 编写最初版本

### 3.1 导入第三方库

这里面我们要用到爬虫常见的几种库 requests、json 这两个库中只有 requests 库是需要我们自行安装的，win10 系统的小伙伴可以通过命令安装

```cmd
pip install requests
```

### 3.2 编写代码

下边是编写代码部分，首先进行导包

```python
import requests
import json
```

然后输入我们找到的数据包网址

```python
url = 'https://www.pixiv.net/ajax/illust/82505946/pages?lang=zh'
```

接下来就是应对网站反爬的一些措施 (headers) 这个网站虽然有反爬，但是并不是很严，我么只需要加上一些常规的请求参数就好

```python
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'referer': 'https://www.pixiv.net/artworks/82505946',
        'cookie': cookie
}
```

这里因为个人隐私， cookie 未给出，在此提示小伙伴们， cookie 为身份信息不要轻易泄露！ 到这里我们就可以去请求网页信息了

```python
response = requests.get(url,headers=headers).text
```

如果这时候打印 "response" 看会发现他的信息有一些瑕疵，图片地址并不是我们常见的样子 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090144.png) 所以我们需要用到 json 库进行转换，转换以后就是我们常见的字典的样子

```python
res_json = json.loads(response)
```

这是使用 pprint 打印后的效果 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090149.png) 这样是不是很直观呢，可以看到，我们需要的 original 在 'body' 里。然后对应的内容是一个列表，这时候我们需要使用循环获取他每个内容。取到 'urls' 的内容里边的 'original' 。

```python
body = res_json['body']
for datas in body:
    download_url = datas['urls']['original']
```

这样我们就得到了图片的下载地址 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090159.png) 然后就是保存了，但是我们需要给每张图片一个名字进行存储，看了眼刚才图片下载地址最后一个 ’/‘ 后边是由作品 id 和图片顺序组成的。这是一个很好的名字，因为 windows 系统按名称排序后就是原本作品的顺序。 我们可以使用 split 的方法分割 url

```python
name = download_url.split('/')[-1]
```

最后就是请求图片数据和保存了

```python
content = requests.get(download_url,headers=headers).content
with open('pixiv-pictures'+'\\'+name,mode='wb')as f:
    f.write(content)
```

**Tips:** 平时我们请求图片数据一般是不用加上请求头的，但是这个网站如果不给是请求不到数据的 这样，一个最基础的代码就写完了

```python
from pprint import pprint

import requests
import json

id = '82505946'
url = 'https://www.pixiv.net/ajax/illust/{}/pages?lang=zh'.format(id)
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'referer': 'https://www.pixiv.net/artworks/82505946',
        'cookie': cookie

}

response = requests.get(url,headers=headers).text
res_json = json.loads(response)

body = res_json['body']
for datas in body:
    download_url = datas['urls']['original']

    name = download_url.split('/')[-1]

    content = requests.get(download_url,headers=headers).content
    with open(name,mode='wb')as f:
        f.write(content)

```

## 4\. 发现问题

虽然程序现在写完了，但是还不完美，需要进一步改进。我会在下一个模块分别进行完善

1.  储存路径 图片的下载位置是和这个后缀为 .py 的程序在同一个文件夹内。我们平时肯定是希望是有单独一个文件夹储存图片，这个文件夹内有不同作品的文件夹，再一层才是各个作品的所有图片。
    
2.  网络异常 由于这个网站是外网，网络难免会有些影响，有时候就会请求不到数据。
    
3.  速度过慢 由于这个代码是同步编写，所以爬虫必须先获取第一张图片内容，然后保存，都结束以后才能开始下载第二张的工作。这样效率就很低，非常的浪费时间。
    
4.  功能单一 目前程序只有通过 id 下载图片这一个功能，比起那些项目功能太少。
    

## 5\. 初步优化版本

为了方便实现功能，我对代码进行了封装 分为了几个函数 make\_path,get\_name,get\_url,res\_pic

```python
def get_name(id):
    name_url = 'https://www.pixiv.net/artworks/{}'.format(id)
    res = requests.get(name_url, headers=headers).text
    title = re.findall('<title>(.*?)</title>', res, re.S)
    for pic_name in title:
        return pic_name
```

这个链接是从排行榜刚一点进去的页面，里面包含了作品的名字。可以通过正则表达式提取出来

```python
def make_path():
    os.makedirs('pixiv_pic', exist_ok=True)
    pic_name = get_name(id)
    print(pic_name)
    dw_path = 'pixiv_pic' + '\\' + pic_name
    os.makedirs(dw_path, exist_ok=True)
```

利用 os 模块创建 'pixiv\_pic' 文件夹，调用 get\_name 函数获取作品名称并创建对应文件夹于 'pixiv\_pic' 内

```python
def get_url(id):
    url = 'https://www.pixiv.net/ajax/illust/{}/pages?lang=zh'.format(id)
    res = requests.get(url, headers=headers).text
    res_json = json.loads(res)
    body = res_json['body']
    pic_list = []
    if body:
        for i in body:
            pic_url = i['urls']['original']
            pic_list.append(pic_url)
        return pic_list

```

对上一版本代码进行优化，并将得到的图片下载地址添加到列表中方便传递

```python
def res_pic(url):
    name = url.split('/')[-1]
    for _ in range(1, 11):
        try:
            response = requests.get(url, headers=headers, timeout=3).content
            with open(dw_path + '\\' + name, 'wb')as f:
                f.write(response)
                f.flush()
                print(datetime.datetime.now(), '正在下载{}....'.format(name))
                break
        except:
            if _ == 10:
                print("下载失败")
            else:
                print(datetime.datetime.now(), "{}正在进行第{}次重试".format(name, _))
```

对下载保存部分添加了异常处理部分，防止因为网络不稳定而导致的中途下载失败 PS: 对于异常处理最常用的方法是递归调用，但是在这里方便大家的理解，我写成了循环。这样虽然也是可以实现这个功能，但是代码量会比递归要多。 这里我解决了 4.1,4.2 的问题，下边的模块我会解决下载速度慢的问题

## 6\. 校验异步爬取速度— scrapy 试水

对于下载速度慢，往往有两种方法，第一种是异步编写，第二种是多线程&多进程，由于本人对于多进程不是很了解所以在这里只对比异步和多线程 一提起异步我就第一时间想到了 scrapy 框架，这个框架可算是爬虫利器，有很多的功能，运行速度也是非常快的。以前一位群里的小伙伴因为用 scrapy 爬取被网站封 ip 的情况。 光说不练假把式,光练不说傻把式。由于 scrapy 需要编写许多个文件，这里就不做展示了，因为他的出现只是为了测速。 因为要测速，所以我找了个有 200 张图片的作品进行测试，下面放对比图 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090213.png) ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090219.png) 不做任何处理起始时间下午13:57:43,结束下午13:59:34，足足接近两分钟！！！ 下面轮到 scrapy 的表现了 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090222.png) ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090225.png) 看到没，这就是异步的强大。但是呢 python 内置的 threading 也不慢，那么有没有一个东西既是异步又是多线程呢？ 答案是有的，他是 ThreadPoolExecutor 模块，这个模块是对 threading 再进行优化，它始终以异步方式执行调用，这样就把多线程和异步结合到了一起，下面我会给出代码

## 7\. 利用线程池加快下载速度

这里只是讲使用，具体内容我会单发一篇文章

```python
futures = []
    for index, downloadLink in enumerate(list):
        futures.append(pool.submit(res_pic, downloadLink))
```

这里的 futures 是这线程池的使用方法，传入的数据必须是通过循环传入， res\_pic 是之前的下载保存函数 下面是效果图 ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090228.png) ![image-pixiv_tags](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200723090231.png)

## 8\. EXE 可运行程序

对于一个有编程环境的同学来说，今天这个程序就算是写完了，但是如果你想把这个程序分享给其他人就必须改一些参数了 我想到的方法有以下几种，第一种 利用 input 方法进行变量传值；第二种 但写一个文本文档然后用 python 进行读取；第三种 GUI 我以上三种方法都去尝试了，最终决定采用 ini 文件读取

### 8.1 ini 文件的基本写法

ini 配置文件由节、键、值组成。 【节】：

```python
[section]
```

【参数】（键=值）：

```python
name=value
```

【注解】： 注解使用分号表示（;），在分号后面的文字，直到该行结尾都全部为注释。

```python
;comment textINI文件的数据格式的例子（配置文件的内容）
```

example:

```python
[Section1 Name]
Keyname1=value1
Keyname2=value2
... ...
[Section2 Name]
Keyname21=value21
Keyname22=value22
```

一般来说，段与段直接的名字是不能重复的。而段内的参数对是有序的，可重复的。

### 8.2 python 读取文件的方法

#### 8.2.1 configparser

这是 python 内置的一个专门读取 ini 文件的模块 但在使用之前需要先获取一下文件的路径

```python
config_file='config.ini'
path = os.path.join(os.getcwd(), config_file)
```

然后使用 configparser 类

```python
config = configparser.ConfigParser()
config.read(path, encoding='utf-8-sig')
```

或是 \`\`\`configRaw = configparser.RawConfigParser()\`\`\` 这里的 RawConfigParser 和 ConfigParser 是两种方法，区别在于 ConfigParser 可以识别 “%” 的语句，但是由于我们的 cookie 字段内带有 % ，所以我们需要用 RawConfigParser 下面是读取文件的通用方法

```python
import os
import configparser


class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: config.ini")
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)
```

#### 8.2.2 获取参数里的值

上边已经写了通用的方法，所以在我们的下载文件中直接调用就可以了

```python
from config import Config
```

这里小写的 config 是获取上述文件的文件名，大写的是自己定义的 Config 类 然后自己定义一个函数，功能是获取 id,cookie 和线程池的最大线程数 poolnum

```python
def getconfig():
    global id, cookie, pool_num
    global_config = Config()
    id = global_config.getRaw('config', 'id')
    cookie = global_config.getRaw('config', 'cookie')
    pool_num = int(global_config.getRaw('config', 'poolnum'))
```

由于 global 声明了全局的变量，所以其他的函数中也可以去使用，方便调用

### 8.3 python 打包成 exe 可运行程序

对此 python 也是有一个模块进行打包 首先进行安装

```python
pip install pyinstaller
```

打包的方法也是很简单，在命令行中输入

```python
pyinstaller -F xxx.py
```

在 .py文件同一个文件夹内的dist文件夹内有一个同名 exe 文件，双击就能运行了

## 9\. 后续更新思路

其实这个项目并不难，就是普通动态加载的 json 数据，唯一的难点就是科学上网。但是我希望通过这个项目的不断完善，来告诉大家一些项目的完成流程。同时，这也是编程的目的。编程就是发现问题—解决问题的过程。 本人很懒，本着能不干就不干，能躺着绝不坐着，能少些代码绝不多一个字的原则，我发现 pixiv 这个网站上只有预览但没有下载功能，尤其是在遇到网络高峰，图片根本就加载不出来。所以我就去了全球最大的代码托管平台 GitHub 上查找，发现只有进行模拟登录的老代码，亦或是作者很久没有维护的代码。没有轮子只能自己造了，所以有了这篇文章。 后续的更新无非就是一次同时下载多个作品，可视化窗口，获取排行榜的实时信息等等，但是这些都是我所不熟悉的领域，所以，学无止境，一开始以为自己能了，啥都会了，但是如果真的遇到问题了，就会发现书到用时方恨少。 许多东西都是在自己的实践中学会的，比如说这个项目中的多线程，异常处理，添加配置文件都是我再尝试中不断摸索不断学习的。

## 10\. 源码分享

在文章末尾提供下载链接

## 11\. 写在最后

这篇文章是我第一次写文章，写的不好多有担待，如有问题欢迎指出。学习嘛，不就是相互交流，发现问题并改正嘛。 学习，是自己的事，我不奢求这篇文章能带给你们什么能力的提升，只是分享一下我的经历，和提供一种学习的方式。 好了，谢谢大家的观看，bye