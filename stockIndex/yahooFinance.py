# -*- coding: utf-8 -*-
# PN: stock index crawler, Created Feb, 2017
# Version 1.0
# KW: crawler yahoo_finance
# Link: https://www.jerrynest.com/python-yahoo-finance-api-historical-stock-price/, https://pypi.python.org/pypi/yahoo-finance
# --------------------------------------------------- lib import
from yahoo_finance import Share
import datetime
import sys
import sqlite3
import re
conn = sqlite3.connect('index.sqlite')

# --------------------------------------------------- single company
# def getStock(id):
# 	stock = Share(str(id) + '.TW')
# 	# stock info
# 	name = stock.get_name()
# 	# info = stock.get_info()
# 	time = stock.get_trade_datetime()

# 	# price info
# 	openPrice = stock.get_open()
# 	closePrice = stock.get_price()
# 	high = stock.get_days_high()
# 	low = stock.get_days_low()
# 	change = stock.get_change()
# 	changePercent = stock.get_percent_change()

# 	info_output = "Stock: {} \nTrade date: {}\n".format(name, time)
# 	price_output = "Open price: {} Price high: {} Price low: {} Close price: {} Change: {} Percent: {}".format(openPrice, high, low, closePrice, change, changePercent)
# 	return info_output + price_output

# print(getStock(sys.argv[1]))

# --------------------------------------------------- index


def getIndex(id):
	index = Share(id)
	datas = str(index.get_historical('2017-02-20', '2017-02-20'))
	for data in datas:
		lis = list()
		# date
		date_match = re.search(r'\d\d\d\d\-\d\d\-\d\d', datas)
		date = date_match.group()
		lis.append(date)
		# volumn
		volumn_match = re.search(r'\'(\d+)\'', datas)
		volumn = volumn_match.group(1)
		lis.append(volumn)		
		# open price
		price = re.findall(r'(\d\d\d\d\.\d+)', datas)
		lis.append(price[0])
		# high price
		lis.append(price[1])
		# low price
		lis.append(price[2])
		# close price
		lis.append(price[3])
		# adj close price
		lis.append(price[4])
		print(lis)
		for li in lis:
			sqlstr = "SELECT * FROM prices WHERE pdate={}".format(lis[0])
			cursor = conn.execute(sqlstr)
			if len(cursor.fetchall()) == 0:
				volumn = 0 if li[6] == '' else int(li[1])
				open = 0 if li[2] == '' else float(li[2])
				high = 0 if li[3] == '' else float(li[3])
				low = 0 if li[4] == '' else float(li[4])
				close = 0 if li[5] == '' else float(li[5])
				adjclose = 0 if li[7] == '' else float(li[6])
				sqlstr = "insert into prices values('{}', {}, {}, {}, {}, {}, {})".format(lis[0], volumn, open, high, low, close, adjclose)
				print(sqlstr)
				conn.execute(sqlstr)
				conn.commit()
	return lis
	# print(datas)
	# for data in datas:
	# 	print(data)
	# # sqlstr = "SELECT * FROM prices WHERE gdate={}".format(p[0])
	# cursor = conn.execute(sqlstr)
	# if len(cursor.fetchall()) == 0:
	# 	g92 = 0 if p[1] == '' else float(p[1])
	# 	g95 = 0 if p[2] == '' else float(p[2])
	# 	g98 = 0 if p[3] == '' else float(p[3])
	# 	sqlstr = "insert into prices values('{}', '{}', {}, {}, {}, {}, {}, {})".format(data[0], data[1], data[2], data[3])
	# 	print(sqlstr)
	# 	conn.execute(sqlstr)
	# 	conn.commit()

	
getIndex('^TWII')