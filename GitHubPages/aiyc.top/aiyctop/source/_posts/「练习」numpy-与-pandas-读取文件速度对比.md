---
title: 「练习」Numpy 与 Pandas 读取文件速度对比
tags: []
id: '856'
categories:
  - - 数据分析练习题
date: 2020-08-30 08:08:28
---

本题就是操作 Numpy 与 Pandas 读取文件，并对比速度： 数据集：

*   rating.txt：[https://aiyc.lanzous.com/iSU8ufj79af](https://aiyc.lanzous.com/iSU8ufj79af)
    
*   rating.csv：[https://aiyc.lanzous.com/iy3upfxymba](https://aiyc.lanzous.com/iy3upfxymba)
    

```python
import numpy as np
import pandas as pd
import time

start_time = time.time()
data = np.genfromtxt('./rating.txt', delimiter=',')
end_reading_time = time.time()
print('Numpy reading time: {}ms'.format(round((end_reading_time - start_time) * 1000, 2)))

start_time = time.time()
data = pd.read_table('./rating.csv', 
    names=['user_id', 'book_id', 'rating'],
    sep=',')
end_reading_time = time.time()
print('Pandas reading time: {}ms'.format(round((end_reading_time - start_time) * 1000, 2)))

# 输出
Numpy reading time: 27029.64ms
Pandas reading time: 1003.31ms
```