---
title: Python在线编译器简单实现
tags: []
id: '1491'
categories:
  - - 在线编程搭建
date: 2021-02-21 20:28:34
---

你好，我是悦创。因为项目，需要在网页中嵌入编译器。这个分为两部分，前端单独编译器及后端 flask 服务，前端编译器部分可参考：[https://www.aiyc.top/1490.html](https://www.aiyc.top/1490.html) ，里面有源码，后端部分参考一下： 看到菜鸟教程的 Python 编译器发现挺有意思，想搞明白它的原理是啥，于是我输入了以下代码：

```python
import sys,os
print(sys.version_info)
print(sys.executable)
print(sys.path[0])
print(os.listdir(sys.path[0]))
with open("/usercode/file.py") as e:
    print(e.read())
```

我个人推测，它是将post请求的代码数据写入了 [服务器](https://www.baidu.com/s?wd=服务器&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd) 的一个文件，然后用服务器的 python 编译器执行返回结果： 于是我自己简单实现一个 目录结构：

```cmake
OnlineEXEC
----zxby.py
----app
    ----flaskrun.py
```

## zxby.py 代码实现：

```python
# -*- coding: utf-8 -*-
#__author__="AI悦创"

import os,sys,subprocess,tempfile,time


# 创建临时文件夹,返回临时文件夹路径
TempFile = tempfile.mkdtemp(suffix='_test', prefix='python_')
# 文件名
FileNum = int(time.time()*1000)
# python编译器位置
EXEC = sys.executable

#获取python版本
def get_version():
    v = sys.version_info
    version = "python %s.%s" %(v.major,v.minor)
    return version

# 获得py文件名
def get_pyname():
    global FileNum
    return 'test_%d' % FileNum

# 接收代码写入文件
def write_file(pyname, code):
    fpath = os.path.join(TempFile, '%s.py' % pyname)
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
    r["version"] = get_version()
    pyname = get_pyname()
    fpath = write_file(pyname, code)
    try:
        # subprocess.check_output 是 父进程等待子进程完成，返回子进程向标准输出的输出结果
        # stderr是标准输出的类型
        outdata = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = decode(e.output)
        return r
    else:
        # 成功返回的数据
        r['output'] = outdata
        r["code"]="Success"
        return r
    finally:
        # 删除文件(其实不用删除临时文件会自动删除)
        try:
            os.remove(fpath)
        except Exception as e:
            exit(1)

# if __name__ == '__main__':
#     code ="""print("你好")"""
#     print(main(code))
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
        print(code)
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

打开 postman 测试：

## 正确代码测试：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221202620986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 错误代码测试：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221202737636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)