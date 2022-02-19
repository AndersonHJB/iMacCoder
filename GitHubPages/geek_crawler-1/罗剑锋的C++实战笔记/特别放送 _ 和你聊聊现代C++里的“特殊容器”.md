<audio title="特别放送 _ 和你聊聊现代C++里的“特殊容器”" src="https://static001.geekbang.org/resource/audio/50/c2/50bca371858db90ef6f61f3e1c3115c2.mp3" controls="controls"></audio> 
<p>你好，我是Chrono。</p><p>《罗剑锋的C++实战笔记》这门课已经完结有一年多的时间了，看到有很多同学还在留言区研究、探讨C++的技术问题，我非常开心。能够为现代C++在国内的推广普及做一点力所能及的贡献，对我来说，实在是一件很有意义的事情。</p><h2>一个好消息</h2><p>现在，还有一个好消息要告诉持续关注这门课的朋友们。年初的时候，人民邮电出版社的编辑在网上联系到了我，他们也对现代C++很感兴趣，想把这个线上的课程“搬”到线下，改成纸质的实体图书。</p><p>于是，这大半年来，我就花了很多精力与出版社合作，把这门课的内容重新整理完善，改成更适合纸质图书阅读的形式。现在来看，虽然核心的内容不变，但在语言表述、示例代码、整体架构方面都做了非常大的修改，可以说是把这门课由内到外动了一个“大手术”，完全变成了另外一幅面孔另一个人。</p><p><img src="https://static001.geekbang.org/resource/image/3c/3f/3cb3e4b565f5b6fc656803d8dfac513f.png?wh=957x315" alt=""></p><blockquote>
<p>罗剑锋的《C++实战笔记》已经在极客商城上线，你可以点击<a href="https://shop18793264.m.youzan.com/wscgoods/detail/2oiy2u01z4b3c6d?dc_ps=2911469729606718469.200001">链接</a>购买。</p>
</blockquote><p>另外，这门课上线之初考虑到国内的C++应用现状，使用的是C++11/14，GCC的版本是5.4，而到了一年之后的今天，确实显得有点老旧了。所以借着这次出版图书的机会，我也做了一个全面的升级，C++标准更新到了17/20，GCC的版本是7.5和10.3，应该可以在一两年的时间之内不会过时。</p><!-- [[[read_end]]] --><p>相应地，图书里的示例代码也做了更新和调整，全部使用C++17/20标准和GCC7/10编译通过，应用了许多标准里的新特性。</p><p>而且，为了让图书更具“实战”价值，我还在每个章节都新增了很多的内容，比如用Docker/Kubernetes搭建开发环境、C++各标准特性介绍、C++20的格式化功能、范围算法、Boost程序库精选等等。这些都是当初设计这门课的时候想写但因为种种原因没有来得及写的内容，现在终于能够呈现在广大C++爱好者面前了，也算是了结了我的一份心愿。</p><p>因为示例代码都使用了新标准，原来的GitHub项目cpp_study（<a href="https://github.com/chronolaw/cpp_study">https://github.com/chronolaw/cpp_study</a>）已经不太合适了，所以我又新开了一个项目cpp_note（<a href="https://github.com/chronolaw/cpp_note">https://github.com/chronolaw/cpp_note</a>），并且在DockerHub上提供了打包好的镜像，可以使用命令“docker pull chronolaw/cpp_note”拉取后直接在本地运行。</p><p>不过，由于目前GitHub不够稳定，有的时候可能访问起来有困难，如果你有需要，可以在这里留言，我会在国内找个托管网站做项目同步，方便大家的使用和学习。</p><p>那么接下来呢，我就摘取图书中的一部分新内容，<strong>来聊聊C++17标准里提供的optional和variant这两种特殊容器。</strong></p><p>容器我们都已经很熟悉了，那什么是“特殊容器”呢？</p><p>传统意义上C++里的容器，指的就是在课程<a href="https://time.geekbang.org/column/article/243319">第12讲</a>里介绍的顺序容器、有序容器和无序容器，但随着语言的发展，标准库里也增加了一些新的数据结构。它们不完全符合容器的定义，但在用法、用途上又很像容器，所以这类数据结构一般就统称为“特殊容器”。</p><h2>可选值optional</h2><p>你一定知道，C++的函数只能返回一个值，这个值必须是可用的、有效的、有意义的，比如分配的字节数、创建的对象指针、查找字符串的位置等等。</p><p>不过，很多时候函数如果执行不成功，就不一定能够返回有意义的值，比如内存空间不足、创建对象失败、模式字符串不存在等等，这个时候函数的返回值就会是无效的。</p><p>但C++的传统方式在表示“无效”概念的时候是比较麻烦的，它通常会用一个特殊的0或者-1来表示，比如分配内存、创建对象返回nullptr，查找字符返回npos。</p><p>但还有很多时候函数调用可能并不存在这种“无效值”，比如我们在实数域上求平方根，如果操作对象是负数，那么函数就没有恰当的方法来处理，没有办法返回一个合理的“无效值”。</p><p>当然，我们可以把这种情况视为错误，用抛出异常的方式来报错，但这样的成本太高，而且有的场合下异常的使用也可能受到限制。</p><p>所以，<strong>我们就需要有一种简单、轻量级的概念，它能够表示任何的“无效值”，这在现代C++中就是模板类optional。</strong></p><p>optional可以近似地看做是只能容纳一个元素的特殊容器，而这样的容器就会有是否持有元素的两种状态，“空”和“非空”，恰好就对应无效和有效，不需要使用特殊的0或者-1，非常自然地解决了我们上面遇到的难题。</p><p>optional对象默认是空的，也就是处于无效状态，给它赋值后因为里面有了元素，就变成了有效状态，判断optional对象是否有效可以调用它的成员函数has_value()，示例代码如下：</p><pre><code>optional&lt;int&gt; op; 						// 持有int的optional对象
assert(!op.has_value()); 				// 默认是无效值

