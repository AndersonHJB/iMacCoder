<audio title="23 _ 瞧一瞧Linux：SLAB如何分配内存？" src="https://static001.geekbang.org/resource/audio/9a/a2/9a22a3720027800ff033f04218e0a9a2.mp3" controls="controls"></audio> 
<p>你好，我是LMOS。</p><p>上节课我们学习了伙伴系统，了解了它是怎样管理物理内存页面的。那么你自然会想到这个问题：Linux系统中，比页更小的内存对象要怎样分配呢？</p><p>带着这个问题，我们来一起看看<strong>SLAB分配器的原理和实现。</strong>在学习过程中，你也可以对照一下我们Cosmos的内存管理组件，看看两者的内存管理有哪些异同。</p><h2>SLAB</h2><p>与Cosmos物理内存页面管理器一样，Linux中的伙伴系统是以页面为最小单位分配的，现实更多要以内核对象为单位分配内存，其实更具体一点说，就是根据内核对象的实例变量大小来申请和释放内存空间，这些数据结构实例变量的大小通常从几十字节到几百字节不等，远远小于一个页面的大小。</p><p>如果一个几十字节大小的数据结构实例变量，就要为此分配一个页面，这无疑是对宝贵物理内存的一种巨大浪费，因此一个更好的技术方案应运而生，就是<strong>Slab分配器</strong>（由Sun公司的雇员Jeff Bonwick在Solaris 2.4中设计并实现）。</p><p>由于作者公开了实现方法，后来被Linux所借鉴，用于实现内核中更小粒度的内存分配。看看吧，你以为Linux很强大，真的强大吗？不过是站在巨人的肩膀上飞翔的。</p><h3>走进SLAB对象</h3><p>何为SLAB对象？在SLAB分配器中，它把一个内存页面或者一组连续的内存页面，划分成大小相同的块，其中这一个小的内存块就是SLAB对象，但是这一组连续的内存页面中不只是SLAB对象，还有SLAB管理头和着色区。</p><!-- [[[read_end]]] --><p>我画个图你就明白了，如下所示。</p><p><img src="https://static001.geekbang.org/resource/image/1b/22/1b210fe094e7eba4b19ef118f76e6322.jpg?wh=5881x2933" alt="" title="SLAB对象示意图"></p><p>上图中有一个内存页面和两个内存页面的SLAB，你可能对着色区有点陌生，我来给你讲解一下。</p><p>这个着色区也是一块动态的内存块，建立SLAB时才会设置它的大小，目的是为了错开不同SLAB中的对象地址，降低硬件Cache行中的地址争用，以免导致Cache抖动效应，整个系统性能下降。</p><p>SLAB头其实是一个数据结构，但是它不一定放在保存对象内存页面的开始。通常会有一个保存SLAB管理头的SLAB，在Linux中，SLAB管理头用kmem_cache结构来表示，代码如下。</p><pre><code>struct array_cache {
    unsigned int avail;
    unsigned int limit;
    void *entry[]; 
};
struct kmem_cache {
    //是每个CPU一个array_cache类型的变量，cpu_cache是用于管理空闲对象的 
    struct array_cache __percpu *cpu_cache;
    unsigned int size; //cache大小
    slab_flags_t flags;//slab标志
    unsigned int num;//对象个数
    unsigned int gfporder;//分配内存页面的order
    gfp_t allocflags;
    size_t colour;//着色区大小
    unsigned int colour_off;//着色区的开始偏移
    const char *name;//本SLAB的名字
    struct list_head list;//所有的SLAB都要链接起来
    int refcount;//引用计数
    int object_size;//对象大小
    int align;//对齐大小
    struct kmem_cache_node *node[MAX_NUMNODES];//指向管理kmemcache的上层结构
};
</code></pre><p>上述代码中，有多少个CPU，就会有多少个array_cache类型的变量。这种为每个CPU构造一个变量副本的同步机制，就是<strong>每CPU变量</strong>（per-cpu-variable）。array_cache结构中"entry[]"表示了一个遵循LIFO顺序的数组，"avail"和"limit"分别指定了当前可用对象的数目和允许容纳对象的最大数目。</p><p><img src="https://static001.geekbang.org/resource/image/83/b6/8392800e70d37795c902b0d5dfebe5b6.jpg?wh=4008x2196" alt="" title="kmem_cache结构图解"></p><h3>第一个kmem_cache</h3><p>第一个kmem_cache是哪里来的呢？其实它是静态定义在代码中的，如下所示。</p><pre><code>static struct kmem_cache kmem_cache_boot = {
    .batchcount = 1,
    .limit = BOOT_CPUCACHE_ENTRIES,
    .shared = 1,
    .size = sizeof(struct kmem_cache),
    .name = &quot;kmem_cache&quot;,
};

