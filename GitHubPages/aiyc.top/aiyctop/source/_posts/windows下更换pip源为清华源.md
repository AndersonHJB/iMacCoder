---
title: Windows下更换pip源为清华源
tags: []
id: '1657'
categories:
  - - 技术杂谈
date: 2021-05-08 19:40:47
---

你好，我是悦创。

1.  打开 appdata 文件夹，在资源管理器的地址栏输入 `%appdata%` 后回车：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508192633540.png) 2. 新建一个 pip 文件夹，在 pip 文件夹里面新建一个配置文件 `pip.ini`： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508193011731.png) 3. 在配置文件中输入如下内容后保存即可：

```cmd
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

再次使用 pip，即会使用新源。