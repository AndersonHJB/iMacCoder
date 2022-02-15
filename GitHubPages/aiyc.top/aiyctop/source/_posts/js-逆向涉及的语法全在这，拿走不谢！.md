---
title: JS 逆向涉及的语法全在这，拿走不谢！
tags: []
id: '784'
categories:
  - - JavaScript 逆向系列课
  - - 技术杂谈
date: 2020-08-09 12:55:33
---

你好，我是悦创。 欢迎关注公众号：AI悦创「网站右侧二维码」，公众号最先更新！ ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807142337.png)

> 今天我们主要会介绍跟 JavaScript 的逆向相关的基础知识以及 JavaScript 必备的语法以及一些进阶的内容。

## 目录

1.  JavaScript 简介 1.1 JavaScript 介绍 1.2 网页三剑客 1.3 JavaScript 发展
    
2.  JavaScript 语法 2.1 数据类型 ​ 2.1.1 Object 对象 ​ 2.1.1.1 对象数据结构 ​ 2.1.2 Array 数组 ​ 2.1.3 String 字符串 ​ 2.1.4 Number 数字 ​ 2.1.5 Boolean 布尔值 ​ 2.1.6 Map 映射 ​ 2.1.7 Set 集合 ​ 2.1.8 null/ undefined 空值/未定义 （2.1.9） 2.2 控制流 ​ 2.2.1 条件判断 2.3 函数 ​ 2.3.1 定义 ​ 2.3.2 变量作用域 ​ 2.3.3 高阶函数 ​ 2.3.4 闭包 ​ 2.3.5 特殊对象
    
3.  JavaScript 进阶
    
4.  总结
    

> 第一小节，我讲简单介绍一下 JavaScript 的背景，发展，以及它与 CSS HTML 之间的联系； 第二小节，是本节课的重点，我将着重介绍 JavaScript 的语法知识，讲解其中的变量类型，函数以及控制流等等； 第三小节，是本节课的进阶内容，我将介绍一些 JavaScript 的进阶知识，包括 **事件循环、原型链、异步编程等等**，这些进阶内容都是我们在处理 JS 逆向的时候可能遇到的基础知识，希望大家能静下心来学习。 最后，我将把以上的知识点做一个总结。

## 1\. JavaScript 简介

### 1.1 JavaScript 介绍

众所周知，JavaScript 是一个弱类型语言，灵活并且强大是前端领域不可或缺的编程语言。在后端领域也有所作为，但是它是怎么来的呢？ 这里我简单介绍一下：JavaScript 最初由网景公司 netscape 的 Brendon Eich 发明，最初取名为 LiveScrip ，根据百度百科上的介绍，当年 34 岁的 Brendon Eich 只花了 10 天的时间，就将 JavaScript 发明了出来。**但是由于缺乏严谨的论证和设计，导致后来编写出来的程序混乱不堪（其实也是因为多种版本的兴起，但 JavaScript 的出现解决了当初网页刷新需要很久的时间），JavaScript 在当时参考了 C 语言、Java 语言、Scheme 语言以及 Self 语言。因此，JavaScript 是函数式编程和面向对象编程的产物，相当于一个四不像。** **然而，**就死这样的四不像，之后却成为风靡全球成为互联网中最受欢迎的语言之一。 后来 JavaScript 与微软的 JScript 以及 CEnvi 的 ScriptEase 三足鼎立。1997 年的时候，在 ECMA （欧洲计算机制造商协会）的协调下，将几个版本的 JavaScript 统一成一个标准名为：ECMA-262，并发布 ECMAScript 1.0，简称 ES1。这为后面 JavaScript 的快速发展奠定了基础。 1998 年和 1999 年分别发布了 ES2 和 ES3，10 年以后也就是 2009 年 ES5 才发布。ES5 中有很多现代的语法和数据结构是现代 JavaScript 基础，如今大多数 JS 的特性都是基于这个版本（ES5）。 6 年后，也就是 2015年，ES6 发布，这个版本在 ES5 的基础上有长足的进步。有解决了回调地狱的 promise 等特性。因此，用达尔文的进化论来讲，经过了 20 多年的发展，JavaScript 已经从一个原始的大猩猩逐渐成长为一个心智完备且强大的现代人类。 为了让同学们更加直观的了解到，我把它总结了下面几点：

