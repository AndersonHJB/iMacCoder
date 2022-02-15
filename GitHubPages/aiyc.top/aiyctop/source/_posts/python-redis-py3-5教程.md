---
title: Python redis-py3.5教程
tags: []
id: '1711'
categories:
  - - redis-py
date: 2021-05-24 16:06:40
---

> 本人长期招收 Python 一对一学员，欢迎联系微信：Jiabcdefh

## redis-py

你好，我是悦创。很早之前 ，写了一篇 Python redis 的教程：[还在手动插入 redis 数据？Python 带你解决！](https://www.aiyc.top/167.html)，备用链接：https://blog.csdn.net/qq\_33254766/article/details/117221658 现在准备写个大规模的异步新闻爬虫实战项目，需要控制 url 所以，就顺便把看最新版的英文稍微整理出来。由于本人英文有限，如果有翻译问题，欢迎指教和评论。 The Python interface to the Redis key-value store.

> Redis 键值存储的 Python 接口。

## Python 2 Compatibility Note「Python 2 兼容性说明」

redis-py 3.5.x will be the last version of redis-py that supports Python 2. The 3.5.x line will continue to get bug fixes and security patches that support Python 2 until August 1, 2020. redis-py 4.0 will be the next major version and will require Python 3.5+. redis-py 3.5.x 将是支持 Python 2 的最后一个 redis-py 版本。3.5.x 将继续获得支持 Python 2 的 bug 修复和安全补丁，直到 2020 年 8月1日。redis-py 4.0 将是下一个主要版本，需要 Python 3.5+。

## Installation「安装」

redis-py requires a running Redis server. See [Redis's quickstart](https://redis.io/topics/quickstart) for installation instructions.

> Redis -py 需要运行 Redis 服务器。参见 Redis 的快速入门安装说明。：[https://redis.io/topics/quickstart](https://redis.io/topics/quickstart)

redis-py can be installed using pip similar to other Python packages. Do not use sudo with pip. It is usually good to work in a [virtualenv](https://virtualenv.pypa.io/en/latest/) or [venv](https://docs.python.org/3/library/venv.html) to avoid conflicts with other package managers and Python projects. For a quick introduction see [Python Virtual Environments in Five Minutes](https://www.aiyc.top/1709.html).

> redi-py 可以使用 pip 安装，类似于其他 Python 包。不要使用 sudo 与 pip 。在 [virtualenv](https://virtualenv.pypa.io/en/latest/) 或 [venv](https://docs.python.org/3/library/venv.html) 中工作通常很好，以避免与其他包管理器和 Python 项目的冲突。有关快速介绍，请参见 [Python 虚拟环境五分钟](https://www.aiyc.top/1709.html)。

要安装 redis-py，只需：

```cmd
$ pip install redis
```

或从源代码：

```cmd
$ python setup.py install
```

## Contributing「贡献」

Want to contribute a feature, bug report, or report an issue? Check out our [guide to contributing](https://github.com/andymccurdy/redis-py/blob/master/CONTRIBUTING.rst). 是否要提供功能，错误报告或报告问题？查看我们的[贡献指南](https://github.com/andymccurdy/redis-py/blob/master/CONTRIBUTING.rst)。

## Getting Started「开始」

在开始之前，你要在命令行启动 redis，命令：

```redis
➜  Django_Leraning git:(main) ✗ redis-server
14540:C 24 May 2021 16:09:21.363 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
14540:C 24 May 2021 16:09:21.363 # Redis version=6.0.7, bits=64, commit=00000000, modified=0, pid=14540, just started
14540:C 24 May 2021 16:09:21.363 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
14540:M 24 May 2021 16:09:21.364 * Increased maximum number of open files to 10032 (it was originally set to 256).
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`   `,    )     Running in standalone mode
 `-._`-...-` __...-.``-._'` _.-'     Port: 6379
     `-._   `._    /     _.-'         PID: 14540
  `-._    `-._  `-./  _.-'    _.-'
 `-._`-._    `-.__.-'    _.-'_.-'
     `-._`-._        _.-'_.-'               http://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 `-._`-._    `-.__.-'    _.-'_.-'
     `-._`-._        _.-'_.-'    
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

14540:M 24 May 2021 16:09:21.365 # Server initialized
14540:M 24 May 2021 16:09:21.365 * Loading RDB produced by version 6.0.7
14540:M 24 May 2021 16:09:21.365 * RDB age 2 seconds
14540:M 24 May 2021 16:09:21.365 * RDB memory usage when created 1.06 Mb
14540:M 24 May 2021 16:09:21.365 * DB loaded from disk: 0.000 seconds
14540:M 24 May 2021 16:09:21.365 * Ready to accept connections
```

```python
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
b'bar'
```

By default, all responses are returned as bytes in Python 3 and str in Python 2. The user is responsible for decoding to Python 3 strings or Python 2 unicode objects. 默认情况下，所有响应在 Python 3 中以 **字节** 形式返回，在 Python 2 中以 str 形式返回。用户负责解码到 Python 3 字符串或 Python 2 unicode 对象。 If **all** string responses from a client should be decoded, the user can specify decode\_responses=True to Redis.**init**. In this case, any Redis command that returns a string type will be decoded with the encoding specified. 如果来自客户端的所有字符串响应都应该被解码，用户可以指定 `decode_responses=True` 为 Redis.\_\_init\_\_。在这种情况下，任何返回字符串类型的 Redis 命令都将使用指定的编码进行解码。

```python
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0, decode_responses="True")
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
b'bar'

```

The default encoding is "utf-8", but this can be customized with the encoding argument to the redis.Redis class. The encoding will be used to automatically encode any strings passed to commands, such as key names and values. When decode\_responses=True, string data returned from commands will be decoded with the same encoding. 默认的编码是 "utf-8"，但是可以通过 redis 的 encoding 参数进行自定义。复述, Redis 类。该编码将用于自动编码传递给命令的任何字符串，比如键名和值。当 `decode_responses=True` 时，命令返回的字符串数据将使用相同的编码进行解码。 Redis：

```python
def __init__(self, host='localhost', port=6379,
                 db=0, password=None, socket_timeout=None,
                 socket_connect_timeout=None,
                 socket_keepalive=None, socket_keepalive_options=None,
                 connection_pool=None, unix_socket_path=None,
                 encoding='utf-8', encoding_errors='strict',
                 charset=None, errors=None,
                 decode_responses=False, retry_on_timeout=False,
                 ssl=False, ssl_keyfile=None, ssl_certfile=None,
                 ssl_cert_reqs='required', ssl_ca_certs=None,
                 ssl_check_hostname=False,
                 max_connections=None, single_connection_client=False,
                 health_check_interval=0, client_name=None, username=None):
```

## Upgrading from redis-py 2.X to 3.0「edis-py 从 2.x 升级到 3.0」

redis-py 3.0 introduces many new features but required a number of backwards incompatible changes to be made in the process. This section attempts to provide an upgrade path for users migrating from 2.X to 3.0. Redis-py 3.0 引入了许多新特性，但在此过程中需要进行一些向后不兼容的更改。本节试图为从 2.X 迁移的用户提供一个升级路径 3.0 。

### Python Version Support「Python版本支持」

redis-py supports Python 3.5+. redis-py 支持 Python 3.5+。

### Client Classes: Redis and StrictRedis「客户端类: Redis 和 StrictRedis」

redis-py 3.0 drops support for the legacy "Redis" client class. "StrictRedis" has been renamed to "Redis" and an alias named "StrictRedis" is provided so that users previously using "StrictRedis" can continue to run unchanged. Redis-py 3.0 支持传统的 “Redis” 客户端类。“StrictRedis” 已更名为“Redis”，并提供了一个别名 “StrictRedis” ，以便以前使用 “StrictRedis” 的用户可以继续运行不变。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021052416455131.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) The 2.X "Redis" class provided alternative implementations of a few commands. This confused users (rightfully so) and caused a number of support issues. To make things easier going forward, it was decided to drop support for these alternate implementations and instead focus on a single client class. 2.X“ Redis”类提供了一些命令的替代实现。这使用户感到困惑（理应如此），并导致了许​​多支持问题。为了使事情变得更容易，我们决定放弃对这些替代实现的支持，而将精力集中在单个客户端类上。 2.X users that are already using StrictRedis don't have to change the class name. StrictRedis will continue to work for the foreseeable future. 已经使用 StrictRedis的2.X 用户不必更改类名。StrictRedis 将在可预见的未来继续努力。 2.X users that are using the Redis class will have to make changes if they use any of the following commands: 如果使用 Redis 类的 2.X 用户必须使用以下任何命令，则必须进行更改：

*   SETEX: The argument order has changed. The new order is (name, time, value). 参数顺序已更改。新订单为（名称，时间，值）。
*   LREM: The argument order has changed. The new order is (name, num, value). 参数顺序已更改。新的顺序是（名称，数字，值）。
*   TTL and PTTL: The return value is now always an int and matches the official Redis command (>0 indicates the timeout, -1 indicates that the key exists but that it has no expire time set, -2 indicates that the key does not exist) 现在的返回值始终是一个 int，并且与正式的 Redis 命令匹配（> 0 表示超时，-1 表示密钥存在但未设置过期时间，-2 表示密钥不存在）

> 上面一直把原文保留下来，有点小费劲，接下来我就不保留原文了，有兴趣的可以直接去 GitHub 上阅读。：[https://github.com/andymccurdy/redis-py](https://github.com/andymccurdy/redis-py)

### SSL Connections「SSL 连接」

redis-py 3.0 changes the default value of the `ssl_cert_reqs` option from `None` to `'required'`. See `Issue 1016 <https://github.com/andymccurdy/redis-py/issues/1016>`\_. This change enforces hostname validation when accepting a cert from a remote SSL terminator. If the terminator doesn't properly set the hostname on the cert this will cause redis-py 3.0 to raise a ConnectionError. redis-py 3.0 将 ssl\_cert\_reqs 选项的默认值从“无”更改为“必需”。参见 [问题1016](https://github.com/andymccurdy/redis-py/issues/1016) 。从远程 SSL 终结器接受证书时，此更改将强制执行主机名验证。如果终止符未在证书上正确设置主机名，这将导致 redis-py 3.0 引发 ConnectionError。 This check can be disabled by setting `ssl_cert_reqs` to `None`. Note that doing so removes the security check. Do so at your own risk. 可以通过将 ssl\_cert\_reqs 设置为 None 来禁用此检查。请注意，这样做会删除安全检查。这样做自担风险。 Example with hostname verification using a local certificate bundle (linux): 使用本地证书捆绑包（linux）进行主机名验证的示例：

```python
 >>> import redis
>>> r = redis.Redis(host='xxxxxx.cache.amazonaws.com', port=6379, db=0,
                    ssl=True,
                    ssl_ca_certs='/etc/ssl/certs/ca-certificates.crt')
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
b'bar'
```

Example with hostname verification using [certifi](https://pypi.org/project/certifi/): 剩下的有时间就来更新！