void __init kmem_cache_init(void)
{
    int i;
    //指向静态定义的kmem_cache_boot
    kmem_cache = &amp;kmem_cache_boot;

    for (i = 0; i &lt; NUM_INIT_LISTS; i++)
        kmem_cache_node_init(&amp;init_kmem_cache_node[i]);
    //建立保存kmem_cache结构的kmem_cache
    create_boot_cache(kmem_cache, &quot;kmem_cache&quot;,
        offsetof(struct kmem_cache, node) +
                  nr_node_ids * sizeof(struct kmem_cache_node *),
                  SLAB_HWCACHE_ALIGN, 0, 0);
    //加入全局slab_caches链表中
    list_add(&amp;kmem_cache-&gt;list, &amp;slab_caches);
    {
        int nid;
        for_each_online_node(nid) {
            init_list(kmem_cache, &amp;init_kmem_cache_node[CACHE_CACHE + nid], nid);
            init_list(kmalloc_caches[KMALLOC_NORMAL][INDEX_NODE],                      &amp;init_kmem_cache_node[SIZE_NODE + nid], nid);
        }
    }
    //建立kmalloc函数使用的的kmem_cache
    create_kmalloc_caches(ARCH_KMALLOC_FLAGS);
}
</code></pre><h3>管理kmem_cache</h3><p>我们建好了第一个kmem_cache，以后kmem_cache越来越多，而且我们并没有看到kmem_cache结构中有任何指向内存页面的字段，但在kmem_cache结构中有个保存kmem_cache_node结构的指针数组。</p><p>kmem_cache_node结构是每个内存节点对应一个，它就是用来管理kmem_cache结构的，它开始是静态定义的，初始化时建立了第一个kmem_cache结构之后，init_list函数负责一个个分配内存空间，代码如下所示。</p><pre><code>#define NUM_INIT_LISTS (2 * MAX_NUMNODES)
//定义的kmem_cache_node结构数组
static struct kmem_cache_node __initdata init_kmem_cache_node[NUM_INIT_LISTS];

struct kmem_cache_node {
    spinlock_t list_lock;//自旋锁
    struct list_head slabs_partial;//有一部分空闲对象的kmem_cache结构
    struct list_head slabs_full;//没有空闲对象的kmem_cache结构
    struct list_head slabs_free;//对象全部空闲kmem_cache结构
    unsigned long total_slabs; //一共多少kmem_cache结构
    unsigned long free_slabs;  //空闲的kmem_cache结构
    unsigned long free_objects;//空闲的对象
    unsigned int free_limit;
};
static void __init init_list(struct kmem_cache *cachep, struct kmem_cache_node *list,
                int nodeid)
{
    struct kmem_cache_node *ptr;
    //分配新的 kmem_cache_node 结构的空间
    ptr = kmalloc_node(sizeof(struct kmem_cache_node), GFP_NOWAIT, nodeid);
    BUG_ON(!ptr);
    //复制初始时的静态kmem_cache_node结构
    memcpy(ptr, list, sizeof(struct kmem_cache_node));
    spin_lock_init(&amp;ptr-&gt;list_lock);
    MAKE_ALL_LISTS(cachep, ptr, nodeid);
    //设置kmem_cache_node的地址
    cachep-&gt;node[nodeid] = ptr;
}
</code></pre><p>我们第一次分配对象时，肯定没有对应的内存页面存放对象，那么SLAB模块就会调用<strong>cache_grow_begin函数</strong>获取内存页面，然后用获取的页面来存放对象，我们一起来看看代码。</p><pre><code>static void slab_map_pages(struct kmem_cache *cache, struct page *page,void *freelist)
{
    //页面结构指向kmem_cache结构
    page-&gt;slab_cache = cache;
    //指向空闲对象的链表
    page-&gt;freelist = freelist;
}
static struct page *cache_grow_begin(struct kmem_cache *cachep,
                gfp_t flags, int nodeid)
{
    void *freelist;
    size_t offset;
    gfp_t local_flags;
    int page_node;
    struct kmem_cache_node *n;
    struct page *page;

    WARN_ON_ONCE(cachep-&gt;ctor &amp;&amp; (flags &amp; __GFP_ZERO));
    local_flags = flags &amp; (GFP_CONSTRAINT_MASK|GFP_RECLAIM_MASK);
    //获取页面
    page = kmem_getpages(cachep, local_flags, nodeid);
    //获取页面所在的内存节点号
    page_node = page_to_nid(page);
    //根据内存节点获取对应kmem_cache_node结构
    n = get_node(cachep, page_node);
    //分配管理空闲对象的数据结构
    freelist = alloc_slabmgmt(cachep, page, offset,
            local_flags &amp; ~GFP_CONSTRAINT_MASK, page_node);
    //让页面中相关的字段指向kmem_cache和空闲对象
    slab_map_pages(cachep, page, freelist);
    //初始化空闲对象管理数据
    cache_init_objs(cachep, page);
    return page;
}

