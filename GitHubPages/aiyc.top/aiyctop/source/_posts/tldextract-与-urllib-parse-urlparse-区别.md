---
title: tldextract 与 urllib.parse.urlparse 区别
tags: []
id: '1477'
categories:
  - - 技术杂谈
date: 2021-02-20 11:02:02
---

## 文件：links\_list.txt

```text
//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico
../static/img/favicon.ico
//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_468795d.css
//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_415cfee.css
https://www.baidu.com/
http://tieba.baidu.com/
https://zhidao.baidu.com/
http://music.baidu.com/
http://image.baidu.com/
http://v.baidu.com/
http://map.baidu.com/
http://wenku.baidu.com/
http://news.baidu.com/
//help.baidu.com
/
/guonei
/guoji
/mil
/finance
/ent
/sports
/internet
/tech
/game
/lady
/auto
/house
/
/guonei
/guoji
/mil
/finance
/ent
/sports
/internet
/tech
/game
/lady
/auto
/house
javascript:void(0);
javascript:void(0);
javascript:void(0);
http://www.xinhuanet.com/politics/leaders/2021-02/19/c_1127116367.htm
https://news.cctv.com/2021/02/18/ARTI0oS4jOZhFlwrMpSoGgO4210218.shtml
https://xhpfmapi.zhongguowangshi.com/vh512/share/9774794?channel=weixin
http://m.news.cctv.com/2021/02/16/ARTI9eVg1dwru0Ocmui7i0I1210216.shtml
http://m.news.cctv.com/2021/02/17/ARTIDhJalPvA8jlxyPNo1zG8210217.shtml
https://cn.chinadaily.com.cn/a/202102/19/WS602f7010a3101e7ce97401f8.html
http://www.ce.cn/xwzx/gnsz/gdxw/202102/19/t20210219_36319873.shtml
https://wap.peopleapp.com/article/6137376/6044308
http://baijiahao.baidu.com/s?id=1692172482372438662
http://baijiahao.baidu.com/s?id=1692112492256036454
http://baijiahao.baidu.com/s?id=1692113817177132737
http://baijiahao.baidu.com/s?id=1692167966517789469
http://baijiahao.baidu.com/s?id=1692169295846378065
http://baijiahao.baidu.com/s?id=1692168717836498590
http://baijiahao.baidu.com/s?id=1692171361260104000
http://baijiahao.baidu.com/s?id=1692171751149486104
http://baijiahao.baidu.com/s?id=1692171314329445883
https://baijiahao.baidu.com/s?id=1692164857126287148&wfr=content
http://baijiahao.baidu.com/s?id=1692171148298779099
http://baijiahao.baidu.com/s?id=1692169521956174639
http://baijiahao.baidu.com/s?id=1692171992858859962
http://baijiahao.baidu.com/s?id=1692167169560507810
http://baijiahao.baidu.com/s?id=1692169809003390085
http://baijiahao.baidu.com/s?id=1692163989733193905
http://baijiahao.baidu.com/s?id=1692168733538070229
?https://baijiahao.baidu.com/s?id=1692169536381777496&wfr=content
http://baijiahao.baidu.com/s?id=1692173757432852305
https://baijiahao.baidu.com/s?id=1692169651221340372&wfr=content
https://baijiahao.baidu.com/s?id=1692169095355879035&wfr=content
https://baijiahao.baidu.com/s?id=1692167775139335655&wfr=content
http://baijiahao.baidu.com/s?id=1692113216751012397
http://baijiahao.baidu.com/s?id=1692122029239116348
http://baijiahao.baidu.com/s?id=1692172397154756713
http://baijiahao.baidu.com/s?id=1692083862859520821
http://baijiahao.baidu.com/s?id=1692167449252468281
http://baijiahao.baidu.com/s?id=1692166281928400927
https://baijiahao.baidu.com/s?id=1692124607631097118&wfr=content
https://baijiahao.baidu.com/s?id=1692107973786509140&wfr=content
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
http://www.qstheory.cn/zt2020/llxjj/index.htm
https://www.baidu.com/s?wd=%E4%B8%AD%E7%BE%8E%E5%85%83%E9%A6%96%E9%80%9A%E8%AF%9D%EF%BC%8C%E4%B8%96%E7%95%8C%E6%8E%A5%E6%94%B6%E5%88%B0%E8%BF%99%E4%BA%9B%E7%A7%AF%E6%9E%81%E4%BF%A1%E5%8F%B7
https://www.baidu.com/s?wd=%E5%BC%95%E7%BB%8F%E6%8D%AE%E5%85%B8%E8%AF%9D%E6%96%B0%E6%98%A5%EF%BC%81%E5%93%81%E8%AF%BB%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%BC%95%E7%94%A8%E7%9A%84%E8%AF%97%E8%AF%8D%E4%B9%8B%E7%BE%8E
https://www.baidu.com/s?wd=%E4%B8%AD%E5%8D%B0%E5%8A%A0%E5%8B%92%E4%B8%87%E6%B2%B3%E8%B0%B7%E5%86%B2%E7%AA%81%E7%8E%B0%E5%9C%BA%E8%A7%86%E9%A2%91%E5%85%AC%E5%BC%80
https://www.baidu.com/s?wd=%E5%9B%BD%E9%98%B2%E9%83%A8%E5%9B%9E%E5%BA%94%E4%B8%BA%E4%BD%95%E5%85%AC%E5%B8%83%E8%A7%A3%E6%94%BE%E5%86%9B%E4%BC%A4%E4%BA%A1%E6%83%85%E5%86%B5
https://www.baidu.com/s?wd=2021%E5%B9%B4%E9%AB%98%E8%80%83%E6%97%B6%E9%97%B4%E7%A1%AE%E5%AE%9A
https://www.baidu.com/s?wd=%E7%BE%8E%E7%A7%B0%E5%B0%86%E7%BB%B4%E6%8C%81%E5%AF%B9%E5%8D%8E%E5%8A%A0%E5%BE%81%E5%85%B3%E7%A8%8E%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94
https://www.baidu.com/s?wd=%E4%B8%AD%E7%BA%AA%E5%A7%94%E8%AF%84%E8%AE%BA%E4%BD%A0%E5%A5%BD%E6%9D%8E%E7%84%95%E8%8B%B1
https://www.baidu.com/s?wd=%E7%94%B7%E5%AD%90%E9%81%9B%E5%BC%AF%E5%8F%91%E7%8E%B03%E5%B9%B4%E5%89%8D%E4%B8%A2%E7%9A%84%E6%89%8B%E6%9C%BA
https://www.baidu.com/s?wd=%E7%BE%8E%E5%9B%BD%E6%9C%80%E8%80%81%E5%B0%91%E5%B9%B4%E7%8A%AF%E6%9C%8D%E5%88%9168%E5%B9%B4%E5%90%8E%E5%87%BA%E7%8B%B1
https://www.baidu.com/s?wd=%E9%9F%A9%E5%9B%BD%E5%A5%B3%E5%AD%90%E5%92%AC%E6%8E%89%E6%80%A7%E4%BE%B5%E8%80%85%E8%88%8C%E5%A4%B4%E8%A2%AB%E5%88%A4%E6%97%A0%E7%BD%AA
http://baijiahao.baidu.com/s?id=1692116658709020854
http://baijiahao.baidu.com/s?id=1692116658709020854
http://baijiahao.baidu.com/s?id=1692109250462039445
http://baijiahao.baidu.com/s?id=1692109250462039445
http://baijiahao.baidu.com/s?id=1692111540627913377
http://baijiahao.baidu.com/s?id=1692111540627913377
http://baijiahao.baidu.com/s?id=1692039431890680523
http://baijiahao.baidu.com/s?id=1692099318073102003
http://baijiahao.baidu.com/s?id=1692114372183650477
http://baijiahao.baidu.com/s?id=1692083156262934113
http://baijiahao.baidu.com/s?id=1692087263316422208
https://baijiahao.baidu.com/s?id=1692042747404671829
http://baijiahao.baidu.com/s?id=1692115483967351388
http://baijiahao.baidu.com/s?id=1692032530350714205
http://baijiahao.baidu.com/s?id=1692093241461734361
http://baijiahao.baidu.com/s?id=1692088091088867927
http://baijiahao.baidu.com/s?id=1692087627448472669
http://baijiahao.baidu.com/s?id=1692113189788229863
http://baijiahao.baidu.com/s?id=1692118773264002841
https://baijiahao.baidu.com/s?id=1692086035058445203&wfr=content
http://baijiahao.baidu.com/s?id=1692046936333798310
http://baijiahao.baidu.com/s?id=1692118668680608984
http://baijiahao.baidu.com/s?id=1692113487955330666
http://baijiahao.baidu.com/s?id=1692113487955330666


http://www.piyao.org.cn/yybgt/index.htm
http://report.12377.cn:13225/toreportinputNormal_anis.do
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
javascript:void(0);
http://downpack.baidu.com/baidunews_AndroidPhone_1014720b.apk
https://itunes.apple.com/cn/app/id482820737
//news-bos.cdn.bcebos.com/mvideo/baidu_news_protocol.html
https://news-bos.cdn.bcebos.com/mvideo/privacy.html
//help.baidu.com/newadd?prod_id=5&category=1
//news-bos.cdn.bcebos.com/mvideo/pcnews_licence.html
//www.baidu.com/duty/
http://net.china.cn/chinese/index.htm
http://www.cyberpolice.cn/wfjb/
http://www.bjjubao.org/
#{url}
#{url}
/sh
javascript:void(0);
/sh
#{url}
/sh
#{url}
#{url}
#{url}
#{url}
#{url}
#{url}
#{url}
#{url}
#{url}

```

