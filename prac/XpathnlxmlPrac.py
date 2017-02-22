# -*- coding: utf-8 -*-
# PN: Xpath lxml practice, Created Feb, 2017
# Version 1.0
# KW: http://cuiqingcai.com/2621.html crawler Xpath lxml tutorial
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
# auto-fix </li>, <body>, <html>
html = etree.HTML(text)
result = etree.tostring(html)
print(result)