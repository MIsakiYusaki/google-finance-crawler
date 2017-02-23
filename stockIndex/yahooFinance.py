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
conn = sqlite3.connect('index.sqlite')
import csv
import re

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
with open('datedata.csv', 'r') as f:
	datereader = csv.reader(f, delimiter=' ', skipinitialspace=True)
	for row in datereader:
		date = row
		print(date)
		# def getIndex(id):
		# 	index = Share(id)
		# 	datas = str(index.get_historical('{}'.format(date), '{}'.format(date)))
		# 	lis = list()
		# 	# date
		# 	pdate_match = re.search(r'\d\d\d\d\-\d\d\-\d\d', datas)
		# 	pdate = pdate_match.group()
		# 	lis.append(pdate)
		# 	# volumn
		# 	volumn_match = re.search(r'\'(\d+)\'', datas)
		# 	volumn = volumn_match.group(1)
		# 	lis.append(volumn)
		# 	# open price test
		# 	openPrice_match = re.search(r'Open\'\: \'(\d\d\d\d\.\d+)\'', datas)
		# 	openPrice = openPrice_match.group(1)
		# 	lis.append(openPrice)
		# 	# high price
		# 	highPrice_match = re.search(r'High\'\: \'(\d\d\d\d\.\d+)\'', datas)
		# 	highPrice = highPrice_match.group(1)
		# 	lis.append(highPrice)
		# 	# low price
		# 	lowPrice_match = re.search(r'Low\'\: \'(\d\d\d\d\.\d+)\'', datas)
		# 	lowPrice = lowPrice_match.group(1)
		# 	lis.append(lowPrice)
		# 	# close price
		# 	closePrice_match = re.search(r'Close\'\: \'(\d\d\d\d\.\d+)\'', datas)
		# 	closePrice = closePrice_match.group(1)
		# 	lis.append(closePrice)
		# 	# adj close price
		# 	adjclosePrice_match = re.search(r'Adj_Close\'\: \'(\d\d\d\d\.\d+)\'', datas)
		# 	adjclosePrice = adjclosePrice_match.group(1)
		# 	lis.append(adjclosePrice)

		# 	sqlstr = "SELECT * FROM prices WHERE pdate={}".format(lis[0])
		# 	print(sqlstr)
		# 	print(conn)
		# 	cursor = conn.execute(sqlstr)
		# 	if len(cursor.fetchall()) == 0:
		# 		volumn = 0 if lis[1] == '' else int(lis[1])
		# 		open = 0 if lis[2] == '' else float(lis[2])
		# 		high = 0 if lis[3] == '' else float(lis[3])
		# 		low = 0 if lis[4] == '' else float(lis[4])
		# 		close = 0 if lis[5] == '' else float(lis[5])
		# 		adjclose = 0 if lis[6] == '' else float(lis[6])
		# 		sqlstr = "INSERT OR IGNORE INTO prices values('{}', {}, {}, {}, {}, {}, {})".format(lis[0], volumn, open, high, low, close, adjclose)
		# 		print(sqlstr)
		# 		conn.execute(sqlstr)
		# 		conn.commit()

	
getIndex('^TWII')