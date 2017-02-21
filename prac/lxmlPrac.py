# -*- coding: utf-8 -*-
# PN: Xpath lxml practice, Created Feb, 2017
# Version 1.0
# KW: crawler Xpath lxml tutorial
# Link: http://cuiqingcai.com/2621.html
# --------------------------------------------------- lib import
from lxml import etree
# --------------------------------------------------- example to use
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# --------------------------------------------------- part 1: analyse html content(initialize, then print out)
# auto-fix </li>, <body>, <html> througn libxml2 features
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result)
# --------------------------------------------------- part 2: load html document
# html = etree.parse('hello.html')
# result = etree.tostring(html, pretty_print=True)
# print(result)
# --------------------------------------------------- part 3: apply xpath
html = etree.parse('hello.html')

# print(type(html))    # element tree
# result = html.xpath('//li')
# print(result)
# print(type(result))    # list element
# print(type(result[0]))

# result = html.xpath('//li/@class')    # 找到具有class屬性的元素
# print(result)

# result = html.xpath('//li/a[@href="link1.html"]')    # li > a href > "link1.html"
# print(result)

# result = html.xpath('//li/a//@class')    # find all classes under li (not included li)
# print(result)

# result = html.xpath('//li[last()]/a/@href')    # (li > a href)'s last class
# print(result)

# result = html.xpath('//li[last()-1]/a')    # find last - 1 (li > a href)'s content (.text), ps: a is a list, so result[0]
# print(result[0].text)

# result = html.xpath('//*[@class="bold"]')  # 搜尋class = bold的 tag
# print(result[0].tag)