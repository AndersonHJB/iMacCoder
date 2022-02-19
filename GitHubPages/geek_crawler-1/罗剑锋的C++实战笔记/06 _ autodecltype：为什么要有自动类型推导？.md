<audio title="06 _ autodecltype：为什么要有自动类型推导？" src="https://static001.geekbang.org/resource/audio/d0/33/d0dec00dd6b1003f2238d36f60b20e33.mp3" controls="controls"></audio> 
<p>你好，我是Chrono。</p><p>前两周我们从宏观的层面上重新认识了C++，从今天开始，我们将进入一个新的“语言特性”单元，“下沉”到微观的层面去观察C++，一起去见一些老朋友、新面孔，比如const、exception、lambda。</p><p>这次要说的，就是C++11里引入的一个很重要的语言特性：自动类型推导。</p><h2>自动类型推导</h2><p>如果你有过一些C++的编程经验，了解过C++11，那就一定听说过“<strong>自动类型推导</strong>”（auto type deduction）。</p><p>它其实是一个非常“老”的特性，C++之父Bjarne Stroustrup（B·S )早在C++诞生之初就设计并实现了它，但因为与早期C语言的语义有冲突，所以被“雪藏”了近三十年。直到C99消除了兼容性问题，C++11才让它再度登场亮相。</p><p>那为什么要重新引入这个“老特性”呢？为什么非要有“自动类型推导”呢？</p><p>我觉得，你可以先从字面上去理解，把这个词分解成三个部分：“自动”“类型”和“推导”。</p><ul>
<li>“自动”就是让计算机去做，而不是人去做，相对的是“手动”。</li>
<li>“类型”指的是操作目标，出来的是编译阶段的类型，而不是数值。</li>
<li>“推导”就是演算、运算，把隐含的值给算出来。</li>
</ul><p>好，我们来看一看“自动类型推导”之外的其他几种排列组合，通过对比的方式来帮你理解它。</p><!-- [[[read_end]]] --><p>像计算“a = 1 + 1”，你可以在写代码的时候直接填上2，这就是“手动数值推导”。你也可以“偷懒”，只写上表达式，让电脑在运行时自己算，这就是“自动数值推导”。</p><p>“数值推导”对于人和计算机来说都不算什么难事，所以手动和自动的区别不大，只有快慢的差异。但“类型推导”就不同了。</p><p>因为C++是一种静态强类型的语言，任何变量都要有一个确定的类型，否则就不能用。在“自动类型推导”出现之前，我们写代码时只能“手动推导”，也就是说，在声明变量的时候，必须要明确地给出类型。</p><p>这在变量类型简单的时候还好说，比如int、double，但在泛型编程的时候，麻烦就来了。因为泛型编程里会有很多模板参数，有的类型还有内部子类型，一下子就把C++原本简洁的类型体系给搞复杂了，这就迫使我们去和编译器“斗智斗勇”，只有写对了类型，编译器才会“放行”（编译通过）。</p><pre><code>int       i = 0;            // 整数变量，类型很容易知道
double    x = 1.0;          // 浮点数变量，类型很容易知道

std::string str = &quot;hello&quot;;  // 字符串变量，有了名字空间，麻烦了一点

std::map&lt;int, std::string&gt; m = // 关联数组，名字空间加模板参数，很麻烦
        {{1,&quot;a&quot;}, {2,&quot;b&quot;}};    // 使用初始化列表的形式

std::map&lt;int, std::string&gt;::const_iterator // 内部子类型，超级麻烦
iter = m.begin();

