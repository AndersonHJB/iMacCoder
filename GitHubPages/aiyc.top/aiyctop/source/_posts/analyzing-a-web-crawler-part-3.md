---
title: Analyzing a web crawler (part 3)
tags: []
id: '2138'
categories:
  - - Alex Homework
date: 2022-01-06 06:08:28
---

There are no significant changes to much of our functions' code, however there have been some changes that have occurred to the parse content function, this one in particular:

```python
def parse_detail_content(htmls):
    for html in htmls:
        detail_content_url = html.get("href", "https://www.aiyc.top")
        # print(detail_content_url)
        # time.sleep(10)
        # # print(detail_content_url)
        html = crawler(detail_content_url)
        DELAYWAIT.wait(detail_content_url)
        # print(html)
        try:
            soup = BeautifulSoup(html, "lxml")
        except:
            print("None or Remotely disconnected connection to server")
            pass
        detail_content_title_list = soup.select(".box_con .bookname h1")
        print(detail_content_title_list)
        if detail_content_title_list:
            detail_content_title = detail_content_title_list[0].string.strip()
        # contents = soup.select("#content")[0].select("p")
        contents = soup.select("#content")[0].select("p")
        # print(contents, end="\n\n\n\n")
        content_text = ""
        for content in contents:
            content = content.string.strip()
            content_text += content
        yield {
            "detailed content title": detail_content_title,
            "content": content_text
        }
        print(content_text)
```

The main change we have made towards our parse detail content function, is that we have added a try-except statement for our bs4 connection to the website's server, this way we know whether the server's response returns nothing, or the server has remotely shut down our connection to it, thus recognizing us as someone using a bot, and not a legitimate human using their own computer to access the webpage. This will make our bot more "technologically advanced" when it comes to saving us and potentially any future users some time, in case they run into any errors while running the bot on whatever website they are trying to crawl. This ensures that if there is no response from the server for a long time, or there has been some errors that may not directly return to the python console, the crawler's user will be notified of it, this way they don't have to sit there and wait for nothing particularly useful to happen. There has been another minor change that has occurred to our main function that calls all the smaller functions inside of our crawler's class:

```python
def main():
    home_url = "http://www.b520.cc/0_7/"
    html = crawler(home_url)
    content = list(parse_directory(html))
    # print(story_title)
    for i in content:
        save(str(i) + "\n", "../b520/data/story_information{}.txt".format(story_title))
    r = parse_detail_content(content)
    for index, i in enumerate(r):
        print(i)
```

You may not be able to see the change immediately, this is because we only added two new lines of code. We basically are enumerating a object that contains another object called "content" that holds a list of all the contens of the story that we want to parse. We enumerate this object called "r", and we can print the numerate that is enumerated through by the function. This helps us when we want to see what the python interpreter is cycling through and running after we hit the green run button in PyCharm. The third and final change we added to our crawler, is the custom DelayWait function that we made a class for in a seperate python file, and we added this code into the parse\_detail\_content() function.

```python
def parse_detail_content(htmls):
    for html in htmls:
        detail_content_url = html.get("href", "https://www.aiyc.top")
        # print(detail_content_url)
        # time.sleep(10)
        # # print(detail_content_url)
        html = crawler(detail_content_url)
        DELAYWAIT.wait(detail_content_url)
        # print(html)
        try:
            soup = BeautifulSoup(html, "lxml")
        except:
            print("None or Remotely disconnected connection to server")
            pass
        detail_content_title_list = soup.select(".box_con .bookname h1")
        print(detail_content_title_list)
        if detail_content_title_list:
            detail_content_title = detail_content_title_list[0].string.strip()
        # contents = soup.select("#content")[0].select("p")
        contents = soup.select("#content")[0].select("p")
        # print(contents, end="\n\n\n\n")
        content_text = ""
        for content in contents:
            content = content.string.strip()
            content_text += content
        yield {
            "detailed content title": detail_content_title,
            "content": content_text
        }
        print(content_text)
```

We use a custom DelayWait object called "DELAYWAIT" that we defined in the few lines at the beginning of our python file. We made this DelayWait custom wait function in a class in a seperate python file called "DelayWait.py" This file contains the following code:

```python
from urllib import parse
from datetime import datetime
import time, requests


class DelayWait(object):
    def __init__(self, delay=3):
        self.delay = delay
        self.urls = dict()

    def wait(self, url):
        netloc = parse.urlparse(url).netloc
        # {"site": datetime.now()}
        lastOne = self.urls.get(netloc)
        if lastOne and self.delay > 0:
            timeWait = self.delay - (datetime.now() - lastOne).seconds
            if timeWait > 0:
                time.sleep(timeWait)
        else:
            self.urls[netloc] = datetime.now()


if __name__ == "__main__":
    urls = ['http://www.baidu.com'] * 10
    d = DelayWait()
    for url in urls:
        html = requests.get(url)
        d.wait(url)
        print(html.status_code)
```

We use a special function called "netloc" to essentially "lock" the request time and delay from the connection our computer generates to the server, this way we have a steady response time, and the server won't immediately flag us for suspicious amounts of requests. It basically grabs the delay between the previous request, and the current one, subtracts the first connection's delay time from the seocnd one, this way it creates a perfect balance for the remaining number, and that number is the perfect delay for our connection to sustain without the website's server flagging our ip for suspicious network traffic.