*   JavaScript 诞生于 20多年前，由 NetScape 的 Brendan Eich 发明设计，最初命名为：LiveScript
*   后来为了跟上当初比较火的 Java 就更名为了 JavaScript ，并与微软的 JScript 和 CEnvi 的 ScriptEase 三足鼎立
*   1997 年，在 ECMA （欧洲计算机制造商协会）的协调下，由 NetScape、Sun、微软、Borland 组成的工作组确定统一标准：ECMA-262，并发布 ECMAScript 1.0，简称 ES1
*   1998 年 ES2 发布，1999年 ES3 发布
*   2009 年 ES5 发布，如今大多数 JS 的特性都是这个版本
*   2015 年 ES6 发布，在 ES6 上有很多实用特性的改进

### 1.2 网页三剑客

都说 JavaScript 是前端语言，而我们知道前端有**网页三剑客**之称，这三剑客有哪些呢？

*   JavaScript
*   CSS
*   HTML

**那它们之间的关系如何呢？**

*   HTML 是结构层，相当于人的骨骼和躯体 例如：标题、段落、列表等等；
    
*   CSS 是表现，相当于人的衣服和装饰 例如：字体、背景、颜色、边框、大小等等；
    
*   JavaScript 是行为层，相当于人的行为与动作 例如：点击滚动条、事件与后端交互、小部件、点击弹出窗口、动态显示等等。
    

### 1.3 JavaScript 发展

名称

内容

**前端**

React、Vue、Angular

**后端**

Node.js

**桌面端**

Electron

**物联网**

Arduino

**数据库**

MongoDB

**移动端**

React Native

> 目前来看，JavaScript 因为其本身灵活以及容易上手的特性，再者涉及各个领域。

1.  前端我就不说了，是 JavaScript 绝对的统治领域；
    
2.  后端有 **Node.js** 是一个非常灵活的后端语言；
    
3.  桌面端有 **Electron** ，大名鼎鼎的 **VS Code** 就是由 **Electron** 开发的；
    
4.  物联网有 **Arduino** ；
    
5.  而 **MongoDB 数据库**的 **Shell** 也是用 **JavaScript**；
6.  在移动端 JavaScript 也在不断的发展，我们有 **React Native** 等优秀框架来简化移动端的开发流程。

因此，我们可以看到 JavaScript 是非常全能的。我们有理由相信 JavaScript 在未来还会继续发展和流行，学习这样一门全能的语言是非常重要的（有帮助的） 介绍完了 JavaScript 的背景和发展之后，我们来看一下这个课程的重点。

## 2\. JavaScript 语法

JavaScript 语法，我将分成四个部分来讲。

### 目录

2.1 数据类型 ​ 2.1.1 Object 对象 ​ 2.1.1.1 对象数据结构 ​ 2.1.2 Array 数组 ​ 2.1.3 String 字符串 ​ 2.1.4 Number 数字 ​ 2.1.5 Boolean 布尔值 ​ 2.1.6 Map 映射 ​ 2.1.7 Set 集合 ​ 2.1.8 null/ undefined 空值/未定义 （2.1.9） 2.2 控制流 ​ 2.2.1 条件判断 2.3 函数 ​ 2.3.1 定义 ​ 2.3.2 变量作用域 ​ 2.3.3 高阶函数 ​ 2.3.4 闭包 ​ 2.3.5 特殊对象 2.4 特殊对象

### 2.1 数据类型

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807142833.png) JavaScript 的数据类型有很多种，其中基本类型有六种，分别是以下类型：

*   2.1.1 Object 对象 ​ 2.1.1.1 对象数据结构
    
*   2.1.2 Array 数组
    
*   2.1.3 String 字符串
    
*   2.1.4 Number 数字
    
*   2.1.5 Boolean 布尔值
    
*   2.1.6 Map 映射
    
*   2.1.7 Set 集合
    
*   2.1.8 null / undefined 空值/未定义（2.1.9）
    

我将数组（ Array ）从对象（Object）中提取出来讲是因为它是一个非常重要的特殊对象，而映射 Map 以及集合 Set 是 ES6 中才出现的数据类型，我也将单独讲解一下。

#### 2.1.1 Object 对象

*   是以 Key-Value 键值对的形式存在的集合
*   键（Key）都是字符串（String）类型
*   值（Value）可以是任意类型
*   对象的拷贝分为深浅拷贝
    *   浅拷贝：只复制对象的内存地址，类似于指针
    *   深拷贝：完全克隆，生成一个新对象

```javascript
// define an object
let obj = {hello: 'world'};

// shallow copy
let obj2 = obj;

// deep copy
let obj3 = JSON.parse(JSON.stringify(obj));
```

我们先来看看对象，它是以**键值对**的形式存在的集合，**JavaScript 的对象跟 Python 中的数据类型——字典（Dictionary）非常类似。**是一个用来表示**映射的数据结构，但是它也有一些限制。**其中，一个比较大的限制是它的 **Key 只能是字符串类型，而 Value 可以是任意的数据类型。** 另外，我们需要注意的一点是：

