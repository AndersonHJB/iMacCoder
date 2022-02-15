---
title: Python去掉文件中空行
tags: []
id: '1546'
categories:
  - - Python
  - - Python 小玩意
date: 2021-03-05 15:35:21
---

## 方法一

```python
# coding = utf-8
def clearBlankLine():
    file1 = open('text1.txt', 'r', encoding='utf-8') # 要去掉空行的文件 
    file2 = open('text2.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()


```

## 方法二

```python
mystr = 'aiyuechuang\n\n\n2021'
print("".join([s for s in mystr.splitlines(True) if s.strip()]))
```

### 解析 Python splitlines() 方法

#### 描述

Python splitlines() 按照行 ('\\r', '\\r\\n', \\n') 分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

#### 语法

splitlines() 方法语法：

```python
str.splitlines([keepends])
```

#### 参数

*   keepends -- 在输出结果里是否保留换行符 ('\\r', '\\r\\n', \\n')，默认为 False，不包含换行符，如果为 True，则保留换行符。

#### 返回值

返回一个包含各行作为元素的列表。

#### 实例

以下实例展示了 splitlines() 函数的使用方法：

```python
#!/usr/bin/python

str1 = 'ab c\n\nde fg\rkl\r\n'
print(str1.splitlines())

str2 = 'ab c\n\nde fg\rkl\r\n'
print(str2.splitlines(True))
```

以上实例输出结果如下：

```python
['ab c', '', 'de fg', 'kl']
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```