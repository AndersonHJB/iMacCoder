---
title: JavaScript - PC 端通过纯 js 播放音频文件（播放提示音）
tags: []
id: '2033'
categories:
  - - 技术杂谈
date: 2021-11-30 20:01:36
---

你好，我是悦创。

## 前言

有时候，我们可能有这样一个需求，当到达条件时，网页会播放一个提示音告知用户。

## 实现

> 当然，你也可以写一个
> 
> 标签，通过 js 获取 DOM，来操作。

```javascript
// 创建<audio>标签(参数:音频文件路径)
const audio = new Audio('x.mp3');

// 业务逻辑
if(){
  //...
  // 播放声音
  audio.play();
}

```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/cfea7865d3154809a578bd5e8f4feb98.png)