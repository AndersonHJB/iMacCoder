---
title: 手摸手带你部署Django
tags: []
id: '1497'
categories:
  - - Django
date: 2021-02-22 13:11:47
---

**补充说明：** 关于项目部署，历来是开发和运维人员的痛点。造成部署困难的主要原因是大家的 Linux 环境不同，这包括发行版、解释器、插件、运行库、配置、版本级别等等太多太多的细节。因此，一个成功的部署案例，往往很难移植到别的环境下，总是要填许多坑。那么，别人的案例就没有参考价值了么?当然不是，部署的过程其实就是参考很多的成功案例，摸索出自己适用的方式！这过程中需要什么？熟练的 Linux 技能是最基本的！一些部署的经验和灵活的思维也是要有的。不惧怕满屏的英文错误信息，能从中抓住问题的耐心更是要有的。 鉴于以上原因，我在这一节并没有介绍得太详细，因为多说多错。但肯定是一个成功的案例，不能说你按照我的方案没有部署成功，那么我这个就是错误的，这有失偏颇。 那么有没有比较好的大家都能用起来的部署方案呢？Docker了解一下！

## 基本概念

首先介绍一些 Django 部署的基本概念。 本节不涉及 ASGI 部署，在前面的章节有介绍，其实两者类同。 Django 的主要部署的方式是 WSGI，它是 Web 服务器和 Web 应用的 Python 标准，也是所谓的同步服务和默认服务。 **Django** 支持：

*   Gunicorn
*   uWSGI
*   Apache
*   Nginx

它们可以混搭。个人推荐 Nginx 配合 uWSGI。

### application 对象

用 WSGI 部署的关键是一个叫做 `application` 的可调用对象，应用服务器用它与你的代码交互，是所有请求的接口和入口。 `application` 一般位于一个 Python 模块中，以名为 `application` 的对象的形式出现，且对服务器可见。 我们使用 `startproject` 命令创建项目时会自动创建 `/wsgi.py`文件，其中就包含了 `application` 对象，直接使用即可。Django 开发服务器和生产环境的 WSGI 部署都使用它。 WSGI 服务器从其配置文件中获取 `application` 对象的路径。Django 的开发服务器（ `runserver` ），从配置项 `WSGI_APPLICATION` 中获取。默认值是 `.wsgi.application`，指向 `/wsgi.py` 中的 `application` 。

### 配置 settings 模块

当 WSGI 服务器（uWSGI、Gunicorn等）加载应用时，Django 需要导入配置模块。 Django 利用 `DJANGO_SETTINGS_MODULE` 环境变量来决定使用哪个settings.py模块，它的值是一个圆点路径字符串。开发环境和生产环境可以配置不同的settings.py。 若未设置该变量， `wsgi.py` 默认将其设置为 `your_site.settings`， `your_site` 即工程名字。 注意：由于环境变量是进程级的，所以如果在同一进程运行多个 Django 站点将出错。为了避免此问题，可以为每个站点使用 `my_wsgi` 的 daemon 模式。或者在 `wsgi.py` 中强制设置 `os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"` ，重写来自环境变量的值。

### WSGI 中间件

如果你想使用WSGI 中间件，可以如下将原来的application包裹起来：

```python
from helloworld.wsgi import HelloWorldApplication
application = HelloWorldApplication(application)
```

## 部署架构

本节将重点介绍基于下面的架构部署 Django：

```python
Python3.8 + ubuntu 16.04 + Nginx + uWSGI + Django3.1
```

首先，你得有一台 ubuntu 机器，真实物理机和虚拟机都行，如果是阿里云ECS主机并且带有独立公网 IP，那是最好不过。 我这里和大家一样，什么都没有，只有虚拟机，囧。 至于如何安装 ubutun、Python3.8 和 Django3.1，不是本节的内容，请自行解决。下面我假定你已将安装好了这三者。 在部署之前请务必按照部署清单检查完毕后，收集静态文件和媒体文件，并将 DEBGU 设置为 False。

## 一、安装 Nginx

