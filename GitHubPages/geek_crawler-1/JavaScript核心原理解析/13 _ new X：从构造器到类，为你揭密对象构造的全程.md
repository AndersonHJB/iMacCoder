<audio title="13 _ new X：从构造器到类，为你揭密对象构造的全程" src="https://static001.geekbang.org/resource/audio/af/86/afd99eaefdac81619b6f77a3ceb9cd86.mp3" controls="controls"></audio> 
<p>你好，我是周爱民。</p><p>今天我只跟你聊一件事，就是JavaScript构造器。标题中的这行代码中规中矩，是我这个专栏题目列表中难得的正经代码。</p><blockquote>
<p>NOTE：需要稍加说明的是：这行代码在JavaScript 1.x的某些版本或具体实现中是不能使用的。即使ECMAScript ed1开始就将它作为标准语法之一，当时也还是有许多语言并不支持它。</p>
</blockquote><p><strong>构造器</strong>这个东西，是JavaScript中面向对象系统的核心概念之一。跟“属性”相比，如果属性是静态的结构，那么“构造器”就是动态的逻辑。</p><p>没有构造器的JavaScript，就是一个充填了无数数据的、静态的对象空间。这些对象之间既没有关联，也不能衍生，更不可能发生交互。然而，这却真的就是JavaScript 1.0那个时代的所谓“面向对象系统”的基本面貌。</p><h2>基于对象的JavaScript</h2><p>为什么呢？因为JavaScript1.0的时代，也就是最早最早的JavaScript其实是没有继承的。</p><p>你可能会说，既然是没有继承的，那么JavaScript为什么一开始就能声称自己是“面向对象”的、“类似Java”的一门语言呢？其实这个讲法是前半句对，后半句不对。JavaScript和Java名字相似，但语言特性却大是不同，这就跟北京的“海淀五路居”和“五路居”一样，差了得有20公里。</p><!-- [[[read_end]]] --><p>那前半句为什么是对的呢？JavaScript 1.0连继承都没有，为什么又能称为面向对象的语言呢？</p><p>其实从我在前两讲中讲过的内容来看，JavaScript 1.0确实已经可以将函数作为构造器，并且在函数中向它的实例（也就是<code>this</code>对象）抄写类声明的那些属性。在早期的面向对象理论里面，就已经可以称这个函数为<strong>类</strong>，而这个被创建出来的实例为<strong>对象</strong>了。</p><p>所以，有了类、对象，以及一个约定的构造过程，有了这三个东西，JavaScript就声称了自己是一门“面向对象”的语言，并且还是一门“有类语言”。</p><p>所以JavaScript从1.0开始就有类，在这个类（也就是构造器）中采用的是所谓“类抄写”的方案，将类所拥有的属性声明一项一项地抄写到对象上面，而这个对象，就是我们现在大家都知道的this引用。</p><p>这样一来，一段声明类和构造对象的代码，大概写出来就是下面这个样子，在一个函数里面不停地向this对象写属性，最后再用new运算符来创建一下它的实例就好了。</p><pre><code>function Car() {
  this.name = &quot;Car&quot;;
  this.color = &quot;Red&quot;;
}

var x = new Car();
...
</code></pre><h2>类与构造器</h2><p>由于在这样的构造过程中，<code>this</code>是作为<code>new</code>运算所构造出来的那个实例来使用的，因此JavaScript 1.0约定全局环境中不能使用<code>this</code>的。因为全局环境与<code>new</code>运算无关，全局环境中也并不存在一个被<code>new</code>创建出来的实例。</p><p>然而随着<code>JavaScript 1.1</code>的到来，JavaScript支持“原型继承”了，于是“类抄写”成为了一个过时的方案。对于继承性来说，它显得无用；对于一个具体的实例来说，它又具有“类‘说明了’实例的结构”这样的语义。</p><p>因此，从“<strong>原型继承</strong>”在JavaScript中出现的第一天开始，“类继承VS原型继承”之间就存在不可调和的矛盾。在<code>JavaScript 1.1</code>中，类抄写是可以与原型继承混合使用的。</p><p>例如，你可以用类抄写的方式写一个Device()类，然后再写一个Car()类，最后你可以将Car()类的原型指向Device。这一切都是合理的、正常的写法。</p><pre><code>function Device() {
  this.id = 0; // or increment
}

