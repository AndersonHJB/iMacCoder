---
title: Pandas 快速入门
tags: []
id: '854'
categories:
  - - 数据分析
date: 2020-08-29 16:09:43
---

这是一个 Pandas 快速入门教程，主要面向新用户。这里主要是为那些喜欢“短平快”的读者准备的，有兴趣的读者可通过其它教程文章来一步一步地更复杂的应用知识。 推荐阅读：[数据分析环境搭建](https://blog.csdn.net/qq_33254766/article/details/107772822):[https://blog.csdn.net/qq\_33254766/article/details/107772822](https://blog.csdn.net/qq_33254766/article/details/107772822) 博客文章：[数据分析的环境不会搭？看这里准没错！](https://www.aiyc.top/772.html) 接下来，我讲使用 jupyter 给你演示代码。 测试工作环境是否有安装好了 Pandas，导入相关包如下：

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Hello, Pandas, aiyuechuang")
```

然后执行一下，看有没有问题，如果正常应该会在终端输出区看到以下结果 - ![image-20200829095902035](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200829160807.png)

## 对象创建

通过传递值列表来创建一个系列，让 Pandas 创建一个默认的整数索引：

```python
import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])

print(s)
```

执行后输出结果如下 -

```python
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

通过传递 `numpy` 数组，使用 `date_range` 索引和标记列来创建 `DataFrame` ：

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=7)
print(dates)

print("--"*16)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
```

执行后输出结果如下 -

```python
DatetimeIndex(['2020-08-29', '2020-08-30', '2020-08-31', '2020-09-01',
               '2020-09-02', '2020-09-03', '2020-09-04'],
              dtype='datetime64[ns]', freq='D')
--------------------------------
                   A         B         C         D
2020-08-29  0.423786 -0.732253 -0.722855  0.046483
2020-08-30 -0.599389 -0.956869 -0.242626 -1.826388
2020-08-31  0.418684  0.200296  0.325539  1.245381
2020-09-01  0.330894  1.239780 -0.199876  0.065322
2020-09-02 -0.261397  1.014110  0.675852  0.849021
2020-09-03  1.207348 -0.581915  0.766255 -1.228912
2020-09-04 -0.420951  0.506618  0.919810  1.513165
```

通过传递可以转换为类似系列的对象的字典来创建 DataFrame。参考以下示例代码 -

```python
import pandas as pd
import numpy as np

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20200829'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)
```

执行上面示例代码后，输出结果如下 -

```python
     A          B    C  D      E    F
0  1.0 2020-08-29  1.0  3   test  foo
1  1.0 2020-08-29  1.0  3  train  foo
2  1.0 2020-08-29  1.0  3   test  foo
3  1.0 2020-08-29  1.0  3  train  foo
```

有指定 `dtypes` ，参考以下示例代码 -

```python
import pandas as pd
import numpy as np

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20200829'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2.dtypes)
```

执行上面示例代码后，输出结果如下 -

```python
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

## 查看数据

查看框架的顶部和底部的数据行。参考以下示例代码 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.head())
print("--------------" * 10)
print(df.tail(3))
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-29  0.807385 -0.318713  0.378694 -0.043608
2020-08-30 -0.719791  0.519050  0.718745  0.637981
2020-08-31  0.741096 -0.486432  0.044287 -0.964318
2020-09-01  0.380431 -0.726524 -0.961768 -0.914437
2020-09-02 -0.328136 -0.889492  0.093190  0.002288
--------------------------------------------------------------------------------------------------------------------------------------------
                   A         B         C         D
2020-09-02 -0.328136 -0.889492  0.093190  0.002288
2020-09-03 -0.190139 -0.943466  1.158113 -2.848946
2020-09-04  0.458626  0.336019  0.869484 -1.703215
```

显示索引，列和底层 numpy 数据，参考以下代码 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print("index is :" )
print(df.index)
print("columns is :" )
print(df.columns)
print("values is :" )
print(df.values)
```

执行上面示例代码后，输出结果如下 -

```python
index is :
DatetimeIndex(['2020-08-29', '2020-08-30', '2020-08-31', '2020-09-01',
               '2020-09-02', '2020-09-03', '2020-09-04'],
              dtype='datetime64[ns]', freq='D')
columns is :
Index(['A', 'B', 'C', 'D'], dtype='object')
values is :
[[ 0.01288665 -1.18594068  0.24580713  2.15426786]
 [ 1.67486677  0.87409119  0.29649716 -1.75876067]
 [ 0.0040266   0.09371827  0.32776491 -0.54749886]
 [ 0.05724459  0.09745475  1.41199215  0.54834326]
 [ 0.98339446 -1.39677847  1.63535289  0.99654273]
 [-0.47201257 -0.09082532  0.70418416 -1.88253312]
 [-0.00742794  0.115286    0.31591592 -0.28403796]]
```