我不太推荐 Apache2，偏爱 Nginx。 Ubuntu 默认源里面的 Nginx 版本比较旧，需要先添加一个 Nginx 的源，再通过 apt-get 安装 Nginx。 换最新的源和安装，看此教程：[Ubuntu升级或安装Nginx最新稳定版（包安装）](https://www.aiyc.top/1496.html)：https://www.aiyc.top/1496.html。 备用链接教程：[https://blog.csdn.net/qq\_33254766/article/details/113930667](https://blog.csdn.net/qq_33254766/article/details/113930667)

```bash
apt-get update
apt-get install nginx
```

一般这个都没问题，Nginx 是居家必备软件，各家. Linux 下都可以顺利安装。 使用 `service --status-all` 命令查看一下，安装好后，服务应该会自动启动：

```bash
......
 [ + ]  network-manager
 [ + ]  networking
 [ + ]  nginx
 [ + ]  ondemand
 [ - ]  plymouth
 [ - ]  plymouth-log
......
```

如果能看到带 + 号的 nginx ，表明一切 ok！

> PS：我部署的时候，出现是 - 号，我推测有可能是安装最新版 1.18.0 造成的，我的页面访问是正常的。

然后，通过 `ifconfig` ，查看一下你的 ubuntu 虚拟机的 ip 地址，我这里是 `192.168.1.121` 。使用同一局域网内的主机，通过浏览器访问 `192.168.1.121` ，如果能看到下面的界面，说明 Nginx 服务正常。 **如果你是用服务器的话，记得开启 80 端口，然后直接访问公网 IP 即可。** ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222130841150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 二、安装 uWSGI

Django 的主要部署平台是 WSGI，它也是 Python 的标准 web 服务器和应用。 uWSGI 是实现了 WSGI 协议的 WSGI 服务器。 uWSGI 是一个快速的、自我驱动的、对开发者和系统管理员友好的应用容器服务器，完全由 C 编写。 uWSGI的官网地址：[https://uwsgi-docs.readthedocs.io/en/latest/index.html](https://uwsgi-docs.readthedocs.io/en/latest/index.html) **根据血和泪的经验教训，请确保安装的是最新版本的uwsgi，否则可能出现各种坑。** 所以不建议使用：`pip3 install uwsgi` (不一定是最新版) 不建议使用：`pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz`(也不一定是最新版) 而是建议到 [https://uwsgi-docs.readthedocs.io/en/latest/Download.html](https://uwsgi-docs.readthedocs.io/en/latest/Download.html) 页面，下载`Stable/LTS`版本的源文件。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022213094261.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) **为什么要最新版？**因为现在的官方教程和相关技术文章全是以新版编写的，很多参数名，用法有较大改变。用旧版，你可能连跑都跑不起来。 我这里下载的是`uwsgi-2.0.19.1.tar.gz`，可能等到你看到此文时，已经不是最新的了。 在 ubuntu 中，解压源码，然后指定安装位置，将 uWSGI 安装好：

```bash
# 解压文件
tar -zxvf uwsgi你的压缩包名称 

# 进入解压目录
sudo python3 setup.py install
```

实际操作：

```bash
# 解压文件
root@iZ8vb1o9x5vmr6vy4go7tsZ:~# ls
p5py-master  uwsgi-2.0.19.1.tar.gz
root@iZ8vb1o9x5vmr6vy4go7tsZ:~# tar -zxvf uwsgi-2.0.19.1.tar.gz
# 进入解压目录
root@iZ8vb1o9x5vmr6vy4go7tsZ:~# ls
p5py-master  uwsgi-2.0.19.1  uwsgi-2.0.19.1.tar.gz
root@iZ8vb1o9x5vmr6vy4go7tsZ:~# cd uwsgi-2.0.19.1/
root@iZ8vb1o9x5vmr6vy4go7tsZ:~/uwsgi-2.0.19.1# sudo python3 setup.py install
```

**注意！注意！一定要注意！如果你使用了虚拟环境，那么你必须使用虚拟环境的 Python 解释器安装 uWSGI！！！**也就是说，你的Django 代码使用的哪个 Python 解释器，你的 uWSGI 服务器也必须使用同一个解释器。 安装完毕后，尝试运行一下 uwsgi： 输入 uwsgi 即可。

```bash
root@iZ8vb1o9x5vmr6vy4go7tsZ:~/uwsgi-2.0.19.1# uwsgi
*** Starting uWSGI 2.0.19.1 (64bit) on [Mon Feb 22 11:27:55 2021] ***
compiled with version: 7.5.0 on 22 February 2021 03:25:10
os: Linux-4.15.0-128-generic #131-Ubuntu SMP Wed Dec 9 06:57:35 UTC 2020
nodename: iZ8vb1o9x5vmr6vy4go7tsZ
machine: x86_64
clock source: unix
detected number of CPU cores: 1
current working directory: /root/uwsgi-2.0.19.1
detected binary path: /usr/local/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** WARNING: you are running uWSGI without its master process manager ***
your processes number limit is 7794
your memory page size is 4096 bytes
detected max file descriptor number: 65535
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
The -s/--socket option is missing and stdin is not a socket.
```

虽然运行出错了，但至少表明你的 uWSGI。在系统可执行命令路径中。 如果出现找不到命令的提示，那么建议创建一个指向 `/usr/local/bin` 目录的软链接。这些都是 Linux 管理员的业务领域，不展开介绍了。 **需要提醒大家注意的是权限的问题，该 sudo 的时候要 sudo。还有读写权限，看看当前用户是否具备相关文件的读写能力。很多时候部署失败，都不是 Python 和 Django 层面的原因，而是你的 Linux 管理业务还不够熟练。**

## 三、配置 uwsgi

软件安装好了后，首先是要拷贝项目代码。 因为我这里是在 Windows 下使用 Pycharm 编写的代码，不是在 ubuntu 虚拟机内编写的代码，所以需要将项目文件先整体拷贝到虚拟机中。（当然，最佳的方式是通过 Pycharm 进行远程开发。） 这个过程，也是八仙过海，各有奇招，我就当你将项目文件拷贝过去了。 在项目的根目录下，也就是有 `manage.py` 的目录下，新建一个 `uwsgi.ini` 文件。文件名可以随便，但后缀必须是 `ini`。 在里面写入下面的配置内容：

```ini
[uwsgi]
chdir = /home/feixue/python/www/for_test    //项目根目录
module = for_test.wsgi:application     //  指定wsgi模块下的application对象
socket = 127.0.0.1:8000         //对本机8000端口提供服务
master = true                   //主进程

# 以上4个是核心配置项

#vhost = true          //多站模式
#no-site = true        //多站模式时不设置入口模块和文件
#workers = 2           //子进程数
#reload-mercy = 10
#vacuum = true         //退出、重启时清理文件
#max-requests = 1000
#limit-as = 512
#buffer-size = 30000
#pidfile = /var/run/uwsgi9090.pid    //pid文件，用于下脚本启动、停止该进程
daemonize = /home/feixue/python/www/for_test/run.log    // 日志文件
disable-logging = true   //不记录正常信息，只记录错误信息
```

详细说明：

*   配置项中以 ‘#’ 开头的都是被注释的项目，不起作用；
*   以双斜杠开头，表示注释；
*   chdir 是你的项目根目录。我这里的项目名叫 for\_test；
*   moudule 是你的入口 wsgi 模块，将 for\_test 替换成你的项目名称；
*   socket 是通信端口设置，和我一样就行；
*   master=True 表示以主进程模式运行；
*   demonize 是你的日志文件，会自动建立
*   disable-logging = true 表示不记录正常信息，只记录错误信息。否则你的日志可能很快就爆满了。
*   env： 指定 `DJANGO_SETTINGS_MODULE`的值
*   home：可选的项目虚拟环境路径

我的具体填写：

```ini
[uwsgi]
socket = :8100
chdir=/root/aiyc_coder

# Django s wsgi file
module          = p5py.wsgi:application

# process-related settings
# master
master          = true

# maximum number of worker processes
processes       = 4

# ... with appropriate permissions - may be needed
chmod-socket    = 664
# clear environment on exit
vacuum          = true
```

* * *

也可以通过命令参数的方式，不过就显得复杂可不可修改了：

```bash
uwsgi --chdir=/path/to/your/project \
    --module=mysite.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=mysite.settings \
    --master --pidfile=/tmp/project-master.pid \
    --socket=127.0.0.1:49152 \      # can also be a file
    --processes=5 \                 # number of worker processes
    --uid=1000 --gid=2000 \         # if root, uwsgi can drop privileges
    --harakiri=20 \                 # respawn processes taking more than 20 seconds
    --max-requests=5000 \           # respawn processes after serving 5000 requests
    --vacuum \                      # clear environment on exit
    --home=/path/to/virtual/env \   # optional path to a virtual environment
    --daemonize=/var/log/uwsgi/yourproject.log      # background the process
```

## 四、配置 Nginx

uWSGI 设置好了，就配置一下 Nginx。 备份 `/etc/nginx/sites-available` 文件夹内的 default 文件，然后编辑它（不同的 Nginx 版本可能配置方法不一样）：

```bash
##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# http://wiki.nginx.org/Pitfalls
# http://wiki.nginx.org/QuickStart
# http://wiki.nginx.org/Configuration
#
# Generally, you will want to move this file somewhere, and start with a clean
# file but keep this around for reference. Or just disable in sites-enabled.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

# Default server configuration
#
server {
    listen 80;
    listen [::]:80;

    # SSL configuration
    #
    # listen 443 ssl default_server;
    # listen [::]:443 ssl default_server;
    #
    # Note: You should disable gzip for SSL traffic.
    # See: https://bugs.debian.org/773332
    #
    # Read up on ssl_ciphers to ensure a secure configuration.
    # See: https://bugs.debian.org/765782
    #
    # Self signed certs generated by the ssl-cert package
    # Don't use them in a production server!
    #
    # include snippets/snakeoil.conf;

    # root /var/www/html;

    # Add index.php to the list if you are using PHP
    # index index.html index.htm index.nginx-debian.html;

    server_name 192.168.1.121;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        # try_files $uri $uri/ =404;
        include  uwsgi_params;
                uwsgi_pass  127.0.0.1:8000;  
    }
    location /static {

    alias /home/feixue/python/www/for_test/static;
    }
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #   include snippets/fastcgi-php.conf;
    #
    #   # With php7.0-cgi alone:
    #   fastcgi_pass 127.0.0.1:9000;
    #   # With php7.0-fpm:
    #   fastcgi_pass unix:/run/php/php7.0-fpm.sock;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #   deny all;
    #}
}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#   listen 80;
#   listen [::]:80;
#
#   server_name example.com;
#
#   root /var/www/example.com;
#   index index.html;
#
#   location / {
#       try_files $uri $uri/ =404;
#   }
#}
```

关键是这一部分：

```ini
server {
    listen 80;

    listen [::]:80;

    server_name 192.168.1.121;

    location / {
        include  uwsgi_params;
        uwsgi_pass  127.0.0.1:8000;  
    }

    location /static {
        alias /home/feixue/python/www/for_test/static;
    }
}
```

请将 `server_name` 改成你的实际IP。`include uwsgi_params` 一定要一样。`uwsgi_pass` 和你uWSGI配置中的 `socket` 要一样。`location /static` 的alias改成你的实际情况，让静态文件得以部署。 修改完毕，保存退出，然后重启 nginx 服务： **我的实际操作：** 原文件内容：

```bash
##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# https://www.nginx.com/resources/wiki/start/
# https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/
# https://wiki.debian.org/Nginx/DirectoryStructure
#
# In most cases, administrators will remove this file from sites-enabled/ and
# leave it as reference inside of sites-available where it will continue to be
# updated by the nginx packaging team.
#
# This file will automatically load configuration files provided by other
# applications, such as Drupal or Wordpress. These applications will be made
# available underneath a path with that package name, such as /drupal8.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

# Default server configuration
#
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # SSL configuration
    #
    # listen 443 ssl default_server;
    # listen [::]:443 ssl default_server;
    #
    # Note: You should disable gzip for SSL traffic.
    # See: https://bugs.debian.org/773332
    #
    # Read up on ssl_ciphers to ensure a secure configuration.
    # See: https://bugs.debian.org/765782
    #
    # Self signed certs generated by the ssl-cert package
    # Don't use them in a production server!
    #
    # include snippets/snakeoil.conf;

    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
    }

    # pass PHP scripts to FastCGI server
    #
    #location ~ \.php$ {
    #   include snippets/fastcgi-php.conf;
    #
    #   # With php-fpm (or other unix sockets):
    #   fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
    #   # With php-cgi (or other tcp sockets):
    #   fastcgi_pass 127.0.0.1:9000;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #   deny all;
    #}
}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#  listen 80;
#  listen [::]:80;
#
#  server_name example.com;
#
#  root /var/www/example.com;
#  index index.html;
#
#  location / {
#      try_files $uri $uri/ =404;
#  }
#}
```

**我的修改内容：**

```bash
server {
    listen 80;
    listen [::]:80;

    server_name 39.101.141.162;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
        include  uwsgi_params;
        uwsgi_pass  :8100;
    }

    location /static {

    alias /root/aiyc_coder/static;
    }
}
```

修改完毕，保存退出，然后重启 nginx 服务：

```bash
sudo service nginx restart
```

## 五、启动服务

下面我们可以尝试启动服务了！ 进入项目的根目录，也就是有 `uwsgi.ini` 文件的地方，运行：

```bash
sudo uwsgi uwsgi.ini
```

## 补充

系统提示：

```bash
[uWSGI] getting INI configuration from uwsgi.ini
```

到主机浏览器中访问 ‘192.168.1.121’，却看见下面的错误提示页面：

```bash
DisallowedHost at /
Invalid HTTP_HOST header: '192.168.1.121'. You may need to add '192.168.1.121' to ALLOWED_HOSTS.
Request Method: GET
Request URL:    http://192.168.1.121/
Django Version: 1.11.3
Exception Type: DisallowedHost
Exception Value:    
Invalid HTTP_HOST header: '192.168.1.121'. You may need to add '192.168.1.121' to ALLOWED_HOSTS.
Exception Location: /usr/local/lib/python3.5/dist-packages/django/http/request.py in get_host, line 113
Python Executable:  /usr/local/bin/uwsgi
Python Version: 3.5.2
......
```

不要被它们吓到！很多人都不愿意仔细看错误信息，其实解决办法，人家已经提示得非常清楚了，需要在 ALLOWED\_HOSTS 配置项目中添加 `'192.168.1.121'`。 进入相应目录，编辑 settings.py 文件：

```bash
DEBUG = False

ALLOWED_HOSTS = ['192.168.1.121']
```

同时将 DEBUG 设置为. False。 在 ubuntu 中 ，运行下面的命令：

```bash
sudo killall -9 uwsgi
```

这会删除先前的. uWSGI 进程。 过几秒，一定要过几秒，数5下，然后：

```bash
sudo uwsgi uwsgi.ini
```

为什么要过几秒？因为端口释放有延迟啦。 再次在浏览器中访问 `192.168.1.121`，看到欢迎信息则说明部署成功了。 ![img](https://img-blog.csdnimg.cn/img_convert/930045ecc6f2518671c0066607c164f6.png) 上面的信息是因为我配置了一条 url 和一个简单的视图：

```python
# 根urls.py

from django.urls import path
from django.contrib import admin
from app1 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.index),
]

# app1/views.py

from django.shortcuts import HttpResponse

def index(request):

    return HttpResponse("恭喜你，成功部署了DJango！")
```

到此一个基本的 Django 项目就部署好了。