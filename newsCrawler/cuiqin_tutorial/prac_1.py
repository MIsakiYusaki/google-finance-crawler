# 抓蟲基本功		20161222
# encoding: utf-8  # 解決ASCII編碼問題 or # -*- coding: UTF-8 -*-

import urllib2

# 分兩個階段(Request, urlopen)寫是用來處理遇到需要修改Request的時候
request = urllib2.Request("http://blog.marsw.tw")
response = urllib2.urlopen(request)
html = response.read()
print html

fileout = file('01_blog.html', 'w')
fileout.write(html)
fileout.close()





# import urllib2

# wiki = "https://en.wikipedia.org/wiki/India"

# page = urllib2.urlopen(wiki)
# # 導入Beautiful suop函數解析從網址返回的數據
# from bs4 import BeautifulSoup
# # 在'page'變量解析html內容並以Beautiful Soup格式存儲
# soup = BeautifulSoup(page, 'lxml')

# print soup.prettify()