> JavaScript 中的深浅拷贝，这是 JavaScript 中对象或数组经常出现的操作，得加以区分。

对于浅拷贝来说：**新拷贝的变量储存的其实是被拷贝对象的内存地址，（相当于指针）任何在新拷贝的对象上的操作将直接改变被拷贝对象的内容。** 对于深拷贝来说：相反，**新拷贝的变量是被拷贝对象的整体克隆，而不是内存地址。因此两者没有任何联系，分别改变其内容，也不会互相影响。**

*   对于一些**引用操作**，我们**经常使用浅拷贝**，这样操作**比较方便**。
*   而对于一些需要**增删改的操作**,例如：ToDoList 这样的应用来说，我们就需要深拷贝了。

##### 2.1.1.1 对象数据结构：

```javascript
// This is an Object
let me = {
    name: 'AI悦创',
    gender: 'male',
    age: "secret",
    nationality: 'Chain',
    team: 'AIYC',
};

// assign attributes
me.title = 'mr';
me.education = 'College';

// get all keys
Object.keys(me)

// get all Values
Object.values(me)

// iterate
for (let key in me) {
    if (me.hasOwnProperty(key)){
        const value = me[key]
    }
}
```

上面的代码是对象的数据结构的一些基本操作，包括如何定义、获取值、设定值、遍历等等。

#### 2.1.2 Array 数组

*   数组是一个有序排列的集合
*   数组的值可以是任意类型
*   数组的拷贝分为深浅拷贝
    *   与对象一致

数组（Array）是一个有序排列的集合，与 Python 中列表（List）类似。数组的值可以是任意的数据类型，他同样有深浅拷贝的问题，这个跟我上面讲的对象是一致的，数组的增删改查都在下面列出来了。

```javascript
// This ia an array
let items = [1, 2, 3, 4, 5];

// get an item from the array
let index = 1;
items[index];

// set an item value
items[index] = 2;

// get array length
items.length;

// append an item
items.push(6);

// insert an item
items.splice(
    0, // index to insert
    0, // delete count
    0, // item to insert
);

// delete an item
items.splice(
    0, // index to delete
    1, // delete count
);

// iterate
items.map(d=>d);
items.forEach(d=>{
    // do something
})
```

*   **查找**是利用**索引**来实现的，语法是： **items 方括号加索引——items\[index\]**；
    
*   要获取**数组的长度**，只要在其后面加 **.length**；
    
*   如果要在数组末尾添加一个元素，只需要调用 **Push** 这个方法；
    
*   如果需要**在某个地方插入一个元素**，只需要调用 **splice** 这个方法；
    
*   **删除一个元素**同样是用 **splice** 这个方法，但是**需要注明第 2 个参数** —— **Delete count 不为 0**，所以这个 **splice** 这个方法既可以添加元素，又可以删除元素。大家不要混淆了！
    
*   另外遍历数组的方法有两个：
    
    *   第一个方法是 **Map**
    *   第二个方法是 **forEach**
    
    上面两个方法的区别是，**Map 是会返回一个新数组，而 forEach 不会**。因此，在需要对数组元素进行操作并返回新数组的时候我们用——**Map**，如果不需要返回则用 **forEach**
    

#### 2.1.3 String 字符串

*   字符串是任何 **单引号或双引号** 定义的类型

```javascript
// This is a string
let str = 'Hello AI悦创';
```

> 这个其实和许多语言类似，可是 JavaScript 不区分单引号和双引号；（如果，学过 Python 的就会知道其实和 Python 中的 字符串（str）数据类型很相似。）

因此，JavaScript 规范上有些松散，我们用一些工具来对此进行规范，例如：**ESLint**。但代码的规范不在本专栏范围内，我就不多介绍了。

```python
# This is a string in Python
str_data = 'AI悦创'
```

#### 2.1.4 Number 数字

*   数字是任何表示数字的类型

```javascript
// This is a number
let num = 123;
```

> 可以是整数也可以是小数，注意：JavaScript 不像其他语言有整形和浮点型区别，所有数字相关的类型都是一个类型 Number。

#### 2.1.5 Boolean 布尔值

*   布尔值是表示 **True** 或 **False** 的类型

```javascript
// This is a Boolean
let bool = true;
```

映射（Map）和集合（Set）是 ES6 中新增的类型，以解决 ES5 中对象（Object）和数组（Array）的不足。

#### 2.1.6 Map 映射

###### 映射跟对象非常接近，不同的是：映射的键 （Key）可以是任何类型，其他跟对象类似。

*   键（Key）值（Value）对关系的集合
*   与对象不同的是，键可以为任何类型

