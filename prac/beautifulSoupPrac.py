# -*- coding: utf-8 -*-
# PN: beautifulSoup practice, Created Feb, 2017
# Version 1.0
# KW: crawler beautifulSoup tutorial
# Link: http://cuiqingcai.com/1319.html
# --------------------------------------------------- lib import
from bs4 import BeautifulSoup
# --------------------------------------------------- part 1: read html
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# soup = BeautifulSoup(html, "lxml")	# using lxml compile to create beautifulsoup element
# soup = BeautifulSoup(open('index.html'), 'lxml')	# open exsited html file to create beautifulsoup element
# print(soup.prettify())
# --------------------------------------------------- part 2-1: print tags' name, attrs
# print(soup.title)
# print(soup.title.attrs, '\n')
# print(soup.head)
# print(soup.head.attrs, '\n')
# print(soup.a)
# print(soup.a.attrs, '\n')
# print(soup.p)
# print(soup.p.attrs, '\n')
# --------------------------------------------------- part 2-2: get element's tag
# print(soup.p['class'])
# print(soup.p.get('class'))
# --------------------------------------------------- part 2-3: modify element's tag
# soup.p['class'] = 'newTitle'
# print(soup.p['class'])
# --------------------------------------------------- part 3: get tag's content
# print(soup.p.string)

# print(soup.head.contents[0])
# print(soup.head.children)
# print(soup.head.descendant)
# print(soup.head.parent)
# print(soup.head.sibling)
# print(soup.head.previous_sibling)

# # 去除多餘的空白或換行
# for string in soup.stripped_strings:
#     print(repr(string))

# using regular expression
# import re
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

# --------------------------------------------------- part 4-1: find specific tags
# soup.find_all("title")

# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(attrs={"data-foo":"value"})

# # 設定搜尋上限
# soup.find_all("a", limit=2)
# --------------------------------------------------- part 4-2: find specific tags using css selector
# print(soup.select('a'))
# print(soup.select('.sister')[1].get_text())

# print(soup.select('title')[0].get_text())
# for title in soup.select('title'):
#     print(title.get_text())


# # 組合式查詢 - 1
# print(soup.select('p #link1'))

# # 組合式查詢 - 2
# print(soup.select('head > title'))
