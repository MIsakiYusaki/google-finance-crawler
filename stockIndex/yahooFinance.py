# -*- coding: utf-8 -*-
# PN: stock index crawler, Created Feb, 2017
# Version 1.1
# KW: crawler yahoo_finance
# Link: https://www.jerrynest.com/python-yahoo-finance-api-historical-stock-price/, https://pypi.python.org/pypi/yahoo-finance
# --------------------------------------------------- lib import
from yahoo_finance import Share
import datetime
import sys
import sqlite3
import csv
import re
# --------------------------------------------------- disp_menu()
def disp_menu():
	print("--------------------")
	print("Yahoo Price Crawler System")
	print("--------------------")
	print("1. Stock Crawler")
	print("2. Index Crawler")
	print("3. Currency Crawler")
	print("4. Coming soon")
	print("0. System close")
	print("--------------------")
# --------------------------------------------------- disp_menu()
def stock_menu():
	print("--------------------")
	print("Stock Crawler")
	print("--------------------")
	print("1. Daily infomation")
	print("2. Historical infomation")
	print("3. Finantial infomation")
	print("0. Previous page")
	print("--------------------")
# --------------------------------------------------- part1-1: getStock_daily
def getStock_daily(id):
	# print("not finish")
	stock = Share(id)
	# stock info
	name = stock.get_name()
	# print(name)
	# info = stock.get_info()
	time = stock.get_trade_datetime()

	# price info
	openPrice = stock.get_open()
	closePrice = stock.get_price()
	high = stock.get_days_high()
	low = stock.get_days_low()
	change = stock.get_change()
	changePercent = stock.get_percent_change()

	info_output = "Stock: {} \nTrade date: {}\n".format(name, time)
	price_output = "Open price: {} Price high: {} Price low: {} Close price: {} Change: {} Percent: {}".format(openPrice, high, low, closePrice, change, changePercent)
	print(info_output + price_output)
# --------------------------------------------------- part1-2: getStock_his
def getStock_his(id, year, month, day, term):
	conn = sqlite3.connect('firm.sqlite')
	stock = Share(id)
	name = id
	date = datetime.date(year, month, day)
	for i in range(1, term+1):
		weekday = date.isoweekday()
		try:
			datas = str(stock.get_historical('{}'.format(date), '{}'.format(date)))
			# print(datas)
			lis = list()
			# date
			pdate_match = re.search(r'\d\d\d\d\-\d\d\-\d\d', datas)
			pdate = pdate_match.group()
			lis.append(pdate)
			# stock name
			lis.append(name)
			# weekday
			lis.append(weekday)
			# volumn
			volumn_match = re.search(r'\'(\d+)\'', datas)
			volumn = volumn_match.group(1)
			lis.append(volumn)

			# open price test
			openPrice_match = re.search(r'Open\'\: \'(\d+\.\d+)\'', datas)
			openPrice = openPrice_match.group(1)
			lis.append(openPrice)
			# high price
			highPrice_match = re.search(r'High\'\: \'(\d+\.\d+)\'', datas)
			highPrice = highPrice_match.group(1)
			lis.append(highPrice)
			# low price
			lowPrice_match = re.search(r'Low\'\: \'(\d+\.\d+)\'', datas)
			lowPrice = lowPrice_match.group(1)
			lis.append(lowPrice)
			# close price
			closePrice_match = re.search(r'Close\'\: \'(\d+\.\d+)\'', datas)
			closePrice = closePrice_match.group(1)
			lis.append(closePrice)

			# adj close price
			adjclosePrice_match = re.search(r'Adj_Close\'\: \'(\d+\.\d+)\'', datas)
			adjclosePrice = adjclosePrice_match.group(1)
			lis.append(adjclosePrice)
			# print(lis)	# test whether lis exists
			sqlstr = "SELECT * FROM price WHERE name={}".format(lis[0])
			sqlstr = "SELECT * FROM price WHERE pdate={} ORDER BY pdate DESC".format(lis[0])
			# print(sqlstr)
			cursor = conn.execute(sqlstr)
			if len(cursor.fetchall()) == 0:
				name = 0 if lis[1] == '' else str(lis[1])
				weekday = 0 if lis[2] == '' else int(lis[2])
				volumn = 0 if lis[3] == '' else int(lis[3])
				open = 0 if lis[4] == '' else float(lis[4])
				high = 0 if lis[5] == '' else float(lis[5])
				low = 0 if lis[6] == '' else float(lis[6])
				close = 0 if lis[7] == '' else float(lis[7])
				adjclose = 0 if lis[8] == '' else float(lis[8])
				sqlstr = "INSERT OR IGNORE INTO price values('{}', '{}', {}, {}, {}, {}, {}, {}, {})".format(lis[0], name, weekday, volumn, open, high, low, close, adjclose)
				conn.execute(sqlstr)
				conn.commit()
				print(sqlstr)
			date = date - datetime.timedelta(1)
		except:
			date = date - datetime.timedelta(1)
