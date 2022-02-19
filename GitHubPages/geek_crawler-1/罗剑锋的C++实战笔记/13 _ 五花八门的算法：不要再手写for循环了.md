<audio title="13 _ 五花八门的算法：不要再手写for循环了" src="https://static001.geekbang.org/resource/audio/e7/3d/e7402ecdfb023dbb0738e8f52cf99a3d.mp3" controls="controls"></audio> 
<p>你好，我是Chrono。</p><p>上节课我提到了计算机界的经典公式“算法 + 数据结构 = 程序”，公式里的“数据结构”就是C++里的容器，容器我们已经学过了，今天就来学习下公式里的“算法”。</p><p>虽然算法是STL（标准库前身）的三大要件之一（容器、算法、迭代器），也是C++标准库里一个非常重要的部分，但它却没有像容器那样被大众广泛接受。</p><p>从我观察到的情况来看，很多人都会在代码里普遍应用vector、set、map，但几乎从来不用任何算法，聊起算法这个话题，也是“一问三不知”，这的确是一个比较奇怪的现象。而且，很多语言对算法也不太“上心”。</p><p>但是，在C++里，算法的地位非常高，甚至有一个专门的“算法库”。早期，它是泛型编程的示范和应用，而在C++引入lambda表达式后，它又成了函数式编程的具体实践，所以，<strong>学习掌握算法能够很好地训练你的编程思维，帮你开辟出面向对象之外的新天地</strong>。</p><h2>认识算法</h2><p>从纯理论上来说，算法就是一系列定义明确的操作步骤，并且会在有限次运算后得到结果。</p><p>计算机科学里有很多种算法，像排序算法、查找算法、遍历算法、加密算法，等等。但是在C++里，算法的含义就要狭窄很多了。</p><p>C++里的算法，指的是<strong>工作在容器上的一些泛型函数</strong>，会对容器内的元素实施的各种操作。</p><!-- [[[read_end]]] --><p>C++标准库目前提供了上百个算法，真的可以说是“五花八门”，涵盖了绝大部分的“日常工作”。比如：</p><ul>
<li>remove，移除某个特定值；</li>
<li>sort，快速排序；</li>
<li>binary_search，执行二分查找；</li>
<li>make_heap，构造一个堆结构；</li>
<li>……</li>
</ul><p>不过要是“说白了”，算法其实并不神秘，因为所有的算法本质上都是for或者while，通过循环遍历来逐个处理容器里的元素。</p><p>比如说count算法，它的功能非常简单，就是统计某个元素的出现次数，完全可以用range-for来实现同样的功能：</p><pre><code>vector&lt;int&gt; v = {1,3,1,7,5};    // vector容器

auto n1 = std::count(          // count算法计算元素的数量 
    begin(v), end(v), 1        // begin()、end()获取容器的范围
);  

