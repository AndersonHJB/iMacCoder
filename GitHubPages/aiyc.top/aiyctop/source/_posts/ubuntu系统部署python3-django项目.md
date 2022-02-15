---
title: Ubuntu系统部署Python3 Django项目
tags:
  - Django
id: '1507'
categories:
  - - Django
date: 2021-03-07 08:03:15
---

> 本项目github地址: https://github.com/icbug-development-team/Django-code-editor

#### 项目难点:

1.  解决Django项目中static文件夹静态资源无法加载问题
2.  创建python3的Venv虚拟环境
3.  使用Nginx反向代理，代理网站
4.  uwsgi部分报错问题

> 提示：本教程仅用于Ubuntu18.04 ，其它系统版本可能不成功

* * *

## 环境搭建

### 搭建环境介绍

Ubuntu18.04系统(root权限)+Nginx+uwsgi+Python3.6+Django 本项目使用VENV虚拟环境进行部署

### 环境搭建

#### 更新APT索引

```
apt update

apt upgrade
```

#### 安装并创建虚拟环境

安装virtualenv和virtualenvwrapper

```
apt install virtualenv
apt install virtualenvwrapper
```

#### 配置ENV程序环境

编辑 ~/.bashrc

```
vim  ~/.bashrc
```

在 ~/.bashrc文件中添加

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```

之后重载一下.bashrc即可

```
source ~/.bashrc
```

没有报错即可继续，有的话可以自行百度一下，CSDN上面一般会有很多解决方案！ 我们来检测一下是否安装成功

```
mkvirtualenv
```

有如下显示即为成功 ![image-20210224153306866](https://img-1258624733.file.myqcloud.com/img/20210224153307.png) 但是这个配置的版本为Python2 ![image-20210224153345532](https://img-1258624733.file.myqcloud.com/img/20210224153346.png) 这个先不用管，创建文件时指定Python3.6程序即可

#### 创建虚拟环境

这里是很容易出错的一步，这一步骤必须在**/usr/bin**目录下进行创建，否则会找不到Python程序!

```
mkvirtualenv -p python3.6 p5py
```

![image-20210224153704192](https://img-1258624733.file.myqcloud.com/img/20210224153705.png) 上图即为成功 简单介绍一下虚拟环境的进入和退出的方式 退出环境命令

```
deactivate
```

进入虚拟环境

```
workon p5py  # p5py为虚拟环境名称
```

### 安装Django环境

接下来的一系列步骤都要在我们创建虚拟环境p5py进行完成 安装Python3 Django模块

```
pip3 install django
```

![image-20210224154040305](https://img-1258624733.file.myqcloud.com/img/20210224154041.png)

### 上传项目

这里需要特别注意一下，建议打包为zip文件进行上传 如果你用的是xshell可以安装lrzsz程序

```
apt install lrzsz
```

在命令行中输入rz即可上传单个文件压缩包 上传后进行解压，如果你的系统没有unzip程序请使用`apt install unzip`自行安装 我放在根目录下进行解压，解压完成后删掉zip压缩包即可 如下图: ![image-20210224154952511](https://img-1258624733.file.myqcloud.com/img/20210224154954.png)

* * *

### 试运行Python Django

在项目根目录下输入

```
python3 manage.py runserver 0.0.0.0:8000
```

如果项目在对应端口成功加载即为django程序没有任何问题 如果有问题根据报错自行寻找解决方法进行处理 ![image-20210224155312962](https://img-1258624733.file.myqcloud.com/img/20210224155314.png)

### 安装Nginx

本次安装nginx最新稳定版本nginx(nginx 1.18) 首先需要ppa镜像添加插件

```
sudo apt-get install software-properties-common
```

添加ppa镜像：

```
sudo add-apt-repository ppa:nginx/stable 
```

更新源

```
apt update
```

安装nginx

```
apt install nginx
```

之后查看nginx版本号确定版本是否正确

```
(p5py) root@iZ8v:/p5py# nginx -v
nginx version: nginx/1.18.0 (Ubuntu)
```

### 安装并测试uwsgi

![img](https://img-1258624733.file.myqcloud.com/img/20210224160147.jpg) 这里一定不要用apt进行安装，要用pip3的方式进行安装，apt安装会导致很多报错！

```
pip3 install uwsgi
```

安装完成后如下画面： ![image-20210224160319347](https://img-1258624733.file.myqcloud.com/img/20210224160321.png) **下面我们来测试一下我们的 uwsgi网站服务器** 创建个test.py，用vim编辑打开

```
touch test.py
vim test.py
```

写入如下内容:

```python
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
```

使用uwsgi测试启动命令指定端口以及文件

```
uwsgi --http :8000 --wsgi-file test.py
```

用F12 Network查看是否为200 OK状态码 ![image-20210224161011576](https://img-1258624733.file.myqcloud.com/img/20210224161012.png)

* * *

## 部署Django

### uwsgi\_params 拷贝到项目根目录

复制nginx目录下的uwsgi\_params文件到根目录

```
cp /etc/nginx/uwsgi_params /p5py  # Tips:中间有空格，/p5py为根目录下的p5py文件夹，也是项目的根目录
```

### 创建uwsgi目录，编写uwsgi配置文件

在项目根目录下创建uwsgi文件夹

```
(p5py) root@iZ8v:/p5py# mkdir uwsgi && cd uwsgi
```

创建uwsgi.ini配置文件

```
vim uwsgi.ini

