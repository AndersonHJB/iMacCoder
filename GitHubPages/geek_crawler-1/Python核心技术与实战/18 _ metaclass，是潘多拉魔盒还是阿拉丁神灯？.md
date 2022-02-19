<audio title="18 _ metaclass，是潘多拉魔盒还是阿拉丁神灯？" src="https://static001.geekbang.org/resource/audio/f5/58/f553a545f2646e3acba6ccd0a08b6058.mp3" controls="controls"></audio> 
<p>你好，我是蔡元楠，极客时间《大规模数据处理实战》专栏的作者。今天我想和你分享的主题是：metaclass，是潘多拉魔盒还是阿拉丁神灯？</p><p>Python中有很多黑魔法，比如今天我将分享的metaclass。我认识许多人，对于这些语言特性有两种极端的观点。</p><ul>
<li>一种人觉得这些语言特性太牛逼了，简直是无所不能的阿拉丁神灯，必须找机会用上才能显示自己的Python实力。</li>
<li>另一种观点则是认为这些语言特性太危险了，会蛊惑人心去滥用，一旦打开就会释放“恶魔”，让整个代码库变得难以维护。</li>
</ul><p>其实这两种看法都有道理，却又都浅尝辄止。今天，我就带你来看看，metaclass到底是潘多拉魔盒还是阿拉丁神灯？</p><p>市面上的很多中文书，都把metaclass译为“元类”。我一直认为这个翻译很糟糕，所以也不想在这里称metaclass为元类。因为如果仅从字面理解，“元”是“本源”“基本”的意思，“元类”会让人以为是“基本类”。难道Python的metaclass，指的是Python 2的Object吗？这就让人一头雾水了。</p><p>事实上，meta-class的meta这个词根，起源于希腊语词汇meta，包含下面两种意思：</p><ol>
<li>“Beyond”，例如技术词汇metadata，意思是描述数据的超越数据；</li>
<li>“Change”，例如技术词汇metamorphosis，意思是改变的形态。</li>
</ol><!-- [[[read_end]]] --><p>metaclass，一如其名，实际上同时包含了“超越类”和“变形类”的含义，完全不是“基本类”的意思。所以，要深入理解metaclass，我们就要围绕它的<strong>超越变形</strong>特性。接下来，我将为你展开metaclass的超越变形能力，讲清楚metaclass究竟有什么用？怎么应用？Python语言设计层面是如何实现metaclass的 ？以及使用metaclass的风险。</p><h2>metaclass的超越变形特性有什么用？</h2><p><a href="https://pyyaml.org/wiki/PyYAMLDocumentation">YAML</a>是一个家喻户晓的Python工具，可以方便地序列化/逆序列化结构数据。YAMLObject的一个<strong>超越变形能力</strong>，就是它的任意子类支持序列化和反序列化（serialization &amp; deserialization）。比如说下面这段代码：</p><pre><code>class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return &quot;%s(name=%r, hp=%r, ac=%r, attacks=%r)&quot; % (
       self.__class__.__name__, self.name, self.hp, self.ac,      
       self.attacks)

yaml.load(&quot;&quot;&quot;
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
&quot;&quot;&quot;)

Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

