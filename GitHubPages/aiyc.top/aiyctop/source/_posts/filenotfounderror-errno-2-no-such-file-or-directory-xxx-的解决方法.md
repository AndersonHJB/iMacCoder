---
title: 'FileNotFoundError: [Errno 2] No such file or directory: ''XXX'' 的解决方法'
tags: []
id: '1286'
categories:
  - - Python 算法指南
date: 2020-12-16 23:40:15
---

### 错误描述：

FileNotFoundError: \[Errno 2\] No such file or directory: ‘XXX’ 的解决方法 在编写爬虫文件的过程中，一般会将爬取下来的文件保存在一个文件夹内，而当选取的文件夹不存在时，会报错"FileNotFoundError: \[Errno 2\] No such file or directory".

### 例如

```python
def __init__(self, path = './'):
        #save the path
        self.path = path

def save2Img(self, fname, url):
        #save the image
        img = self.reqPage(url)
        #file's name and suffix
        fname = fname + '.' +url.rsplit('.',1)[-1]
        #file's path
        fpath = os.path.join(self.path,fname)
        #save the image
        with open(fpath,'wb') as f:     #<-----报错位置
            f.write(img)   
```

指定的路径是当前路径，而保存路径为‘img’文件夹。如果之前’img‘文件夹不存在，就会报文件未找到的错误提示。

### 解决方法

解决该问题的方法主要分为两种：

#### 第一种：代码解决

在代码中加入预检测，如果文件夹路径不存在，则创建文件夹路径。

```python
def __init__(self, path = './'):
        #save the path
        self.path = path
        if not os.path.exists(path):    
            os.mkdir(path)
```

### 第二种：手动添加

在编码的过程中，确定要保存文件的文件夹路径，提前创建文件夹；或者直接保存在已有的文件夹内。