---
title: Ubuntu系统部署Python3 Django项目「零失败」
tags: []
id: '1534'
categories:
  - - Django
date: 2021-03-01 14:57:09
---

**Powered By icbug & AI悦创** 本项目 github 地址：[https://github.com/AndersonHJB/Python\_Online\_Programming](https://github.com/AndersonHJB/Python_Online_Programming)

# 项目难点

1.  解决 Django 项目中 static 文件夹静态资源无法加载问题
2.  创建 python3 的 Venv 虚拟环境
3.  使用 Nginx 反向代理，代理网站
4.  uwsgi 部分报错问题 > 提示：本教程仅用于 Ubuntu18.04 ，其它系统版本可能不成功

# 1.0 环境搭建

## 1.1 搭建环境介绍

Ubuntu18.04 系统( root 权限)+Nginx+uwsgi+Python3.6+Django 本项目使用 VENV 虚拟环境进行部署。

## 1.2 环境搭建

### 1.2.1 更新 APT 索引

```bash
apt update
```

```bash
apt upgrade
```

### 1.2.2 安装并创建虚拟环境

安装 virtualenv 和 virtualenvwrapper

```bash
apt install virtualenv
```

```bash
apt install virtualenvwrapper
```

### 1.2.3 配置 ENV 程序环境

编辑 `~/.bashrc`

```bash
vim  ~/.bashrc
```

在 `~/.bashrc` 文件中添加，配置环境变量。

```bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```

之后重载一下 `.bashrc` 即可：

```bash
source ~/.bashrc
```

没有报错即可继续，有的话可以自行百度一下，CSDN上面一般会有很多解决方案！ 我们来检测一下是否安装成功：

```bash
mkvirtualenv
```

有如下显示即为成功： ![image.png](https://img-blog.csdnimg.cn/img_convert/7161d592789820acf4b0214e7815f5b4.png) 但是这个配置的版本为 Python2： ![image.png](https://img-blog.csdnimg.cn/img_convert/c471d6af44b7e892a67d4d96350303dd.png) 这个先不用管，创建文件时指定 Python3.6 程序即可。

### 1.2.4 创建虚拟环境

因为，在 Linux 下，不会有自动查找环境变量这一功能，所以我们就需要进入 python3 路径或者指定 python3 路径。

#### 方法一：

这里是很容易出错的一步，这一步骤必须在 **/usr/bin** 目录下进行创建，否则会找不到Python程序！！！ 因为 ubuntu 自带的 python3 存在路径 ：

```bash
root@iZ8vb8h5pbkzfj43uzuuc9Z:~# which python3
/usr/bin/python3
```

所以要进入该路径下。

```bash
cd /usr/bin/
```

```bash
mkvirtualenv -p python3.6 p5py
```

出现如下类似的结果即可： ![image.png](https://img-blog.csdnimg.cn/img_convert/208a3d621e6959528dbd094c6ae7df6a.png)

#### 方法二：

```bash
mkvirtualenv -p /usr/bin/python3.6 Tester
```

![image.png](https://img-blog.csdnimg.cn/img_convert/cd56a22cab56274f13dcd7ec62c6e38d.png) 上图即为成功。成功之后会自动进入虚拟环境。

> PS：这里我使用的是 p5py 虚拟环境。

简单介绍一下虚拟环境的进入和退出的方式 退出环境命令：

```bash
deactivate
```

进入虚拟环境：

```bash
workon p5py  # p5py为虚拟环境名称
```

## 1.3 安装 Django 环境

接下来的一系列步骤都要在我们创建虚拟环境 p5py 进行完成，安装 Python3 Django 模块。

```bash
pip3 install django
```

![image.png](https://img-blog.csdnimg.cn/img_convert/66bad743f4d4ba4b899e3abb64912fe5.png)

## 1.4 上传项目

这里需要特别注意一下，建议打包为 zip 文件进行上传，如果你用的是 xshell 可以安装 lrzsz 程序。

```bash
apt install lrzsz
```

在命令行中输入 rz 即可上传单个文件压缩包， 上传后进行解压，如果你的系统没有 unzip 程序请使用

```bash
apt install unzip
```

自行安装。我放在根目录下进行解压，解压完成后删掉 zip 压缩包即可 如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/1949db498a71412fd3d8b63890240cd4.png) ![image.png](https://img-blog.csdnimg.cn/img_convert/c67ab7d03fdb59f01ea2934ce99fe0f5.png)

## 1.5 试运行 Django 项目

我的 Django 项目开源了：[https://github.com/AndersonHJB/Python\_Online\_Programming](https://github.com/AndersonHJB/Python_Online_Programming)，记得给整个项目 root 权限。「也可以不用加权限」 在测试的时候，先把 Django 中的 settings.py 中的 DEBUG=True，改成 DEBUG=False。也要把你的服务器 IP 添加到 ALLOWED\_HOSTS 里面。 ![image.png](https://img-blog.csdnimg.cn/img_convert/63ffc2494e91c7c787e1d9ee3489b96b.png) 在运行之前我可以使用如下命令导出项目依赖：

```bash
pip freeze > requirements.txt
```

**注意：项目依赖需要在真实环境「也就是退出虚拟环境」和进入虚拟环境我们都要安装。** \*\* 接下来安装依赖：

```bash
pip3 install -r requirements.txt
```

接下来运行，在项目根目录下输入：

```bash
sudo python3 manage.py runserver 0.0.0.0:80
```

如果项目在对应端口成功加载即为 django 程序没有任何问题，如果有问题根据报错自行寻找解决方法进行处理或者留言。 ![image.png](https://img-blog.csdnimg.cn/img_convert/2d6ebf7e8e1260dce0c579981b69b844.png) 也能运行代码、保存、分享。

## 1.6 安装 Nginx

![image.png](https://img-blog.csdnimg.cn/img_convert/a54ff7bd9335ddacaae70b13ef6792fc.png) 不管是接下来的方法一，还是方法二，你用一种即可。最后访问公网 IP 都会出现上面的结果。

#### 方法一：

本次安装 nginx 最新稳定版本 nginx(nginx 1.18)，首先需要 ppa 镜像添加插件：

```bash
sudo apt-get install software-properties-common
```

添加 ppa 镜像：

```bash
sudo add-apt-repository ppa:nginx/stable 
```

更新源：

```bash
apt update
```

安装 nginx：

```bash
apt install nginx
```

之后查看 nginx 版本号确定版本是否正确：

```bash
(p5py) root@iZ8vb8h5pbkzfj43uzuuc9Z:/p5py# nginx -v
nginx version: nginx/1.18.0 (Ubuntu)
```

#### 方法二：

1）如果你之前安装过 Nginx，你可以输入：

```bash
sudo apt-get --purge remove nginx
```

将 Ngxin 的配置文件和程序全都卸载，然后按照下面的方式安装即可。 2）如果你不想卸载之前的，仍然可以按照下面的方式进行安装升级，但是 `/etc/nginx` 目录下可能会有你之前版本的一些配置文件，比如 `sites-enabled` 文件夹和 `sites-available` 文件夹等等，但1.18.0 稳定版本不需要这些文件夹了，所以最好是卸载了重新安装。

##### Nginx 版本介绍

Nginx 官网下载：[https://nginx.org/en/download.html](https://nginx.org/en/download.html) ![image.png](https://img-blog.csdnimg.cn/img_convert/b4d1c775d51deca43d8b388c733b3700.png)

*   Mainline version：正在开发阶段的版本，可能会有漏洞。
*   Stable version：稳定版
*   Legacy versions： 历史版本
*   本次安装1.18.0的稳定版本

##### 实际操作

安装或升级，需要添加源才能下载 Nginx 的稳定版本，首先输入以下两条命令：

```bash
 sudo wget http://nginx.org/keys/nginx_signing.key
 sudo apt-key add nginx_signing.key
```

在 `/etc/apt/sources.list` 文件中加入下面两行：

```bash
deb http://nginx.org/packages/ubuntu/ codename nginx
deb-src http://nginx.org/packages/ubuntu/ codename nginx
```

注意 codename 要根据系统来选择可以点击查看详细说明：[http://nginx.org/en/linux\_packages.html#stable](http://nginx.org/en/linux_packages.html#stable) ![image.png](https://img-blog.csdnimg.cn/img_convert/dc61f12833d1624e2eabccf01469bd66.png)

```bash
sudo vim /etc/apt/sources.list
```

![image.png](https://img-blog.csdnimg.cn/img_convert/ec666219f71bd24b661f0b50aa06c6ac.png) Ubuntu 其他版本和系统平台更换 codename 即可最后输入：

```bash
sudo apt-get update
sudo apt-get install nginx
```

输入完成之后，如果你看见这句话： ![image.png](https://img-blog.csdnimg.cn/img_convert/3c15c10d3129ee5d2a469572ced8296a.png) 输入 `nginx -v` 查看安装版本：

```bash
root@iZ8vb1o9x5vmr6vy4go7tsZ:~# nginx -v
nginx version: nginx/1.18.0
```

此外，`/etc/nginx/` 下的目录结构： ![image.png](https://img-blog.csdnimg.cn/img_convert/502312d29b455dee5c0ca765ae1591b9.png)

* * *

## 1.7 安装并测试 uwsgi

![image.png](https://img-blog.csdnimg.cn/img_convert/94aac30c2e5375567475504e1140264d.png) 这里一定不要用 apt 进行安装，要用 pip3 的方式进行安装，apt 安装会导致很多报错！

```bash
pip3 install uwsgi
```

安装完成后如下画面： ![image.png](https://img-blog.csdnimg.cn/img_convert/4bbec86ce88f442a095da1e384fe3bae.png) **下面我们来测试一下我们的 uwsgi 网站服务\*\*\*\*器，创建个 test.py，用 vim 编辑打开。**

```bash
touch test.py # 创建文件
vim test.py   # 编辑文件
```

写入如下内容：

```bash
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
```

使用 uwsgi 测试启动命令指定端口以及文件：

```python
uwsgi --http :8000 --wsgi-file test.py
```

用 F12 Network 查看是否为 200 OK 状态码： ![image.png](https://img-blog.csdnimg.cn/img_convert/f336e6a872c41cf8bab6b4c5c0ed6377.png)

# 2.0 部署 Django

## 2.1 uwsgi\_params 拷贝到项目根目录

复制 nginx 目录下的 uwsgi\_params 文件到根目录：

```bash
cp /etc/nginx/uwsgi_params /p5py  # Tips:中间有空格，/p5py为根目录下的p5py文件夹，也是项目的根目录
```

### 2.2 创建 uwsgi 目录，编写 uwsgi 配置文件

在项目根目录下创建 uwsgi 文件夹：

```bash
(p5py) root@iZ8vb8h5pbkzfj43uzuuc9Z:/p5py# mkdir uwsgi && cd uwsgi
```

创建 uwsgi.ini 配置文件：

```bash
(p5py) root@iZ8vb8h5pbkzfj43uzuuc9Z:/p5py# touch uwsgi.ini
```

编辑 uwsgi.ini ：

```bash
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

### 2.3 部署 Nginx 服务

进入 nginx 配置文件夹

```bash
cd /etc/nginx/conf.d/
```

创建 project 配置文件

```bash
vim project.conf
```

写入如下内容：

```bash
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

重启：

```bash
/etc/init.d/nginx restart
```

输入之后的结果：

```bash
(p5py) root@iZ8vb8h5pbkzfj43uzuuc9Z:/etc/nginx/conf.d# /etc/init.d/nginx restart
[ ok ] Restarting nginx (via systemctl): nginx.service.
```

### 2.4 编辑 setting.py，收集静态文件

找到同名文件夹中的 p5py，编辑 setting.py 第一步，把 DEBUG 改为 False： ![image.png](https://img-blog.csdnimg.cn/img_convert/8b3cbc793bc373473251389f1cbec9d0.png) 第二步，确定 Allow Host 选项中有自己的域名，否则无法访问。 ![image.png](https://img-blog.csdnimg.cn/img_convert/3ca55bdd489246ee328e4b7203e28d9e.png) 第三部，重要的一步，配置 static\_root 路径：

```bash
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
```

![image.png](https://img-blog.csdnimg.cn/img_convert/7583d4aa6332c6a4670ffd4d2b75153b.png) 这些配置完成之后，返回项目根目录 运行收集静态程序命令：

```bash
 python3 manage.py collectstatic
```

我的输入：

```bash
(p5py) root@iZ8vb8h5pbkzfj43uzuuc9Z:/p5py#  python3 manage.py collectstatic
```

![image.png](https://img-blog.csdnimg.cn/img_convert/36bddfe718a8251927b9123e012db9de.png) 如上图即为成功。

### 2.5 安装 uwsgi-Python3 插件

```bash
sudo apt-get install uwsgi-plugin-python3
```

进入 uwsgi 文件夹：

```bash
cd uwsgi
```

启动命令：

```bash
uwsgi --ini uwsgi.ini
```

```bash
uwsgi -d --ini uwsgi.ini # 这个-d是后台运行
```

各大服务器厂商的云服务器请确保安全组的端口打开！ 使其在后台运行 确保 socket 端口为正常状态！ 一定在 ini 中再次确认是 socket 而不是 http\_socket!

## 3.0 解析域名

把域名解析到对应的服务器，并在 Setting.py 中把解析的域名添加到 ALLOW\_HOST 中

* * *

## 4.0 SSL部署

参考阿里云文档 [https://help.aliyun.com/document\_detail/98728.html](https://help.aliyun.com/document_detail/98728.html) 其中的 nginx.conf 替换为 conf.d 目录中的 project.conf 即可！

* * *

完整版仓库地址： [https://github.com/AndersonHJB/Python\_Online\_Programming](https://github.com/AndersonHJB/Python_Online_Programming)