```javascript
// This is a Map
let m = new Map([
    [1, 'first as number'],
    ['1', 'first as strings']
]);

// get a value from key
m.get(1);

// set a value
m.set(1, 1);

// clear all
m.clear()
```

#### 2.1.7 Set 集合

###### 集合（Set）相当于去重后的数组

*   相当于不重复值的数组

> 映射（Map）和集合（Set）这两个数据类型用好了，其实是非常管用的——可以节省很多冗余（重复而冗杂）的代码。

```javascript
// This is a set
let s = new Set([1, 2, 3]);
```

#### 2.1.8 null 空值

*   相当于一个 ”空” 的值
*   表示该值为空

#### 2.1.9 undefined 未定义

*   表示 “未定义”
*   通常用于比较不存在的属性或值

**注意：接下来要讲的是两个比较容易混淆的数据类型——空值（null）和未定义（undefined）** **null** 表示**一个值为空，不是其他任何类型；**而**undefined** 表示**该变量没有定义——通常表示不存在的属性和值。**这两个在概念上容易混淆，而在实际的应用中，我**建议赋值的时候永远用** **null** ，而且在**做比较**的时候**永远用三个等号而不是两个等号。** **Ps：** **三个等号与两个等号的区别：** 由于 JavaScript 是弱类型语言，任何类型的值都可以做比较。三个等号为 **true** 的情况，要保证比较双方的值都相同而且类型相同。而两个等号比较会将数据类型转换成一个数据类型后再进行比较。 因此，从开发程序的角度：三个等号的稳定性比两个等号的稳定性要强很多，我永远推荐 **三个等号** ，而不是用两个等号。当然，在反爬的过程中有些开发者为了混淆对方，可能会采用两个等号的情况。这种情况大家要意识到，它们之间是有数据类型转换的。

### 2.2 控制流

循环

*   while
*   for
*   Array
    *   map
    *   forEach

```javascript
// This is a while for loop
while (a < 10){
    a++;
}

// This is a for loop
for (let i = 0; i < 10; i++){
    console.log(i);
}

// Array can also loop
const arr = [1, 2, 3];

// map loop
const arr2 = arr.map(d => d + 1);

// forEach loop
arr.forEach(d => console.log(d));
```

接下来我继续给你们介绍 JavaScript 控制流，这个还是比较容易理解的。首先，我们先来看一下循环，JavaScript 的循环，主要有三种：while 循环、for 循环、数组循环。

*   while 循环是跟其他语言类似的，都是在 while 后跟一个判断条件。
*   for 循环也类似，有三个条件参数
*   数组循环分别是：map 和 forEach （这两个之前已经介绍过了）

#### 2.2.1 条件判断

*   可以是 if () {} else {} 的形式
*   也可以是 if () else 的形式
*   中间条件用 else if 的形式

```javascript
// This is the best
if (a > b) {
    // do something
} else if (a == b) {
    // do something else
} else {
    // do something more
}

// This is ok
if (a > b) alert('ok');
else alert('not ok');
```

上面是 JavaScript 的条件判断，也就是 if else。非常简单跟其他的编程语言非常类似，这里就不多介绍了。大家注意其语法正确就可以。

### 2.3 函数

*   2.3.1 函数的定义
*   2.3.2 变量作用域
*   2.3.3 高阶函数
*   2.3.4 闭包
*   2.3.5 特殊对象

> JavaScript 的函数是本文的重点，因为在 JavaScript 逆向中，我们会看到很多跟函数相关的技巧和方法，请大家认真学习

下面，我给大家介绍函数的定义、变量、作用域、高阶函数、闭包以及特殊对象，这些内容对我们理解 JavaScript 代码有着非常重要的作用。特别是高阶函数和闭包，在一些代码混淆里会有很多这样的例子。

#### 2.3.1 函数的定义

*   带函数名
    *   function funcName (param) {statement}
    *   const funcName = function (param) {statement}
*   不带函数名（匿名函数）
    *   (function (param) {statement} () )

```javascript
// With function name 1
function funcName1 (param) {
    // do something
    return param;
};

// With function name 2
// const funcName 等于一个匿名函数
const funcName2 = function (param) {
    // do something
    return param;
};

// Without function name
(function (param) {
    // do something
    return param;
})('Hello AI悦创')
```