static void cache_grow_end(struct kmem_cache *cachep, struct page *page)
{
    struct kmem_cache_node *n;
    void *list = NULL;
    if (!page)
        return;
    //初始化结page构的slab_list链表
    INIT_LIST_HEAD(&amp;page-&gt;slab_list);
    //根据内存节点获取对应kmem_cache_node结构.
    n = get_node(cachep, page_to_nid(page));
    spin_lock(&amp;n-&gt;list_lock);
    //slab计数增加
    n-&gt;total_slabs++;
    if (!page-&gt;active) {
        //把这个page结构加入到kmem_cache_node结构的空闲链表中
        list_add_tail(&amp;page-&gt;slab_list, &amp;n-&gt;slabs_free);
        n-&gt;free_slabs++;
    } 
    spin_unlock(&amp;n-&gt;list_lock);
}
</code></pre><p>上述代码中的注释已经很清楚了，cache_grow_begin函数会为kmem_cache结构分配用来存放对象的页面，随后会调用与之对应的cache_grow_end函数，把这页面挂载到kmem_cache_node结构的链表中，并让页面指向kmem_cache结构。</p><p>这样kmem_cache_node，kmem_cache，page这三者之间就联系起来了。你再看一下后面的图，就更加清楚了。</p><p><img src="https://static001.geekbang.org/resource/image/e7/30/e7b479af38d5ed1ab00f35b4fe88fe30.jpg?wh=5437x3654" alt="" title="SLAB全局结构示意图"></p><p>上图中page可能是一组连续的pages，但是只会把第一个page挂载到kmem_cache_node中，同时，在slab_map_pages函数中又让page指向了kmem_cache。</p><p>但你要特别留意kmem_cache_node中的三个链表，它们分别挂载的pages，有一部分是空闲对象的page、还有对象全部都已经分配的page，以及全部都为空闲对象的page。这是为了提高分配时查找kmem_cache的性能。</p><h2>SLAB分配对象的过程</h2><p>有了前面对SLAB数据结构的了解，SLAB分配对象的过程你自己也能推导出来，无非是根据请求分配对象的大小，查找对应的kmem_cache结构，接着从这个结构中获取arry_cache结构，然后分配对象。</p><p>如果没有空闲对象了，就需要在kmem_cache对应的kmem_cache_node结构中查找有空闲对象的kmem_cache。如果还是没找到，最后就要分配内存页面新增kmem_cache结构了。</p><p><img src="https://static001.geekbang.org/resource/image/78/fe/78868f267073d4b0a8fb73b15bb41bfe.jpg?wh=2828x2700" alt="" title="SLAB分配对象的过程图解"></p><p>下面我们从接口开始了解这些过程。</p><h3>SLAB分配接口</h3><p>其实在Linux内核中，用的最多的是kmalloc函数，经常用于分配小的缓冲区，或者数据结构分配实例空间，这个函数就是SLAB分配接口，它是用来分配对象的，这个对象就是一小块内存空间。</p><p>下面一起来看看代码。</p><pre><code>static __always_inline void *__do_kmalloc(size_t size, gfp_t flags,unsigned long caller)
{
    struct kmem_cache *cachep;
    void *ret;
    if (unlikely(size &gt; KMALLOC_MAX_CACHE_SIZE))
        return NULL;
    //查找size对应的kmem_cache
    cachep = kmalloc_slab(size, flags);
    if (unlikely(ZERO_OR_NULL_PTR(cachep)))
        return cachep;
    //分配对象
    ret = slab_alloc(cachep, flags, caller);
    return ret;
}

