---
title: Web Crawling Lesson 3 Notes
tags: []
id: '1896'
categories:
  - - Alex Homework
date: 2021-09-15 05:45:45
---

There are two main schemes that are in urls of websites that you most likely visit frequently: https, and http. The difference between these two in the backend, is that https runs on port 443 in your computer, and http runs on port 80. Most websites nowadays use https instead of http, unless the website is quite old, or is run by a small company or a few people, and not a big corporation like Google or Facebook. Speaking of schemes, there are three main parts to a url, such as the starting point of a url, which is the scheme, and it is typically "https" or "http", then comes a colon, and the second thing, is the host. For example, when you go to amazon.com, the host is "amazon" since that's the name of the website you are trying to access. Even though there is a parameter called the "path" in a url, it is typically hidden inside the host name, since websites don't really particularly want the user to know what port the website is running on. You can get the ip address where a website is running on by inspecting the network request. Since the website is running on that remote address, you can enter that remote address into a browser as a url, and it will bring you to that website as usual, although your browser may warn you that the site you are going to is potentially dangerous, your browser only does that because it does not want you accessing websites through their ip, since you don't necessarily know what website you are visiting, which could result in potentially unwanted results, so be sure that if you are using a ip address to visit a website, that it is a trusted site, and is safe. If you think getting the remote address of a website through inspecting the site's html/frontend code is too complicated, then you can use your computer's terminal or command prompt, depending on your os, and use the nslookup command, and enter the website that you want to get the address for. You can also specify the port on which you want to access the website, by putting a colon after the url of the website, and entering the port after that colon. Keep in mind that if you try to use an unsupported port that the website's developer(s) has not configured yet, then the website will return an error, stating that depending on what port you tried to use, will say that either you tried to access a http website, but it's https, vice versa. In order to make your web crawler safe, you have to only crawl safe sites, and nowadays, safe sites are typically sites that run on https schemes, unless the site is very old or potentially malicious. Here is an example of some code that can check to see if a url that is going to be crawled is https or http:

```py
from urllib.parse import urlparse
urls_lst = [
    "https://www.spotify.com/hk-zh/download/windows/",
    "https://www.microsoft.com/zh-cn/p/spotify-music/9ncbcszsjrsb?cid=spotifyweb-windows10-store-direct&rtc=1&activetab=pivot:overviewtab",
    "https://www.aiyc.top/sevenpythonlearn",
    "http://p5py.com/",
    "http://aiyuechuang.com/",
    "http://aiyc.com/",
    "http://Alex.cn.com/",
]

good_urls_list = []
bad_urls_list = []

for item in urls_lst:
    result = urlparse(item)

    if "https" == result.scheme:
        good_urls_list.append(item)

    elif "http" == result.scheme:
        bad_urls_list.append(item)

print(good_urls_list)
print(bad_urls_list)
```

The code above seperates https urls, which are considered "good" urls, and "http" urls which are considered "bad" urls, into seperate lists, and using this concept, we can make it so that in the future when developing web crawlers, we can check to see if the url is in the bad url list after appending all determined "bad" urls to that "bad url list", and if the url is in the bad url list, then to not crawl that website. There are two useful functions from a library called "urllib", and it is the urlparse() and the urlsplit() functions. What they do is basically, splitting up an entire url, and telling you what each part in the url is, such as the "https" part of a url, will be the "scheme" and this is particularly useful if you want to run conditional checks on the type of scheme in a url that you may want to crawl, which could be potentially useful. The urlparse() and the urlsplit() functions are very similar, although they have one major difference, and that is the fact that the urlparse() method prints out the "params" parameter, even if there is nothing in that parameter, whereas the urlsplit() function will not print out the "params" parameter if there is no value of it. These two methods are very useful, especially with web crawlers, so it is important to know the difference between the two, in case you need to use them.