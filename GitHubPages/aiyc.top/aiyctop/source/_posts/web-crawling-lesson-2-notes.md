---
title: Web Crawling Lesson 2 Notes
tags: []
id: '1887'
categories:
  - - Alex Homework
date: 2021-09-11 07:35:24
---

A very important concept in web crawling, is the efficiency of the web crawler. If you web crawler is very slow, then it will be very tedious to keep waiting for the results that the web crawler returns to come out. No repeating data is also a big part of efficiency, since there's no point in waiting a while for data to be returned, and be returned repeating data, data that will be useless. This means that if we wanted to generate urls or crawl urls for a certain website, we don't want to crawl the same url more than once. This is where url checks will come in handy. The following code below is an example for a movie website called "douban.com":

```py
url1 = "https://www.douban.com/var/page={page_num}"
url2 = "https://www.douban.com/view/page={page_num}"

list1 = []

if url1 in ["https://www.douban.com/var/page={page_num}"]:
    for i in range(10):
        formatted_url1 = url1.format(page_num=i)
        list1.append(formatted_url1)

    for i in range(10):
        formatted_url2 = url2.format(page_num=i)
        list1.append(formatted_url2)

elif url2 in ["https://www.douban.com/view/page={page_num}"]:
    for i in range(10):
        formatted_url1 = url1.format(page_num=i)
        list1.append(formatted_url1)

    for i in range(10):
        formatted_url2 = url2.format(page_num=i)
        list1.append(formatted_url2)


print(list1)
```

The reason why the code above is inefficient is because we never actually checked the urls PROPERLY, since all we did was run a basic list check for the urls, that we know will be satisfied, so there is no point in doing that. Also, there are some redundant usages of for loops in the code above, since we have two for loops, that are essentially doing the same thing. The third issue about the code above, is that it cannot be used in many scenarios, or it is "inefficient", because it technically can't really thoroughly check the urls that are being passed to it, since we are only passing the urls that is pre-set and "ordered" for us, whereas in a real-scenario, a website won't properly organize everything for a web crawler, so you will have to make it work no matter what urls are being passed to it, as long as some keywords in the url are passed. Here is an example that is much better:

```py
url_var = "https://www.douban.com/var/page={page_num}"
url_view = "https://www.douban.com/view/page={page_num}"

url_list_var = []
for i in range(10):
    url_list_var.append(url_var.format(page_num=i))

url_list_view = []
for i in range(10):
    url_list_view.append(url_view.format(page_num=i))

url_list = url_list_var + url_list_view

head = []
tail = []
for url in url_list:
    if "var" in url:
        head.append(url)
    elif "view" in url:
        tail.append(url)
    else:
        print("No url specified.")

result = head + tail

print(result)
```

The example above is a much better and cleaner code, because it does not redundantly use for loops and if statements to check pre-set things that we already know what they are, and the code above will work much more efficiently with being more all-rounded for any situation involving checking urls, since it uses head and tail lists, instead of just randomly adding the urls to one single list and not adding them depending on if the url should be near the front of the list/first half of the list, or the the second half of the list, and then combined. The code above basically generates 10 of each url and adds them each to their separate lists, and iterates through the loops, checks to see if they are of each of their types, and depending on their types, add them to the "heads" or "tails" lists, and combines those two lists into one list, and returns that one list. This means that as long as their are urls being iterated through, it will always add the right type of urls to the right list, and it is much less redundant and more efficient and "usable" with more situations than the previous first code. Small tip: when using requests to send a request to a server or api or a url/website, if the data/response returned is in binary, you can call the response data as .content because binary is a universal code format. For most websites nowadays, if you want to crawl data from their website, they will require not only a user-agent, but also a referer. A referer is basically a second layer of authentication. For example, if you are crawling an image from a website that requires both, and you only give the user-agent, then the image can not be crawled or opened after it has been crawled, because the "format" of the image isn't correct, but in reality, it's really that the image just doesn't have the second layer of authentication aka the referer fulfilled.