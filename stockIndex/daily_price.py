# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: stock price crawler (daily from google), Created Sep. 2017
Ver: 1.1 (crawl firm daily price from google)
Link: 
'''
# --------------------------------------------------- libs import
import time,datetime
import requests
import sqlite3
from urllib.request import urlopen, Request, URLError
from urllib.parse import urlencode
# --------------------------------------------------- Main panel
def disp_menu():
    print("--------------------")
    print("Store intraday stock price")
    print("--------------------")
    print("1. Create table")
    print("2. Crawl firm price")
    print("3. Clear table")
    print("0. End")
    print("--------------------")

def get_price(comp, start, end):
    '''
    Crawl daily price from google finance
    Usage: get_price(<comp ticker>, <start day>, <end day>)
    ps: TPE
    '''
    url = 'http://www.google.com/finance/historical?q={0}'.format(comp)
    url += '&startdate={0}&enddate={1}&output=csv'.format(start, end)
    res = urlopen(url)
    outptr = res.read().decode('utf-8').splitlines()
    outptr.reverse()
    rows = []
    for each in range(0, len(outptr)-1):
        # print(outptr[each])
        ts, open_, high, low, close, volume = outptr[each].rstrip().split(',')
        open_, high, low, close = [float(x) for x in [open_, high, low, close]]
        dt = datetime.datetime.strptime(ts, '%d-%b-%y')
        rows.append([comp, dt, open_, high, low, close, volume])
    conn = sqlite3.connect('firm.sqlite')
    conn.executemany("INSERT OR IGNORE INTO {} (ticker, dt, open, high, low, close, volume) VALUES (?,?,?,?,?,?,?)".format(comp), rows)
    conn.commit()

if __name__ == '__main__':
    while True:
        disp_menu()
        choice = int(input("Choose function: "))
        print("-----------------------------------------")
        if choice == 0:
            break
        # -- 1. Create table --
        elif choice == 1:
            conn = sqlite3.connect('firm.sqlite')
            try:
                choice = str(input("Key-in Table name: "))
                sqlstr = ('CREATE TABLE {} (ticker TEXT, dt DATETIME UNIQUE, open NUMERIC, high NUMERIC, low NUMERIC, close NUMERIC, volume NUMERIC)'.format(str(choice)))
                conn.execute(sqlstr)
                conn.commit()
                print('-- Table created --')
            except Exception as e:
                print(str(e))
        # -- 1. Create table --
        elif choice == 2:
            try:
                start_day = str(input("Key-in start day(ex: 20111227): "))
                end_day = str(input("Key-in end day(ex: 30111227): "))
                ticker = str(input("Key-in ticker(ex: AAPL): "))
                q = get_price(ticker, start_day, end_day)
                print('-- Finish crawl --')
            except Exception as e:
                print(str(e))
        # -- 3. Clear DB --
        elif choice == 3:
            conn = sqlite3.connect('firm.sqlite')
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