？？？ = bind1st(std::less&lt;int&gt;(), 2);  // 根本写不出来
</code></pre><p>虽然你可以用typedef或者using来简化类型名，部分减轻打字的负担，但关键的“手动推导”问题还是没有得到解决，还是要去翻看类型定义，找到正确的声明。这时，C++的静态强类型的优势反而成为了劣势，阻碍了程序员的工作，降低了开发效率。</p><p>其实编译器是知道（而且也必须知道）这些类型的，但它却没有办法直接告诉你，这就很尴尬了。一边是急切地想知道答案，而另一边却只给判个对错，至于怎么错了、什么是正确答案，“打死了也不说”。</p><p>但有了“自动类型推导”，问题就迎刃而解了。这就像是在编译器紧闭的大门上开了道小口子，你跟它说一声，它就递过来张小纸条，具体是什么不重要，重要的是里面存了我们想要的类型。</p><p>这个“小口子”就是关键字<strong>auto</strong>，在代码里的作用像是个“占位符”（placeholder）。写上它，你就可以让编译器去自动“填上”正确的类型，既省力又省心。</p><pre><code>auto  i = 0;          // 自动推导为int类型
auto  x = 1.0;        // 自动推导为double类型

auto  str = &quot;hello&quot;;  // 自动推导为const char [6]类型

std::map&lt;int, std::string&gt; m = {{1,&quot;a&quot;}, {2,&quot;b&quot;}};  // 自动推导不出来

auto  iter = m.begin();  // 自动推导为map内部的迭代器类型

auto  f = bind1st(std::less&lt;int&gt;(), 2);  // 自动推导出类型，具体是啥不知道
</code></pre><p>不过需要注意的是，因为C++太复杂，“自动类型推导”有时候可能失效，给不出你想要的结果。比如，在上面的这段代码里，就把字符串的类型推导成了“const char [6]”而不是“std::string”。而有的时候，编译器也理解不了代码的意思，推导不出恰当的类型，还得你自己“亲力亲为”。</p><p>在这个示例里，你还可以直观感觉到auto让代码干净整齐了很多，不用去写那些复杂的模板参数了。但如果你把“自动类型推导”理解为仅仅是简化代码、少打几个字，那就实在是浪费了C++标准委员会的一番苦心。</p><p><strong>除了简化代码，auto还避免了对类型的“硬编码”</strong>，也就是说变量类型不是“写死”的，而是能够“自动”适应表达式的类型。比如，你把map改为unordered_map，那么后面的代码都不用动。这个效果和类型别名（<a href="https://time.geekbang.org/column/article/235301">第5讲</a>）有点像，但你不需要写出typedef或者using，全由auto“代劳”。</p><p>另外，你还应该认识到，“自动类型推导”实际上和“attribute”一样（<a href="https://time.geekbang.org/column/article/235295">第4讲</a>），是编译阶段的特殊指令，指示编译器去计算类型。所以，它在泛型编程和模板元编程里还有更多的用处，后面我会陆续讲到。</p><h2>认识auto</h2><p>刚才说了，auto有时候会不如你设想的那样工作，因此在使用的时候，有一些需要特别注意的地方，下面我就给你捋一捋。</p><p>首先，你要知道，auto的“自动推导”能力只能用在“<strong>初始化</strong>”的场合。</p><p>具体来说，就是<strong>赋值初始化</strong>或者<strong>花括号初始化</strong>（初始化列表、Initializer list），变量右边必须要有一个表达式（简单、复杂都可以）。这样你才能在左边放上auto，编译器才能找到表达式，帮你自动计算类型。</p><p>如果不是初始化的形式，只是“纯”变量声明，那就无法使用auto。因为这个时候没有表达式可以让auto去推导。</p><pre><code>auto x = 0L;    // 自动推导为long
auto y = &amp;x;    // 自动推导为long*
auto z {&amp;x};    // 自动推导为long* 

auto err;       // 错误，没有赋值表达式，不知道是什么类型
</code></pre><p>这里还有一个特殊情况，在类成员变量初始化的时候（<a href="https://time.geekbang.org/column/article/235301">第5讲</a>），目前的C++标准不允许使用auto推导类型（但我个人觉得其实没有必要，也许以后会放开吧）。所以，在类里你还是要老老实实地去“手动推导类型”。</p><pre><code>class X final
{
    auto a = 10;  // 错误，类里不能使用auto推导类型
};
</code></pre><p>知道了应用场合，你还需要了解auto的推导规则，保证它能够按照你的意思去工作。虽然标准里规定得很复杂、很细致，但我总结出了两条简单的规则，基本上够用了：</p><ul>
<li><strong>auto总是推导出“值类型”，绝不会是“引用”；</strong></li>
<li><strong>auto可以附加上const、volatile、*、&amp;这样的类型修饰符，得到新的类型。</strong></li>
</ul><p>下面我举几个例子，你一看就能明白：</p><pre><code>auto        x = 10L;		// auto推导为long，x是long

