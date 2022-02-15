---
title: Python导出和导入所有依赖包
tags: []
id: '1722'
categories:
  - - 技术杂谈
date: 2021-06-01 11:05:30
---

## 导出所有依赖包

### 整个环境的依赖包导出

进入项目目录，执行以下命令：

```python
pip freeze > requirements.txt
```

然后在当前目录是可以看到生成 “requirements.txt” 文件，可以打开看看，会发现有很多个包信息，其实这里是把你当前 python 环境的所有包的相关信息导出来了。如果我们只需导出当前项目所需的依赖包，我可以采用另外一种方式。

### 只导出项目所需的依赖包

进入项目目录，执行以下命令：

```python
pipreqs ./
```

默认情况下，是没有安装 “pipregs” 插件，所以会提示以下错误：

```python
pipreqs: command not found
```

因此，我们需要安装这个插件，执行以下命令：

```python
pip install pipreqs
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210601104803604.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) **注意：** 如果你是多虚拟环境的，需要你进入到指定的虚拟环境来进行安装，否则也是没法使用。 安装好后，我们就执行以下命令来导出依赖包：

```python
pipreqs ./
```

稍微等一会就可以导出成功： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210601105905580.png) 可以打开 “requirements.tx” 文件看看，会发现少了很多多余的依赖包信息。

## 导入依赖包

我们可以用上面的“requirements.txt”文件来导入依赖包，快速构建好环境。特别是我们需要把项目迁移到其它环境进行部署，此时就非常方便了。 我自己在我的环境新建一个 python 环境 “my\_py37\_test" ，将上述的代码工程移到这个环境，先直接运行看看效果，发现是报错，报没有相应库，这个和我们预料一样，我们确实还没有安装相应的库。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210601110137212.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 我们可以通过以下命令来执行：

```python
pip install -r requirements.txt
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210601110226131.png) 执行完后，我们重新运行代码，可以发现，是没有问题的。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210601110323644.png)