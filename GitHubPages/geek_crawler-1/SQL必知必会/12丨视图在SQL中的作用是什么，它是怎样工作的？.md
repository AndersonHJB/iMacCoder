<audio title="12丨视图在SQL中的作用是什么，它是怎样工作的？" src="https://static001.geekbang.org/resource/audio/7c/ba/7ccceb296d99aaf83bbc8de24d9d46ba.mp3" controls="controls"></audio> 
<p>我们之前对SQL中的数据表查询进行了讲解，今天我们来看下如何对视图进行查询。视图，也就是我们今天要讲的虚拟表，本身是不具有数据的，它是SQL中的一个重要概念。从下面这张图中，你能看到，虚拟表的创建连接了一个或多个数据表，不同的查询应用都可以建立在虚拟表之上。</p><p><img src="https://static001.geekbang.org/resource/image/6c/e8/6c7cd968b0bd24ce5689a08c052eade8.jpg" alt=""></p><p>视图一方面可以帮我们使用表的一部分而不是所有的表，另一方面也可以针对不同的用户制定不同的查询视图。比如，针对一个公司的销售人员，我们只想给他看部分数据，而某些特殊的数据，比如采购的价格，则不会提供给他。</p><p>刚才讲的只是视图的一个使用场景，实际上视图还有很多作用，今天我们就一起学习下。今天的文章里，你将重点掌握以下的内容：</p><ol>
<li>什么是视图？如何创建、更新和删除视图？</li>
<li>如何使用视图来简化我们的SQL操作？</li>
<li>视图和临时表的区别是什么，它们各自有什么优缺点？</li>
</ol><h2>如何创建，更新和删除视图</h2><p>视图作为一张虚拟表，帮我们封装了底层与数据表的接口。它相当于是一张表或多张表的数据结果集。视图的这一特点，可以帮我们简化复杂的SQL查询，比如在编写视图后，我们就可以直接重用它，而不需要考虑视图中包含的基础查询的细节。同样，我们也可以根据需要更改数据格式，返回与底层数据表格式不同的数据。</p><!-- [[[read_end]]] --><p>通常情况下，小型项目的数据库可以不使用视图，但是在大型项目中，以及数据表比较复杂的情况下，视图的价值就凸显出来了，它可以帮助我们把经常查询的结果集放到虚拟表中，提升使用效率。理解和使用起来都非常方便。</p><h3>创建视图：CREATE VIEW</h3><p>那么该如何创建视图呢？创建视图的语法是：</p><pre><code>CREATE VIEW view_name AS
SELECT column1, column2
FROM table
WHERE condition
</code></pre><p>实际上就是我们在SQL查询语句的基础上封装了视图VIEW，这样就会基于SQL语句的结果集形成一张虚拟表。其中view_name为视图名称，column1、column2代表列名，condition代表查询过滤条件。</p><p>我们以NBA球员数据表为例。我们想要查询比NBA球员平均身高高的球员都有哪些，显示他们的球员ID和身高。假设我们给这个视图起个名字player_above_avg_height，那么创建视图可以写成：</p><pre><code>CREATE VIEW player_above_avg_height AS
SELECT player_id, height
FROM player
WHERE height &gt; (SELECT AVG(height) from player)
</code></pre><p>视图查询结果（18条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/a0/35/a05ac6169562c0f95bf8387df3577635.png" alt=""><br>
当视图创建之后，它就相当于一个虚拟表，可以直接使用：</p><pre><code>SELECT * FROM player_above_avg_height
</code></pre><p>运行结果和上面一样。</p><h3>嵌套视图</h3><p>当我们创建好一张视图之后，还可以在它的基础上继续创建视图，比如我们想在虚拟表player_above_avg_height的基础上，找到比这个表中的球员平均身高高的球员，作为新的视图player_above_above_avg_height，那么可以写成：</p><pre><code>CREATE VIEW player_above_above_avg_height AS
SELECT player_id, height
FROM player
WHERE height &gt; (SELECT AVG(height) from player_above_avg_height)
</code></pre><p>视图查询结果（11条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/6b/5b/6b7416b24d91786c023bf10eee50355b.png" alt=""></p><p>你能看到这个视图的数据记录数为11个，比之前的记录少了7个。</p><h3>修改视图：ALTER VIEW</h3><p>修改视图的语法是：</p><pre><code>ALTER VIEW view_name AS
SELECT column1, column2
FROM table
WHERE condition
</code></pre><p>你能看出来它的语法和创建视图一样，只是对原有视图的更新。比如我们想更新视图player_above_avg_height，增加一个player_name字段，可以写成：</p><pre><code>ALTER VIEW player_above_avg_height AS
SELECT player_id, player_name, height
FROM player
WHERE height &gt; (SELECT AVG(height) from player)
</code></pre><p>这样的话，下次再对视图进行查询的时候，视图结果就进行了更新。</p><pre><code>SELECT * FROM player_above_avg_height
</code></pre><p>运行结果（18条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/d9/bb/d91a3d7978b12fc52c194d1ce58410bb.png" alt=""></p><h3>删除视图：DROP VIEW</h3><p>删除视图的语法是：</p><pre><code>DROP VIEW view_name
</code></pre><p>比如我们想把刚才创建的视图删除，可以使用：</p><pre><code>DROP VIEW player_above_avg_height
</code></pre><p>需要说明的是，SQLite不支持视图的修改，仅支持只读视图，也就是说你只能使用CREATE VIEW和DROP VIEW，如果想要修改视图，就需要先DROP然后再CREATE。</p><h2>如何使用视图简化SQL操作</h2><p>从上面这个例子中，你能看出视图就是对SELECT语句进行了封装，方便我们重用它们。下面我们再来看几个视图使用的例子。</p><h3>利用视图完成复杂的连接</h3><p>我在讲解SQL99标准连接操作的时候，举了一个NBA球员和身高等级连接的例子，有两张表，分别为player和height_grades。其中height_grades记录了不同身高对应的身高等级。这里我们可以通过创建视图，来完成球员以及对应身高等级的查询。</p><p>首先我们对player表和height_grades表进行连接，关联条件是球员的身高height（在身高等级表规定的最低身高和最高身高之间），这样就可以得到这个球员对应的身高等级，对应的字段为height_level。然后我们通过SELECT得到我们想要查询的字段，分别为球员姓名player_name、球员身高height，还有对应的身高等级height_level。然后把取得的查询结果集放到视图player_height_grades中，即：</p><pre><code>CREATE VIEW player_height_grades AS
SELECT p.player_name, p.height, h.height_level
FROM player as p JOIN height_grades as h
ON height BETWEEN h.height_lowest AND h.height_highest
</code></pre><p>运行结果（37条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/31/d2/3185f62845a19162c19b22673da6c8d2.png" alt=""></p><p>以后我们进行查询的时候，可以直接通过视图查询，比如我想查询身高介于1.90m和2.08m之间的球员及他们对应的身高：</p><pre><code>SELECT * FROM player_height_grades WHERE height &gt;= 1.90 AND height &lt;= 2.08
</code></pre><p>运行结果（26条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/8c/89/8c060eb06386b95cb31ff43c95948a89.png" alt=""></p><p>这样就把一个相对复杂的连接查询转化成了视图查询。</p><h3>利用视图对数据进行格式化</h3><p>我们经常需要输出某个格式的内容，比如我们想输出球员姓名和对应的球队，对应格式为player_name(team_name)，就可以使用视图来完成数据格式化的操作：</p><pre><code>CREATE VIEW player_team AS 
SELECT CONCAT(player_name, '(' , team.team_name , ')') AS player_team FROM player JOIN team WHERE player.team_id = team.team_id
</code></pre><p>首先我们将player表和team表进行连接，关联条件是相同的team_id。我们想要的格式是<code>player_name(team_name)</code>，因此我们使用CONCAT函数，即<code>CONCAT(player_name, '(' , team.team_name , ')')</code>，将player_name字段和team_name字段进行拼接，得到了拼接值被命名为player_team的字段名，将它放到视图player_team中。</p><p>这样的话，我们直接查询视图，就可以得到格式化后的结果：</p><pre><code>SELECT * FROM player_team
</code></pre><p>运行结果（37条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/28/0d/280a22627fd84cd8450245041a3bba0d.png" alt=""></p><h3>使用视图与计算字段</h3><p>我们在数据查询中，有很多统计的需求可以通过视图来完成。正确地使用视图可以帮我们简化复杂的数据处理。</p><p>我以球员比赛成绩表为例，对应的是player_score表。这张表中一共有19个字段，它们代表的含义如下：</p><p><img src="https://static001.geekbang.org/resource/image/8a/d2/8a77858d8c9633c7c4128dd454ad38d2.png" alt=""><br>
如果我想要统计每位球员在每场比赛中的二分球、三分球和罚球的得分，可以通过创建视图完成：</p><pre><code>CREATE VIEW game_player_score AS
SELECT game_id, player_id, (shoot_hits-shoot_3_hits)*2 AS shoot_2_points, shoot_3_hits*3 AS shoot_3_points, shoot_p_hits AS shoot_p_points, score  FROM player_score
</code></pre><p>然后通过查询视图就可以完成。</p><pre><code>SELECT * FROM game_player_score
</code></pre><p>运行结果（19条记录）：</p><p><img src="https://static001.geekbang.org/resource/image/b0/dc/b0edf8453df44d018315f68e89f7e3dc.png" alt=""></p><p>你能看出正确使用视图可以简化复杂的SQL查询，让SQL更加清爽易用。不过有一点需要注意，视图是虚拟表，它只是封装了底层的数据表查询接口，因此有些RDBMS不支持对视图创建索引（有些RDBMS则支持，比如新版本的SQL Server）。</p><h2>总结</h2><p>今天我讲解了视图的使用，包括创建，修改和删除视图。使用视图有很多好处，比如安全、简单清晰。</p><ol>
<li>安全性：虚拟表是基于底层数据表的，我们在使用视图时，一般不会轻易通过视图对底层数据进行修改，即使是使用单表的视图，也会受到限制，比如计算字段，类型转换等是无法通过视图来对底层数据进行修改的，这也在一定程度上保证了数据表的数据安全性。同时，我们还可以针对不同用户开放不同的数据查询权限，比如人员薪酬是个敏感的字段，那么只给某个级别以上的人员开放，其他人的查询视图中则不提供这个字段。</li>
<li>简单清晰：视图是对SQL查询的封装，它可以将原本复杂的SQL查询简化，在编写好查询之后，我们就可以直接重用它而不必要知道基本的查询细节。同时我们还可以在视图之上再嵌套视图。这样就好比我们在进行模块化编程一样，不仅结构清晰，还提升了代码的复用率。</li>
</ol><p>另外，我们也需要了解到视图是虚拟表，本身不存储数据，如果想要通过视图对底层数据表的数据进行修改也会受到很多限制，通常我们是把视图用于查询，也就是对SQL查询的一种封装。那么它和临时表又有什么区别呢？在实际工作中，我们可能会见到各种临时数据。比如你可能会问，如果我在做一个电商的系统，中间会有个购物车的功能，需要临时统计购物车中的商品和金额，那该怎么办呢？这里就需要用到临时表了，临时表是真实存在的数据表，不过它不用于长期存放数据，只为当前连接存在，关闭连接后，临时表就会自动释放。</p><p><img src="https://static001.geekbang.org/resource/image/8a/30/8afa99e7d1ac1de2c802cf0c61004b30.jpg" alt=""><br>
今天我们对视图进行了讲解，你能用自己的语言来说下视图的优缺点么？另外视图在更新的时候会影响到数据表吗？</p><p>欢迎你在评论区写下你的思考，也欢迎把这篇文章分享给你的朋友或者同事，一起交流一下。</p>