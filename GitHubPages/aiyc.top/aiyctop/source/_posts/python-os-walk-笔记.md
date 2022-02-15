---
title: Python os.walk() 笔记
tags: []
id: '1672'
categories:
  - - Python os库
date: 2021-05-14 09:33:51
---

我们先使用如下代码：

```python
import os

path = 'Path_file'
for i in os.walk(path):
    print(i)
# ("当前文件夹的地址", "当前文件夹下的文件夹名称", "当前文件夹下的文件，不包含子目录文件")
```

获得的输出结果：

```python
('Path_file', ['Tester_walk02', 'Tester_walk01', 'detail_file'], ['I_Have_a_Dream.txt'])
('Path_file/Tester_walk02', [], ['Tester_walk02_I_Have_a_Dream.txt'])
('Path_file/Tester_walk01', [], ['Tester_walk01_I_Have_a_Dream.txt'])
('Path_file/detail_file', [], ['Path_file_detail_file_I_Have_a_Dream.txt'])
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210514084108555.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)