函数的定义有三种，前两种是带函数名定义的，而后一种是不带函数名定义的——也就是匿名函数。 **带函数名：** 第一种定义方式是 **function 关键字加函数名称**，然后**定义参数和函数内容。** 第二种方式是用**定义变量的方式**，来定义函数。例如：**const funcName** 等于一个**匿名函数。** 这两种定义是有区别的，第一种直接用 **function 关键词的定义**——是**函数声明**。而在 JavaScript 中函数声明高于一切，因此在浏览器加载好这段代码的时候，会首先将这个函数加载进来。因此，不管这个定义在哪个位置都可以被调用到。相反的是，用**定义变量的方式的函数就会有一定的执行顺序。** 如果，用定义变量的方式的函数，在**引用之后**则会出现报错的情况，而函数声明则不会。 **匿名函数：** 最后是匿名函数，很多时候匿名函数在 JavaScript 逆向中 **更为常见** ，因为这是一种有效的混淆方式。后面介绍的高阶函数和闭包都可能用到匿名函数。

#### 2.3.2 变量作用域

*   变量的定义
    *   var, const, let 定义的变量是有作用域的
    *   var 定义的变量在各自的函数内部起作用
    *   const、let 定义的变量为块级作用域
*   变量的提升
    *   扫描整个函数体的语句，将所有声明变量提升到函数顶部
*   全局作用域
    *   如果不指定 var，const，let 申明关键词来定义变量，该变量将被绑定到全局变量 windows 上
*   块级作用域
    *   let，const 将作用在 for、while 等循环语句里

接下来我们来看一下变量的作用域，在 ES5 时代 JavaScript 变量定义主要是 var 这个关键词，后来在 ES6 中增加了 const、let 这种关键字。

*   对于 var 来说，它的作用也是在函数内部，而 const、let 定义的变量的作用域是在块级作用域，待会我们会讲。
    
*   所谓变量提升，就是 JavaScript 的引擎会扫描整个函数体的语句，将所有的声明变量提升到函数顶部。因此后来定义的变量被提前引用的话，是不会出翔 undefined 的错误。关于 JavaScript 变量提升的例子其实还有很多，具体大家可以上网找一下资料学习一下，加深自己的理解。
    
*   全局作用域就是当不指定 var、const、let 等声明语句的时候，定义的变量会绑定在全局变量 Windows 上面。
    
*   块级作用域就是指 const、let 定义的变量的作用域在 for、while 等循环语句中，而不能被外部访问到。这样的好处在于**提升代码的封装性。**

#### 2.3.3 高阶函数

*   定义
    *   接收另一个函数**作为参数**的函数称作**高阶函数**
*   用途
    *   回调
    *   Callback
    *   数组操作
    *   filter、sort、map、forEach

```javascript
function first(a, b, callback) {
    return callback(a, b);
}

function second(c, d) {
    return c + d;
}

first(1, 2, second);
```

JavaScript 的函数中，另一个比较重要的知识点是高阶函数，所谓高阶函数就是：在函数中接收**另一个函数**作为参数，然后在函数中运行。 那问题来了，为什么会有高阶函数的存在呢？ 在 ES6 的 Promise 出来之前，其中一个比较重要的作用就是异步操作，相信很多在 2015年前做过前端的朋友都会对回调函数不陌生，这是当时的一个异步编程的标准。但是这种随着 Promise、async/await 等方式的出现已经逐渐的被淘汰了。这个我们后面会将。 另外比较重要的作用是在数组操作中，需要在方法中传入回调函数，来完成数组的操作。上面的代码是一个高阶函数的例子。主函数 first 接收一个回调函数作为参数传入，在主函数中获得 a，b 参数并传入回调函数 second 最后得到的结果作为返回值返回。 如果，我们下面调用这个函数（first）得到的结果其实就是：1+2 = 3 的结果。

#### 2.3.4 闭包

*   定义
    *   函数的返回值可以为**函数**
    *   所有的参数和变量**都保存在返回函数中**
    *   当调用返回函数时才会执行所有的运算逻辑（当返回的函数被执行的时候，才会将所有的运算逻辑返回结果）
*   用途
    *   匿名自执行函数
    *   封装
    *   结果封装

```javascript
function closureFunc(a, b) {
    return function (i) {
        return Math.pow(a + b, i);
    }
}
```

闭包在 JavaScript 中同样是一个非常重要的概念，很多 JavaScript 逆向过程中都会碰到大量使用闭包的场景。 其定义主要有三点，第一：函数的返回值为**函数**；第二，所有的参数和变量都保存在返回的函数里面；第三，当返回的函数被执行的时候，才会将所有的运算逻辑返回结果。（这个概念跟 Python 中的装饰器非常类似）有兴趣的同学将会在下一篇：[Python 强大的装饰器](./02-2-装饰器完整版.md) 如果你对装饰器比较熟悉的话，要理解闭包就非常简单了。这时候又小伙伴会问：闭包有什么作用呢？ **闭包有什么作用？** 其实闭包的作用有很多，这里我主要给大家列 3 点：匿名自执行函数、封装、结果缓存。

