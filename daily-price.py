# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: stock price crawler (daily price via google), Created Sep. 2017
Ver: 1.2 (modify function to crawl a list of company)
Link: 
'''
# --------------------------------------------------- libs import
import time,datetime
import requests
import sqlite3
conn = sqlite3.connect('ignore/daily.sqlite')
import csv
import tqdm
from urllib.request import urlopen, Request, URLError
from urllib.parse import urlencode
# --------------------------------------------------- Main panel
def disp_menu():
    print("--------------------")
    print("Daily stock price crawler")
    print("--------------------")
    print("1. Create table")
    print("2. Crawl firm price")
    print("3. Clear table (1)")
    print("4. Clear table (all)")
    print("0. End")
    print("--------------------")

def get_price(comp, start, end):
    '''
    Crawl daily price via google finance api
    Usage: get_price(<comp ticker>, <start day>, <end day>)
    ps: TPE
    '''
    url = 'http://finance.google.com/finance/historical?q={0}'.format(comp)
    url += '&startdate={0}&enddate={1}&output=csv'.format(start, end)
    res = urlopen(url)
    outptr = res.read().decode('utf-8').splitlines()
    outptr.reverse()
    rows = []
    for each in range(0, len(outptr)-1):
        try:
            ts, open_, high, low, close, volume = outptr[each].rstrip().split(',')
            open_, high, low, close = [float(x) for x in [open_, high, low, close]]
            dt = str(datetime.datetime.strptime(ts, '%d-%b-%y'))[0:10]
            serialnum = comp + dt[0:4] + dt[5:7] + dt[8:10]
            rows.append([serialnum, comp, dt, open_, high, low, close, volume])
            sqlstr = "INSERT OR IGNORE INTO {} (id, ticker, dt, open, high, low, close, volume) VALUES (?,?,?,?,?,?,?,?)".format(comp)
            conn.executemany(sqlstr, rows)
            conn.commit()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    while True:
        comp_name = ["AAPL", "AMZN", "MSFT", "GS", "GE", "IBM", "DIS", "INTC", "WMT", "JPM"]
        disp_menu()
        choice = int(input("Choose function: "))
        print("-----------------------------------------")
        # -- 0. Exit program --
        if choice == 0:
            break
        # -- 1. Create table --
        elif choice == 1:
            try:
                with open('firmlis.csv', 'r') as in_file:
                    reader = csv.reader(in_file, delimiter=' ')
                    next(reader, None)
                    for row in reader:
                        sqlstr = 'CREATE TABLE {} (id TEXT UNIQUE, ticker TEXT, dt DATETIME, open NUMERIC, high NUMERIC, low NUMERIC, close NUMERIC, volume NUMERIC)'.format(str(', '.join(row)))
                        conn.execute(sqlstr)
                        conn.commit()
                        print('-- Table created --')
            except Exception as e:
                print(e)
        # -- 2. Import price --
        elif choice == 2:
            try:
                with open('firmlis.csv', 'r') as in_file:
                    reader = csv.reader(in_file, delimiter=' ')
                    next(reader, None)
                    for row in tqdm.tqdm(reader):
                        start_day = "19970702"
                        end_day = "20171031"
                        get_price(str(', '.join(row)), start_day, end_day)
                    print('-- Finish crawl --')
            except Exception as e:
                print(e)
        # -- 3. Clear table (1) --
        elif choice == 3:
            try:
                choice_1 = str(input("Key-in Symbols: "))
                sqlstr = 'DELETE from {}'.format(choice_1)
                choice_2 = str(input("Delete table? (Y/N) "))
                if choice_2 == 'Y' or choice_2 == 'y':
                    cursor = conn.execute(sqlstr)
                    conn.execute(sqlstr)
                    conn.commit()
                    print('-- Table is cleared --')
            except Exception as e:
                print(e)
        # -- 4. Clear table (all) --
        elif choice == 4:
            try:
                with open('firmlis.csv', 'r') as in_file:
                    reader = csv.reader(in_file, delimiter=' ')
                    next(reader, None)
                    confirm = str(input("Delete all tables? (Y/N) "))
                    if confirm == 'Y' or confirm == 'y':
                        for row in reader:
                            sqlstr = 'DELETE from {}'.format(', '.join(row))
                            cursor = conn.execute(sqlstr)
                            conn.execute(sqlstr)
                            conn.commit()
                    print('-- Tables are cleared --')
            except Exception as e:
                print(e)