# 写入内容如下:

[uwsgi]
socket=:8080
plugin=python3
wsgi-file=p5py/wsgi.py
master=true
processes=1
threads=1
stats = 127.0.0.1:8000
vhost = true
```

* * *

### 部署Nginx服务

进入nginx配置文件夹

```
cd /etc/nginx/conf.d/
```

创建project配置文件

```
vim project.conf
```

写入如下内容：

```nginx
server {
    listen 80;

    server_name localhost;
    charset utf-8;
    client_max_body_size 75M;

    location /static {
        alias /p5py/static;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
        #include /p5py/p5py/uwsgi_params;
    }
}

```

编辑nginx目录下nginx.conf文件 `vim nginx.conf` 添加include conf语句： 在server{ }中添加如下内容

```nginx
include /etc/nginx/conf.d/project.conf;

```

保存nginx.conf文件 然后重启nginx网络服务器：

```
/etc/init.d/nginx restart
```

### 编辑setting.py，收集静态文件

找到同名文件夹中的p5py，编辑setting.py 第一步，把DEBUG改为False ![image-20210224162727282](https://img-1258624733.file.myqcloud.com/img/20210224162728.png) 第二步，确定Allow Host选项中有自己的域名，否则无法访问 第三部，重要的一步，配置static\_root路径 ![image-20210224162851012](https://img-1258624733.file.myqcloud.com/img/20210224162852.png)

```
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
```

这些配置完成之后，返回项目根目录 运行收集静态程序命令

```
 python3 manage.py collectstatic
```

![image-20210224162959244](https://img-1258624733.file.myqcloud.com/img/20210224163000.png) 如上图即为成功

### 安装uwsgi-Python3插件

```
sudo apt-get install uwsgi-plugin-python3
```

进入uwsgi文件夹

```
cd uwsgi
```

启动命令

```
uwsgi -d --ini uwsgi.ini
```

各大服务器厂商的云服务器请确保安全组的端口打开！ 使其在后台运行 确保socket端口为正常状态！ 一定在ini中再次确认是socket而不是http\_socket!

* * *

## 解析域名

把域名解析到对应的服务器，并在Setting.py中把解析的域名添加到ALLOW\_HOST中

* * *

## SSL部署

参考阿里云文档 https://help.aliyun.com/document\_detail/98728.html 其中的nginx.conf替换为conf.d目录中的project.conf即可！

* * *

完整版仓库地址： https://github.com/icbug-development-team/Django-code-editor