function Car() {
  this.name = &quot;Car&quot;;
  this.color = &quot;Red&quot;;
}

Car.prototype = new Device();

var x = new Car();
console.log(x.id); //
</code></pre><p>于是现在，你可以用new运算来创建子类Car()的实例了，例如按照以前的习惯，我们称这个实例为x，这也仍然没有问题。</p><p>但是在面向对象编程（OOP）中，<code>x</code>既是<code>Car()</code>的子类实例，也是“Device()”的子类实例，这是OOP的继承性所约定的基本概念。这正是这门语言很有趣的地方：<strong>一方面使用了类继承的基础结构和概念，另一方面又要实现原型继承和基于原型链检查的逻辑。</strong>例如，你用<code>x instanceof Device</code>这样的代码来检查一下，看看“<code>x</code>是不是<code>Device()</code>的子类实例”。</p><pre><code># `x`是`Device()`的子类实例吗？
&gt; x instanceof Device
true
</code></pre><p>于是，这里的<code>instanceof</code>运算被实现为一个<strong>动态地访问原型链</strong>的过程：它将从<code>Car.prototype</code>属性逆向地在原型链中查到你指定的——“原型”。</p><p>首先，JavaScript从对象<code>x</code>的内部结构中取得它的原型。这个原型的存在，与<code>new</code>运算是直接相关的——在早期的JavaScript中，有且仅有<code>new</code>运算会向对象内部写“原型”这个属性（称为"[[Prototype]]"内部槽）。由于new运算是依据它运算时所使用的构造器来填写这个属性的，所以这意味着它在实际实现时，将Car.prototype这个值，直接给填到x对象的内部属性去了。</p><pre><code>// x = new Car()
x.[[Prototype]] === Car.prototype
</code></pre><p>在<code>instanceof</code>运算中，<code>x instanceof AClass</code>表达式的右侧是一个类名（对于之前的例子来说，它指向构造器Car），但实际上JavaScript是使用<code>AClass.prototype</code>来做比对的，对于“Car()构造器”来说，就是“Car.prototype”。但是，如果上一个例子需要检查的是<code>x instanceof Device</code>，也就是“Device.prototype”，那么这二者显然是不等值的。</p><p>所以，<code>instanceof</code>运算会再次取“x.[[Prototype] [[Prototype]]”这个内部原型，也就是顺着原型链向上查找，并且你将找到一个等值于“x的内部原型”的东西。</p><pre><code>// 因为
x.[[Prototype]] === Car.prototype
// 且
Car.prototype = new Device()

// 所以
x.[[Prototype]].[[Prototype]] === Device.prototype
</code></pre><p>现在，由于在<code>x</code>的原型链上发现了“x instanceof Device”运算右侧的“Device.prototype”，所以这个表达式将返回True值，表明：</p><p><span class="orange">对象<code>x</code>是<code>Device()</code>或其子类的一个实例。</span></p><p>现在，对于大多数JavaScript程序员来说，上述过程应该都不是秘密，也并不是特别难解的核心技术。但是在它的实现过程中所带有的语言设计方面的这些历史痕迹，却不是那么容易一望即知的了。</p><h2>ECMAScript 6之后的类</h2><p>在ECMAScript 6之前，JavaScript中的<strong>函数</strong>、<strong>类</strong>和<strong>构造器</strong>这三个概念是混用的。一般来说，它们都被统一为“<strong>函数Car()</strong>”这个基础概念，而当它用作“x = new Car()”这样的运算，或从<code>x.constructor</code>这样的属性中读取时，它被理解为<strong>构造器</strong>；当它用作“x instanceof Car”这样的运算，或者讨论OOP的继承关系时，它被理解为<strong>类</strong>。</p><p>习惯上，如果程序要显式地、字面风格地说明一个函数是构造器、或者用作构造过程，那么它的函数名应该首字母大写。同时，如果一个函数要被明确声明为“静态类（也就不需要创建实例的类，例如Math）”，那么它的函数名也应该首字母大写。</p><blockquote>
<p>NOTE: 仅从函数名的大小写来判断，只是惯例。没有任何方法来确认一个函数是不是“被设计为”构造器，或者静态类，又或者“事实上”是不是二者之一。</p>
</blockquote><p>从ECMAScript 6开始，JavaScript有了使用<code>class</code>来声明“类”的语法。例如：</p><pre><code>class AClass {
  ...
}
</code></pre><p>自此之后，JavaScript的“类”与“函数”有了明确的区别：<strong>类只能用new运算来创建，而不能使用“()”来做函数调用。</strong>例如：</p><pre><code>&gt; new AClass()
AClass {}

&gt; AClass()
TypeError: Class constructor AClass cannot be invoked without 'new'
</code></pre><p>如果你尝试将“ES6的类”作为函数调用，那么JavaScript就会抛出一个异常。</p><p>在ECMAScript 6之后，JavaScript内部是明确区分方法与函数的：不能对方法做new运算。如果你尝试这样做，JavaScript也会抛一个异常出来，提示你“这个函数不是一个构造器（is not a constructor）”。例如：</p><pre><code># 声明一个带有方法的对象字面量
&gt; obj = { foo() {} }
{ foo: [Function: foo] }

# 对方法使用new运算会导致异常
&gt; new obj.foo()
TypeError: obj.foo is not a constructor
</code></pre><p>注意这个异常中又出现了关键字“constructor”。这让我们的讨论又一次回到了开始的话题：<strong>什么是构造器？</strong></p><p>在ECMAScript 6之后，函数可以简单地分为三个大类：</p><ol>
<li>类：只可以做new运算；</li>
<li>方法：只可以做调用“( )”运算；</li>
<li>一般函数：（除部分函数有特殊限制外，）同时可以做new和调用运算。</li>
</ol><p>其中，典型的“方法”在内部声明时，有三个主要特征：</p><ol>
<li>具有一个名为“主对象<code>[[HomeObject]]</code>”的内部槽；</li>
<li>没有名为“构造器<code>[[Construct]]</code>”的内部槽；</li>
<li>没有名为“<code>prototype</code>”的属性。</li>
</ol><p>后两种特征（没有<code>[[Construct]]</code>内部槽和<code>prototype</code>属性）完全排除了一个普通方法用作构造器的可能。对照来看，所谓“类”其实也是作为方法来创建的，但它有独立的构造过程和原型属性。</p><p>函数的“.prototype”的属性描述符中的设置比较特殊，它不能删除，但可以修改（‘writable’ is true）。当这个值被修改成null值时，它的子类对象是以null值为原型的；当它被修改成非对象值时，它的子类对象是以Object.prototype为原型的；否则，当它是一个对象类型的值时，它的子类才会使用该对象作为原型来创建实例。</p><p>运算符“new”总是依照这一规则来创建对象实例<code>this</code>。</p><p>不过，对于“类”和一般的“构造器（函数）”，这个创建过程会略有不同。</p><h2>创建<code>this</code>的顺序问题</h2><p>如前所述，如果对ECMAScript 6之前的构造器函数（例如<code>f</code>）使用<code>new</code>运算，那么这个new运算会使用<code>f.prototype</code>作为原型来创建一个<code>this</code>对象，然后才是调用<code>f()</code>函数，并将这个函数的执行过程理解为“类抄写（向用户实例抄写类所声明的属性）”。从用户代码的视角上来看，这个新对象就是由当前<code>new</code>运算所操作的那个函数<code>f()</code>创建的。</p><p>这在语义上非常简洁明了：由于<code>f()</code>是this的类，因此<code>f.prototype</code>决定了this的原型，而<code>f()</code>执行过程决定了初始化this实例的方式。但是它带来了一个问题，一个从JavaScript 1.1开始至今都困扰JavaScript程序员的问题：</p><p><span class="orange">无法创建一个有特殊性质的对象，也无法声明一个具有这类特殊性质的类。</span></p><p>这是什么意思呢？比如说，所有的函数有一个公共的父类/祖先类，称为<code>Function()</code>。所以你可以用<code>new Function()</code>来创建一个普通函数，这个普通函数也是可以调用的，在JavaScript中这是很正常的用法，例如：</p><pre><code>&gt; f = new Function;

&gt; f instanceof Function
true

&gt; f()
undefine
</code></pre><p>接下来，你也确实可以用传统方法写一个<code>Function()</code>的子类，但这样的子类创建的实例就不能调用。例如：</p><pre><code>&gt; MyFunction = function() {};

&gt; MyFunction.prototype = new Function;

&gt; f = new MyFunction;

&gt; [f instanceof MyFunction, f instanceof Function]
[ true, true ]

&gt; f()
TypeError: f is not a funct
</code></pre><p>至于原因，你可能也已经知道了：JavaScript所谓的函数，其实是“一个有<code>[[Call]]</code>内部槽的对象”。而<code>Function()</code>作为JavaScript原生的函数构造器，它能够在创建的对象（例如<code>this</code>）中添加这个内部槽，而当使用上面的继承逻辑时，用户代码（例如<code>MyFunction()</code>）就只是创建了一个普通的对象，因为用户代码没有能力操作JavaScript引擎层面才支持的那些“内部槽”。</p><p>所以，有一些“类/构造器”在ECMAScript 6之前是不能派生子类的，例如Function，又例如Date。</p><p>而到了ECMAScript 6，它的“类声明”采用了不同的构造逻辑。ECMAScript 6要求所有子类的构造过程都不得创建这个<code>this</code>实例，并主动的把这个创建的权力“交还”给父类、乃至祖先类。这也就是ECMAScript 6中类的两个著名特性的由来，即，如果类声明中通过extends指定了父类，那么：</p><ol>
<li>必须在构造器方法（constructor）中显式地使用<code>super()</code>来调用父类的构造过程；</li>
<li>在上述调用结束之前，是不能使用<code>this</code>引用的。</li>
</ol><p>显然，真实的<code>this</code>创建就通过层层的<code>super()</code>交给了父类或祖先类中支持创建这个实例的构造过程。这样一来，子类中也能得到一个“拥有父类所创建的带有内部槽的”实例，因此上述的<code>Function()</code>和<code>Date()</code>等等的子类也就可以实现了。例如，你可以在class MyFunction的声明中直接用extends指示父类为Function。</p><pre><code>&gt; class MyFunction extends Function { }

&gt; f = new MyFunction;

&gt; f()
undefine
</code></pre><p>这样一来，即使<code>MyFunction()</code>的类声明中缺省了“constructor()”构造方法，这种情况下JavaScript会在这种情况下为它自动创建一个，并且其内部也仅有一个“super()”代码。关于这些过程的细节，我将留待下一讲再具体地与你解析。在这里，你最应该关注的是这个过程带来的必然结果：</p><p><span class="orange">ECMAScript 6的类是由父类或祖先类创建<code>this</code>实例的。</span></p><p>不过仍然有一点是需要补充的：如果类声明<code>class</code>中不带有<code>extends</code>子句，那么它所创建出来的类与传统JavaScript的函数/构造器是一样的，也就是由自己来创建<code>this</code>对象。很显然，这是因为它无法找到一个显式指示的父类。不过关于这种情况，仍然隐藏了许多实现细节，我将会在下一讲中与你一起来学习它。</p><h2>用户返回new的结果</h2><p>在JavaScript中关于new运算与构造函数的最后一个有趣的设计，就是<strong>用户代码可以干涉new运算的结果</strong>。默认情况下，这个结果就是上述过程所创建出来的<code>this</code>对象实例，但是用户可以通过在构造器函数/方法中使用<code>return</code>语句来显式地重置它。</p><p>这也是从JavaScript 1.0就开始具有的特性。因为JavaScript 1.x中的函数、类与构造器是混用的，所以用户代码在函数中“返回些什么东西”是正常的语法，也是正常的逻辑需求。但是JavaScript要求在构造器中返回的数据必须是一个对象，否则就将抛出一个运行期的异常。</p><p>这个处理的约定，从ECMAScript ed3开始有了些变化。从ECMAScript ed3开始，检测构造器返回值的逻辑从<code>new</code>运算符中移到了<code>[[Construct]]</code>的处理过程中，并且重新约定：当构造器返回无效值（非对象值或null）时，使用原有已经创建的<code>this</code>对象作为构造过程<code>[[Constuct]]</code>的返回值。</p><p>因此到了ECMAScript 6之后，那些一般函数，以及非派生类，就延续了这一约定：<strong>使用已经创建的<code>this</code>对象来替代返回的无效值</strong>。这意味着它们总是能返回一个对象，要么是new运算按规则创建的this，要么是用户代码返回的对象。</p><blockquote>
<p>NOTE: 关于为什么非派生类也支持这一约定的问题，我后续的课程中会再次讲到。基本上来说，你可以认为这是为了让它与一般构造器保持足够的“相似性”。</p>
</blockquote><p>然而严格来说，引擎是不能理解“为什么用户代码会在构造器中返回一个一般的值类型数据”的。因为对于类的预期是返回一个对象，返回这种“无效值”是与预期矛盾的。因此，对于那些派生的子类（即声明中使用了<code>extends</code>子句的类），ECMAScript要求严格遵循“不得在构造器中返回非对象值（以及null值）”的设计约定，并在这种情况下直接抛出异常。例如：</p><pre><code>## (注：ES3之前将抛出异常）
&gt; new (function() {return 1});
{}

## 非派生类的构造方法返回无效值
&gt; new (class { constructor() { return 1 } })
{}

## 派生类的构造方法返回无效值
&gt; new (class extends Object { constructor() { return 1 } })
TypeError: Derived constructors may only return object or undefine
</code></pre><h2>知识回顾</h2><p>今天这一讲的一些知识点，是与你学习后续的专栏内容有关的。包括：</p><ol>
<li>在使用类声明来创建对象时，对象是由父类或祖先类创建的实例，并使用<code>this</code>引用传递到当前（子级的）类的。</li>
<li>在类的构造方法和一般构造器（函数）中返回值，是可以影响new运算的结果的，但JavaScript确保new运算不会得到一个非对象值。</li>
<li>类或构造器（函数）的首字母大写是一种惯例，而不是语言规范层面的约束。</li>
<li>类继承过程也依赖内部构造过程（<code>[[Contruct]]</code>）和原型属性（prototype），并且类继承实际上是原型继承的应用与扩展，不同于早期JavaScript1.0使用的类抄写。</li>
</ol><p>无论如何，从JavaScript 1.0开始的“类抄写”这一特性依然是可用的。无论是在普通函数、类还是构造器中，都可以向<code>this</code>引用上抄写属性，但这个过程变得与“如何实现继承性”完全无关。这里的<code>this</code>可以是函数调用时传入的，而不再仅仅来自于new运算的内置的构造过程创建。</p><h2>思考题</h2><ol>
<li>除了使用new X运算，还有什么方法可以创建新的对象？</li>
<li>在ECMAScript 6之后，除了new X之外，还有哪些方法可以操作原型/原型链？</li>
</ol><p>这些问题既是对本小节内容的回顾，也是下一阶段的课程中会用到的一些基础知识。建议你好好地寻求一下答案。</p><p>最后，希望你喜欢我的分享，也欢迎你把文章分享给你的朋友。</p>