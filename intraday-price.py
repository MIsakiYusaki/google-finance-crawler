# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: intraday stock price, Created July. 2017
Ver 1.2 (modify code to crawl from list of company)
Link: 
'''
# --------------------------------------------------- lib import
import datetime
import re
import requests
from urllib.request import urlopen, Request, URLError
from urllib.parse import urlencode
import sqlite3
conn = sqlite3.connect('ignore/intra-daily.sqlite')
# --------------------------------------------------- Main panel
def disp_menu():
	print("--------------------")
	print("Store intraday stock price")
	print("--------------------")
	print("1. Create table")
	print("2. Trans")
	print("3. Clear table")
	print("0. End")
	print("--------------------")
# --------------------------------------------------- program
def get_google_finance_intraday(database, exchange, ticker, period=60, days=15):
	'''
	[Variables]
	database: connected table name
	exchange: trading place of ticker, NASDAQ, NYSE, TPE...etc
	ticker: symbols of the target stock
	period: in seconds
	days: maximum with 15 days
	DJI: INDEXDJX
	'''
	url = 'http://www.google.com/finance/getprices?'
	url = url + 'x={exchange}&q={ticker}&i={period}&p={days}d&f=d,o,h,l,c,v'.format(exchange=exchange, ticker=ticker, period=period, days=days)
	rows = []
	times = []
	response = urlopen(url)
	reader = response.read().decode('utf-8').splitlines()
	for row in reader:
		if re.match(r'[a|\d]',row[0]):
			timer, close, high, low, open_, volume = row.split(',')
			if timer[0].startswith('a'):
				day = float(timer[1:])
				timer = 0
			else:
				timer = float(timer)
			open_, high, low, close = [float(x) for x in [open_, high, low, close]]
			dt = datetime.datetime.fromtimestamp(day + (period * timer))
			rows.append([ticker, dt, close, high, low, open_, volume])
	conn.executemany("INSERT OR IGNORE INTO {} (ticker, dt, close, high, low, open, volume) VALUES (?,?,?,?,?,?,?)".format(database), rows)
	conn.commit()
# --------------------------------------------------- control center
while True:
    comp_name = ["AAPL", "AMZN", "MSFT", "GS", "GE", "IBM", "DIS", "INTC", "WMT", "JPM"]
	disp_menu()
	choice = int(input("Choose function: "))
	print("-----------------------------------------")
	if choice == 0:
		break
	# -- 1. Create table --
    elif choice == 1:
        try:
            with open('firmlis-intra.csv', 'r') as in_file:
                reader = csv.reader(in_file, delimiter=' ')
                next(reader, None)
                for row in reader:
                    sqlstr = 'CREATE TABLE {} (id TEXT UNIQUE, ticker TEXT, dt DATETIME, open NUMERIC, high NUMERIC, low NUMERIC, close NUMERIC, volume NUMERIC)'.format(str(', '.join(row)))
                    conn.execute(sqlstr)
                    conn.commit()
                    print('-- Table created --')
        except Exception as e:
            print(e)
	# -- 2. Trans first phase --
	elif choice == 2:
		try:
			choice_1 = str(input("Key-in store DB: "))
			choice_2 = str(input("Key-in Exchange: "))
			choice_3 = str(input("Key-in Symbols: "))
			get_google_finance_intraday(choice_1, choice_2, choice_3)
			print('-- Price imported --')
			print("-----------------------------------------")
		except Exception as e:
			print(str(e))
	# -- 3. Clear DB --
	elif choice == 3:
		try:
			choice_1 = str(input("Key-in Symbols: "))
			sqlstr = 'delete from {}'.format(choice_1)
			cursor = conn.execute(sqlstr)
			choice_2 = str(input("Delete table? (Y/N) "))
			if choice_2 == 'Y' or choice_2 == 'y':
				conn.execute(sqlstr)
				conn.commit()
				print('-- Table is clear --')
		except Exception as e:
			print(str(e))
	else:
		print('-- Return --')