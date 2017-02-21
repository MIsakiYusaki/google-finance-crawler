# -*- coding: utf-8 -*-
# PN: beautifulSoup practice, Created Feb, 2017
# Version 1.0
# KW: crawler beautifulSoup tutorial
# Link: http://cuiqingcai.com/1319.html
# --------------------------------------------------- lib import
from bs4 import BeautifulSoup as sp


# In[3]:

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


# In[4]:

soup = sp(html, "lxml")


# In[5]:

print(soup)


# In[6]:

print(soup.p['class'])


# In[7]:

soup.p['class'] = 'newTitle'
print(soup.p['class'])


# In[8]:

print(soup.p.string)


# In[9]:

print(soup.attrs)


# In[10]:

print(soup.head.contents[0])


# In[11]:

print(soup.head.children)


# In[12]:

for child in soup.body.children:
    print(child)


# In[13]:

for string in soup.strings:
    print(repr(string))


# In[14]:

# 去除多餘的空白或換行
for string in soup.stripped_strings:
    print(repr(string))


# In[15]:

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)


# In[16]:

soup.find_all("title")


# In[17]:

data_soup = sp('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo":"value"})


# In[18]:

# 設定搜尋上限
soup.find_all("a", limit=2)


# In[19]:

print(soup.select('a'))


# In[20]:

print(soup.select('.sister')[1].get_text())


# In[21]:

print(type(soup.select('title')))
print(soup.select('title')[0].get_text())

for title in soup.select('title'):
    print(title.get_text())


# In[22]:

# 組合式查詢 - 1
print(soup.select('p #link1'))


# In[23]:

# 組合式查詢 - 2
print(soup.select('head > title'))


# In[ ]:



