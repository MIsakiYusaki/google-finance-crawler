# -*- coding: utf-8 -*-
# Author: Jimmy Chen
# PN: intraday stock price, Created July. 2017
# Ver 1.1 (program finish, transfer google finance data into SQLite DB)
# Link: 
# --------------------------------------------------- lib import
import csv
import datetime
import re
from urllib.request import urlopen, Request, URLError
from urllib.parse import urlencode
import sqlite3
conn = sqlite3.connect('priceDB.sqlite')

import pandas as pd
import requests
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
'''
[Variables]
database: connected table name
exchange: trading place of ticker, NASDAQ, NYSE, TPE...etc
ticker: symbols of the target stock
period: in seconds
days: maximum with 15 days
'''
def get_google_finance_intraday(database, exchange, ticker, period=60, days=15):
	url = 'http://www.google.com/finance/getprices?'
	url = url + 'x={exchange}&q={ticker}&i={period}&p={days}d&f=d,o,h,l,c,v'.format(exchange=exchange, ticker=ticker, period=period, days=days)
	rows = []
	times = []
	response = urlopen(url)
	reader = response.read().decode('utf-8').splitlines()
	for row in reader:
		if re.match(r'[a|\d]',row[0]):
			timer, close, high, low, open_, volume = row.split(',')
			# rows.append([id_, close, high, low, open_, volume])
			if timer[0].startswith('a'):
				day = float(timer[1:])
				timer = 0
			else:
				timer = float(timer)
			open_, high, low, close = [float(x) for x in [open_, high, low, close]]
			dt = datetime.datetime.fromtimestamp(day + (period * timer))
			# print(dt)
			rows.append([ticker, dt, close, high, low, open_, volume])
	# sqlstr = 
	conn.executemany("INSERT OR IGNORE INTO {} (ticker, dt, close, high, low, open, volume) VALUES (?,?,?,?,?,?,?)".format(database), rows)
	conn.commit()
# --------------------------------------------------- control center
while True:
	disp_menu()
	choice = int(input("Choose function: "))
	print("-----------------------------------------")
	if choice == 0:
		break
	# -- 1. Create table --
	elif choice == 1:
		try:
			choice = str(input("Key-in Table name: "))
			sqlstr = ('CREATE TABLE {} (ticker TEXT, dt DATETIME UNIQUE, close NUMERIC, high NUMERIC, low NUMERIC, open NUMERIC, volume NUMERIC)'.format(str(choice)))
			conn.execute(sqlstr)
			conn.commit()
			print('-- Table created --')
		except Exception as e:
			print(str(e))
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