auto&amp;       x1 = x;		  // auto推导为long，x1是long&amp;
auto*       x2 = &amp;x;	  // auto推导为long，x2是long*
const auto&amp; x3 = x;	      // auto推导为long，x3是const long&amp;
auto        x4 = &amp;x3;	  // auto推导为const long*，x4是const long*
</code></pre><h2>认识decltype</h2><p>前面我都在说auto，其实，C++的“自动类型推导”还有另外一个关键字：<strong>decltype</strong>。</p><p>刚才你也看到了，auto只能用于“初始化”，而这种“<strong>向编译器索取类型</strong>”的能力非常有价值，把它限制在这么小的场合，实在是有点“屈才”了。</p><p>“自动类型推导”要求必须从表达式推导，那在没有表达式的时候，该怎么办呢？</p><p>其实解决思路也很简单，就是“自己动手，丰衣足食”，自己带上表达式，这样就走到哪里都不怕了。</p><p>decltype的形式很像函数，后面的圆括号里就是可用于计算类型的表达式（和sizeof有点类似），其他方面就和auto一样了，也能加上const、*、&amp;来修饰。</p><p>但因为它已经自带表达式，所以不需要变量后面再有表达式，也就是说可以直接声明变量。</p><pre><code>int x = 0;					// 整型变量

decltype(x)     x1;      // 推导为int，x1是int
decltype(x)&amp;    x2 = x;    // 推导为int，x2是int&amp;，引用必须赋值
decltype(x)*    x3;      // 推导为int，x3是int*
decltype(&amp;x)    x4;      // 推导为int*，x4是int*
decltype(&amp;x)*   x5;      // 推导为int*，x5是int**
decltype(x2)    x6 = x2;  // 推导为int&amp;，x6是int&amp;，引用必须赋值
</code></pre><p>把decltype和auto比较一下，简单来看，好像就是把表达式改到了左边而已，但实际上，在推导规则上，它们有一点细微且重要的区别：</p><p><strong>decltype不仅能够推导出值类型，还能够推导出引用类型，也就是表达式的“原始类型”</strong>。</p><p>在示例代码中，我们可以看到，除了加上*和&amp;修饰，decltype还可以直接从一个引用类型的变量推导出引用类型，而auto就会把引用去掉，推导出值类型。</p><p>所以，你完全可以把decltype看成是一个真正的类型名，用在变量声明、函数参数/返回值、模板参数等任何类型能出现的地方，只不过这个类型是在编译阶段通过表达式“计算”得到的。</p><p>如果不信的话，你可以用using类型别名来试一试。</p><pre><code>using int_ptr = decltype(&amp;x);    // int *
using int_ref = decltype(x)&amp;;    // int &amp;
</code></pre><p>既然decltype类型推导更精确，那是不是可以替代auto了呢？</p><p>实际上，它也有个缺点，就是写起来略麻烦，特别在用于初始化的时候，表达式要重复两次（左边的类型计算，右边的初始化），把简化代码的优势完全给抵消了。</p><p>所以，C++14就又增加了一个“<strong>decltype(auto)</strong>”的形式，既可以精确推导类型，又能像auto一样方便使用。</p><pre><code>int x = 0;						// 整型变量