print yaml.dump(Monster(
    name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT']))

# 输出
!Monster
ac: 16
attacks: [BITE, HURT]
hp: [3, 6]
name: Cave lizard
</code></pre><p>这里YAMLObject的特异功能体现在哪里呢？</p><p>你看，调用统一的yaml.load()，就能把任意一个yaml序列载入成一个Python Object；而调用统一的yaml.dump()，就能把一个YAMLObject子类序列化。对于load()和dump()的使用者来说，他们完全不需要提前知道任何类型信息，这让超动态配置编程成了可能。在我的实战经验中，许多大型项目都需要应用这种超动态配置的理念。</p><p>比方说，在一个智能语音助手的大型项目中，我们有1万个语音对话场景，每一个场景都是不同团队开发的。作为智能语音助手的核心团队成员，我不可能去了解每个子场景的实现细节。</p><p>在动态配置实验不同场景时，经常是今天我要实验场景A和B的配置，明天实验B和C的配置，光配置文件就有几万行量级，工作量真是不小。而应用这样的动态配置理念，我就可以让引擎根据我的文本配置文件，动态加载所需要的Python类。</p><p>对于YAML的使用者，这一点也很方便，你只要简单地继承yaml.YAMLObject，就能让你的Python Object具有序列化和逆序列化能力。是不是相比普通Python类，有一点“变态”，有一点“超越”？</p><p>事实上，我在Google见过很多Python开发者，发现能深入解释YAML这种设计模式优点的人，大概只有10%。而能知道类似YAML的这种动态序列化/逆序列化功能正是用metaclass实现的人，更是凤毛麟角，可能只有1%了。</p><h2>metaclass的超越变形特性怎么用？</h2><p>刚刚提到，估计只有1%的Python开发者，知道YAML的动态序列化/逆序列化是由metaclass实现的。如果你追问，YAML怎样用metaclass实现动态序列化/逆序列化功能，可能只有0.1%的人能说得出一二了。</p><p>因为篇幅原因，我们这里只看YAMLObject的load()功能。简单来说，我们需要一个全局的注册器，让YAML知道，序列化文本中的 <code>!Monster</code> 需要载入成 Monster这个Python类型。</p><p>一个很自然的想法就是，那我们建立一个全局变量叫 registry，把所有需要逆序列化的YAMLObject，都注册进去。比如下面这样：</p><pre><code>registry = {}

def add_constructor(target_class):
    registry[target_class.yaml_tag] = target_class
</code></pre><p>然后，在Monster 类定义后面加上下面这行代码：</p><pre><code>add_constructor(Monster)
</code></pre><p>但这样的缺点也很明显，对于YAML的使用者来说，每一个YAML的可逆序列化的类Foo定义后，都需要加上一句话，<code>add_constructor(Foo)</code>。这无疑给开发者增加了麻烦，也更容易出错，毕竟开发者很容易忘了这一点。</p><p>那么，更优的实现方式是什么样呢？如果你看过YAML的源码，就会发现，正是metaclass解决了这个问题。</p><pre><code># Python 2/3 相同部分
class YAMLObjectMetaclass(type):
  def __init__(cls, name, bases, kwds):
    super(YAMLObjectMetaclass, cls).__init__(name, bases, kwds)
    if 'yaml_tag' in kwds and kwds['yaml_tag'] is not None:
      cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
  # 省略其余定义

# Python 3
class YAMLObject(metaclass=YAMLObjectMetaclass):
  yaml_loader = Loader
  # 省略其余定义

# Python 2
class YAMLObject(object):
  __metaclass__ = YAMLObjectMetaclass
  yaml_loader = Loader
  # 省略其余定义
</code></pre><p>你可以发现，YAMLObject把metaclass都声明成了YAMLObjectMetaclass，尽管声明方式在Python 2 和3中略有不同。在YAMLObjectMetaclass中， 下面这行代码就是魔法发生的地方：</p><pre><code>cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml) 
</code></pre><p>YAML应用metaclass，拦截了所有YAMLObject子类的定义。也就说说，在你定义任何YAMLObject子类时，Python会强行插入运行下面这段代码，把我们之前想要的<code>add_constructor(Foo)</code>给自动加上。</p><pre><code>cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
</code></pre><p>所以YAML的使用者，无需自己去手写<code>add_constructor(Foo)</code> 。怎么样，是不是其实并不复杂？</p><p>看到这里，我们已经掌握了metaclass的使用方法，超越了世界上99.9%的Python开发者。更进一步，如果你能够深入理解，Python的语言设计层面是怎样实现metaclass的，你就是世间罕见的“Python大师”了。</p><h2><strong>Python底层语言设计层面是如何实现metaclass的？</strong></h2><p>刚才我们提到，metaclass能够拦截Python类的定义。它是怎么做到的？</p><p>要理解metaclass的底层原理，你需要深入理解Python类型模型。下面，我将分三点来说明。</p><h3>第一，所有的Python的用户定义类，都是type这个类的实例。</h3><p>可能会让你惊讶，事实上，类本身不过是一个名为 type 类的实例。在Python的类型世界里，type这个类就是造物的上帝。这可以在代码中验证：</p><pre><code># Python 3和Python 2类似
class MyClass:
  pass

instance = MyClass()

type(instance)
# 输出
&lt;class '__main__.C'&gt;

type(MyClass)
# 输出
&lt;class 'type'&gt;
</code></pre><p>你可以看到，instance是MyClass的实例，而MyClass不过是“上帝”type的实例。</p><h3>第二，用户自定义类，只不过是type类的<code>__call__</code>运算符重载。</h3><p>当我们定义一个类的语句结束时，真正发生的情况，是Python调用type的<code>__call__</code>运算符。简单来说，当你定义一个类时，写成下面这样时：</p><pre><code>class MyClass:
  data = 1
</code></pre><p>Python真正执行的是下面这段代码：</p><pre><code>class = type(classname, superclasses, attributedict)
</code></pre><p>这里等号右边的<code>type(classname, superclasses, attributedict)</code>，就是type的<code>__call__</code>运算符重载，它会进一步调用：</p><pre><code>type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)
</code></pre><p>当然，这一切都可以通过代码验证，比如下面这段代码示例：</p><pre><code>class MyClass:
  data = 1
  
