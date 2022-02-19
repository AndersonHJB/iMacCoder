<audio title="11 _ this：从JavaScript执行上下文的视角讲清楚this" src="https://static001.geekbang.org/resource/audio/fd/8e/fdeecc9c032154797493f95166d7a58e.mp3" controls="controls"></audio> 
<p>在<a href="https://time.geekbang.org/column/article/127495">上篇文章</a>中，我们讲了词法作用域、作用域链以及闭包，并在最后思考题中留了下面这样一段代码：</p><pre><code>var bar = {
    myName:&quot;time.geekbang.com&quot;,
    printName: function () {
        console.log(myName)
    }    
}
function foo() {
    let myName = &quot;极客时间&quot;
    return bar.printName
}
let myName = &quot;极客邦&quot;
let _printName = foo()
_printName()
bar.printName()
</code></pre><p>相信你已经知道了，在printName函数里面使用的变量myName是属于全局作用域下面的，所以最终打印出来的值都是“极客邦”。这是因为JavaScript语言的作用域链是由词法作用域决定的，而词法作用域是由代码结构来确定的。</p><p>不过按照常理来说，调用<code>bar.printName</code>方法时，该方法内部的变量myName应该使用bar对象中的，因为它们是一个整体，大多数面向对象语言都是这样设计的，比如我用C++改写了上面那段代码，如下所示：</p><pre><code>#include &lt;iostream&gt;
using namespace std;
class Bar{
    public:
    char* myName;
    Bar(){
      myName = &quot;time.geekbang.com&quot;;
    }
    void printName(){
       cout&lt;&lt; myName &lt;&lt;endl;
    }  
} bar;

char* myName = &quot;极客邦&quot;;
int main() {
	bar.printName();
	return 0;
}
</code></pre><p>在这段C++代码中，我同样调用了bar对象中的printName方法，最后打印出来的值就是bar对象的内部变量myName值——“time.geekbang.com”，而并不是最外面定义变量myName的值——“极客邦”，所以<strong>在对象内部的方法中使用对象内部的属性是一个非常普遍的需求</strong>。但是JavaScript的作用域机制并不支持这一点，基于这个需求，JavaScript又搞出来另外一套<strong>this机制</strong>。</p><p>所以，在JavaScript中可以使用this实现在printName函数中访问到bar对象的myName属性了。具体该怎么操作呢？你可以调整printName的代码，如下所示：</p><!-- [[[read_end]]] --><pre><code>printName: function () {
        console.log(this.myName)
    }    
