# -*- coding: utf-8 -*-
# PN: twse chart
# Version 1.0
# KW: plotting
# --------------------------------------------------- libs import
import sqlite3
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import matplotlib.pyplot as pt
# --------------------------------------------------- connect db
conn = sqlite3.connect('twse.sqlite')
# --------------------------------------------------- disp_menu()
def disp_menu():
	print("加權指數歷史查詢系統")
	print("--------------------")
	print("1. 顯示歷年價格資訊")
	print("2. 價格走勢圖")
	print("0. 結束")
	print("--------------------")
# --------------------------------------------------- fetch_data()
def chart():
	data = []
	cursor = conn.execute("select * from prices order by date;")
	for row in cursor:
		data.append(list(row))
	x = np.arange(0, len(data))
	dataset = [list(), list(), list()]
	for i in range(0, len(data)):
		for j in range(0, 3):
			dataset[j].append(data[i][j+1])
	w = np.array(dataset[0])	# price
	y = np.array(dataset[1])	# change
	z = np.array(dataset[2])	# volumn
	pt.ylabel("NTD$")
	pt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))
	pt.plot(x, w, color="blue", label="price")
	pt.plot(x, y, color="red", label="change")
	# pt.plot(x, z, color="green", label="volumn")
	pt.xlim(0, len(data))
	pt.ylim(10, 40)
	pt.title("TWSE Trend (Taiwan)")
	pt.legend()
	pt.show()
# --------------------------------------------------- disp_alldata()
def disp_alldata():
	cursor = conn.execute('select * from prices order by date desc;')    # desc => descending date
	n = 0
	for row in cursor:
		print("日期: {}，price: {}，change: {}，volumn: {}".format(row[0], row[1], row[2], row[3]))
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
		disp_alldata()
	elif choice == 2:
		chart()
	else:
		break
	x = input("Press Enter")