描述显示数据的快速统计摘要，参考以下示例代码 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
print(df.describe())
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-29 -0.065283  0.201978 -1.395291 -0.472833
2020-08-30 -2.216017  1.439254 -0.898431  0.694591
2020-08-31 -0.263753 -0.288935 -0.231206 -0.147319
2020-09-01  0.312959 -0.469501 -0.282111  0.112078
2020-09-02  0.493605  1.298389  0.097549  1.532902
2020-09-03 -1.182668 -0.291830 -1.864092 -0.238197
2020-09-04 -1.481326 -1.005145 -0.116462 -1.200571
              A         B         C         D
count  7.000000  7.000000  7.000000  7.000000
mean  -0.628926  0.126316 -0.670006  0.040093
std    1.012451  0.920667  0.735144  0.873397
min   -2.216017 -1.005145 -1.864092 -1.200571
25%   -1.331997 -0.380665 -1.146861 -0.355515
50%   -0.263753 -0.288935 -0.282111 -0.147319
75%    0.123838  0.750184 -0.173834  0.403334
max    0.493605  1.439254  0.097549  1.532902
```

调换数据，参考以下示例代码 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.T)
```

执行上面示例代码后，输出结果如下 -

```python
   2020-08-29  2020-08-30  2020-08-31  2020-09-01  2020-09-02  2020-09-03
A    0.075554    0.648802   -0.071104   -0.458166   -0.912635   -0.095206
B   -0.329878    0.097211    0.752085    2.874639    1.346920    0.173810
C    0.183538   -0.908932    0.353632    0.116192   -0.793903   -0.574757
D   -1.722152    0.919850   -0.471265   -0.296586   -3.350305   -0.574489
```

通过轴排序，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_index(axis=1, ascending=False))
```

执行上面示例代码后，输出结果如下 -

```python
                   D         C         B         A
2020-08-29  1.990931 -0.168664  0.712581 -0.685785
2020-08-30  0.152966 -1.226357  1.499605 -0.540651
2020-08-31 -0.397362 -1.234490  0.610494  0.548959
2020-09-01  0.739899  0.721714 -0.600218 -0.186226
2020-09-02 -0.312199 -1.581504  0.863348  1.079959
2020-09-03 -0.254521  0.689556  1.090193 -0.496942
```

按值排序，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_values(by='B'))
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-29 -0.201046 -1.027556 -0.579530  1.084087
2020-09-03 -0.836144 -0.531457  0.631848 -0.564901
2020-09-01 -1.391908 -0.256019  0.272547 -0.839429
2020-08-31 -0.787409 -0.252629 -0.037748  0.797137
2020-08-30  1.031670  0.233176 -0.743074  0.628917
2020-09-02  0.754330  0.789836 -0.100603 -0.752409
```

## 选择区块

> 注意虽然用于选择和设置的标准Python/Numpy表达式是直观的，可用于交互式工作，但对于生产代码，但建议使用优化的_Pandas_数据访问方法`.at`，`.iat`，`.loc`，`.iloc`和`.ix`。

### 获取

选择一列，产生一个系列，相当于 `df.A` ，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df['A'])
```

执行上面示例代码后，输出结果如下 -

```python
2020-08-29    0.074854
2020-08-30    0.518566
2020-08-31   -0.418200
2020-09-01   -1.024968
2020-09-02   -0.596725
2020-09-03   -0.815188
Freq: D, Name: A, dtype: float64
```

选择通过 `[]` 操作符，选择切片行。参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[0:3])

print("========= 指定选择日期 ========")

print(df['20200829':'20200830'])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-29  1.168542 -1.012085 -1.736293  0.388442
2020-08-30 -0.220818 -0.485138 -1.108098 -1.264528
2020-08-31 -0.338424  0.335214 -0.700398 -1.178918
========= 指定选择日期 ========
                   A         B         C         D
2020-08-29  1.168542 -1.012085 -1.736293  0.388442
2020-08-30 -0.220818 -0.485138 -1.108098 -1.264528
```

### 按标签选择