## tldextract 代码

```python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:37 上午
# @Author  : AI悦创
# @FileName: 测试代码.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
import tldextract

news_links = []
with open("links_list.txt", "r")as f:
    link_list_text = f.readlines()
    print(link_list_text)
    print(len(link_list_text))
    for link in link_list_text:
        if not link.startswith("http"):
            continue
        tld = tldextract.extract(link)
        print(tld)
```

```python
/usr/local/bin/python3 /Users/apple/PycharmProjects/Coder/Python3_WebCrawler_Coder/测试代码.py
['//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico\n', '../static/img/favicon.ico\n', '//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_468795d.css\n', '//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_415cfee.css\n', 'https://www.baidu.com/\n', 'http://tieba.baidu.com/\n', 'https://zhidao.baidu.com/\n', 'http://music.baidu.com/\n', 'http://image.baidu.com/\n', 'http://v.baidu.com/\n', 'http://map.baidu.com/\n', 'http://wenku.baidu.com/\n', 'http://news.baidu.com/\n', '//help.baidu.com\n', '/\n', '/guonei\n', '/guoji\n', '/mil\n', '/finance\n', '/ent\n', '/sports\n', '/internet\n', '/tech\n', '/game\n', '/lady\n', '/auto\n', '/house\n', '/\n', '/guonei\n', '/guoji\n', '/mil\n', '/finance\n', '/ent\n', '/sports\n', '/internet\n', '/tech\n', '/game\n', '/lady\n', '/auto\n', '/house\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'http://www.xinhuanet.com/politics/leaders/2021-02/19/c_1127116367.htm\n', 'https://news.cctv.com/2021/02/18/ARTI0oS4jOZhFlwrMpSoGgO4210218.shtml\n', 'https://xhpfmapi.zhongguowangshi.com/vh512/share/9774794?channel=weixin\n', 'http://m.news.cctv.com/2021/02/16/ARTI9eVg1dwru0Ocmui7i0I1210216.shtml\n', 'http://m.news.cctv.com/2021/02/17/ARTIDhJalPvA8jlxyPNo1zG8210217.shtml\n', 'https://cn.chinadaily.com.cn/a/202102/19/WS602f7010a3101e7ce97401f8.html\n', 'http://www.ce.cn/xwzx/gnsz/gdxw/202102/19/t20210219_36319873.shtml\n', 'https://wap.peopleapp.com/article/6137376/6044308\n', 'http://baijiahao.baidu.com/s?id=1692172482372438662\n', 'http://baijiahao.baidu.com/s?id=1692112492256036454\n', 'http://baijiahao.baidu.com/s?id=1692113817177132737\n', 'http://baijiahao.baidu.com/s?id=1692167966517789469\n', 'http://baijiahao.baidu.com/s?id=1692169295846378065\n', 'http://baijiahao.baidu.com/s?id=1692168717836498590\n', 'http://baijiahao.baidu.com/s?id=1692171361260104000\n', 'http://baijiahao.baidu.com/s?id=1692171751149486104\n', 'http://baijiahao.baidu.com/s?id=1692171314329445883\n', 'https://baijiahao.baidu.com/s?id=1692164857126287148&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692171148298779099\n', 'http://baijiahao.baidu.com/s?id=1692169521956174639\n', 'http://baijiahao.baidu.com/s?id=1692171992858859962\n', 'http://baijiahao.baidu.com/s?id=1692167169560507810\n', 'http://baijiahao.baidu.com/s?id=1692169809003390085\n', 'http://baijiahao.baidu.com/s?id=1692163989733193905\n', 'http://baijiahao.baidu.com/s?id=1692168733538070229\n', '?https://baijiahao.baidu.com/s?id=1692169536381777496&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692173757432852305\n', 'https://baijiahao.baidu.com/s?id=1692169651221340372&wfr=content\n', 'https://baijiahao.baidu.com/s?id=1692169095355879035&wfr=content\n', 'https://baijiahao.baidu.com/s?id=1692167775139335655&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692113216751012397\n', 'http://baijiahao.baidu.com/s?id=1692122029239116348\n', 'http://baijiahao.baidu.com/s?id=1692172397154756713\n', 'http://baijiahao.baidu.com/s?id=1692083862859520821\n', 'http://baijiahao.baidu.com/s?id=1692167449252468281\n', 'http://baijiahao.baidu.com/s?id=1692166281928400927\n', 'https://baijiahao.baidu.com/s?id=1692124607631097118&wfr=content\n', 'https://baijiahao.baidu.com/s?id=1692107973786509140&wfr=content\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'http://www.qstheory.cn/zt2020/llxjj/index.htm\n', 'https://www.baidu.com/s?wd=%E4%B8%AD%E7%BE%8E%E5%85%83%E9%A6%96%E9%80%9A%E8%AF%9D%EF%BC%8C%E4%B8%96%E7%95%8C%E6%8E%A5%E6%94%B6%E5%88%B0%E8%BF%99%E4%BA%9B%E7%A7%AF%E6%9E%81%E4%BF%A1%E5%8F%B7\n', 'https://www.baidu.com/s?wd=%E5%BC%95%E7%BB%8F%E6%8D%AE%E5%85%B8%E8%AF%9D%E6%96%B0%E6%98%A5%EF%BC%81%E5%93%81%E8%AF%BB%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%BC%95%E7%94%A8%E7%9A%84%E8%AF%97%E8%AF%8D%E4%B9%8B%E7%BE%8E\n', 'https://www.baidu.com/s?wd=%E4%B8%AD%E5%8D%B0%E5%8A%A0%E5%8B%92%E4%B8%87%E6%B2%B3%E8%B0%B7%E5%86%B2%E7%AA%81%E7%8E%B0%E5%9C%BA%E8%A7%86%E9%A2%91%E5%85%AC%E5%BC%80\n', 'https://www.baidu.com/s?wd=%E5%9B%BD%E9%98%B2%E9%83%A8%E5%9B%9E%E5%BA%94%E4%B8%BA%E4%BD%95%E5%85%AC%E5%B8%83%E8%A7%A3%E6%94%BE%E5%86%9B%E4%BC%A4%E4%BA%A1%E6%83%85%E5%86%B5\n', 'https://www.baidu.com/s?wd=2021%E5%B9%B4%E9%AB%98%E8%80%83%E6%97%B6%E9%97%B4%E7%A1%AE%E5%AE%9A\n', 'https://www.baidu.com/s?wd=%E7%BE%8E%E7%A7%B0%E5%B0%86%E7%BB%B4%E6%8C%81%E5%AF%B9%E5%8D%8E%E5%8A%A0%E5%BE%81%E5%85%B3%E7%A8%8E%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94\n', 'https://www.baidu.com/s?wd=%E4%B8%AD%E7%BA%AA%E5%A7%94%E8%AF%84%E8%AE%BA%E4%BD%A0%E5%A5%BD%E6%9D%8E%E7%84%95%E8%8B%B1\n', 'https://www.baidu.com/s?wd=%E7%94%B7%E5%AD%90%E9%81%9B%E5%BC%AF%E5%8F%91%E7%8E%B03%E5%B9%B4%E5%89%8D%E4%B8%A2%E7%9A%84%E6%89%8B%E6%9C%BA\n', 'https://www.baidu.com/s?wd=%E7%BE%8E%E5%9B%BD%E6%9C%80%E8%80%81%E5%B0%91%E5%B9%B4%E7%8A%AF%E6%9C%8D%E5%88%9168%E5%B9%B4%E5%90%8E%E5%87%BA%E7%8B%B1\n', 'https://www.baidu.com/s?wd=%E9%9F%A9%E5%9B%BD%E5%A5%B3%E5%AD%90%E5%92%AC%E6%8E%89%E6%80%A7%E4%BE%B5%E8%80%85%E8%88%8C%E5%A4%B4%E8%A2%AB%E5%88%A4%E6%97%A0%E7%BD%AA\n', 'http://baijiahao.baidu.com/s?id=1692116658709020854\n', 'http://baijiahao.baidu.com/s?id=1692116658709020854\n', 'http://baijiahao.baidu.com/s?id=1692109250462039445\n', 'http://baijiahao.baidu.com/s?id=1692109250462039445\n', 'http://baijiahao.baidu.com/s?id=1692111540627913377\n', 'http://baijiahao.baidu.com/s?id=1692111540627913377\n', 'http://baijiahao.baidu.com/s?id=1692039431890680523\n', 'http://baijiahao.baidu.com/s?id=1692099318073102003\n', 'http://baijiahao.baidu.com/s?id=1692114372183650477\n', 'http://baijiahao.baidu.com/s?id=1692083156262934113\n', 'http://baijiahao.baidu.com/s?id=1692087263316422208\n', 'https://baijiahao.baidu.com/s?id=1692042747404671829\n', 'http://baijiahao.baidu.com/s?id=1692115483967351388\n', 'http://baijiahao.baidu.com/s?id=1692032530350714205\n', 'http://baijiahao.baidu.com/s?id=1692093241461734361\n', 'http://baijiahao.baidu.com/s?id=1692088091088867927\n', 'http://baijiahao.baidu.com/s?id=1692087627448472669\n', 'http://baijiahao.baidu.com/s?id=1692113189788229863\n', 'http://baijiahao.baidu.com/s?id=1692118773264002841\n', 'https://baijiahao.baidu.com/s?id=1692086035058445203&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692046936333798310\n', 'http://baijiahao.baidu.com/s?id=1692118668680608984\n', 'http://baijiahao.baidu.com/s?id=1692113487955330666\n', 'http://baijiahao.baidu.com/s?id=1692113487955330666\n', '\n', '\n', 'http://www.piyao.org.cn/yybgt/index.htm\n', 'http://report.12377.cn:13225/toreportinputNormal_anis.do\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'http://downpack.baidu.com/baidunews_AndroidPhone_1014720b.apk\n', 'https://itunes.apple.com/cn/app/id482820737\n', '//news-bos.cdn.bcebos.com/mvideo/baidu_news_protocol.html\n', 'https://news-bos.cdn.bcebos.com/mvideo/privacy.html\n', '//help.baidu.com/newadd?prod_id=5&category=1\n', '//news-bos.cdn.bcebos.com/mvideo/pcnews_licence.html\n', '//www.baidu.com/duty/\n', 'http://net.china.cn/chinese/index.htm\n', 'http://www.cyberpolice.cn/wfjb/\n', 'http://www.bjjubao.org/\n', '#{url}\n', '#{url}\n', '/sh\n', 'javascript:void(0);\n', '/sh\n', '#{url}\n', '/sh\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n']
165
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='tieba', domain='baidu', suffix='com')
ExtractResult(subdomain='zhidao', domain='baidu', suffix='com')
ExtractResult(subdomain='music', domain='baidu', suffix='com')
ExtractResult(subdomain='image', domain='baidu', suffix='com')
ExtractResult(subdomain='v', domain='baidu', suffix='com')
ExtractResult(subdomain='map', domain='baidu', suffix='com')
ExtractResult(subdomain='wenku', domain='baidu', suffix='com')
ExtractResult(subdomain='news', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='xinhuanet', suffix='com')
ExtractResult(subdomain='news', domain='cctv', suffix='com')
ExtractResult(subdomain='xhpfmapi', domain='zhongguowangshi', suffix='com')
ExtractResult(subdomain='m.news', domain='cctv', suffix='com')
ExtractResult(subdomain='m.news', domain='cctv', suffix='com')
ExtractResult(subdomain='cn', domain='chinadaily', suffix='com.cn')
ExtractResult(subdomain='www', domain='ce', suffix='cn')
ExtractResult(subdomain='wap', domain='peopleapp', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='qstheory', suffix='cn')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='baijiahao', domain='baidu', suffix='com')
ExtractResult(subdomain='www', domain='piyao', suffix='org.cn')
ExtractResult(subdomain='report', domain='12377', suffix='cn')
ExtractResult(subdomain='downpack', domain='baidu', suffix='com')
ExtractResult(subdomain='itunes', domain='apple', suffix='com')
ExtractResult(subdomain='news-bos.cdn', domain='bcebos', suffix='com')
ExtractResult(subdomain='net', domain='china', suffix='cn')
ExtractResult(subdomain='www', domain='cyberpolice', suffix='cn')
ExtractResult(subdomain='www', domain='bjjubao', suffix='org')

Process finished with exit code 0
```

