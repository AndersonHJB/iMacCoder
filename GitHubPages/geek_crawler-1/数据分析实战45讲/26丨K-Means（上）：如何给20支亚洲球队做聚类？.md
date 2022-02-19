<audio title="26丨K-Means（上）：如何给20支亚洲球队做聚类？" src="https://static001.geekbang.org/resource/audio/bc/86/bc32d39df47bfa5cc044cd9c2a778886.mp3" controls="controls"></audio> 
<p>今天我来带你进行K-Means的学习。K-Means是一种非监督学习，解决的是聚类问题。K代表的是K类，Means代表的是中心，你可以理解这个算法的本质是确定K类的中心点，当你找到了这些中心点，也就完成了聚类。</p><p>那么请你和我思考以下三个问题：</p><ul>
<li>
<p>如何确定K类的中心点？</p>
</li>
<li>
<p>如何将其他点划分到K类中？</p>
</li>
<li>
<p>如何区分K-Means与KNN？</p>
</li>
</ul><p>如果理解了上面这3个问题，那么对K-Means的原理掌握得也就差不多了。</p><p>先请你和我思考一个场景，假设我有20支亚洲足球队，想要将它们按照成绩划分成3个等级，可以怎样划分？</p><h2>K-Means的工作原理</h2><p>对亚洲足球队的水平，你可能也有自己的判断。比如一流的亚洲球队有谁？你可能会说伊朗或韩国。二流的亚洲球队呢？你可能说是中国。三流的亚洲球队呢？你可能会说越南。</p><p>其实这些都是靠我们的经验来划分的，那么伊朗、中国、越南可以说是三个等级的典型代表，也就是我们每个类的中心点。</p><p>所以回过头来，如何确定K类的中心点？一开始我们是可以随机指派的，当你确认了中心点后，就可以按照距离将其他足球队划分到不同的类别中。</p><p>这也就是K-Means的中心思想，就是这么简单直接。你可能会问：如果一开始，选择一流球队是中国，二流球队是伊朗，三流球队是韩国，中心点选择错了怎么办？其实不用担心，K-Means有自我纠正机制，在不断的迭代过程中，会纠正中心点。中心点在整个迭代过程中，并不是唯一的，只是你需要一个初始值，一般算法会随机设置初始的中心点。</p><!-- [[[read_end]]] --><p>好了，那我来把K-Means的工作原理给你总结下：</p><ol>
<li>
<p>选取K个点作为初始的类中心点，这些点一般都是从数据集中随机抽取的；</p>
</li>
<li>
<p>将每个点分配到最近的类中心点，这样就形成了K个类，然后重新计算每个类的中心点；</p>
</li>
<li>
<p>重复第二步，直到类不发生变化，或者你也可以设置最大迭代次数，这样即使类中心点发生变化，但是只要达到最大迭代次数就会结束。</p>
</li>
</ol><h2>如何给亚洲球队做聚类</h2><p>对于机器来说需要数据才能判断类中心点，所以我整理了2015-2019年亚洲球队的排名，如下表所示。</p><p>我来说明一下数据概况。</p><p>其中2019年国际足联的世界排名，2015年亚洲杯排名均为实际排名。2018年世界杯中，很多球队没有进入到决赛圈，所以只有进入到决赛圈的球队才有实际的排名。如果是亚洲区预选赛12强的球队，排名会设置为40。如果没有进入亚洲区预选赛12强，球队排名会设置为50。</p><p><img src="https://static001.geekbang.org/resource/image/d8/4a/d8ac2a98aa728d64f919bac088ed574a.png" alt=""><br>
针对上面的排名，我们首先需要做的是数据规范化。你可以把这些值划分到[0,1]或者按照均值为0，方差为1的正态分布进行规范化。具体数据规范化的步骤可以看下13篇，也就是<a href="https://time.geekbang.org/column/article/77059">数据变换</a>那一篇。</p><p>我先把数值都规范化到[0,1]的空间中，得到了以下的数值表：</p><p><img src="https://static001.geekbang.org/resource/image/a7/17/a722eeab035fb13751a6dc5c0530ed17.png" alt=""><br>
如果我们随机选取中国、日本、韩国为三个类的中心点，我们就需要看下这些球队到中心点的距离。</p><p>距离有多种计算的方式，有关距离的计算我在KNN算法中也讲到过：</p><ul>
<li>
<p>欧氏距离</p>
</li>
<li>
<p>曼哈顿距离</p>
</li>
<li>
<p>切比雪夫距离</p>
</li>
<li>
<p>余弦距离</p>
</li>
</ul><p>欧氏距离是最常用的距离计算方式，这里我选择欧氏距离作为距离的标准，计算每个队伍分别到中国、日本、韩国的距离，然后根据距离远近来划分。我们看到大部分的队，会和中国队聚类到一起。这里我整理了距离的计算过程，比如中国和中国的欧氏距离为0，中国和日本的欧式距离为0.732003。如果按照中国、日本、韩国为3个分类的中心点，欧氏距离的计算结果如下表所示：</p><p><img src="https://static001.geekbang.org/resource/image/b6/e9/b603ccdb93420c8455aea7278efaece9.png" alt=""><br>
然后我们再重新计算这三个类的中心点，如何计算呢？最简单的方式就是取平均值，然后根据新的中心点按照距离远近重新分配球队的分类，再根据球队的分类更新中心点的位置。计算过程这里不展开，最后一直迭代（重复上述的计算过程：计算中心点和划分分类）到分类不再发生变化，可以得到以下的分类结果：</p><p><img src="https://static001.geekbang.org/resource/image/12/98/12c6039884ee99742fbbebf198425998.png" alt=""><br>
所以我们能看出来第一梯队有日本、韩国、伊朗、沙特、澳洲；第二梯队有中国、伊拉克、阿联酋、乌兹别克斯坦；第三梯队有卡塔尔、泰国、越南、阿曼、巴林、朝鲜、印尼、叙利亚、约旦、科威特和巴勒斯坦。</p><h2>如何使用sklearn中的K-Means算法</h2><p>sklearn是Python的机器学习工具库，如果从功能上来划分，sklearn可以实现分类、聚类、回归、降维、模型选择和预处理等功能。这里我们使用的是sklearn的聚类函数库，因此需要引用工具包，具体代码如下：</p><pre><code>from sklearn.cluster import KMeans
</code></pre><p>当然K-Means只是sklearn.cluster中的一个聚类库，实际上包括K-Means在内，sklearn.cluster一共提供了9种聚类方法，比如Mean-shift，DBSCAN，Spectral clustering（谱聚类）等。这些聚类方法的原理和K-Means不同，这里不做介绍。</p><p>我们看下K-Means如何创建：</p><pre><code>KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')
</code></pre><p>我们能看到在K-Means类创建的过程中，有一些主要的参数：</p><ul>
<li>
<p><strong>n_clusters</strong>: 即K值，一般需要多试一些K值来保证更好的聚类效果。你可以随机设置一些K值，然后选择聚类效果最好的作为最终的K值；</p>
</li>
<li>
<p><strong>max_iter</strong>： 最大迭代次数，如果聚类很难收敛的话，设置最大迭代次数可以让我们及时得到反馈结果，否则程序运行时间会非常长；</p>
</li>
<li>
<p><strong>n_init</strong>：初始化中心点的运算次数，默认是10。程序是否能快速收敛和中心点的选择关系非常大，所以在中心点选择上多花一些时间，来争取整体时间上的快速收敛还是非常值得的。由于每一次中心点都是随机生成的，这样得到的结果就有好有坏，非常不确定，所以要运行n_init次, 取其中最好的作为初始的中心点。如果K值比较大的时候，你可以适当增大n_init这个值；</p>
</li>
<li>
<p><strong>init：</strong> 即初始值选择的方式，默认是采用优化过的k-means++方式，你也可以自己指定中心点，或者采用random完全随机的方式。自己设置中心点一般是对于个性化的数据进行设置，很少采用。random的方式则是完全随机的方式，一般推荐采用优化过的k-means++方式；</p>
</li>
<li>
<p><strong>algorithm</strong>：k-means的实现算法，有“auto” “full”“elkan”三种。一般来说建议直接用默认的"auto"。简单说下这三个取值的区别，如果你选择"full"采用的是传统的K-Means算法，“auto”会根据数据的特点自动选择是选择“full”还是“elkan”。我们一般选择默认的取值，即“auto” 。</p>
</li>
</ul><p>在创建好K-Means类之后，就可以使用它的方法，最常用的是fit和predict这个两个函数。你可以单独使用fit函数和predict函数，也可以合并使用fit_predict函数。其中fit(data)可以对data数据进行k-Means聚类。 predict(data)可以针对data中的每个样本，计算最近的类。</p><p>现在我们要完整地跑一遍20支亚洲球队的聚类问题。我把数据上传到了<a href="https://github.com/cystanford/kmeans">GitHub</a>上，你可以自行下载。</p><pre><code># coding: utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
# 输入数据
data = pd.read_csv('data.csv', encoding='gbk')
train_x = data[[&quot;2019年国际排名&quot;,&quot;2018世界杯&quot;,&quot;2015亚洲杯&quot;]]
df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=3)
# 规范化到[0,1]空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
# kmeans算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)
</code></pre><p>运行结果：</p><pre><code>国家  2019年国际排名  2018世界杯  2015亚洲杯  聚类
0       中国         73       40        7   2
1       日本         60       15        5   0
2       韩国         61       19        2   0
3       伊朗         34       18        6   0
4       沙特         67       26       10   0
5      伊拉克         91       40        4   2
6      卡塔尔        101       40       13   1
7      阿联酋         81       40        6   2
8   乌兹别克斯坦         88       40        8   2
9       泰国        122       40       17   1
10      越南        102       50       17   1
11      阿曼         87       50       12   1
12      巴林        116       50       11   1
13      朝鲜        110       50       14   1
14      印尼        164       50       17   1
15      澳洲         40       30        1   0
16     叙利亚         76       40       17   1
17      约旦        118       50        9   1
18     科威特        160       50       15   1
19    巴勒斯坦         96       50       16   1
</code></pre><h2>总结</h2><p>今天我给你讲了K-Means算法原理，我们再来看下开篇我给你提的三个问题。</p><p>如何确定K类的中心点？其中包括了初始的设置，以及中间迭代过程中中心点的计算。在初始设置中，会进行n_init次的选择，然后选择初始中心点效果最好的为初始值。在每次分类更新后，你都需要重新确认每一类的中心点，一般采用均值的方式进行确认。</p><p>如何将其他点划分到K类中？这里实际上是关于距离的定义，我们知道距离有多种定义的方式，在K-Means和KNN中，我们都可以采用欧氏距离、曼哈顿距离、切比雪夫距离、余弦距离等。对于点的划分，就看它离哪个类的中心点的距离最近，就属于哪一类。</p><p>如何区分K-Means和KNN这两种算法呢？刚学过K-Means和KNN算法的同学应该能知道两者的区别，但往往过了一段时间，就容易混淆。所以我们可以从三个维度来区分K-Means和KNN这两个算法：</p><ul>
<li>
<p>首先，这两个算法解决数据挖掘的两类问题。K-Means是聚类算法，KNN是分类算法。</p>
</li>
<li>
<p>这两个算法分别是两种不同的学习方式。K-Means是非监督学习，也就是不需要事先给出分类标签，而KNN是有监督学习，需要我们给出训练数据的分类标识。</p>
</li>
<li>
<p>最后，K值的含义不同。K-Means中的K值代表K类。KNN中的K值代表K个最接近的邻居。</p>
</li>
</ul><p><img src="https://static001.geekbang.org/resource/image/eb/c5/eb60546c6a3d9bc6a1538049c26723c5.png" alt=""><br>
那么学完了今天的内容后，你能说一下K-Means的算法原理吗？如果我们把上面的20支亚洲球队用K-Means划分成5类，在规范化数据的时候采用标准化的方式（即均值为0，方差为1），该如何编写程序呢？运行的结果又是如何？</p><p>欢迎你在评论区与我分享你的答案，也欢迎点击“请朋友读”，把这篇文章分享给你的朋友或者同事。</p><p></p>