int n2 = 0;
for(auto x : v) {              // 手写for循环
    if (x == 1) {              // 判断条件，然后统计
        n2++;
    }
}  
</code></pre><p>你可能会问，既然是这样，我们直接写for循环不就好了吗，为什么还要调用算法来“多此一举”呢？</p><p>在我看来，这应该是一种“境界”，<strong>追求更高层次上的抽象和封装</strong>，也是函数式编程的基本理念。</p><p>每个算法都有一个清晰、准确的命名，不需要额外的注释，让人一眼就可以知道操作的意图，而且，算法抽象和封装了反复出现的操作逻辑，也更有利于重用代码，减少手写的错误。</p><p>还有更重要的一点：和容器一样，算法是由那些“超级程序员”创造的，它的内部实现肯定要比你随手写出来的循环更高效，而且必然经过了良好的验证测试，绝无Bug，无论是功能还是性能，都是上乘之作。</p><p>如果在以前，你不使用算法还有一个勉强可以说的理由，就是很多算法必须要传入一个函数对象，写起来很麻烦。但是现在，因为有可以“<strong>就地定义函数</strong>”的lambda表达式，算法的形式就和普通循环非常接近了，所以刚刚说的也就不再是什么问题了。</p><p>用算法加上lambda表达式，你就可以初步体验函数式编程的感觉（即函数套函数）：</p><pre><code>auto n = std::count_if(      // count_if算法计算元素的数量
    begin(v), end(v),       // begin()、end()获取容器的范围
    [](auto x) {            // 定义一个lambda表达式
        return x &gt; 2;       // 判断条件
    }
);                          // 大函数里面套了三个小函数
</code></pre><h2>认识迭代器</h2><p>在详细介绍算法之前，还有一个必须要了解的概念，那就是迭代器（iterator），它相当于算法的“手脚”。</p><p>虽然刚才我说算法操作容器，但实际上它看到的并不是容器，而是指向起始位置和结束位置的迭代器，算法只能通过迭代器去“<strong>间接</strong>”访问容器以及元素，算法的能力是由迭代器决定的。</p><p>这种间接的方式有什么好处呢？</p><p>这就是泛型编程的理念，与面向对象正好相反，<strong>分离了数据和操作</strong>。算法可以不关心容器的内部结构，以一致的方式去操作元素，适用范围更广，用起来也更灵活。</p><p>当然万事无绝对，这种方式也有弊端。因为算法是通用的，免不了对有的数据结构虽然可行但效率比较低。所以，对于merge、sort、unique等一些特别的算法，容器就提供了专门的替代成员函数（相当于特化），这个稍后我会再提一下。</p><p>C++里的迭代器也有很多种，比如输入迭代器、输出迭代器、双向迭代器、随机访问迭代器，等等，概念解释起来不太容易。不过，你也没有必要把它们搞得太清楚，因为常用的迭代器用法都是差不多的。你可以把它简单地理解为另一种形式的“智能指针”，只是它<strong>强调的是对数据的访问</strong>，而不是生命周期管理。</p><p>容器一般都会提供begin()、end()成员函数，调用它们就可以得到表示两个端点的迭代器，具体类型最好用auto自动推导，不要过分关心：</p><pre><code>vector&lt;int&gt; v = {1,2,3,4,5};    // vector容器

auto iter1 = v.begin();        // 成员函数获取迭代器，自动类型推导
auto iter2 = v.end();
</code></pre><p>不过，我建议你使用更加通用的全局函数begin()、end()，虽然效果是一样的，但写起来比较方便，看起来也更清楚（另外还有cbegin()、cend()函数，返回的是常量迭代器）：</p><pre><code>auto iter3 = std::begin(v);   // 全局函数获取迭代器，自动类型推导
auto iter4 = std::end(v);
</code></pre><p>迭代器和指针类似，也可以前进和后退，但你不能假设它一定支持“<code>++</code>”“<code>--</code>”操作符，最好也要用函数来操作，常用的有这么几个：</p><ul>
<li>distance()，计算两个迭代器之间的距离；</li>
<li>advance()，前进或者后退N步；</li>
<li>next()/prev()，计算迭代器前后的某个位置。</li>
</ul><p>你可以参考下面的示例代码快速了解它们的作用：</p><pre><code>array&lt;int, 5&gt; arr = {0,1,2,3,4};  // array静态数组容器

auto b = begin(arr);          // 全局函数获取迭代器，首端
auto e = end(arr);            // 全局函数获取迭代器，末端

assert(distance(b, e) == 5);  // 迭代器的距离

auto p = next(b);              // 获取“下一个”位置
assert(distance(b, p) == 1);    // 迭代器的距离
assert(distance(p, b) == -1);  // 反向计算迭代器的距离

advance(p, 2);                // 迭代器前进两个位置，指向元素'3'
assert(*p == 3);
assert(p == prev(e, 2));     // 是末端迭代器的前两个位置
</code></pre><h2>最有用的算法</h2><p>接下来我们就要大量使用各种函数，进入算法的函数式编程领域了。</p><h4>手写循环的替代品</h4><p>首先，我带你来认识一个最基本的算法for_each，它是手写for循环的真正替代品。</p><p>for_each在逻辑和形式上与for循环几乎完全相同：</p><pre><code>vector&lt;int&gt; v = {3,5,1,7,10};   // vector容器

