---
title: linux mysql 查看默认端口号和修改端口号
tags: []
id: '2061'
categories:
  - - uncategorized
date: 2021-12-07 12:37:02
---

```mysql
 如何查看mysql 默认端口号和修改端口号 2015-03-19 17:42:18


1. 登录mysql

[root@test /]# mysql -u root -p
Enter password:


2. 使用命令show global variables like 'port';查看端口号

mysql> show global variables like 'port';
+---------------+-------+
 Variable_name  Value 
+---------------+-------+
 port  3306 
+---------------+-------+
1 row in set (0.00 sec)


3. 修改端口，编辑/etc/my.cnf文件，早期版本有可能是my.conf文件名，增加端口参数，并且设定端口，注意该端口未被使用，保存退出。

[root@test etc]# vi my.cnf
[mysqld]
port=3506
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

"my.cnf" 11L, 261C written
[root@test etc]#

4. 重新启动mysql

[root@test ~]# /etc/init.d/mysqld restart
Stopping mysqld: [ OK ]
Starting mysqld: [ OK ]

5.再次登录后检查端口已修改为’3506’.

[root@test etc]# mysql -u root -p
Enter password:
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.1.66 Source distribution

Copyright (c) 2000, 2012, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show global variables like 'port';
+---------------+-------+
 Variable_name  Value 
+---------------+-------+
 port  3506 
+---------------+-------+
1 row in set (0.00 sec)

mysql>

总结：注意修改的端口不要被占用，而且要有规划，不要轻意的总是调整数据库端口。还有就是安全保障，记得与负责网络的人提前通知，以免端口无法正常使用。 
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh ![在这里插入图片描述](https://img-blog.csdnimg.cn/c9f56f26bb854de18ef76629c5d47c0f.png)