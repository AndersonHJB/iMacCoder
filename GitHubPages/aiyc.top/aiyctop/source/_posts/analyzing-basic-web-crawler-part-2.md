---
title: Analyzing basic web crawler part 2
tags: []
id: '2103'
categories:
  - - Alex Homework
date: 2021-12-18 12:54:00
---

```python
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time

story_title = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", }


def crawler(url):
    try:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            return html.text
        else:
            return "None"
    except RequestException as e:
        return e


def parse_directory(html):
    global story_title
    soup = BeautifulSoup(html, "lxml")
    story_title = soup.select("#info h1")[0].string
    directorys = soup.select("#list dl dd a")[9:]
    # print(directory)
    for dir in directorys:
        href = dir.get("href")
        chapter_title = dir.string
        yield {
            "href": href,
            "chapter_title": chapter_title
        }


def parse_detail_content(htmls):
    for html in htmls:
        detail_content_url = html.get("href", "https://www.aiyc.top")
        time.sleep(1)
        # print(detail_content_url)
        html = crawler(detail_content_url)
        soup = BeautifulSoup(html, "lxml")
        detail_content_title_list = soup.select(".box_con .bookname h1")
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
        # print(content_text)

    # for content in contents:
    #   # print(list(content.stripped_strings))
    #   yield {
    #       "detail_content_title": detail_content_title,
    #       "content": content.string
    #
    #   # print(content.text)


def save(content, filename):
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(content)


def main():
    home_url = "http://www.b520.cc/0_7/"
    html = crawler(home_url)
    content = list(parse_directory(html))
    # print(story_title)
    for i in content:
        save(str(i) + "\n", "../b520/data/story_information{}.txt".format(story_title))
    r = parse_detail_content(content)
    for index, i in enumerate(r):
        content_old = i.get("content", "default_content")
        content = content_old.split("。")
        for con in content:
            save(con + "。\n", f"data/content/{f'{index+1}' + i.get('detailed content title', 'default_name')}.md")


if __name__ == '__main__':
    main()
```

There is not much difference from the first part of this web crawler compared to the current version, apart from the fact that we have made it slightly more intelligent, such as creating markdown files to store the data it crawls for each story, instead of simply saving it in a messy text file. It also saves each chapter as an individual file, as well as making each sentence seperated by a new line, this way the text is much easier to read line by line, instead of having to read loads of text at once. There were not many changes to individual functions, however we did change certain things of the main function that controls the activity of the crawler, such as 1. making it store data in a different format, using a different extension from the last time we made changes to this crawler, getting the content variables from the list of elements in each chapter of the story, this way we can split each line, adding a new line after each period in each chapter's elements. We also iterate through the list of chapters and their contents, creating a new file for each chapter in the process, using formatted strings, and the custom save() function we made for our crawler. That's it for now! The changes are constantly being updated, I'm leanring many new things, and this crawler will be much more intelligent and resourceful in the future.