</code></pre><p>接下来咱们就展开来介绍this，不过在讲解之前，希望你能区分清楚<strong>作用域链</strong>和<strong>this</strong>是两套不同的系统，它们之间基本没太多联系。在前期明确这点，可以避免你在学习this的过程中，和作用域产生一些不必要的关联。</p><h2>JavaScript中的this是什么</h2><p>关于this，我们还是得先从执行上下文说起。在前面几篇文章中，我们提到执行上下文中包含了变量环境、词法环境、外部环境，但其实还有一个this没有提及，具体你可以参考下图：</p><p><img src="https://static001.geekbang.org/resource/image/b3/8d/b398610fd8060b381d33afc9b86f988d.png" alt=""></p><center><span class="reference">执行上下文中的this</span></center><p>从图中可以看出，<strong>this是和执行上下文绑定的</strong>，也就是说每个执行上下文中都有一个this。前面<a href="https://time.geekbang.org/column/article/120257">《08 | 调用栈：为什么JavaScript代码会出现栈溢出？》</a>中我们提到过，执行上下文主要分为三种——全局执行上下文、函数执行上下文和eval执行上下文，所以对应的this也只有这三种——全局执行上下文中的this、函数中的this和eval中的this。</p><p>不过由于eval我们使用的不多，所以本文我们对此就不做介绍了，如果你感兴趣的话，可以自行搜索和学习相关知识。</p><p>那么接下来我们就重点讲解下<strong>全局执行上下文中的this</strong>和<strong>函数执行上下文中的this</strong>。</p><h2>全局执行上下文中的this</h2><p>首先我们来看看全局执行上下文中的this是什么。</p><p>你可以在控制台中输入<code>console.log(this)</code>来打印出来全局执行上下文中的this，最终输出的是window对象。所以你可以得出这样一个结论：全局执行上下文中的this是指向window对象的。这也是this和作用域链的唯一交点，作用域链的最底端包含了window对象，全局执行上下文中的this也是指向window对象。</p><h2>函数执行上下文中的this</h2><p>现在你已经知道全局对象中的this是指向window对象了，那么接下来，我们就来重点分析函数执行上下文中的this。还是先看下面这段代码：</p><pre><code>function foo(){
  console.log(this)
}
foo()
</code></pre><p>我们在foo函数内部打印出来this值，执行这段代码，打印出来的也是window对象，这说明在默认情况下调用一个函数，其执行上下文中的this也是指向window对象的。估计你会好奇，那能不能设置执行上下文中的this来指向其他对象呢？答案是肯定的。通常情况下，有下面三种方式来设置函数执行上下文中的this值。</p><h3>1. 通过函数的call方法设置</h3><p>你可以通过函数的<strong>call</strong>方法来设置函数执行上下文的this指向，比如下面这段代码，我们就并没有直接调用foo函数，而是调用了foo的call方法，并将bar对象作为call方法的参数。</p><pre><code>let bar = {
  myName : &quot;极客邦&quot;,
  test1 : 1
}
function foo(){
  this.myName = &quot;极客时间&quot;
}
foo.call(bar)
console.log(bar)
console.log(myName)
</code></pre><p>执行这段代码，然后观察输出结果，你就能发现foo函数内部的this已经指向了bar对象，因为通过打印bar对象，可以看出bar的myName属性已经由“极客邦”变为“极客时间”了，同时在全局执行上下文中打印myName，JavaScript引擎提示该变量未定义。</p><p>其实除了call方法，你还可以使用<strong>bind</strong>和<strong>apply</strong>方法来设置函数执行上下文中的this，它们在使用上还是有一些区别的，如果感兴趣你可以自行搜索和学习它们的使用方法，这里我就不再赘述了。</p><h3>2. 通过对象调用方法设置</h3><p>要改变函数执行上下文中的this指向，除了通过函数的call方法来实现外，还可以通过对象调用的方式，比如下面这段代码：</p><pre><code>var myObj = {
  name : &quot;极客时间&quot;, 
  showThis: function(){
    console.log(this)
  }
}
myObj.showThis()
</code></pre><p>在这段代码中，我们定义了一个myObj对象，该对象是由一个name属性和一个showThis方法组成的，然后再通过myObj对象来调用showThis方法。执行这段代码，你可以看到，最终输出的this值是指向myObj的。</p><p>所以，你可以得出这样的结论：<strong>使用对象来调用其内部的一个方法，该方法的this是指向对象本身的</strong>。</p><p>其实，你也可以认为JavaScript引擎在执行<code>myObject.showThis()</code>时，将其转化为了：</p><pre><code>myObj.showThis.call(myObj)
</code></pre><p>接下来我们稍微改变下调用方式，把showThis赋给一个全局对象，然后再调用该对象，代码如下所示：</p><pre><code>var myObj = {
  name : &quot;极客时间&quot;,
  showThis: function(){
    this.name = &quot;极客邦&quot;
    console.log(this)
  }
}
var foo = myObj.showThis
foo()
</code></pre><p>执行这段代码，你会发现this又指向了全局window对象。</p><p>所以通过以上两个例子的对比，你可以得出下面这样两个结论：</p><ul>
<li><strong>在全局环境中调用一个函数，函数内部的this指向的是全局变量window。</strong></li>
<li><strong>通过一个对象来调用其内部的一个方法，该方法的执行上下文中的this指向对象本身。</strong></li>
</ul><h3>3. 通过构造函数中设置</h3><p>你可以像这样设置构造函数中的this，如下面的示例代码：</p><pre><code>function CreateObj(){
  this.name = &quot;极客时间&quot;
}
var myObj = new CreateObj()
</code></pre><p>在这段代码中，我们使用new创建了对象myObj，那你知道此时的构造函数CreateObj中的this到底指向了谁吗？</p><p>其实，当执行new CreateObj()的时候，JavaScript引擎做了如下四件事：</p><ul>
<li>首先创建了一个空对象tempObj；</li>
<li>接着调用CreateObj.call方法，并将tempObj作为call方法的参数，这样当CreateObj的执行上下文创建时，它的this就指向了tempObj对象；</li>
<li>然后执行CreateObj函数，此时的CreateObj函数执行上下文中的this指向了tempObj对象；</li>
<li>最后返回tempObj对象。</li>
</ul><p>为了直观理解，我们可以用代码来演示下：</p><pre><code>  var tempObj = {}
  CreateObj.call(tempObj)
  return tempObj
