---
title: A悦创学员作业代码提交方法
tags: []
id: '1730'
categories:
  - - GitHub
date: 2021-06-05 22:52:21
---

## 添加你的作业文件夹及文件

我接下来，要 Fork 这个仓库：[https://github.com/aiyuechuang/Git\_Study](https://github.com/aiyuechuang/Git_Study) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605180800261.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 正在 Fork Ing。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605180858404.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 使用 Git 进行下载： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605180944360.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 使用如下命令下载：

```git
git clone git@github.com:AndersonHJB/Git_Study.git
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605181155450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 本地文件夹里面就会出现和仓库同名的文件夹： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605181329769.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 接下来，在这个下载的 Git\_Study 文件夹下，创建属于自己的课程文件夹，比如我是：AI悦创 学员，所以我创建的学员文件夹为：20210605-AI悦创

*   20210605：你报名时间
*   你的名字 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605210007859.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 这会比如我学的课程是：Python3网络爬虫实战，那我就创建：Python 网络爬虫实战课程代码

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605210229645.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 之后，把每节课的代码放到每节课对应的文件夹里面。 比如：我第一节课，Python3 爬虫基础原理。我就创建如下文件夹： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605210754590.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 代码放进去即可，每次建议配上：`README.md` 这个文件里面写上你遇到的问题或者其他问题。 这个文件是 markdown 文件。建议去学一下：[https://www.runoob.com/markdown/md-tutorial.html](https://www.runoob.com/markdown/md-tutorial.html) 所使用的软件：[https://typora.io/](https://typora.io/) 那下次课的作业就也是这样： ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021060521162619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 如果你还学了其他课程，那就创建其他课程： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605211723490.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

#### 这个过程中，为什么我不帮你们创建文件夹呢？因为很多时候你们也要学会操作，或许我操作就几秒，但你们却要挺长的时间，这也是学习的过程。

## 添加 Fork 原仓库的地址

### step 1、进入到本地仓库的目录。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605212903483.png)

### step 2、执行命令 git remote -v 查看你的远程仓库的路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605213008117.png) 如果只有上面 2 行，说明你未设置 upstream （中文叫：上游代码库）。一般情况下，设置好一次 upstream 后就无需重复设置。

### step 3、添加上游仓库

执行命令：

```python
git remote add upstream https://github.com/aiyuechuang/Git_Study.git
```

把我这个测试的仓库设置为你的 upstream 。 这个命令执行后，没有任何返回信息；所以再次执行命令 `git remote -v` 检查是否成功。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605213530314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

> PS：我在这个测试的原仓库更新了文件： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605214150277.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

创建一个 sh 文件，里面编写如下内容：

```sh
git status
git add .
git commit . -m "update"
#git status
git push
git fetch upstream
git checkout main
git merge --no-edit upstream/main
# git commit
git push
```

把文件放进你的项目文件夹里面即可。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605224611806.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 然后在 git 的命令行输入：

```sh
sh aiyc_code_push.sh
```

## 最后提交到到总仓库

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605224814718.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605224839187.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605224850292.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605225031533.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210605225046191.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 到这里就可以了，然后跟我说一声就好。每次上课后，想要我编写的代码，就直接运行：

```sh
sh aiyc_code_push.sh
```

即可，你本地就能看见了。GitHub 上面也能看见。