*   第一匿名自执行函数：例如一段代码中定义一个返回函数的匿名函数，并调用这个函数。
*   第二封装：封装闭包可以将一些计算逻辑隐藏在返回函数中，这样会提升代码的可读性
*   第三结果缓存：很多时候我们并不急于将函数的结果计算出来，而是要留在后来（后面）执行。用闭包的方式可以将函数缓存在返回函数里，以供后面执行。很多前端的面试都会考闭包，其中最经典的就是**一个 for 循环加 setTimeOut 的场景。为什么最后总是输出一样的数字，**这个其实还跟事件循环有关，后面我会给大家讲到的。这道题的正确答案就是用闭包。

好了，上面讲了这么多烧脑的概念，接下来我给大家介绍一个比较简单的知识点，也就是特殊对象。

#### 2.3.5 特殊对象

*   JSON
    *   JSON、对象的序列化/反序列化的操作
    *   JSON.stringfy 序列化
    *   JSON.parse 反序列化
*   Date
    *   JS 的时间操作对象
    *   new Date(dateString)

JS 中的特殊对象有不少，这里我就给大家介绍两个。第一个是 JSON 全部大写，这是一个静态变量，主要负责对象的序列化和反序列化。JSON.stringfy 负责序列化，JSON.parse 负责反序列化。 你可能已经注意到，这两个操作在之前我们做对象的深拷贝中有用到，这其实只是其中的一种方式。另一种特殊对象是 Date，这个主要负责时间的处理，需要用 New 关键词来构造。

## 3\. JavaScript 进阶

### 目录

*   3.1 事件循环
*   3.2 原型链
*   3.3 异步编程
*   3.4 浏览器存储
*   3.5 跨域
*   3.6 Webpack 打包

### 3.1 事件循环（Event Loop）

*   定义：主线程不断的重复获取执行消息、再获取执行不断循环的机制，被称为：事件循环
*   为什么需要事件循环
    *   JavaScript 是单线程的
    *   在处理异步操作的时候需要事件循环机制
*   相关概念
    *   堆（Heap）：大块非结构化内存区域，储存对象、数据
    *   栈（Stack）：调用栈，储存该次循环，待主程序执行的任务
    *   队列（Queue）：事件队列，先进先出被推入调用栈中
*   \###### 宏任务（Macro Task）和微任务（Micro Task）
*   \###### Node.js 事件循环

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807143037.PNG) 很多人可能都听说过事件循环这个概念，但它究竟是个什么呢？ 其实要理解也不难，这里我们先看一下定义：事件循环是主线程不断的重复获取执行信息，再获取执行不断循环的机制。这里有些拗口，其实我们可以稍微理解一下。我们首先要知道，JavaScript 是单线程的，因此如果每一个异步操作都阻塞在主线程里，将会造成程序卡顿的现象，这样的结果是不可以接受的。因此我们需要一个事件循环机制，来处理这些异步操作。 这里简单介绍三个相关概念：

*   堆（Heap）：这是大块的非结构化内存区域，用于储存对象和数据。
*   栈（Stack）：这里的栈其实是调用栈，用于储存该次循环所需要顺序执行的，待主程序任务执行的任务。
*   队列（Queue）：这是一个事件队列。采用先进先出的方式被推入调用栈。每一次循环结束后，主程序都会去任务队列里调用任务消息。任务消息与一个函数相关联，将其以及相关的同步函数推入调用栈里，主程序再将同步执行调用栈里面的函数。待执行完毕后进行下一轮循环，这就是 JavaScript 的事件循环。

关于事件循环这里我们还有其他两个概念：宏任务和微任务，以及 Node.js 事件循环，鉴于文章篇幅的关系，我就不多介绍这两个知识点了，感兴趣的同学可以到网上搜索相关的资料，自学完成。

### 3.2 原型链

*   概念
    *   prototype
    *   \_\_proto\_\_
    *   constructor
*   应用场景
    *   继承、代码复用