</code></pre><p>这样，我们就通过new关键字构建好了一个新对象，并且构造函数中的this其实就是新对象本身。</p><p>关于new的具体细节你可以参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new">这篇文章</a>，这里我就不做过多介绍了。</p><h2>this的设计缺陷以及应对方案</h2><p>就我个人而言，this并不是一个很好的设计，因为它的很多使用方法都冲击人的直觉，在使用过程中存在着非常多的坑。下面咱们就来一起看看那些this设计缺陷。</p><h3>1. 嵌套函数中的this不会从外层函数中继承</h3><p>我认为这是一个严重的设计错误，并影响了后来的很多开发者，让他们“前赴后继”迷失在该错误中。我们还是结合下面这样一段代码来分析下：</p><pre><code>var myObj = {
  name : &quot;极客时间&quot;, 
  showThis: function(){
    console.log(this)
    function bar(){console.log(this)}
    bar()
  }
}
myObj.showThis()
</code></pre><p>我们在这段代码的showThis方法里面添加了一个bar方法，然后接着在showThis函数中调用了bar函数，那么现在的问题是：bar函数中的this是什么？</p><p>如果你是刚接触JavaScript，那么你可能会很自然地觉得，bar中的this应该和其外层showThis函数中的this是一致的，都是指向myObj对象的，这很符合人的直觉。但实际情况却并非如此，执行这段代码后，你会发现<strong>函数bar中的this指向的是全局window对象，而函数showThis中的this指向的是myObj对象</strong>。这就是JavaScript中非常容易让人迷惑的地方之一，也是很多问题的源头。</p><p><strong>你可以通过一个小技巧来解决这个问题</strong>，比如在showThis函数中<strong>声明一个变量self用来保存this</strong>，然后在bar函数中使用self，代码如下所示：</p><pre><code>var myObj = {
  name : &quot;极客时间&quot;, 
  showThis: function(){
    console.log(this)
    var self = this
    function bar(){
      self.name = &quot;极客邦&quot;
    }
    bar()
  }
}
myObj.showThis()
console.log(myObj.name)
console.log(window.name)
</code></pre><p>执行这段代码，你可以看到它输出了我们想要的结果，最终myObj中的name属性值变成了“极客邦”。其实，这个方法的的本质是<strong>把this体系转换为了作用域的体系</strong>。</p><p>其实，<strong>你也可以使用ES6中的箭头函数来解决这个问题</strong>，结合下面代码：</p><pre><code>var myObj = {
  name : &quot;极客时间&quot;, 
  showThis: function(){
    console.log(this)
    var bar = ()=&gt;{
      this.name = &quot;极客邦&quot;
      console.log(this)
    }
    bar()
  }
}
myObj.showThis()
console.log(myObj.name)
console.log(window.name)
</code></pre><p>执行这段代码，你会发现它也输出了我们想要的结果，也就是箭头函数bar里面的this是指向myObj对象的。这是因为ES6中的箭头函数并不会创建其自身的执行上下文，所以箭头函数中的this取决于它的外部函数。</p><p>通过上面的讲解，你现在应该知道了this没有作用域的限制，这点和变量不一样，所以嵌套函数不会从调用它的函数中继承this，这样会造成很多不符合直觉的代码。要解决这个问题，你可以有两种思路：</p><ul>
<li>第一种是把this保存为一个self变量，再利用变量的作用域机制传递给嵌套函数。</li>
<li>第二种是继续使用this，但是要把嵌套函数改为箭头函数，因为箭头函数没有自己的执行上下文，所以它会继承调用函数中的this。</li>
</ul><h3>2. 普通函数中的this默认指向全局对象window</h3><p>上面我们已经介绍过了，在默认情况下调用一个函数，其执行上下文中的this是默认指向全局对象window的。</p><p>不过这个设计也是一种缺陷，因为在实际工作中，我们并不希望函数执行上下文中的this默认指向全局对象，因为这样会打破数据的边界，造成一些误操作。如果要让函数执行上下文中的this指向某个对象，最好的方式是通过call方法来显示调用。</p><p>这个问题可以通过设置JavaScript的“严格模式”来解决。在严格模式下，默认执行一个函数，其函数的执行上下文中的this值是undefined，这就解决上面的问题了。</p><h2>总结</h2><p>好了，今天就到这里，下面我们来回顾下今天的内容。</p><p>首先，在使用this时，为了避坑，你要谨记以下三点：</p><ol>
<li>当函数作为对象的方法调用时，函数中的this就是该对象；</li>
<li>当函数被正常调用时，在严格模式下，this值是undefined，非严格模式下this指向的是全局对象window；</li>
<li>嵌套函数中的this不会继承外层函数的this值。</li>
</ol><p>最后，我们还提了一下箭头函数，因为箭头函数没有自己的执行上下文，所以箭头函数的this就是它外层函数的this。</p><p>这是我们“JavaScript执行机制”模块的最后一节了，五节下来，你应该已经发现我们将近一半的时间都是在谈JavaScript的各种缺陷，比如变量提升带来的问题、this带来问题等。我认为了解一门语言的缺陷并不是为了否定它，相反是为了能更加深入地了解它。我们在谈论缺陷的过程中，还结合JavaScript的工作流程分析了出现这些缺陷的原因，以及避开这些缺陷的方法。掌握了这些，相信你今后在使用JavaScript的过程中会更加得心应手。</p><h2>思考时间</h2><p>你可以观察下面这段代码：</p><pre><code>let userInfo = {
  name:&quot;jack.ma&quot;,
  age:13,
  sex:male,
  updateInfo:function(){
    //模拟xmlhttprequest请求延时
    setTimeout(function(){
      this.name = &quot;pony.ma&quot;
      this.age = 39
      this.sex = female
    },100)
  }
}

userInfo.updateInfo()
</code></pre><p>我想通过updateInfo来更新userInfo里面的数据信息，但是这段代码存在一些问题，你能修复这段代码吗？</p><p>欢迎在留言区与我分享你的想法，也欢迎你在留言区记录你的思考过程。感谢阅读，如果你觉得这篇文章对你有帮助的话，也欢迎把它分享给更多的朋友。</p><p></p>