op = 10; 								// 赋值，持有有效值
if (op.has_value()) {					// 判断是否有效
  cout &lt;&lt; &quot;value is valid&quot; &lt;&lt; endl;
} 
</code></pre><p>如果optional是有效的，也就是说里面有值，那么我们可以调用成员函数value()获取值的引用，而另一个成员函数value_or()则更灵活些，如果optional无效就会返回给定的替代值，可以免去我们检查的步骤，代码写起来更加简单：</p><pre><code>optional&lt;int&gt; op1 = 42; 				// 初始化有效值的optional

if (op1.has_value()) {					// 判断是否有效
    cout &lt;&lt; op1.value() &lt;&lt; endl; 		// 获取值的引用
}

optional&lt;int&gt; op2; 						// 初始化无效值的optional
cout &lt;&lt; op2.value_or(99) &lt;&lt; endl; 		// 无效，返回给定的替代值
</code></pre><p>不过另一方面，optional行为表现的又很像指针，可以用*/-&gt;来直接访问内部的值，也能够显式（explicit）转换为bool值，或者用reset()清空内容，用起来非常像我们之前讲过的智能指针unique_ptr：</p><pre><code>optional&lt;string&gt; op {&quot;zelda&quot;};			// 持有string的optional对象
assert(op); 							// 可以像指针一样bool判断
assert(!op-&gt;empty() &amp;&amp; *op == &quot;zelda&quot;);	// 使用*/-&gt;访问内部的值

op.reset();								// 清空内部的值
assert(!op); 							// 此时是无效值
</code></pre><p>同样的，optional也可以用工厂函数make_optional()来创建，不过与直接构造不同，即使不提供初始化参数，它也必定会用“零值”创建出一个有效值的optional对象，这一点我们在用的时候要特别注意，例如：</p><pre><code>auto op1 = make_optional&lt;int&gt;();		// 使用默认值构造有效值
auto op2 = make_optional&lt;string&gt;();		// 使用默认值构造有效值

assert(op1 &amp;&amp; op2); 					// make_optional总是有效的
assert(op1 == 0); 						// 值是默认的0
assert(op2-&gt;empty());					// 值是空字符串

auto op3 = make_optional&lt;string&gt;(&quot;hi&quot;);			// 带参数创建optional
auto op4 = make_optional&lt;vector&lt;int&gt;&gt;({1,2,3});	// 带参数创建optional

assert(op3-&gt;size() == 2);
assert(op4-&gt;at(0) == 1);
</code></pre><p>好了，现在我们有了optional，当函数需要返回可能无效的值的时候就简单了，只需要把函数的返回值用optional包装一下就可以，比如之前说到的实数求平方根：</p><pre><code>auto safe_sqrt = [](double x) {			// lambda表达式开平方
    optional&lt;double&gt; v; 				// 默认是无效值

    if (x &lt; 0) {						// 负数无法求平方根
        return v; 						// 返回无效值
    }

    v  = ::sqrt(x); 					// 正数平方根有效
    return v; 							// 返回有效值
};

assert(!safe_sqrt(-1)); 				// 负数无法求平方根
assert(safe_sqrt(9).value() == 3); 		// 正数平方根有效
</code></pre><p>关于optional最后我们要注意的是，当它内部持有的是bool类型的时候，由于它本身可以转型成bool，但含义是值的有效性，而并非内部的bool真假，所以我们写代码的时候就必须判断两次，不留意的话很容易误用，例如：</p><pre><code>optional&lt;bool&gt; op {false}; 				// 持有bool的optional对象

if (op) {								// 错误用法，实际上判断的是有效性
    cout &lt;&lt; &quot;misuse&quot; &lt;&lt; endl;
}

if (op &amp;&amp; op.value()) {					// 正确用法，有效后再检查值
    cout &lt;&lt; &quot; right &quot; &lt;&lt; endl;
}
</code></pre><h2>可变值variant</h2><p>C++里有一种特殊的数据结构union，它可以把多种不同的类型“聚合”在一起，运行的时候能够随时切换“身份”，有点“变脸”“多重人格”的感觉，在底层系统级编程的时候非常有用。例如：</p><pre><code>union {									// 定义一个联合体
    int     n; 							// 可以是整数或者浮点数
    float   f;
    double  d;
} x; 									// 定义的同时声明变量