for(const auto&amp; x : v) {        // range for循环
    cout &lt;&lt; x &lt;&lt; &quot;,&quot;;
}

auto print = [](const auto&amp; x)  // 定义一个lambda表达式
{
    cout &lt;&lt; x &lt;&lt; &quot;,&quot;;
};
for_each(cbegin(v), cend(v), print);// for_each算法

for_each(                      // for_each算法，内部定义lambda表达式
    cbegin(v), cend(v),        // 获取常量迭代器
    [](const auto&amp; x)          // 匿名lambda表达式
    {
        cout &lt;&lt; x &lt;&lt; &quot;,&quot;;
    }
);
</code></pre><p>初看上去for_each算法显得有些累赘，既要指定容器的范围，又要写lambda表达式，没有range-for那么简单明了。</p><p>对于很简单的for循环来说，确实是如此，我也不建议你对这么简单的事情用for_each算法。</p><p>但更多的时候，for循环体里会做很多事情，会由if-else、break、continue等语句组成很复杂的逻辑。而单纯的for是“无意义”的，你必须去查看注释或者代码，才能知道它到底做了什么，回想一下曾经被巨大的for循环支配的“恐惧”吧。</p><p>for_each算法的价值就体现在这里，它把要做的事情分成了两部分，也就是两个函数：一个<strong>遍历容器元素</strong>，另一个<strong>操纵容器元素</strong>，而且名字的含义更明确，代码也有更好的封装。</p><p>我自己是很喜欢用for_each算法的，我也建议你尽量多用for_each来替代for，因为它能够促使我们更多地以“函数式编程”来思考，使用lambda来封装逻辑，得到更干净、更安全的代码。</p><h4>排序算法</h4><p>for_each是for的等价替代，还不能完全体现出算法的优越性。但对于“排序”这个计算机科学里的经典问题，你是绝对没有必要自己写for循环的，必须坚决地选择标准算法。</p><p>在求职面试的时候，你也许手写过不少排序算法吧，像选择排序、插入排序、冒泡排序，等等，但标准库里的算法绝对要比你所能写出的任何实现都要好。</p><p>说到排序，你脑海里跳出的第一个词可能就是sort()，它是经典的快排算法，通常用它准没错。</p><pre><code>auto print = [](const auto&amp; x)  // lambda表达式输出元素
{
    cout &lt;&lt; x &lt;&lt; &quot;,&quot;;
};

std::sort(begin(v), end(v));         // 快速排序
for_each(cbegin(v), cend(v), print); // for_each算法
</code></pre><p>不过，排序也有多种不同的应用场景，sort()虽然快，但它是不稳定的，而且是全排所有元素。</p><p>很多时候，这样做的成本比较高，比如TopN、中位数、最大最小值等，我们只关心一部分数据，如果你用sort()，就相当于“杀鸡用牛刀”，是一种浪费。</p><p>C++为此准备了多种不同的算法，不过它们的名字不全叫sort，所以你要认真理解它们的含义。</p><p>我来介绍一些常见问题对应的算法：</p><ul>
<li>要求排序后仍然保持元素的相对顺序，应该用stable_sort，它是稳定的；</li>
<li>选出前几名（TopN），应该用partial_sort；</li>
<li>选出前几名，但不要求再排出名次（BestN），应该用nth_element；</li>
<li>中位数（Median）、百分位数（Percentile），还是用nth_element；</li>
<li>按照某种规则把元素划分成两组，用partition；</li>
<li>第一名和最后一名，用minmax_element。</li>
</ul><p>下面的代码使用vector容器示范了这些算法，注意它们“函数套函数”的形式：</p><pre><code>// top3
std::partial_sort(
    begin(v), next(begin(v), 3), end(v));  // 取前3名

// best3
std::nth_element(
    begin(v), next(begin(v), 3), end(v));  // 最好的3个

// Median
auto mid_iter =                            // 中位数的位置
    next(begin(v), v.size()/2);
std::nth_element( begin(v), mid_iter, end(v));// 排序得到中位数
cout &lt;&lt; &quot;median is &quot; &lt;&lt; *mid_iter &lt;&lt; endl;
    