*   ES6 出来后是否需要原型链？

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807143041.jpg) 原型链是 JavaScript 中理解原型继承比较重要的概念，这里我们简单介绍一下，每一个函数都有一个原型 prototype 属性，这个属性指向函数的原型对象，每个 new 出来的对象都有一个 `__proto__` 属性，指向对象的原型，每个原型都有一个 constructor 属性指向该关联的构造函数。 当读取实例的属性时，如果找不到，就会查找与对象关联的原型中的属性。如果还查不到，就会去找原型的原型，一直找到最顶层为止。 原型链的用途主要是为了理解 JavaScript 代码当中继承和代码的复用的，因为在 ES6 出来之前，JavaScript 中只能用原型来进行对象的封装和继承，理解原型链有助于理解整个**继承和调用的过程**。但是 ES6 中出现了一个 class 关键字，相当于一个类的语法糖，可以直观的进行面向对象操作。 **因此，我们该不该理解原型链呢？** 我的答案是，需要理解。因为我们的专栏是 JavaScript 反爬虫（也就是 JavaScript 逆向），而很多需要阅读和操作的代码都需要经过 Babel 转译后的 ES5 的代码，其中就很可能包含原型链。因此，我们是有必要学习这个内容。我这里限于篇幅的关系不会详细讲解，请同学们看一下上面的图片例子以及网上的资料自行理解。

### 3.3 异步编程

*   回调函数 Callback
    *   通过传入回调函数作为参数在函数中异步执行
    *   优点：简单
    *   缺点：回调地狱
*   Promise
    
    *   ES6 中出现的异步解决方案
    *   可以获取异步操作消息的对象
    *   resolve / reject，then / catch
    *   优点：解决了回调地狱
    *   缺点：代码可读性不高
    
    前面我提到过回调函数，这里我详细讲解一下异步编程。在 ES6 的 promise 出来之前，我们只能用回调函数来解决异步执行问题。这样简单直观，但一个比较重大的问题是其可读性，也就是**回调地狱**，同学们可以看一下下面图片的回调地狱的例子，是不是非常的难以阅读。 ![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807143045.png)
    

在 ES6 中的 promise 的出现，让回调地狱成为过去式，我们可以采用链式调用的方式来串行执行异步函数。promise 是一个可以获取异步操作信息的特殊对象，其中有 resolve + then 和 reject + catch 来分别处理成功和失败的回调，但它的缺点依然存在，在复杂情况下的异步操作可读性依然不高。 为了解决 Promise 的问题，在 ES8 中出现了 async / await 这样的语法糖，帮助我们写出更加可读的代码。它是基于 Promise 的，因此需要了解 Promise 知识，async 相当于一个返回 Promise 的函数，await 可以在函数 async 函数中起阻塞的作用，这样可以大幅度提升代码的可读性。 不过还有一个小小的缺点，并行异步操作还是需要用 promise.all 来执行。总的来说，我们推荐用 async / await 的方式来处理异步操作。 在逆向过程中我们不会看到这个语法，但是我们需要了解其相关原理，这对我们或者逆向过程是有一些帮助的。 **ES6 Promise**

```javascript
const makeRequests = () => {
    return callAPromise()
        .then(() => callAPromise())
        .then(() => callAPromise())
        .then(() => callAPromise())
        .then(() => callAPromise())
}
```

**ES8 async / await**

```javascript
async function fetchData() {
    const result1 = await callAp('https://example.com/endpoint1');
    const result2 = await callAp('https://example.com/endpoint2');
    // ...
}
```

### 3.4 浏览器存储

*   Cookies
    *   主要用于与服务端通信
    *   储存量小
*   Local Storage
    *   存储量相较于 Cookies 更大
    *   只能存储字符串
*   Session Storage
    *   只存在与当前 Session ，关闭浏览器就丢失了
    *   其他与 Local Storage 一样
*   IndexedDB
    *   相当于浏览器上的 SQL 数据库
    *   更大的储存空间
    *   API 较难掌握

Feature

Cookies

Local Storage

Session Storage

IndexedDB

Storage Limit

~4 KB

~5 MB

~5 MB

Up to half of hard drive

Persistent Data？

Yes

Yes

No

Yes

Data Value Type

String

String

String

Any structured data

Indexable？

No

No

No

Yes

在爬虫过程中，有时候我们需要去获取浏览器储存的数据，下面我们来看看有哪些浏览器储存的方式。 第一种是 **Cookies**，这是最简单的储存方式，主要用于跟服务器通信，因为每次请求都会带上 **Cookies** 。 第二种是 **Local Storage** ，这个储存量相对大一些，但还是只能存储 **字符串** 。 第三种是 **Session Storage** ，这个与 **Local Storage** 差不多，不同点是它随着 **Session** 的关闭就丢失了。 第四种是 **IndexedDB** ，这个是存储量最大的方式，可以存储任何结构的数据，缺点是 API 相对来说比较麻烦，比较难以掌握。

### 3.5 跨域

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807143051.png)

*   定义：客户端与不同源的服务器通信

> 这里说的 js 跨域是指通过 js 在不同的域之间进行数据传输或通信，比如用 ajax 向一个不同的域请求数据，或者通过 js 获取页面中不同域的框架中 (iframe) 的数据。只要协议、域名、端口有任何一个不同，都被当作是不同的域。