# --------------------------------------------------- part1-3: finance
def getStock_finance(id):
	# print("not finish")
	stock = Share(id)
	# stock info
	name = stock.get_name()
	# print(name)
	# info = stock.get_info()
	time = stock.get_trade_datetime()

	# price info
	openPrice = stock.get_open()
	closePrice = stock.get_price()
	high = stock.get_days_high()
	low = stock.get_days_low()
	change = stock.get_change()
	changePercent = stock.get_percent_change()

	info_output = "Stock: {} \nTrade date: {}\n".format(name, time)
	price_output = "Open price: {} Price high: {} Price low: {} Close price: {} Change: {} Percent: {}".format(openPrice, high, low, closePrice, change, changePercent)
	print(info_output + price_output)
# --------------------------------------------------- part2: index
def getIndex(id, year, month, day, term):
	conn = sqlite3.connect('index.sqlite')
	index = Share(id)
	name = id
	date = datetime.date(year, month, day)
	for i in range(1, term+1):
		weekday = date.isoweekday()
		try:
			datas = str(index.get_historical('{}'.format(date), '{}'.format(date)))
			lis = list()

			# date
			pdate_match = re.search(r'\d\d\d\d\-\d\d\-\d\d', datas)
			pdate = pdate_match.group()
			lis.append(pdate)
			# index name
			lis.append(name)
			# weekday
			lis.append(weekday)
			# volumn
			volumn_match = re.search(r'\'(\d+)\'', datas)
			volumn = volumn_match.group(1)
			lis.append(volumn)
			# open price test
			openPrice_match = re.search(r'Open\'\: \'(\d+\.\d+)\'', datas)
			openPrice = openPrice_match.group(1)
			lis.append(openPrice)
			# high price
			highPrice_match = re.search(r'High\'\: \'(\d+\.\d+)\'', datas)
			highPrice = highPrice_match.group(1)
			lis.append(highPrice)
			# low price
			lowPrice_match = re.search(r'Low\'\: \'(\d+\.\d+)\'', datas)
			lowPrice = lowPrice_match.group(1)
			lis.append(lowPrice)
			# close price
			closePrice_match = re.search(r'Close\'\: \'(\d+\.\d+)\'', datas)
			closePrice = closePrice_match.group(1)
			lis.append(closePrice)
			# adj close price
			adjclosePrice_match = re.search(r'Adj_Close\'\: \'(\d+\.\d+)\'', datas)
			adjclosePrice = adjclosePrice_match.group(1)
			lis.append(adjclosePrice)
			# print(lis)	# test whether lis exists
			# sqlstr = "SELECT * FROM price WHERE name={}".format(lis[0])
			sqlstr = "SELECT * FROM price WHERE pdate={} ORDER BY pdate DESC".format(lis[0])
			# print(sqlstr)
			cursor = conn.execute(sqlstr)
			if len(cursor.fetchall()) == 0:
				name = 0 if lis[1] == '' else str(lis[1])
				weekday = 0 if lis[2] == '' else int(lis[2])
				volumn = 0 if lis[3] == '' else int(lis[3])
				open = 0 if lis[4] == '' else float(lis[4])
				high = 0 if lis[5] == '' else float(lis[5])
				low = 0 if lis[6] == '' else float(lis[6])
				close = 0 if lis[7] == '' else float(lis[7])
				adjclose = 0 if lis[8] == '' else float(lis[8])
				sqlstr = "INSERT OR IGNORE INTO price values('{}', '{}', {}, {}, {}, {}, {}, {}, {})".format(lis[0], name, weekday, volumn, open, high, low, close, adjclose)
				conn.execute(sqlstr)
				conn.commit()
				print(sqlstr)
			date = date - datetime.timedelta(1)
		except:
			date = date - datetime.timedelta(1)
# --------------------------------------------------- part3: FX
def getCur(id):
	print("not finish")
	currency = Share(id)
	print(currency.get_prev_close())
# --------------------------------------------------- choose function
while True:
	disp_menu()
	choice = int(input("Choose crawler: "))
	if choice == 0:
		break
	elif choice == 1:
		stock_menu()
		choice = int(input("Choose function: "))
		if choice == 0:
			disp_menu()
		elif choice == 1:
			stock = str(input("Key in stock symbol (ex: 2330.TW): "))
			getStock_daily(stock)
		elif choice == 2:
			stock = str(input("Key in stock symbol (ex: 2330.TW): "))
			y = int(input("請輸入抓取之年份: "))
			m = int(input("請輸入抓取之月份: "))
			d = int(input("請輸入抓取之日期: "))
			t = int(input("請輸入抓取之區間: "))
			getStock_his(stock, y, m, d, t)
		elif choice == 3:
			stock = str(input("Key in stock symbol (ex: 2330.TW): "))
			getStock_finance(stock)
	elif choice == 2:
		index = str(input("請輸入抓取之指數代碼 (ex: ^TWII): "))
		y = int(input("請輸入抓取之年份: "))
		m = int(input("請輸入抓取之月份: "))
		d = int(input("請輸入抓取之日期: "))
		t = int(input("請輸入抓取之區間: "))
		getIndex(index, y, m, d, t)
	elif choice == 3:
		cur = str(input("請輸入查詢之指數代碼 (ex: GBPUSD=X): "))
		getCur(cur)
	elif choice == 4:
		print("coming soon")
	else:
		break
	x = input("Press Enter")