## urllib.parse.urlparse

```python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:37 上午
# @Author  : AI悦创
# @FileName: 测试代码.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
from urllib.parse import urlparse

news_links = []
with open("links_list.txt", "r")as f:
    link_list_text = f.readlines()
    print(link_list_text)
    print(len(link_list_text))
    for link in link_list_text:
        if not link.startswith("http"):
            continue
        print(urlparse(link))
```

```python
/usr/local/bin/python3 /Users/apple/PycharmProjects/Coder/Python3_WebCrawler_Coder/测试代码.py
['//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico\n', '../static/img/favicon.ico\n', '//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_468795d.css\n', '//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_415cfee.css\n', 'https://www.baidu.com/\n', 'http://tieba.baidu.com/\n', 'https://zhidao.baidu.com/\n', 'http://music.baidu.com/\n', 'http://image.baidu.com/\n', 'http://v.baidu.com/\n', 'http://map.baidu.com/\n', 'http://wenku.baidu.com/\n', 'http://news.baidu.com/\n', '//help.baidu.com\n', '/\n', '/guonei\n', '/guoji\n', '/mil\n', '/finance\n', '/ent\n', '/sports\n', '/internet\n', '/tech\n', '/game\n', '/lady\n', '/auto\n', '/house\n', '/\n', '/guonei\n', '/guoji\n', '/mil\n', '/finance\n', '/ent\n', '/sports\n', '/internet\n', '/tech\n', '/game\n', '/lady\n', '/auto\n', '/house\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'http://www.xinhuanet.com/politics/leaders/2021-02/19/c_1127116367.htm\n', 'https://news.cctv.com/2021/02/18/ARTI0oS4jOZhFlwrMpSoGgO4210218.shtml\n', 'https://xhpfmapi.zhongguowangshi.com/vh512/share/9774794?channel=weixin\n', 'http://m.news.cctv.com/2021/02/16/ARTI9eVg1dwru0Ocmui7i0I1210216.shtml\n', 'http://m.news.cctv.com/2021/02/17/ARTIDhJalPvA8jlxyPNo1zG8210217.shtml\n', 'https://cn.chinadaily.com.cn/a/202102/19/WS602f7010a3101e7ce97401f8.html\n', 'http://www.ce.cn/xwzx/gnsz/gdxw/202102/19/t20210219_36319873.shtml\n', 'https://wap.peopleapp.com/article/6137376/6044308\n', 'http://baijiahao.baidu.com/s?id=1692172482372438662\n', 'http://baijiahao.baidu.com/s?id=1692112492256036454\n', 'http://baijiahao.baidu.com/s?id=1692113817177132737\n', 'http://baijiahao.baidu.com/s?id=1692167966517789469\n', 'http://baijiahao.baidu.com/s?id=1692169295846378065\n', 'http://baijiahao.baidu.com/s?id=1692168717836498590\n', 'http://baijiahao.baidu.com/s?id=1692171361260104000\n', 'http://baijiahao.baidu.com/s?id=1692171751149486104\n', 'http://baijiahao.baidu.com/s?id=1692171314329445883\n', 'https://baijiahao.baidu.com/s?id=1692164857126287148&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692171148298779099\n', 'http://baijiahao.baidu.com/s?id=1692169521956174639\n', 'http://baijiahao.baidu.com/s?id=1692171992858859962\n', 'http://baijiahao.baidu.com/s?id=1692167169560507810\n', 'http://baijiahao.baidu.com/s?id=1692169809003390085\n', 'http://baijiahao.baidu.com/s?id=1692163989733193905\n', 'http://baijiahao.baidu.com/s?id=1692168733538070229\n', '?https://baijiahao.baidu.com/s?id=1692169536381777496&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692173757432852305\n', 'https://baijiahao.baidu.com/s?id=1692169651221340372&wfr=content\n', 'https://baijiahao.baidu.com/s?id=1692169095355879035&wfr=content\n', 'https://baijiahao.baidu.com/s?id=1692167775139335655&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692113216751012397\n', 'http://baijiahao.baidu.com/s?id=1692122029239116348\n', 'http://baijiahao.baidu.com/s?id=1692172397154756713\n', 'http://baijiahao.baidu.com/s?id=1692083862859520821\n', 'http://baijiahao.baidu.com/s?id=1692167449252468281\n', 'http://baijiahao.baidu.com/s?id=1692166281928400927\n', 'https://baijiahao.baidu.com/s?id=1692124607631097118&wfr=content\n', 'https://baijiahao.baidu.com/s?id=1692107973786509140&wfr=content\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'http://www.qstheory.cn/zt2020/llxjj/index.htm\n', 'https://www.baidu.com/s?wd=%E4%B8%AD%E7%BE%8E%E5%85%83%E9%A6%96%E9%80%9A%E8%AF%9D%EF%BC%8C%E4%B8%96%E7%95%8C%E6%8E%A5%E6%94%B6%E5%88%B0%E8%BF%99%E4%BA%9B%E7%A7%AF%E6%9E%81%E4%BF%A1%E5%8F%B7\n', 'https://www.baidu.com/s?wd=%E5%BC%95%E7%BB%8F%E6%8D%AE%E5%85%B8%E8%AF%9D%E6%96%B0%E6%98%A5%EF%BC%81%E5%93%81%E8%AF%BB%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%BC%95%E7%94%A8%E7%9A%84%E8%AF%97%E8%AF%8D%E4%B9%8B%E7%BE%8E\n', 'https://www.baidu.com/s?wd=%E4%B8%AD%E5%8D%B0%E5%8A%A0%E5%8B%92%E4%B8%87%E6%B2%B3%E8%B0%B7%E5%86%B2%E7%AA%81%E7%8E%B0%E5%9C%BA%E8%A7%86%E9%A2%91%E5%85%AC%E5%BC%80\n', 'https://www.baidu.com/s?wd=%E5%9B%BD%E9%98%B2%E9%83%A8%E5%9B%9E%E5%BA%94%E4%B8%BA%E4%BD%95%E5%85%AC%E5%B8%83%E8%A7%A3%E6%94%BE%E5%86%9B%E4%BC%A4%E4%BA%A1%E6%83%85%E5%86%B5\n', 'https://www.baidu.com/s?wd=2021%E5%B9%B4%E9%AB%98%E8%80%83%E6%97%B6%E9%97%B4%E7%A1%AE%E5%AE%9A\n', 'https://www.baidu.com/s?wd=%E7%BE%8E%E7%A7%B0%E5%B0%86%E7%BB%B4%E6%8C%81%E5%AF%B9%E5%8D%8E%E5%8A%A0%E5%BE%81%E5%85%B3%E7%A8%8E%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94\n', 'https://www.baidu.com/s?wd=%E4%B8%AD%E7%BA%AA%E5%A7%94%E8%AF%84%E8%AE%BA%E4%BD%A0%E5%A5%BD%E6%9D%8E%E7%84%95%E8%8B%B1\n', 'https://www.baidu.com/s?wd=%E7%94%B7%E5%AD%90%E9%81%9B%E5%BC%AF%E5%8F%91%E7%8E%B03%E5%B9%B4%E5%89%8D%E4%B8%A2%E7%9A%84%E6%89%8B%E6%9C%BA\n', 'https://www.baidu.com/s?wd=%E7%BE%8E%E5%9B%BD%E6%9C%80%E8%80%81%E5%B0%91%E5%B9%B4%E7%8A%AF%E6%9C%8D%E5%88%9168%E5%B9%B4%E5%90%8E%E5%87%BA%E7%8B%B1\n', 'https://www.baidu.com/s?wd=%E9%9F%A9%E5%9B%BD%E5%A5%B3%E5%AD%90%E5%92%AC%E6%8E%89%E6%80%A7%E4%BE%B5%E8%80%85%E8%88%8C%E5%A4%B4%E8%A2%AB%E5%88%A4%E6%97%A0%E7%BD%AA\n', 'http://baijiahao.baidu.com/s?id=1692116658709020854\n', 'http://baijiahao.baidu.com/s?id=1692116658709020854\n', 'http://baijiahao.baidu.com/s?id=1692109250462039445\n', 'http://baijiahao.baidu.com/s?id=1692109250462039445\n', 'http://baijiahao.baidu.com/s?id=1692111540627913377\n', 'http://baijiahao.baidu.com/s?id=1692111540627913377\n', 'http://baijiahao.baidu.com/s?id=1692039431890680523\n', 'http://baijiahao.baidu.com/s?id=1692099318073102003\n', 'http://baijiahao.baidu.com/s?id=1692114372183650477\n', 'http://baijiahao.baidu.com/s?id=1692083156262934113\n', 'http://baijiahao.baidu.com/s?id=1692087263316422208\n', 'https://baijiahao.baidu.com/s?id=1692042747404671829\n', 'http://baijiahao.baidu.com/s?id=1692115483967351388\n', 'http://baijiahao.baidu.com/s?id=1692032530350714205\n', 'http://baijiahao.baidu.com/s?id=1692093241461734361\n', 'http://baijiahao.baidu.com/s?id=1692088091088867927\n', 'http://baijiahao.baidu.com/s?id=1692087627448472669\n', 'http://baijiahao.baidu.com/s?id=1692113189788229863\n', 'http://baijiahao.baidu.com/s?id=1692118773264002841\n', 'https://baijiahao.baidu.com/s?id=1692086035058445203&wfr=content\n', 'http://baijiahao.baidu.com/s?id=1692046936333798310\n', 'http://baijiahao.baidu.com/s?id=1692118668680608984\n', 'http://baijiahao.baidu.com/s?id=1692113487955330666\n', 'http://baijiahao.baidu.com/s?id=1692113487955330666\n', '\n', '\n', 'http://www.piyao.org.cn/yybgt/index.htm\n', 'http://report.12377.cn:13225/toreportinputNormal_anis.do\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'javascript:void(0);\n', 'http://downpack.baidu.com/baidunews_AndroidPhone_1014720b.apk\n', 'https://itunes.apple.com/cn/app/id482820737\n', '//news-bos.cdn.bcebos.com/mvideo/baidu_news_protocol.html\n', 'https://news-bos.cdn.bcebos.com/mvideo/privacy.html\n', '//help.baidu.com/newadd?prod_id=5&category=1\n', '//news-bos.cdn.bcebos.com/mvideo/pcnews_licence.html\n', '//www.baidu.com/duty/\n', 'http://net.china.cn/chinese/index.htm\n', 'http://www.cyberpolice.cn/wfjb/\n', 'http://www.bjjubao.org/\n', '#{url}\n', '#{url}\n', '/sh\n', 'javascript:void(0);\n', '/sh\n', '#{url}\n', '/sh\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n', '#{url}\n']
165
ParseResult(scheme='https', netloc='www.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='tieba.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='zhidao.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='music.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='image.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='v.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='map.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='wenku.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='news.baidu.com', path='/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='www.xinhuanet.com', path='/politics/leaders/2021-02/19/c_1127116367.htm\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='news.cctv.com', path='/2021/02/18/ARTI0oS4jOZhFlwrMpSoGgO4210218.shtml\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='xhpfmapi.zhongguowangshi.com', path='/vh512/share/9774794', params='', query='channel=weixin\n', fragment='')
ParseResult(scheme='http', netloc='m.news.cctv.com', path='/2021/02/16/ARTI9eVg1dwru0Ocmui7i0I1210216.shtml\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='m.news.cctv.com', path='/2021/02/17/ARTIDhJalPvA8jlxyPNo1zG8210217.shtml\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='cn.chinadaily.com.cn', path='/a/202102/19/WS602f7010a3101e7ce97401f8.html\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='www.ce.cn', path='/xwzx/gnsz/gdxw/202102/19/t20210219_36319873.shtml\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='wap.peopleapp.com', path='/article/6137376/6044308\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692172482372438662\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692112492256036454\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692113817177132737\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692167966517789469\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692169295846378065\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692168717836498590\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692171361260104000\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692171751149486104\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692171314329445883\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692164857126287148&wfr=content\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692171148298779099\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692169521956174639\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692171992858859962\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692167169560507810\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692169809003390085\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692163989733193905\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692168733538070229\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692173757432852305\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692169651221340372&wfr=content\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692169095355879035&wfr=content\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692167775139335655&wfr=content\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692113216751012397\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692122029239116348\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692172397154756713\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692083862859520821\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692167449252468281\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692166281928400927\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692124607631097118&wfr=content\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692107973786509140&wfr=content\n', fragment='')
ParseResult(scheme='http', netloc='www.qstheory.cn', path='/zt2020/llxjj/index.htm\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E4%B8%AD%E7%BE%8E%E5%85%83%E9%A6%96%E9%80%9A%E8%AF%9D%EF%BC%8C%E4%B8%96%E7%95%8C%E6%8E%A5%E6%94%B6%E5%88%B0%E8%BF%99%E4%BA%9B%E7%A7%AF%E6%9E%81%E4%BF%A1%E5%8F%B7\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E5%BC%95%E7%BB%8F%E6%8D%AE%E5%85%B8%E8%AF%9D%E6%96%B0%E6%98%A5%EF%BC%81%E5%93%81%E8%AF%BB%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%BC%95%E7%94%A8%E7%9A%84%E8%AF%97%E8%AF%8D%E4%B9%8B%E7%BE%8E\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E4%B8%AD%E5%8D%B0%E5%8A%A0%E5%8B%92%E4%B8%87%E6%B2%B3%E8%B0%B7%E5%86%B2%E7%AA%81%E7%8E%B0%E5%9C%BA%E8%A7%86%E9%A2%91%E5%85%AC%E5%BC%80\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E5%9B%BD%E9%98%B2%E9%83%A8%E5%9B%9E%E5%BA%94%E4%B8%BA%E4%BD%95%E5%85%AC%E5%B8%83%E8%A7%A3%E6%94%BE%E5%86%9B%E4%BC%A4%E4%BA%A1%E6%83%85%E5%86%B5\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=2021%E5%B9%B4%E9%AB%98%E8%80%83%E6%97%B6%E9%97%B4%E7%A1%AE%E5%AE%9A\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E7%BE%8E%E7%A7%B0%E5%B0%86%E7%BB%B4%E6%8C%81%E5%AF%B9%E5%8D%8E%E5%8A%A0%E5%BE%81%E5%85%B3%E7%A8%8E%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E4%B8%AD%E7%BA%AA%E5%A7%94%E8%AF%84%E8%AE%BA%E4%BD%A0%E5%A5%BD%E6%9D%8E%E7%84%95%E8%8B%B1\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E7%94%B7%E5%AD%90%E9%81%9B%E5%BC%AF%E5%8F%91%E7%8E%B03%E5%B9%B4%E5%89%8D%E4%B8%A2%E7%9A%84%E6%89%8B%E6%9C%BA\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E7%BE%8E%E5%9B%BD%E6%9C%80%E8%80%81%E5%B0%91%E5%B9%B4%E7%8A%AF%E6%9C%8D%E5%88%9168%E5%B9%B4%E5%90%8E%E5%87%BA%E7%8B%B1\n', fragment='')
ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=%E9%9F%A9%E5%9B%BD%E5%A5%B3%E5%AD%90%E5%92%AC%E6%8E%89%E6%80%A7%E4%BE%B5%E8%80%85%E8%88%8C%E5%A4%B4%E8%A2%AB%E5%88%A4%E6%97%A0%E7%BD%AA\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692116658709020854\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692116658709020854\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692109250462039445\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692109250462039445\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692111540627913377\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692111540627913377\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692039431890680523\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692099318073102003\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692114372183650477\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692083156262934113\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692087263316422208\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692042747404671829\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692115483967351388\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692032530350714205\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692093241461734361\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692088091088867927\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692087627448472669\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692113189788229863\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692118773264002841\n', fragment='')
ParseResult(scheme='https', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692086035058445203&wfr=content\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692046936333798310\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692118668680608984\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692113487955330666\n', fragment='')
ParseResult(scheme='http', netloc='baijiahao.baidu.com', path='/s', params='', query='id=1692113487955330666\n', fragment='')
ParseResult(scheme='http', netloc='www.piyao.org.cn', path='/yybgt/index.htm\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='report.12377.cn:13225', path='/toreportinputNormal_anis.do\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='downpack.baidu.com', path='/baidunews_AndroidPhone_1014720b.apk\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='itunes.apple.com', path='/cn/app/id482820737\n', params='', query='', fragment='')
ParseResult(scheme='https', netloc='news-bos.cdn.bcebos.com', path='/mvideo/privacy.html\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='net.china.cn', path='/chinese/index.htm\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='www.cyberpolice.cn', path='/wfjb/\n', params='', query='', fragment='')
ParseResult(scheme='http', netloc='www.bjjubao.org', path='/\n', params='', query='', fragment='')

Process finished with exit code 0
```