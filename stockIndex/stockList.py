# -*- coding: utf-8 -*-
# PN: stock index crawler, Created Mar, 2017
# Version 1.0
# KW: crawler yahoo_finance
# Link: https://www.jerrynest.com/python-twse-stock-list/
# --------------------------------------------------- lib import
import re
import requests
from bs4 import BeautifulSoup
# --------------------------------------------------- disp_menu()

def stockList():
	url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
	res = requests.get(url, verify=False)
	soup = BeautifulSoup(res.text, 'lxml')
	for row in soup.select('tr'):
		print(row)
		# cols = row.find_all('td')
		# col1 = cols[0].text.encode('utf-8')
		# data = re.search(r'(.*)   (.*)',col1)
		# print(data)
		# if data is not None:
		# 	if data.group(1) is not None:
		# 		if data.group(2) is not None:
		# 			if (len(cols[4].text.encode('utf-8')) != 0):
		# 				symbolid =  filter(str.isalnum,data.group(1))
		# 				symbol = data.group(2)
		# 				start = cols[2].text.encode('utf-8')
		# 				type = cols[4].text.encode('utf-8')
		# 				print(symbolid, symbol, start, type)
 
stockList()

<tr>
<td bgcolor="#FAFAD2">01007T　兆豐國泰R2</td>
<td bgcolor="#FAFAD2">TW00001007T5</td>
<td bgcolor="#FAFAD2">2006/10/13</td>
<td bgcolor="#FAFAD2">上市</td>
<td bgcolor="#FAFAD2"></td>
<td bgcolor="#FAFAD2">EUCIRR</td>
<td bgcolor="#FAFAD2"></td>
</tr>