![](https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807143056.png) 特别注意两点：

> 1、如果是协议和端口造成的跨域问题“前台”是无能为力的； 2、在跨域问题上，域仅仅是通过 “URL 的首部”来识别而不会去尝试判断相同的 ip 地址对应着两个域或两个域是否在同一个 ip 上。

**解决方法**

*   **CORS**
    *   跨域资源共享，解决跨域请求的方案的成熟方案
*   **JSONP**
    *   基于 \\ 标签具有可跨域特性</li> <li>只能用于 GET 请求</li> </ul></li> <li><strong>iframe</strong> <ul> <li>通过 \\</li> </ul></li> </ul> &lt; iframe> 标签在一个页面展示不同源的页面 - 通过 PostMessage 进行页面之间的通信 - 反向代理 - 通过反向代理让客户端与服务端保持相同源 相对于前面的知识点跨域并不是 JavaScript 逆向必须掌握的知识。但掌握了之后对你理解浏览器与服务器之间的数据交互会非常有帮助。我们来看一下几个常见的跨域方式。 第一种 CORS 这是比较流行的跨域方案，叫跨域资源共享，是一个成熟的跨域解决方案，缺点是它有可能暴露端口，安全性方面有一定的风险。 第二种 JSONP 这种比较老的跨域方式，是基于 \\<script> 标签可以跨域的方式，但这种方式只支持 get 请求，因此有很大的局限性。 第三种 iframe 这是将不同源的网页，通过 \\ &lt; iframe> 标签放在同一个页面的跨域方式，页面之间用 PostMessage 来实现。 第四种也就是最后一种也是比较安全的一种，就是利用反向代理，我们可以使用 Nginx 或者 IIS 对请求路由做反向代理。让静态资源与 API 是以同一个资源达到跨域的目的，这种方式隐藏了后面的端口，安全性比较高。 <h3>3.6 Webpack 打包</h3> <img src="https://images-aiyc-1301641396.cos.ap-guangzhou.myqcloud.com/20200807143102.png" alt="" /> <ul> <li>目的 <ul> <li>将不同类型的源文件编译打包成静态文件</li> </ul></li> <li>为什么使用 Webpack <ul> <li>前端技术纷繁复杂，缺乏统一管理</li> <li>大型项目需要模块化</li> <li>对例如 JSX、TS 之类的新记数需要编译之后才能使用</li> </ul></li> <li>编译器</li> <li>插件</li> <li>优化</li> </ul> Webpack 打包技术是前端技术野蛮生长的必然产物，它是将众多技术融合在一起的重要方式，Webpack 打包的目的是为了将不同格式的文件（例如：JS、TS、sass 等），打包编译成固定的静态文件。 我们为什么要用 Webpack 呢？ 原因主要有三点：第一前端技术纷繁复杂，缺乏统一管理、第二大型项目需要模块化、第三对于像 JS、TS 这样的新技术，用编译之后才能使用。我们要用 Webpack 解决以上问题，此外 Webpack 需要配置特定的编译器，我们通常采用 babel作为 JavaScript 的编译器。Webpack 还提供很多插件来以次支持更多的特殊功能。 最后 Webpack 有大量的配置，为了让打包过程变得高效和使用，我们还需要对这些配置进行优化，这也是个技术活。 对 Webpack 打包有兴趣的同学可以到网上搜一下相关的知识，做进一步的学习。 <h2>总结</h2> <h5>1. JavaScript 简介</h5> <ul> <li>背景</li> <li>与 CSS / HTML 关系</li> <li>发展</li> </ul> <h5>2. JavaScript 语法</h5> <ul> <li>数据类型</li> <li>控制流</li> <li>函数</li> <li>特殊对象</li> </ul> <h5>3. JavaScript 进阶</h5> <ul> <li>事件循环</li> <li>原型链</li> <li>异步编程</li> <li>浏览器储存</li> <li>跨域</li> <li>Webpack 打包</li> </ul> 我首先给 JavaScript 进行了一些背景和发展介绍，了解了它与 HTML、CSS 之间的关系，其次我们还了解到了相关语法，包括数据类型、控制流、函数以及特殊对象等等，最后我介绍了 JavaScript 进阶知识，帮助我们深入理解 JavaScript ，其中包括事件循环、原型链、异步编程、浏览器储存、跨域、Webpack 打包。经过本文的学习，相信同学们已经对 JavaScript 基础知识有一定的理解，希望接下来以后，你能在每个知识点上进一步学习，来以次巩固你的 JavaScript 知识，这对后面的实战课程都是有非常大的帮助。 本次文章就这样结束了，我门下期再见！</x-turndown>