instance = MyClass()
MyClass, instance
# 输出
(__main__.MyClass, &lt;__main__.MyClass instance at 0x7fe4f0b00ab8&gt;)
instance.data
# 输出
1

MyClass = type('MyClass', (), {'data': 1})
instance = MyClass()
MyClass, instance
# 输出
(__main__.MyClass, &lt;__main__.MyClass at 0x7fe4f0aea5d0&gt;)

instance.data
# 输出
1
</code></pre><p>由此可见，正常的MyClass定义，和你手工去调用type运算符的结果是完全一样的。</p><h3>第三，metaclass是type的子类，通过替换type的<code>__call__</code>运算符重载机制，“超越变形”正常的类。</h3><p>其实，理解了以上几点，我们就会明白，正是Python的类创建机制，给了metaclass大展身手的机会。</p><p>一旦你把一个类型MyClass的metaclass设置成MyMeta，MyClass就不再由原生的type创建，而是会调用MyMeta的<code>__call__</code>运算符重载。</p><pre><code>class = type(classname, superclasses, attributedict) 
# 变为了
class = MyMeta(classname, superclasses, attributedict)
</code></pre><p>所以，我们才能在上面YAML的例子中，利用YAMLObjectMetaclass的<code>__init__</code>方法，为所有YAMLObject子类偷偷执行<code>add_constructor()</code>。</p><h2><strong>使用metaclass的风险</strong></h2><p>前面的篇幅，我都是在讲metaclass的原理和优点。的的确确，只有深入理解metaclass的本质，你才能用好metaclass。而不幸的是，正如我开头所说，深入理解metaclass的Python开发者，只占了0.1%不到。</p><p>不过，凡事有利必有弊，尤其是metaclass这样“逆天”的存在。正如你所看到的那样，metaclass会"扭曲变形"正常的Python类型模型。所以，如果使用不慎，对于整个代码库造成的风险是不可估量的。</p><p>换句话说，metaclass仅仅是给小部分Python开发者，在开发框架层面的Python库时使用的。而在应用层，metaclass往往不是很好的选择。</p><p>也正因为这样，据我所知，在很多硅谷一线大厂，使用Python metaclass需要特例特批。</p><h2>总结</h2><p>这节课，我们通过解读YAML的源码，围绕metaclass的设计本意“超越变形”，解析了metaclass的使用场景和使用方法。接着，我们又进一步深入到Python语言设计层面，搞明白了metaclass的实现机制。</p><p>正如我取的标题那样，metaclass是Python黑魔法级别的语言特性。天堂和地狱只有一步之遥，你使用好metaclass，可以实现像YAML那样神奇的特性；而使用不好，可能就会打开潘多拉魔盒了。</p><p>所以，今天的内容，一方面是帮助有需要的同学，深入理解metaclass，更好地掌握和应用；另一方面，也是对初学者的科普和警告：不要轻易尝试metaclass。</p><h2>思考题</h2><p>学完了上节课的Python装饰器和这节课的metaclass，你知道了，它们都能干预正常的Python类型机制。那么，你觉得装饰器和metaclass有什么区别呢？欢迎留言和我讨论。</p>