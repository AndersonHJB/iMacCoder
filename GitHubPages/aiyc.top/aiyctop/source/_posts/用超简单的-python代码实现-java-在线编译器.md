---
title: 用超简单的 Python代码实现 Java 在线编译器
tags: []
id: '1492'
categories:
  - - 在线编程搭建
date: 2021-02-21 20:46:21
---

原理参照： [python在线编译器实现](https://www.aiyc.top/1491.html) 代码注释很多，直接上代码 目录结构：

```cmake
OnlineEXEC
----zxby.py
----test.bat(因为测试环境是 windows，linux 可以自行改成 shell)
----app
    ----flaskrun.py
```

## zxby.py 代码实现：

```python
# -*- coding: utf-8 -*-
#__author__="ZJL"

import os,subprocess,tempfile


# 创建临时文件夹,返回临时文件夹路径
TempFile = tempfile.mkdtemp(suffix='_test', prefix='java_')
# javac 和 Java 编译器位置
JAVAC_EXEC = "C:\java\jdk1.8.0_121\\bin\javac"
JAVA_EXEC = "C:\java\jdk1.8.0_121\\bin\java"


# 获得java文件名
def get_javaname(code):
    if code:
        if "public class" in code and "{" in code:
            FileName = code.split("public class ")[1].split("{")[0].strip()
        else:
            FileName = "test"
        return FileName

# 接收代码写入文件
def write_file(jname, code):
    fpath = os.path.join(TempFile, '%s.java' % jname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    print('file path: %s' % fpath)
    return fpath

# 编码
def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

# 主执行函数
def main(code):
    r = dict()
    jname = get_javaname(code)
    fpath = write_file(jname, code)
    try:
        # subprocess.check_output 是 父进程等待子进程完成，返回子进程向标准输出的输出结果
        # stderr是标准输出的类型
        # 编译Java代码
        outdata = decode(subprocess.check_output([JAVAC_EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = decode(e.output)
        return r
    else:
        # 执行Java代码
        # 因为调用原因，bat写绝对路径
        outdata = decode(subprocess.check_output(["D:\\PycharmProjects\\zxbyqjava\\test.bat", TempFile,JAVA_EXEC,jname], stderr=subprocess.STDOUT, timeout=5))
        # 成功返回的数据
        r['output'] = outdata
        r["code"]="Success"
        return r

# if __name__ == '__main__':
#     code ="""public class hello {public static void main(String []args) {System.out.println("Hello World");}}"""
#     print(main(code))
```

## test.bat 代码实现(这个脚本的作用是解决 classpath 路径执行的问题):

```
@echo off

C:
cd %1
%2 %3
```

## flaskrun.py 代码实现：

```python
# -*- coding: utf-8 -*-
#__author__="ZJL"

from flask import Flask
from flask import request
from flask import Response
import json
import zxby

app = Flask(__name__)

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/')
def hello_world():
    return Response_headers('hello world!!!')

@app.route('/run',methods=['POST'])
def run():
    if request.method == 'POST' and request.form['code']:
        code = request.form['code']
        jsondata = zxby.main(code)
        return Response_headers(str(jsondata))

@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(405)
def page_not_found(error):
    content = json.dumps({"error_code": "405"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp

@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp

if __name__ == '__main__':
    app.run(debug=True)

```

测试方法一样，自行测试。