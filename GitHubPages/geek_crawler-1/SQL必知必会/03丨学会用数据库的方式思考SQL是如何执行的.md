<audio title="03丨学会用数据库的方式思考SQL是如何执行的" src="https://static001.geekbang.org/resource/audio/ad/07/ad590188d5b924bf34f75dd6f0324a07.mp3" controls="controls"></audio> 
<p>通过上一篇文章对不同的DBMS的介绍，你应该对它们有了一些基础的了解。虽然SQL是声明式语言，我们可以像使用英语一样使用它，不过在RDBMS（关系型数据库管理系统）中，SQL的实现方式还是有差别的。今天我们就从数据库的角度来思考一下SQL是如何被执行的。</p><p>关于今天的内容，你会从以下几个方面进行学习：</p><ol>
<li>Oracle中的SQL是如何执行的，什么是硬解析和软解析；</li>
<li>MySQL中的SQL是如何执行的，MySQL的体系结构又是怎样的；</li>
<li>什么是存储引擎，MySQL的存储引擎都有哪些？</li>
</ol><h2>Oracle中的SQL是如何执行的</h2><p>我们先来看下SQL在Oracle中的执行过程：</p><p><img src="https://static001.geekbang.org/resource/image/4b/70/4b43aeaf9bb0fe2d576757d3fef50070.png" alt=""><br>
从上面这张图中可以看出，SQL语句在Oracle中经历了以下的几个步骤。</p><ol>
<li>
<p>语法检查：检查SQL拼写是否正确，如果不正确，Oracle会报语法错误。</p>
</li>
<li>
<p>语义检查：检查SQL中的访问对象是否存在。比如我们在写SELECT语句的时候，列名写错了，系统就会提示错误。语法检查和语义检查的作用是保证SQL语句没有错误。</p>
</li>
<li>
<p>权限检查：看用户是否具备访问该数据的权限。</p>
</li>
<li>
<p>共享池检查：共享池（Shared Pool）是一块内存池，最主要的作用是缓存SQL语句和该语句的执行计划。Oracle通过检查共享池是否存在SQL语句的执行计划，来判断进行软解析，还是硬解析。那软解析和硬解析又该怎么理解呢？</p>
<p>在共享池中，Oracle首先对SQL语句进行Hash运算，然后根据Hash值在库缓存（Library Cache）中查找，如果存在SQL语句的执行计划，就直接拿来执行，直接进入“执行器”的环节，这就是软解析。</p>
<p>如果没有找到SQL语句和执行计划，Oracle就需要创建解析树进行解析，生成执行计划，进入“优化器”这个步骤，这就是硬解析。</p>
</li>
<li>
<p>优化器：优化器中就是要进行硬解析，也就是决定怎么做，比如创建解析树，生成执行计划。</p>
</li>
<li>
<p>执行器：当有了解析树和执行计划之后，就知道了SQL该怎么被执行，这样就可以在执行器中执行语句了。</p>
</li>
</ol><!-- [[[read_end]]] --><p>共享池是Oracle中的术语，包括了库缓存，数据字典缓冲区等。我们上面已经讲到了库缓存区，它主要缓存SQL语句和执行计划。而数据字典缓冲区存储的是Oracle中的对象定义，比如表、视图、索引等对象。当对SQL语句进行解析的时候，如果需要相关的数据，会从数据字典缓冲区中提取。</p><p>库缓存这一个步骤，决定了SQL语句是否需要进行硬解析。为了提升SQL的执行效率，我们应该尽量避免硬解析，因为在SQL的执行过程中，创建解析树，生成执行计划是很消耗资源的。</p><p>你可能会问，如何避免硬解析，尽量使用软解析呢？在Oracle中，绑定变量是它的一大特色。绑定变量就是在SQL语句中使用变量，通过不同的变量取值来改变SQL的执行结果。这样做的好处是能提升软解析的可能性，不足之处在于可能会导致生成的执行计划不够优化，因此是否需要绑定变量还需要视情况而定。</p><p>举个例子，我们可以使用下面的查询语句：</p><pre><code>SQL&gt; select * from player where player_id = 10001;
</code></pre><p>你也可以使用绑定变量，如：</p><pre><code>SQL&gt; select * from player where player_id = :player_id;
</code></pre><p>这两个查询语句的效率在Oracle中是完全不同的。如果你在查询player_id = 10001之后，还会查询10002、10003之类的数据，那么每一次查询都会创建一个新的查询解析。而第二种方式使用了绑定变量，那么在第一次查询之后，在共享池中就会存在这类查询的执行计划，也就是软解析。</p><p>因此我们可以通过使用绑定变量来减少硬解析，减少Oracle的解析工作量。但是这种方式也有缺点，使用动态SQL的方式，因为参数不同，会导致SQL的执行效率不同，同时SQL优化也会比较困难。</p><h2>MySQL中的SQL是如何执行的</h2><p>Oracle中采用了共享池来判断SQL语句是否存在缓存和执行计划，通过这一步骤我们可以知道应该采用硬解析还是软解析。那么在MySQL中，SQL是如何被执行的呢？</p><p>首先MySQL是典型的C/S架构，即Client/Server架构，服务器端程序使用的mysqld。整体的MySQL流程如下图所示：</p><p><img src="https://static001.geekbang.org/resource/image/c4/9e/c4b24ef2377e0d233af69925b0d7139e.png" alt=""><br>
你能看到MySQL由三层组成：</p><ol>
<li>连接层：客户端和服务器端建立连接，客户端发送SQL至服务器端；</li>
<li>SQL层：对SQL语句进行查询处理；</li>
<li>存储引擎层：与数据库文件打交道，负责数据的存储和读取。</li>
</ol><p>其中SQL层与数据库文件的存储方式无关，我们来看下SQL层的结构：</p><p><img src="https://static001.geekbang.org/resource/image/30/79/30819813cc9d53714c08527e282ede79.jpg" alt=""></p><ol>
<li>查询缓存：Server如果在查询缓存中发现了这条SQL语句，就会直接将结果返回给客户端；如果没有，就进入到解析器阶段。需要说明的是，因为查询缓存往往效率不高，所以在MySQL8.0之后就抛弃了这个功能。</li>
<li>解析器：在解析器中对SQL语句进行语法分析、语义分析。</li>
<li>优化器：在优化器中会确定SQL语句的执行路径，比如是根据全表检索，还是根据索引来检索等。</li>
<li>执行器：在执行之前需要判断该用户是否具备权限，如果具备权限就执行SQL查询并返回结果。在MySQL8.0以下的版本，如果设置了查询缓存，这时会将查询结果进行缓存。</li>
</ol><p>你能看到SQL语句在MySQL中的流程是：SQL语句→缓存查询→解析器→优化器→执行器。在一部分中，MySQL和Oracle执行SQL的原理是一样的。</p><p>与Oracle不同的是，MySQL的存储引擎采用了插件的形式，每个存储引擎都面向一种特定的数据库应用环境。同时开源的MySQL还允许开发人员设置自己的存储引擎，下面是一些常见的存储引擎：</p><ol>
<li>InnoDB存储引擎：它是MySQL 5.5版本之后默认的存储引擎，最大的特点是支持事务、行级锁定、外键约束等。</li>
<li>MyISAM存储引擎：在MySQL 5.5版本之前是默认的存储引擎，不支持事务，也不支持外键，最大的特点是速度快，占用资源少。</li>
<li>Memory存储引擎：使用系统内存作为存储介质，以便得到更快的响应速度。不过如果mysqld进程崩溃，则会导致所有的数据丢失，因此我们只有当数据是临时的情况下才使用Memory存储引擎。</li>
<li>NDB存储引擎：也叫做NDB Cluster存储引擎，主要用于MySQL Cluster分布式集群环境，类似于Oracle的RAC集群。</li>
<li>Archive存储引擎：它有很好的压缩机制，用于文件归档，在请求写入时会进行压缩，所以也经常用来做仓库。</li>
</ol><p>需要注意的是，数据库的设计在于表的设计，而在MySQL中每个表的设计都可以采用不同的存储引擎，我们可以根据实际的数据处理需要来选择存储引擎，这也是MySQL的强大之处。</p><h2>数据库管理系统也是一种软件</h2><p>我们刚才了解了SQL语句在Oracle和MySQL中的执行流程，实际上完整的Oracle和MySQL结构图要复杂得多：</p><p><img src="https://static001.geekbang.org/resource/image/d9/74/d99e951b69a692c7f075dd21116d3574.png" alt=""><br>
<img src="https://static001.geekbang.org/resource/image/9b/7f/9b515e012856099b05d9dc3a5eaabe7f.png" alt=""><br>
如果你只是简单地把MySQL和Oracle看成数据库管理系统软件，从外部看难免会觉得“晦涩难懂”，毕竟组织结构太多了。我们在学习的时候，还需要具备抽象的能力，抓取最核心的部分：SQL的执行原理。因为不同的DBMS的SQL的执行原理是相通的，只是在不同的软件中，各有各的实现路径。</p><p>既然一条SQL语句会经历不同的模块，那我们就来看下，在不同的模块中，SQL执行所使用的资源（时间）是怎样的。下面我来教你如何在MySQL中对一条SQL语句的执行时间进行分析。</p><p>首先我们需要看下profiling是否开启，开启它可以让MySQL收集在SQL执行时所使用的资源情况，命令如下：</p><pre><code>mysql&gt; select @@profiling;
</code></pre><p><img src="https://static001.geekbang.org/resource/image/bc/c1/bcbfdd58b908dc8820fb57d00ff4dcc1.png" alt=""><br>
profiling=0代表关闭，我们需要把profiling打开，即设置为1：</p><pre><code>mysql&gt; set profiling=1;
</code></pre><p>然后我们执行一个SQL查询（你可以执行任何一个SQL查询）：</p><pre><code>mysql&gt; select * from wucai.heros;
</code></pre><p>查看当前会话所产生的所有profiles：</p><p><img src="https://static001.geekbang.org/resource/image/d9/bf/d9445abcde0f3b38488afe21aca8e9bf.png" alt=""><br>
你会发现我们刚才执行了两次查询，Query ID分别为1和2。如果我们想要获取上一次查询的执行时间，可以使用：</p><pre><code>mysql&gt; show profile;
</code></pre><p><img src="https://static001.geekbang.org/resource/image/09/7d/09ef901a55ffcd32ed263d82e3cf1f7d.png" alt=""><br>
当然你也可以查询指定的Query ID，比如：</p><pre><code>mysql&gt; show profile for query 2;
</code></pre><p>查询SQL的执行时间结果和上面是一样的。</p><p>在8.0版本之后，MySQL不再支持缓存的查询，原因我在上文已经说过。一旦数据表有更新，缓存都将清空，因此只有数据表是静态的时候，或者数据表很少发生变化时，使用缓存查询才有价值，否则如果数据表经常更新，反而增加了SQL的查询时间。</p><p>你可以使用select version()来查看MySQL的版本情况。</p><p><img src="https://static001.geekbang.org/resource/image/08/1a/0815cf2a78889b947cb498622377c21a.png" alt=""></p><h2>总结</h2><p>我们在使用SQL的时候，往往只见树木，不见森林，不会注意到它在各种数据库软件中是如何执行的，今天我们从全貌的角度来理解这个问题。你能看到不同的RDBMS之间有相同的地方，也有不同的地方。</p><p>相同的地方在于Oracle和MySQL都是通过解析器→优化器→执行器这样的流程来执行SQL的。</p><p>但Oracle和MySQL在进行SQL的查询上面有软件实现层面的差异。Oracle提出了共享池的概念，通过共享池来判断是进行软解析，还是硬解析。而在MySQL中，8.0以后的版本不再支持查询缓存，而是直接执行解析器→优化器→执行器的流程，这一点从MySQL中的show profile里也能看到。同时MySQL的一大特色就是提供了各种存储引擎以供选择，不同的存储引擎有各自的使用场景，我们可以针对每张表选择适合的存储引擎。</p><p><img src="https://static001.geekbang.org/resource/image/02/f1/02719a80d54a174dec8672d1f87295f1.jpg" alt=""><br>
今天的内容到这里就结束了，你能说一下Oracle中的绑定变量是什么，使用它有什么优缺点吗？MySQL的存储引擎是一大特色，其中MyISAM和InnoDB都是常用的存储引擎，这两个存储引擎的特性和使用场景分别是什么？</p><p>最后留一道选择题吧，解析后的SQL语句在Oracle的哪个区域中进行缓存？</p><p>A. 数据缓冲区<br>
B. 日志缓冲区<br>
C. 共享池<br>
D. 大池</p><p>欢迎你在评论区写下你的思考，我会在评论区与你一起交流，如果这篇文章帮你理顺了Oracle和MySQL执行SQL的过程，欢迎你把它分享给你的朋友或者同事。</p><p><span class="orange">※注：本篇文章出现的图片请点击<a href="http://github.com/cystanford/SQL-XMind">这里</a>下载高清大图。</span></p>