// partition
auto pos = std::partition(                // 找出所有大于9的数
    begin(v), end(v),
    [](const auto&amp; x)                    // 定义一个lambda表达式
    {
        return x &gt; 9;
    }
); 
for_each(begin(v), pos, print);         // 输出分组后的数据  

// min/max
auto value = std::minmax_element(        //找出第一名和倒数第一
    cbegin(v), cend(v)
);
</code></pre><p>在使用这些排序算法时，还要注意一点，它们对迭代器要求比较高，通常都是随机访问迭代器（minmax_element除外），所以<strong>最好在顺序容器array/vector上调用</strong>。</p><p>如果是list容器，应该调用成员函数sort()，它对链表结构做了特别的优化。有序容器set/map本身就已经排好序了，直接对迭代器做运算就可以得到结果。而对无序容器，则不要调用排序算法，原因你应该不难想到（散列表结构的特殊性质，导致迭代器不满足要求、元素无法交换位置）。</p><h4>查找算法</h4><p>排序算法的目标是让元素有序，这样就可以快速查找，节约时间。</p><p>算法binary_search，顾名思义，就是在已经排好序的区间里执行二分查找。但糟糕的是，它只返回一个bool值，告知元素是否存在，而更多的时候，我们是想定位到那个元素，所以binary_search几乎没什么用。</p><pre><code>vector&lt;int&gt; v = {3,5,1,7,10,99,42};  // vector容器
std::sort(begin(v), end(v));        // 快速排序

auto found = binary_search(         // 二分查找，只能确定元素在不在
    cbegin(v), cend(v), 7
); 
</code></pre><p>想要在已序容器上执行二分查找，要用到一个名字比较怪的算法：lower_bound，它返回第一个“<strong>大于或等于</strong>”值的位置：</p><pre><code>decltype(cend(v)) pos;            // 声明一个迭代器，使用decltype

pos = std::lower_bound(          // 找到第一个&gt;=7的位置
    cbegin(v), cend(v), 7
);  
found = (pos != cend(v)) &amp;&amp; (*pos == 7); // 可能找不到，所以必须要判断
assert(found);                          // 7在容器里

pos = std::lower_bound(               // 找到第一个&gt;=9的位置
    cbegin(v), cend(v), 9
);  
found = (pos != cend(v)) &amp;&amp; (*pos == 9); // 可能找不到，所以必须要判断
assert(!found);                          // 9不在容器里
</code></pre><p>lower_bound的返回值是一个迭代器，所以就要做一点判断工作，才能知道是否真的找到了。判断的条件有两个，一个是迭代器是否有效，另一个是迭代器的值是不是要找的值。</p><p>注意lower_bound的查找条件是“<strong>大于等于</strong>”，而不是“等于”，所以它的真正含义是“大于等于值的第一个位置”。相应的也就有“大于等于值的最后一个位置”，算法叫upper_bound，返回的是第一个“<strong>大于</strong>”值的元素。</p><pre><code>pos = std::upper_bound(             // 找到第一个&gt;9的位置
    cbegin(v), cend(v), 9
);
</code></pre><p>因为这两个算法不是简单的判断相等，作用有点“绕”，不太好掌握，我来给你解释一下。</p><p>它俩的返回值构成一个区间，这个区间往前就是所有比被查找值小的元素，往后就是所有比被查找值大的元素，可以写成一个简单的不等式：</p><pre><code>begin &lt;    x &lt;= lower_bound &lt; upper_bound     &lt; end
</code></pre><p>比如，在刚才的这个例子里，对数字9执行lower_bound和upper_bound，就会返回[10,10]这样的区间。</p><p>对于有序容器set/map，就不需要调用这三个算法了，它们有等价的成员函数find/lower_bound/upper_bound，效果是一样的。</p><p>不过，你要注意find与binary_search不同，它的返回值不是bool而是迭代器，可以参考下面的示例代码：</p><pre><code>multiset&lt;int&gt; s = {3,5,1,7,7,7,10,99,42};  // multiset，允许重复

