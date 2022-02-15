---
title: 错误 No such Table 'auth_user'
tags: []
id: '1673'
categories:
  - - Django 错误集
date: 2021-05-15 14:29:43
---

Django 部署的时候出现错误 No such Table ‘auth\_user’ 如下图： ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210515142649623.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70)

## 原因：

没有用户表格，就是没有创建任何 admin 用户

## 解决办法：

```python
python manage.py migrate
```

```python
python manage.py createsuperuser
```