x.d = 3.14; 							// 像类成员变量那样操作
x.n = 10; 								// 同一时刻只能有一种数据类型
</code></pre><p>不过union的功能比较弱，只能聚合平凡（trivial，或者叫POD/Plain Old Data）的数据类型，遇到像string/vector这样比较复杂的类型就派不上用场。</p><p><strong>在C++17里，标准委员会新引入了一个模板类variant，它可以说是一个“智能union”，能够聚合任意类型，没有任何限制，同时用起来又和union几乎一样方便。</strong></p><p>如果我们以容器的视角来看variant，它就像是只能容纳一个元素的“异质”容器，里面存放的具体类型是不确定的，想知道当前是哪种元素必须调用成员函数index()，它会返回当前元素类型在模板参数列表里的索引：</p><pre><code>variant&lt;int, float, double&gt; v; 			// 可以容纳三种不同的整数

v = 42; 								// 直接赋值为int
assert(v.index() == 0); 				// 索引号是0

v = 3.14f; 								// 直接赋值为float
assert(v.index() == 1); 				// 索引号是1

v = 2.718; 								// 直接赋值为double
assert(v.index() == 2); 				// 索引号是2
</code></pre><p>不过因为variant需要存储任意类型，内部结构比较复杂，所以variant不能像union那样用成员变量的形式来访问内部的值，必须要用外部的函数get()来获取值。get()是一个比较特别的模板函数，调用时必须在函数名后加上模板的尖括号，里面的模板参数可以是类型名或者是索引号。</p><p>很显然，因为variant任意时刻只能持有一种类型，如果用get()访问了不存在的值就会出错，C++会以抛出异常的方式来告知调用者。例如：</p><pre><code>v = 42; 							// 赋值为int
assert(get&lt;0&gt;(v) == 42); 			// 取第0号的值，即int

v = 2.718; 							// 赋值为double
auto x = get&lt;double&gt;(v); 			// 取double的值，即第2号

get&lt;int&gt;(v); 						// 当前是double，所以出错，抛出异常
</code></pre><p>不过抛出异常的方式不太友好，try-catch处理起来比较麻烦，所以我们还可以用另一个模板函数get_if()，它以指针的方式返回variant内部的值，如果不存在就是nullptr，这样用起来就比较轻松了：</p><pre><code>auto p = get_if&lt;int&gt;(&amp;v); 			// 取int的值，不存在就是空指针
assert(p == nullptr);
</code></pre><p>另外，C++还提供了一个全局函数visit()，它是get/get_if之外的另一种更灵活的使用方式，我们可以不需要考虑类型的索引号，以一个集中业务逻辑的“访问器”函数来专门处理variant对象。</p><p>因为variant是“异质”的，所以这个访问器函数最好是泛型的lambda表达式，写起来更方便：</p><pre><code>variant&lt;int, string&gt; v; 			// 可以容纳整数和字符串

auto vistor = [](auto&amp; x) {			// 泛型的lambda，不用写模板参数
    x = x + x; 						// 输入值加倍
    cout &lt;&lt; x &lt;&lt; endl;
};

v = 10; 							// 赋值为int
std::visit(vistor, v); 				// 输出20

v = &quot;ok&quot;;							// 赋值为string
std::visit(vistor, v); 				// 输出okok
</code></pre><p>我们需要特别注意一点，在实现访问器函数的时候，它必须能够处理variant的任何可能类型，否则就无法通过C++的静态编译检查。</p><p>比如，如果我们在这段示例代码中把lambda的赋值语句改成“x = x * x”，那么它肯定是无法应用于string的，所以就会报出一大堆编译错误。</p><p>variant“异质容器”的特性非常有价值，我们深入思考一下就会发现，它完全可以在不使用“继承”“虚函数”的情况下实现面向对象编程里的“多态”特性，也因为没有了虚表指针运行效率会更高。</p><h2>小结</h2><p>好了，今天我们学习了C++传统容器之外的两种新型数据结构：optional和variant。其实它们并不是容器，因为没有迭代器也不能应用算法，但它们和标准容器一样能够“容纳元素”，所以可以视为是特殊的容器。</p><p>简单小结一下今天的内容：</p><ol>
<li>传统的C++在表示无效值时有很多限制，比较麻烦，所以就出现了optional；</li>
<li>optional专门用来表示值有效或者无效，用法很像是单元素容器或者智能指针，最佳的应用场景是函数的返回值；</li>
<li>传统C++的union可以存放多种不同的值，很有用，但局限性很大；</li>
<li>variant是对union的增强，它是一种“异质”容器，能够在运行时改变类型，进而实现泛型多态。</li>
</ol><h2>课下作业</h2><p>按照我们课程的惯例，最后仍然是课下作业时间，给你留两个思考题：</p><ol>
<li>optional很像容器和智能指针，那么与它们的区别在哪里呢？</li>
<li>访问variant对象可以使用get()和visit()，这两个函数各自有什么优点和缺点？</li>
</ol><p><img src="https://static001.geekbang.org/resource/image/36/a5/361f79e4cb5b4bf548a140edaf9a86a5.png?wh=3624x5300" alt=""></p>