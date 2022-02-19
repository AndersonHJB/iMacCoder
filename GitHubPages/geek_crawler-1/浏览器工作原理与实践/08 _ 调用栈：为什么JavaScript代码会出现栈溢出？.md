<audio title="08 _ 调用栈：为什么JavaScript代码会出现栈溢出？" src="https://static001.geekbang.org/resource/audio/10/6c/104e80fb5fe18eb956a5a81f6843ff6c.mp3" controls="controls"></audio> 
<p>在<a href="https://time.geekbang.org/column/article/119046">上篇文章</a>中，我们讲到了，当一段代码被执行时，JavaScript引擎先会对其进行编译，并创建执行上下文。但是并没有明确说明到底什么样的代码才算符合规范。</p><p>那么接下来我们就来明确下，哪些情况下代码才算是“一段”代码，才会在执行之前就进行编译并创建执行上下文。一般说来，有这么三种情况：</p><ol>
<li>当JavaScript执行全局代码的时候，会编译全局代码并创建全局执行上下文，而且在整个页面的生存周期内，全局执行上下文只有一份。</li>
<li>当调用一个函数的时候，函数体内的代码会被编译，并创建函数执行上下文，一般情况下，函数执行结束之后，创建的函数执行上下文会被销毁。</li>
<li>当使用eval函数的时候，eval的代码也会被编译，并创建执行上下文。</li>
</ol><p>好了，又进一步理解了执行上下文，那本节我们就在这基础之上继续深入，一起聊聊<strong>调用栈</strong>。学习调用栈至少有以下三点好处：</p><ol>
<li>可以帮助你了解JavaScript引擎背后的工作原理；</li>
<li>让你有调试JavaScript代码的能力；</li>
<li>帮助你搞定面试，因为面试过程中，调用栈也是出境率非常高的题目。</li>
</ol><p>比如你在写JavaScript代码的时候，有时候可能会遇到栈溢出的错误，如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/0c/70/0c9e2c4f7ee8ca59cfa99a6f51510470.png" alt=""></p><center><span class="reference">栈溢出的错误</span></center><p>那为什么会出现这种错误呢？这就涉及到了<strong>调用栈</strong>的内容。你应该知道JavaScript中有很多函数，经常会出现在一个函数中调用另外一个函数的情况，<strong>调用栈就是用来管理函数调用关系的一种数据结构</strong>。因此要讲清楚调用栈，你还要先弄明白<strong>函数调用</strong>和<strong>栈结构</strong>。</p><!-- [[[read_end]]] --><h2>什么是函数调用</h2><p>函数调用就是运行一个函数，具体使用方式是使用函数名称跟着一对小括号。下面我们看个简单的示例代码：</p><pre><code>var a = 2
function add(){
var b = 10
return  a+b
}
add()
</code></pre><p>这段代码很简单，先是创建了一个add函数，接着在代码的最下面又调用了该函数。</p><p>那么下面我们就利用这段简单的代码来解释下函数调用的过程。</p><p>在执行到函数add()之前，JavaScript引擎会为上面这段代码创建全局执行上下文，包含了声明的函数和变量，你可以参考下图：</p><p><img src="https://static001.geekbang.org/resource/image/7f/da/7fa2ed18e702861890d767ea547533da.png" alt=""></p><center><span class="reference">全局执行上下文</span></center><p>从图中可以看出，代码中全局变量和函数都保存在全局上下文的变量环境中。</p><p>执行上下文准备好之后，便开始执行全局代码，当执行到add这儿时，JavaScript判断这是一个函数调用，那么将执行以下操作：</p><ul>
<li>首先，从<strong>全局执行上下文</strong>中，取出add函数代码。</li>
<li>其次，对add函数的这段代码进行编译，并创建<strong>该函数的执行上下文</strong>和<strong>可执行代码</strong>。</li>
<li>最后，执行代码，输出结果。</li>
</ul><p>完整流程你可以参考下图：</p><p><img src="https://static001.geekbang.org/resource/image/53/ca/537efd9e96771dc50737117e615533ca.png" alt=""></p><center><span class="reference">函数调用过程</span></center><p>就这样，当执行到add函数的时候，我们就有了两个执行上下文了——全局执行上下文和add函数的执行上下文。</p><p>也就是说在执行JavaScript时，可能会存在多个执行上下文，那么JavaScript引擎是如何管理这些执行上下文的呢？</p><p>答案是<strong>通过一种叫栈的数据结构来管理的</strong>。那什么是栈呢？它又是如何管理这些执行上下文呢？</p><h2>什么是栈</h2><p>关于栈，你可以结合这么一个贴切的例子来理解，一条单车道的单行线，一端被堵住了，而另一端入口处没有任何提示信息，堵住之后就只能后进去的车子先出来，这时这个堵住的单行线就可以被看作是一个<strong>栈容器</strong>，车子开进单行线的操作叫做<strong>入栈</strong>，车子倒出去的操作叫做<strong>出栈</strong>。</p><p>在车流量较大的场景中，就会发生反复的入栈、栈满、出栈、空栈和再次入栈，一直循环。</p><p>所以，栈就是类似于一端被堵住的单行线，车子类似于栈中的元素，栈中的元素满足<strong>后进先出</strong>的特点。你可以参看下图：</p><p><img src="https://static001.geekbang.org/resource/image/5e/05/5e2bb65019053abfd5e7710e41d1b405.png" alt=""></p><center><span class="reference">栈示意图</span></center><h2>什么是JavaScript的调用栈</h2><p>JavaScript引擎正是利用栈的这种结构来管理执行上下文的。在执行上下文创建好后，JavaScript引擎会将执行上下文压入栈中，通常把这种用来管理执行上下文的栈称为<strong>执行上下文栈</strong>，又称<strong>调用栈</strong>。</p><p>为便于你更好地理解调用栈，下面我们再来看段稍微复杂点的示例代码：</p><pre><code>var a = 2
function add(b,c){
  return b+c
}
function addAll(b,c){
var d = 10
result = add(b,c)
return  a+result+d
}
addAll(3,6)
</code></pre><p>在上面这段代码中，你可以看到它是在addAll函数中调用了add函数，那在整个代码的执行过程中，调用栈是怎么变化的呢？</p><p>下面我们就一步步地分析在代码的执行过程中，调用栈的状态变化情况。</p><p><strong>第一步，创建全局上下文，并将其压入栈底</strong>。如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/a5/1d/a5d7ec1f8f296412acc045835b85431d.png" alt=""></p><center><span class="reference">全局执行上下文压栈</span></center><p>从图中你也可以看出，变量a、函数add和addAll都保存到了全局上下文的变量环境对象中。</p><p>全局执行上下文压入到调用栈后，JavaScript引擎便开始执行全局代码了。首先会执行a=2的赋值操作，执行该语句会将全局上下文变量环境中a的值设置为2。设置后的全局上下文的状态如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/1d/1d/1d50269dbc5b4c69f83662ecdd977b1d.png" alt=""></p><center><span class="reference">赋值操作改变执行上下文中的值</span></center><p>接下来，<strong>第二步是调用addAll函数</strong>。当调用该函数时，JavaScript引擎会编译该函数，并为其创建一个执行上下文，最后还将该函数的执行上下文压入栈中，如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/7d/52/7d6c4c45db4ef9b900678092e6c53652.png" alt=""></p><center><span class="reference">执行addAll函数时的调用栈</span></center><p>addAll函数的执行上下文创建好之后，便进入了函数代码的执行阶段了，这里先执行的是d=10的赋值操作，执行语句会将addAll函数执行上下文中的d由undefined变成了10。</p><p>然后接着往下执行，<strong>第三步，当执行到add函数</strong>调用语句时，同样会为其创建执行上下文，并将其压入调用栈，如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/cc/37/ccfe41d906040031a7df1e4f1bce5837.png" alt=""></p><center><span class="reference">执行add函数时的调用栈</span></center><p>当add函数返回时，该函数的执行上下文就会从栈顶弹出，并将result的值设置为add函数的返回值，也就是9。如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/03/96/03ca801a5372f941bf17d6088fee0f96.png" alt=""></p><center><span class="reference">add函数执行结束时的调用栈</span></center><p>紧接着addAll执行最后一个相加操作后并返回，addAll的执行上下文也会从栈顶部弹出，此时调用栈中就只剩下全局上下文了。最终如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/d0/7b/d0ac1d6e77735338fa97cc9a3f6c717b.png" alt=""></p><center><span class="reference">addAll函数执行结束时的调用栈</span></center><p>至此，整个JavaScript流程执行结束了。</p><p>好了，现在你应该知道了<strong>调用栈是JavaScript引擎追踪函数执行的一个机制</strong>，当一次有多个函数被调用时，通过调用栈就能够追踪到哪个函数正在被执行以及各函数之间的调用关系。</p><h2>在开发中，如何利用好调用栈</h2><p>鉴于调用栈的重要性和实用性，那么接下来我们就一起来看看在实际工作中，应该如何查看和利用好调用栈。</p><h3>1. 如何利用浏览器查看调用栈的信息</h3><p>当你执行一段复杂的代码时，你可能很难从代码文件中分析其调用关系，这时候你可以在你想要查看的函数中加入断点，然后当执行到该函数时，就可以查看该函数的调用栈了。</p><p>这么说可能有点抽象，这里我们拿上面的那段代码做个演示，你可以打开“开发者工具”，点击“Source”标签，选择JavaScript代码的页面，然后在第3行加上断点，并刷新页面。你可以看到执行到add函数时，执行流程就暂停了，这时可以通过右边“call stack”来查看当前的调用栈的情况，如下图：</p><p><img src="https://static001.geekbang.org/resource/image/c0/a2/c0d303a289a535b87a6c445ba7f34fa2.png" alt=""></p><center><span class="reference">查看函数调用关系</span></center><p>从图中可以看出，右边的“call stack”下面显示出来了函数的调用关系：栈的最底部是anonymous，也就是全局的函数入口；中间是addAll函数；顶部是add函数。这就清晰地反映了函数的调用关系，所以<strong>在分析复杂结构代码，或者检查Bug时，调用栈都是非常有用的</strong>。</p><p>除了通过断点来查看调用栈，你还可以使用console.trace()来输出当前的函数调用关系，比如在示例代码中的add函数里面加上了console.trace()，你就可以看到控制台输出的结果，如下图：</p><p><img src="https://static001.geekbang.org/resource/image/ab/ce/abfba06cd23a7704a6eb148cff443ece.png" alt=""></p><center><span class="reference">使用trace函数输出当前调用栈信息</span></center><h3>2. 栈溢出（Stack Overflow）</h3><p>现在你知道了调用栈是一种用来管理执行上下文的数据结构，符合后进先出的规则。不过还有一点你要注意，<strong>调用栈是有大小的</strong>，当入栈的执行上下文超过一定数目，JavaScript引擎就会报错，我们把这种错误叫做<strong>栈溢出</strong>。</p><p>特别是在你写递归代码的时候，就很容易出现栈溢出的情况。比如下面这段代码：</p><pre><code>function division(a,b){
    return division(a,b)
}
console.log(division(1,2))
</code></pre><p>当执行时，就会抛出栈溢出错误，如下图：</p><p><img src="https://static001.geekbang.org/resource/image/b4/4d/b4f7196077d9ef4eac1ca6a279f2054d.png" alt=""></p><center><span class="reference">栈溢出错误</span></center><p>从上图你可以看到，抛出的错误信息为：超过了最大栈调用大小（Maximum call stack size exceeded）。</p><p>那为什么会出现这个问题呢？这是因为当JavaScript引擎开始执行这段代码时，它首先调用函数division，并创建执行上下文，压入栈中；然而，这个函数是<strong>递归的，并且没有任何终止条件</strong>，所以它会一直创建新的函数执行上下文，并反复将其压入栈中，但栈是有容量限制的，超过最大数量后就会出现栈溢出的错误。</p><p>理解了栈溢出原因后，你就可以使用一些方法来避免或者解决栈溢出的问题，比如把递归调用的形式改造成其他形式，或者使用加入定时器的方法来把当前任务拆分为其他很多小任务。</p><h2>总结</h2><p>好了，今天的内容就讲到这里，下面来总结下今天的内容。</p><ul>
<li>每调用一个函数，JavaScript引擎会为其创建执行上下文，并把该执行上下文压入调用栈，然后JavaScript引擎开始执行函数代码。</li>
<li>如果在一个函数A中调用了另外一个函数B，那么JavaScript引擎会为B函数创建执行上下文，并将B函数的执行上下文压入栈顶。</li>
<li>当前函数执行完毕后，JavaScript引擎会将该函数的执行上下文弹出栈。</li>
<li>当分配的调用栈空间被占满时，会引发“堆栈溢出”问题。</li>
</ul><p>栈是一种非常重要的数据结构，不光应用在JavaScript语言中，其他的编程语言，如C/C++、Java、Python等语言，在执行过程中也都使用了栈来管理函数之间的调用关系。所以栈是非常基础且重要的知识点，你必须得掌握。</p><h2>思考时间</h2><p>最后，我给你留个思考题，你可以看下面这段代码：</p><pre><code>function runStack (n) {
  if (n === 0) return 100;
  return runStack( n- 2);
}
runStack(50000)
</code></pre><p>这是一段递归代码，可以通过传入参数n，让代码递归执行n次，也就意味着调用栈的深度能达到n，当输入一个较大的数时，比如50000，就会出现栈溢出的问题，那么你能优化下这段代码，以解决栈溢出的问题吗？</p><p>欢迎在留言区与我分享你的想法，也欢迎你在留言区记录你的思考过程。感谢阅读，如果你觉得这篇文章对你有帮助的话，也欢迎把它分享给更多的朋友。</p><p></p>