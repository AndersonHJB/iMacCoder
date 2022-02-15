---
title: Python链接和操作sqlite
tags: []
id: '1479'
categories:
  - - Python 自动化办公实战课「推文系列」
date: 2021-02-20 18:32:04
---

## 链接和查询代码

Python 自身携带 sqlite 库，不需要额外安装，直接使用即可。导入代码：

```python
import sqlite3
```

导入代码之后，将 first.db 文件，放到代码文件旁边。这里用的是 ipynb ，所以是把 ipynb 和 first.db 文件放一起，不放一起就只能使用绝对路径。如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/611a815b767e9788fa7464c9b92f5cce.png) 然后使用 sqlite3 库，链接 first.db 文件，代码 `firstdb = sqlite3.connect('first.db')` 正常运行后，写查询语句，从数据库中读取全部数据，如下代码：

```python
# 查询语句
query_sql = "select * from info"
for result in firstdb.execute(query_sql):
    print(result)
```

输出结构效果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/7a28a3c2b327c31ed7b8927a0a439bb5.png) 这是最简单的查询语句。数据库都是支持查询、删除、增加、更新操作的。

## 删除数据操作

删除操作，将数据从数据库中移除，关键词 delete ，先删除一条数据，如下代码：

```python
# 删除特定数据
delete_sql = "delete from info where id = 1 "

firstdb.execute(delete_sql)
firstdb.commit()

# 查询并输出
query_sql = "select * from info"
for result in firstdb.execute(query_sql):
    print(result)
```

运行结果如下图： ![image.png](https://img-blog.csdnimg.cn/img_convert/9e4ceaf0af000065a69d4fa02d3cda16.png)

## 插入更多数据

增加的操作，关键词 add ，使用 for 循环，先批量的增加一些数据

```python
# 插入数据
insert_sql = "insert into info(title, content, author) values ('第{}个标题', '随机的第{}个内容', '匿名')"
for i in range(10,20):
    sql = insert_sql.format(i,i*2)
    firstdb.execute(sql)
    firstdb.commit()


# 查询并输出
query_sql = "select * from info"
for result in firstdb.execute(query_sql):
    print(result)
```

for 循环，从 10 循环到 20，不含 20，然后全部执行 sql 语句和提交到数据库。最后查询全部数据，看下有没有增多，如下结果图： ![image.png](https://img-blog.csdnimg.cn/img_convert/2ea6358fe66fa44d26bb79859d9a4193.png)

## 更新数据操作

数据有增加，最后更新数据，关键词update，做个条件更新，id大于等于4的数据，设置 author 为“不匿名”，如下代码：

```python
# 更新数据
update_sql = "update info set author = '不匿名' where id >= 4"
firstdb.execute(update_sql)


# 查询并输出
query_sql = "select * from info"
for result in firstdb.execute(query_sql):
    print(result)
```

最后的结果图如下： ![image.png](https://img-blog.csdnimg.cn/img_convert/7907b80c7eb1f0911284571d987e94a7.png) 以上就是 Python 操作 sqlite 的全部代码了。

## 【多选题】小练习

数据库支持哪些操作？

*   \[ \] 更新数据
*   \[ \] 新增数据
*   \[ \] 查询数据
*   \[ \] 删除数据