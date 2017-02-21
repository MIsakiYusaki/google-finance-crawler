# -*- coding: utf-8 -*-
# PN: apple news crawler, Created Jan, 2017
# Version 1.0
# KW: 
# ---------------------------------------------------
# --------------------------------------------------- libraries import
import scrapy
from bs4 import BeautifulSoup
# import data structure from items.py
from appleNews.items import ApplenewsItem

class AppleCrawler(scrapy.Spider):
    # set name, urls, parse
    # scrapy crawl name -> 啟動 crawler
    name = 'apple'
    start_urls = ['http://www.appledaily.com.tw/realtimenews/section/new/']
    # 抓取主函數
    def parse(self, response):
        domain = 'http://www.appledaily.com.tw'
        # Beautify with BeautifulSoup
        res = BeautifulSoup(response.body)
        for news in res.select('.rtddt'):
            # print news.select('h1')[0].text     # h1 tag 中的第一個 h1
            # change the url
            # print domain + news.select('a')[0]['href']
            # Generator, 產生器，only activated when for loop start
            # run def 'parse_detail' when yield activated
            # use for second layer(link) content
            yield scrapy.Request(domain + news.select('a')[0]['href'], self.parse_detail)

    # second layer crawler, run when yield function activated
    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        appleNewsitem = ApplenewsItem()
        appleNewsitem['title'] = res.select('#h1')[0].text
        appleNewsitem['content'] = res.select('.trans')[0].text
        appleNewsitem['time'] = res.select('.gggs time')[0].text
        return appleNewsitem
        print res.select('#h1')[0].text

# 將 ApplenewsItem() 抓取下來的內容 appleNewsitem 輸出成 json 檔 (apple.json)
# -> scrapy crawl apple -o apple.json -t json