void *__kmalloc(size_t size, gfp_t flags)
{
    return __do_kmalloc(size, flags, _RET_IP_);
}
static __always_inline void *kmalloc(size_t size, gfp_t flags)
{
    return __kmalloc(size, flags);
}
</code></pre><p>上面代码的流程很简单，就是在__do_kmalloc函数中，查找出分配大小对应的kmem_cache结构，然后调用slab_alloc函数进行分配。可以说，slab_alloc函数才是SLAB的接口函数，但是它的参数中<strong>必须要有kmem_cache结构</strong>。</p><p>具体是如何查找的呢？我们这就来看看。</p><h3>如何查找kmem_cache结构</h3><p>由于SLAB的接口函数slab_alloc，它的参数中必须要有kmem_cache结构指针，指定从哪个kmem_cache结构分配对象，所以在调用slab_alloc函数之前必须给出kmem_cache结构。</p><p>我们怎么查找到它呢？这就需要调用kmalloc_slab函数了，代码如下所示。</p><pre><code>enum kmalloc_cache_type {
    KMALLOC_NORMAL = 0,
    KMALLOC_RECLAIM,
#ifdef CONFIG_ZONE_DMA
    KMALLOC_DMA,
#endif
    NR_KMALLOC_TYPES
};
struct kmem_cache *kmalloc_caches[NR_KMALLOC_TYPES][KMALLOC_SHIFT_HIGH + 1] __ro_after_init ={ static u8 size_index[24] __ro_after_init = {
    3,  /* 8 */
    4,  /* 16 */
    5,  /* 24 */
    5,  /* 32 */
    6,  /* 40 */
    6,  /* 48 */
    6,  /* 56 */
    6,  /* 64 */
    1,  /* 72 */
    1,  /* 80 */
    1,  /* 88 */
    1,  /* 96 */
    7,  /* 104 */
    7,  /* 112 */
    7,  /* 120 */
    7,  /* 128 */
    2,  /* 136 */
    2,  /* 144 */
    2,  /* 152 */
    2,  /* 160 */
    2,  /* 168 */
    2,  /* 176 */
    2,  /* 184 */
    2   /* 192 */
};
//根据分配标志返回枚举类型，其实是0、1、2其中之一
static __always_inline enum kmalloc_cache_type kmalloc_type(gfp_t flags)
{
#ifdef CONFIG_ZONE_DMA
    if (likely((flags &amp; (__GFP_DMA | __GFP_RECLAIMABLE)) == 0))
        return KMALLOC_NORMAL;
    return flags &amp; __GFP_DMA ? KMALLOC_DMA : KMALLOC_RECLAIM;
#else
    return flags &amp; __GFP_RECLAIMABLE ? KMALLOC_RECLAIM : KMALLOC_NORMAL;
#endif
}
struct kmem_cache *kmalloc_slab(size_t size, gfp_t flags)
{
    unsigned int index;
    //计算出index
    if (size &lt;= 192) {
        if (!size)
            return ZERO_SIZE_PTR;
        index = size_index[size_index_elem(size)];
    } else {
        if (WARN_ON_ONCE(size &gt; KMALLOC_MAX_CACHE_SIZE))
            return NULL;
        index = fls(size - 1);
    }
    return kmalloc_caches[kmalloc_type(flags)][index];
}
</code></pre><p>从上述代码，不难发现kmalloc_caches就是个全局的二维数组，kmalloc_slab函数只是根据分配大小和分配标志计算出了数组下标，最后取出其中kmem_cache结构指针。</p><p>那么kmalloc_caches中的kmem_cache，它又是谁建立的呢？我们还是接着看代码。</p><pre><code>struct kmem_cache *__init create_kmalloc_cache(const char *name,
        unsigned int size, slab_flags_t flags,
        unsigned int useroffset, unsigned int usersize)
{
    //从第一个kmem_cache中分配一个对象放kmem_cache
    struct kmem_cache *s = kmem_cache_zalloc(kmem_cache, GFP_NOWAIT);

    if (!s)
        panic(&quot;Out of memory when creating slab %s\n&quot;, name);
    //设置s的对齐参数，处理s的freelist就是arr_cache
    create_boot_cache(s, name, size, flags, useroffset, usersize);
    list_add(&amp;s-&gt;list, &amp;slab_caches);
    s-&gt;refcount = 1;
    return s;
}
//新建一个kmem_cache
static void __init new_kmalloc_cache(int idx, enum kmalloc_cache_type type, slab_flags_t flags)
{
    if (type == KMALLOC_RECLAIM)
        flags |= SLAB_RECLAIM_ACCOUNT;
        //根据kmalloc_info中信息建立一个kmem_cache
    kmalloc_caches[type][idx] = create_kmalloc_cache(
                    kmalloc_info[idx].name[type],
                    kmalloc_info[idx].size, flags, 0,
                    kmalloc_info[idx].size);
}
//建立所有的kmalloc_caches中的kmem_cache
void __init create_kmalloc_caches(slab_flags_t flags)
{
    int i;
    enum kmalloc_cache_type type;
    for (type = KMALLOC_NORMAL; type &lt;= KMALLOC_RECLAIM; type++) {
        for (i = KMALLOC_SHIFT_LOW; i &lt;= KMALLOC_SHIFT_HIGH; i++) {
            if (!kmalloc_caches[type][i])
                //建立一个新的kmem_cache
                new_kmalloc_cache(i, type, flags);
            if (KMALLOC_MIN_SIZE &lt;= 32 &amp;&amp; i == 6 &amp;&amp;
                    !kmalloc_caches[type][1])
                new_kmalloc_cache(1, type, flags);
            if (KMALLOC_MIN_SIZE &lt;= 64 &amp;&amp; i == 7 &amp;&amp;
                    !kmalloc_caches[type][2])
                new_kmalloc_cache(2, type, flags);
        }
    }
}
</code></pre><p>到这里，__do_kmalloc函数中根据分配对象大小查找的所有kmem_cache结构，我们就建立好了，保存在kmalloc_caches数组中。下面我们再去看看对象是如何分配的。</p><h3>分配对象</h3><p>下面我们从slab_alloc函数开始探索对象的分配过程，slab_alloc函数的第一个参数就kmem_cache结构的指针，表示从该kmem_cache结构中分配对象。</p><pre><code>static __always_inline void *slab_alloc(struct kmem_cache *cachep, gfp_t flags, unsigned long caller)
{
    unsigned long save_flags;
    void *objp;
    //关中断
    local_irq_save(save_flags);
    //分配对象
    objp = __do_cache_alloc(cachep, flags);
    //恢复中断
    local_irq_restore(save_flags);
    return objp;
}
</code></pre><p>接口函数总是简单的，真正干活的是__do_cache_alloc函数，下面我们就来看看这个函数。</p><pre><code>static inline void *____cache_alloc(struct kmem_cache *cachep, gfp_t flags)
{
    void *objp;
    struct array_cache *ac;
    //获取当前cpu在cachep结构中的array_cache结构的指针
    ac = cpu_cache_get(cachep);
    //如果ac中的avail不为0,说明当前kmem_cache结构中freelist是有空闲对象
    if (likely(ac-&gt;avail)) {
        ac-&gt;touched = 1;
        //空间对象的地址保存在ac-&gt;entry
        objp = ac-&gt;entry[--ac-&gt;avail];
        goto out;
    }
    objp = cache_alloc_refill(cachep, flags);
out:
    return objp;
}
static __always_inline void *__do_cache_alloc(struct kmem_cache *cachep, gfp_t flags)
{
    return ____cache_alloc(cachep, flags);
}
</code></pre><p>上述代码中真正做事的函数是<strong>____cache_alloc函数</strong>，它首先获取了当前kmem_cache结构中指向array_cache结构的指针，找到它里面空闲对象的地址（如果你不懂array_cache结构，请回到SLAB对象那一小节复习），然后在array_cache结构中取出一个空闲对象地址返回，这样就分配成功了。</p><p>这个速度是很快的，如果array_cache结构中没有空闲对象了，就会调用cache_alloc_refill函数。那这个函数又干了什么呢？我们接着往下看。代码如下所示。</p><pre><code>static struct page *get_first_slab(struct kmem_cache_node *n, bool pfmemalloc)
{
    struct page *page;
    assert_spin_locked(&amp;n-&gt;list_lock);
    //首先从kmem_cache_node结构中的slabs_partial链表上查看有没有page
    page = list_first_entry_or_null(&amp;n-&gt;slabs_partial, struct page,slab_list);
    if (!page) {
    //如果没有
        n-&gt;free_touched = 1;
    //从kmem_cache_node结构中的slabs_free链表上查看有没有page
        page = list_first_entry_or_null(&amp;n-&gt;slabs_free, struct page,slab_list);
        if (page)
            n-&gt;free_slabs--; //空闲slab计数减一
    }
    //返回page
    return page;
}
static void *cache_alloc_refill(struct kmem_cache *cachep, gfp_t flags)
{
    int batchcount;
    struct kmem_cache_node *n;
    struct array_cache *ac, *shared;
    int node;
    void *list = NULL;
    struct page *page;
    //获取内存节点
    node = numa_mem_id();
    ac = cpu_cache_get(cachep);
    batchcount = ac-&gt;batchcount;
    //获取cachep所属的kmem_cache_node
    n = get_node(cachep, node);
    shared = READ_ONCE(n-&gt;shared);
    if (!n-&gt;free_objects &amp;&amp; (!shared || !shared-&gt;avail))
        goto direct_grow;
    while (batchcount &gt; 0) {
        //获取kmem_cache_node结构中其它kmem_cache,返回的是page，而page会指向kmem_cache
        page = get_first_slab(n, false);
        if (!page)
            goto must_grow;
        batchcount = alloc_block(cachep, ac, page, batchcount);
    }
must_grow:
    n-&gt;free_objects -= ac-&gt;avail;
direct_grow:
    if (unlikely(!ac-&gt;avail)) {
        //分配新的kmem_cache并初始化
        page = cache_grow_begin(cachep, gfp_exact_node(flags), node);
        ac = cpu_cache_get(cachep);
        if (!ac-&gt;avail &amp;&amp; page)
            alloc_block(cachep, ac, page, batchcount);
        //让page挂载到kmem_cache_node结构的slabs_list链表上
        cache_grow_end(cachep, page);
        if (!ac-&gt;avail)
            return NULL;
    }
    ac-&gt;touched = 1;
    //重新分配
    return ac-&gt;entry[--ac-&gt;avail];
}
</code></pre><p>调用cache_alloc_refill函数的过程，主要的工作都有哪些呢？我给你梳理一下。</p><p>首先，获取了cachep所属的kmem_cache_node。</p><p>然后调用get_first_slab，获取kmem_cache_node结构还有没有包含空闲对象的kmem_cache。但是请注意，这里返回的是page，因为page会指向kmem_cache结构，page所代表的物理内存页面，也保存着kmem_cache结构中的对象。</p><p>最后，如果kmem_cache_node结构没有包含空闲对象的kmem_cache了，就必须调用cache_grow_begin函数，找伙伴系统分配新的内存页面，而且还要找第一个kmem_cache分配新的对象，来存放kmem_cache结构的实例变量，并进行必要的初始化。</p><p>这些步骤完成之后，再调用cache_grow_end函数，把刚刚分配的page挂载到kmem_cache_node结构的slabs_list链表上。因为cache_grow_begin和cache_grow_end函数在前面已经分析过了，这里不再赘述。</p><h2>重点回顾</h2><p>今天的内容讲完了，我来帮你梳理一下本课程的重点。</p><p>1.为了分配小于1个page的小块内存，Linux实现了SLAB，用kmem_cache结构管理page对应内存页面上小块内存对象，然后让该page指向kmem_cache，由kmem_cache_node结构管理多个page。</p><p>2.我们从Linux内核中使用的kmalloc函数入手，了解了SLAB下整个内存对象的分配过程。</p><p>到此为止，我们对SLAB的研究就告一段落了，是不是感觉和Cosmos内存管理有些相像而又不同呢？甚至我们Cosmos内存管理要更为简洁和高效。</p><h2>思考题</h2><p>Linux的SLAB，使用kmalloc函数能分配多大的内存对象呢？</p><p>欢迎你在留言区跟我交流互动，也欢迎你把这节课分享给你的同事、朋友，跟他一起研究SLAB相关的内容。</p><p>我是LMOS，我们下节课见！</p>