# -*- coding: utf-8 -*-
# PN: gasoline db
# Version 1.0
# KW: crawler, database create, plotting
# --------------------------------------------------- libs import
import sqlite3
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import matplotlib.pyplot as pt
# --------------------------------------------------- connect db
conn = sqlite3.connect('prices.sqlite')

# --------------------------------------------------- disp_menu()
def disp_menu():
	print("加權指數歷史查詢系統")
	print("--------------------")
	print("1. 載入最新價格資訊")
	print("2. 顯示歷年價格資訊")
	print("3. 最近10週價格資訊")
	print("4. 價格走勢圖")
	print("0. 結束")
	print("--------------------")
# --------------------------------------------------- fetch_data()
def chart():
	data = []
	cursor = conn.execute("select * from price order by date;")
	for row in cursor:
		data.append(list(row))
	x = np.arange(0, len(data))
	dataset = [list(), list(), list()]
	for i in range(0, len(data)):
		for j in range(0, 3):
			dataset[j].append(data[i][j+1])
	w = np.array(dataset[0])
	y = np.array(dataset[1])
	z = np.array(dataset[2])
	pt.ylabel("NTD$")
	pt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))
	pt.plot(x, w, color="blue", label="92")
	pt.plot(x, y, color="red", label="95")
	pt.plot(x, z, color="green", label="98")
	pt.xlim(0, len(data))
	pt.ylim(10, 40)
	pt.title("Gasoline Prices Trend (Taiwan)")
	pt.legend()
	pt.show()
# --------------------------------------------------- disp_alldata()
def disp_alldata():
	cursor = conn.execute('select * from prices order by gdate desc;')    # desc => descending date
	n = 0
	for row in cursor:
		print("日期: {}，92無鉛: {}，95無鉛: {}，95無鉛: {}".format(row[0], row[1], row[2], row[3]))
		n += 1
		if n == 20:
			x = input("請按 Enter 繼續 ...(Q: 回主選單)")
			if x == 'Q' or x == 'q':
				break
				n = 0
# --------------------------------------------------- main menu
while True:
	disp_menu()
	choice = int(input("請輸入您的選擇:"))
	if choice == 0:
		break
	elif choice == 1:
		fetch_data()
	elif choice == 2:
		disp_alldata()
	elif choice == 3:
		disp_10data()
	elif choice == 4:
		chart()
	else:
		break
	x = input("Press Enter")