decltype(auto)     x1 = (x);  // 推导为int&amp;，因为(expr)是引用类型
decltype(auto)     x2 = &amp;x;   // 推导为int*
decltype(auto)     x3 = x1;   // 推导为int&amp;
</code></pre><h2>使用auto/decltype</h2><p>现在，我已经讲完了“自动类型推导”的两个关键字：auto和decltype，那么，该怎么用好它们呢？</p><p>我觉得，因为auto写法简单，推导规则也比较好理解，所以，<strong>在变量声明时应该尽量多用auto</strong>。前面已经举了不少例子，这里就不再重复了。</p><p>auto还有一个“最佳实践”，就是“<strong>range-based for</strong>”，不需要关心容器元素类型、迭代器返回值和首末位置，就能非常轻松地完成遍历操作。不过，为了保证效率，最好使用“const auto&amp;”或者“auto&amp;”。</p><pre><code> vector&lt;int&gt; v = {2,3,5,7,11};	// vector顺序容器

 for(const auto&amp; i : v) {	    // 常引用方式访问元素，避免拷贝代价
     cout &lt;&lt; i &lt;&lt; &quot;,&quot;;          // 常引用不会改变元素的值
 }

 for(auto&amp; i : v) {	        // 引用方式访问元素
     i++;	                    // 可以改变元素的值
     cout &lt;&lt; i &lt;&lt; &quot;,&quot;;
 }
</code></pre><p>在C++14里，auto还新增了一个应用场合，就是能够推导函数返回值，这样在写复杂函数的时候，比如返回一个pair、容器或者迭代器，就会很省事。</p><pre><code>auto get_a_set()              // auto作为函数返回值的占位符
{
    std::set&lt;int&gt; s = {1,2,3};
    return s;
}
</code></pre><p>再来看decltype怎么用最合适。</p><p>它是auto的高级形式，更侧重于编译阶段的类型计算，所以常用在泛型编程里，获取各种类型，配合typedef或者using会更加方便。当你感觉“这里我需要一个特殊类型”的时候，选它就对了。</p><p>比如说，定义函数指针在C++里一直是个比较头疼的问题，因为传统的写法实在是太怪异了。但现在就简单了，你只要手里有一个函数，就可以用decltype很容易得到指针类型。</p><pre><code>// UNIX信号函数的原型，看着就让人晕，你能手写出函数指针吗？
void (*signal(int signo, void (*func)(int)))(int)

// 使用decltype可以轻松得到函数指针类型
using sig_func_ptr_t = decltype(&amp;signal) ;
</code></pre><p>在定义类的时候，因为auto被禁用了，所以这也是decltype可以“显身手”的地方。它可以搭配别名任意定义类型，再应用到成员变量、成员函数上，变通地实现auto的功能。</p><pre><code>class DemoClass final
{
public:
    using set_type      = std::set&lt;int&gt;;  // 集合类型别名
private:
    set_type      m_set;                   // 使用别名定义成员变量

    // 使用decltype计算表达式的类型，定义别名
    using iter_type = decltype(m_set.begin());

    iter_type     m_pos;                   // 类型别名定义成员变量
};
</code></pre><h2>小结</h2><p>好了，今天我介绍了C++里的“自动类型推导”，简单小结一下今天的内容。</p><ol>
<li>“自动类型推导”是给编译器下的指令，让编译器去计算表达式的类型，然后返回给程序员。</li>
<li>auto用于初始化时的类型推导，总是“值类型”，也可以加上修饰符产生新类型。它的规则比较好理解，用法也简单，应该积极使用。</li>
<li>decltype使用类似函数调用的形式计算表达式的类型，能够用在任意场合，因为它就是一个编译阶段的类型。</li>
<li>decltype能够推导出表达式的精确类型，但写起来比较麻烦，在初始化时可以采用decltype(auto)的简化形式。</li>
<li>因为auto和decltype不是“硬编码”的类型，所以用好它们可以让代码更清晰，减少后期维护的成本。</li>
</ol><h2>课下作业</h2><p>最后是课下作业时间，给你留两个思考题：</p><ol>
<li>auto和decltype虽然很方便，但用多了也确实会“隐藏”真正的类型，增加阅读时的理解难度，你觉得这算是缺点吗？是否有办法克服或者缓解？</li>
<li>说一下你对auto和decltype的认识。你认为，两者有哪些区别呢？（推导规则、应用场合等）</li>
</ol><p>欢迎你在留言区写下你的思考和答案，如果觉得今天的内容对你有所帮助，也欢迎分享给你的朋友，我们下节课见。</p><p><img src="https://static001.geekbang.org/resource/image/6e/14/6ec0c53ee9917795c0e2a494cfe70014.png" alt=""></p>