auto pos = s.find(7);                      // 二分查找，返回迭代器
assert(pos != s.end());                   // 与end()比较才能知道是否找到

auto lower_pos = s.lower_bound(7);       // 获取区间的左端点
auto upper_pos = s.upper_bound(7);       // 获取区间的右端点

for_each(                                // for_each算法
    lower_pos, upper_pos, print          // 输出7,7,7
);
</code></pre><p>除了binary_search、lower_bound和upper_bound，标准库里还有一些查找算法可以用于未排序的容器，虽然肯定没有排序后的二分查找速度快，但也正因为不需要排序，所以适应范围更广。</p><p>这些算法以find和search命名，不过可能是当时制定标准时的疏忽，名称有点混乱，其中用于查找区间的find_first_of/find_end，或许更应该叫作search_first/search_last。</p><p>这几个算法调用形式都是差不多的，用起来也很简单：</p><pre><code>vector&lt;int&gt; v = {1,9,11,3,5,7};  // vector容器

decltype(v.end()) pos;          // 声明一个迭代器，使用decltype

pos = std::find(                 // 查找算法，找到第一个出现的位置
    begin(v), end(v), 3
);  
assert(pos != end(v));         // 与end()比较才能知道是否找到

pos = std::find_if(            // 查找算法，用lambda判断条件
    begin(v), end(v),
    [](auto x) {              // 定义一个lambda表达式
        return x % 2 == 0;    // 判断是否偶数
    }
);  
assert(pos == end(v));        // 与end()比较才能知道是否找到

array&lt;int, 2&gt; arr = {3,5};    // array容器
pos = std::find_first_of(      // 查找一个子区间
    begin(v), end(v),
    begin(arr), end(arr)
);  
assert(pos != end(v));       // 与end()比较才能知道是否找到
</code></pre><h2>小结</h2><p>C++里有上百个算法，我们不可能也没办法在一节课的时间里全部搞懂，所以我就精挑细选了一些我个人认为最有用的for_each、排序和查找算法，把它们介绍给你。</p><p>在我看来，C++里的算法像是一个大宝库，非常值得你去发掘。比如类似memcpy的copy/move算法（搭配插入迭代器）、检查元素的all_of/any_of算法，用好了都可以替代很多手写for循环。</p><p>你可以课后仔细阅读<a href="https://en.cppreference.com/w/cpp/algorithm">标准文档</a>，对照自己的现有代码，看看哪些能用得上，再试着用算法来改写实现，体会一下算法的简洁和高效。</p><p>简单小结一下这次的内容：</p><ol>
<li>算法是专门操作容器的函数，是一种“智能for循环”，它的最佳搭档是lambda表达式；</li>
<li>算法通过迭代器来间接操作容器，使用两个端点指定操作范围，迭代器决定了算法的能力；</li>
<li>for_each算法是for的替代品，以函数式编程替代了面向过程编程；</li>
<li>有多种排序算法，最基本的是sort，但应该根据实际情况选择其他更合适的算法，避免浪费；</li>
<li>在已序容器上可以执行二分查找，应该使用的算法是lower_bound；</li>
<li>list/set/map提供了等价的排序、查找函数，更适应自己的数据结构；</li>
<li>find/search是通用的查找算法，效率不高，但不必排序也能使用。</li>
</ol><p>和上节课一样，我再附送一个小技巧。</p><p>因为标准算法的名字实在是太普通、太常见了，所以建议你一定要显式写出“std::”名字空间限定，这样看起来更加醒目，也避免了无意的名字冲突。</p><h2>课下作业</h2><p>最后是课下作业时间，给你留两个思考题：</p><ol>
<li>你觉得for_each算法能完全替代for循环吗？</li>
<li>试着自己总结归纳一下，这些排序和查找算法在实际开发中应该如何使用。</li>
</ol><p>欢迎你在留言区写下你的思考和答案，如果觉得今天的内容对你有所帮助，也欢迎分享给你的朋友。我们下节课见。</p><p><img src="https://static001.geekbang.org/resource/image/77/d4/77cbcdf7cf05fe7c6fac877649d627d4.jpg" alt=""></p>