使用标签获取横截面，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[0]])
```

执行上面示例代码后，输出结果如下 -

```python
A   -0.875695
B   -0.988040
C   -0.547882
D   -0.277213
Name: 2020-08-29 00:00:00, dtype: float64
```

通过标签选择多轴，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[:,['A','B']])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B
2020-08-29  0.391367  0.592094
2020-08-30 -0.365202  0.264050
2020-08-31  1.441891 -1.083050
2020-09-01  0.359293 -1.367616
2020-09-02 -0.285904  1.191579
2020-09-03  0.632408 -0.387574
```

显示标签切片，包括两个端点，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc['20200829':'20200830',['A','B']])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B
2020-08-29  0.551755 -0.645298
2020-08-30 -0.727907 -1.029342
```

减少返回对象的尺寸(大小)，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc['20200829',['A','B']])
```

执行上面示例代码后，输出结果如下 -

```python
A    0.219680
B   -1.157237
Name: 2020-08-29 00:00:00, dtype: float64
```

获得标量值，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[0],'A'])
```

执行上面示例代码后，输出结果如下 -

```python
0.17978335417664548
```

快速访问标量(等同于先前的方法)，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.at[dates[0],'A'])
```

执行上面示例代码后，输出结果如下 -

```python
1.0552111949337932
```

## 通过位置选择

通过传递的整数的位置选择，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[3])
```

执行上面示例代码后，输出结果如下 -

```python
A    0.513684
B    1.860135
C   -1.715328
D    0.287749
Name: 2020-09-01 00:00:00, dtype: float64
```

通过整数切片，类似于 numpy/python ，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[3:5,0:2])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B
2020-09-01  0.012190 -0.129104
2020-09-02 -1.737021 -0.111175
```

通过整数位置的列表，类似于 numpy/python 样式，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[[1,2,4],[0,2]])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         C
2020-08-30  1.702940 -0.601230
2020-08-31  0.545379 -2.320346
2020-09-02  1.137590  2.241713
```

明确切片行，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[1:3,:])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-30 -1.311249 -0.480543 -1.423407  0.906780
2020-08-31 -0.244300 -0.319834  1.361514  0.508492
```

明确切片列，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[:,1:3])
```

执行上面示例代码后，输出结果如下 -

```python
                   B         C
2020-08-29  0.108433  0.240245
2020-08-30 -1.965030  0.013905
2020-08-31 -0.108621 -0.419972
2020-09-01 -0.310499  1.033350
2020-09-02  1.261001  1.105728
2020-09-03  1.035046  1.422724
```

要明确获取值，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[1,1])
```

执行上面示例代码后，输出结果如下 -

```python
-1.8179993171247373
```

要快速访问标量(等同于先前的方法)，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iat[1,1])
```

执行上面示例代码后，输出结果如下 -

```python
-0.4438512171705424
```

### 布尔索引

使用单列的值来选择数据，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[df.A > 0])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-29  1.361530 -0.953528 -0.061566  0.334504
2020-08-30  0.456131  2.390191  0.200698  0.548389
2020-08-31  1.001806  1.648814  1.163988  0.972339
2020-09-01  0.163676 -1.665338  2.364750 -0.285190
2020-09-02  0.406306  1.352500 -0.967060  0.244719
2020-09-03  0.580392  0.575044  0.377287 -1.262029
```

从满足布尔条件的 DataFrame 中选择值。，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[df > 0])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D
2020-08-29       NaN  0.513195  0.640740  0.102126
2020-08-30       NaN       NaN       NaN       NaN
2020-08-31  0.438694       NaN       NaN  0.509465
2020-09-01       NaN  2.677832  0.725721  0.568604
2020-09-02  0.516173  0.413873       NaN  0.048414
2020-09-03       NaN  0.728401       NaN  1.167423
```

使用 `isin()` 方法进行过滤，参考以下示例程序 -

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200829', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

print(df2)

print("============= start to filter =============== ")

print(df2[df2['E'].isin(['two','four'])])
```

执行上面示例代码后，输出结果如下 -

```python
                   A         B         C         D      E
2020-08-29 -0.190401 -1.301081 -0.002840 -0.880762    one
2020-08-30  0.432769  0.273666  0.336612 -1.810146    one
2020-08-31 -0.006499  0.402231 -0.777474 -1.409930    two
2020-09-01 -0.709153 -1.334977 -0.159342  0.348316  three
2020-09-02  0.143624 -0.641063  0.072091  0.356473   four
2020-09-03  0.055731 -0.484898 -0.900308 -0.388028  three
============= start to filter =============== 
                   A         B         C         D     E
2020-08-31 -0.006499  0.402231 -0.777474 -1.409930   two
2020-09-02  0.143624 -0.641063  0.072091  0.356473  four
```