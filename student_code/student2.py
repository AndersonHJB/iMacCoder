# from selenium import webdriver
# browser = webdriver.Chrome("../venv/chromedriver")
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import urllib.request
import ssl


class articledownload():
	## How to do the optimal arguement ""
	def __init__(self, url, master):
		self.url = url
		self.master = master

	def GetFullList(self):
		link = []
		code = []
		driver = webdriver.Chrome('../venv/chromedriver')
		driver.get(self.url)
		time.sleep(2)
		elem = driver.find_elements(By.XPATH, "//a[contains(text(), '第') and contains(text(), '章')]")
		for each in elem:
			link.append(each.get_attribute('href'))
			code.append(each.text)
		return link, code

	# error when Call this function outside
	def savemaster(self, link, code):
		Master = pd.DataFrame(list(zip(code, link)), columns=['code', 'source'])
		# Master.to_csv("Master.csv", encoding="utf-8")
		# Master.to_csv(f"{self.master}", encoding="utf-8")
		Master.to_csv(f"{self.master}", encoding="gbk")

	def openpage(self, pagesource):
		context = ssl._create_unverified_context()
		res = urllib.request.urlopen(pagesource, context=context)
		soup = BeautifulSoup(res, "html.parser")
		return soup

	def ChecknewItem(self):
		masterfile = pd.read_csv(self.master, encoding="gbk")
		# print(masterfile)
		OldList = masterfile["source"]
		# print(set(OldList))
		# print(type(OldList))
		# currentlist = GetFullList()  # why this function is not defined
		currentlist = self.GetFullList()  # why this function is not defined
		# downloadlist = list(set(currentlist[1]) - set(OldList))
		downloadlist = list(set(currentlist[0]) - set(OldList))
		return downloadlist

	# def downloadcontent(downloadlist)
	def downloadcontent(self, downloadlist):
		contentlist = []
		for item in downloadlist:
			# soup = openpage(pagesource=item)
			soup = self.openpage(pagesource=item)
			content = soup.find('div', id="content").text
			with open("text.txt", "a+", encoding="utf-8")as f:
				f.write(content)
			contentlist.append(content)
		return contentlist

if __name__ == '__main__':
	p = articledownload(
		url="https://www.xbiquge.so/book/6729/",
		master="aiyc.csv")
	# link, code = p.GetFullList()
	# print(a, b)
	# p.savemaster(link, code)
	r = p.ChecknewItem()
	print(p.downloadcontent(r))
