# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 設定抓取頁面要抓取的變數
# 設定完需由 crawler.py 檔案進行 import 的動作
class ApplenewsItem(scrapy.Item):
    # define the fields for your item here like:
    # 依據要抓取的內容作變數的定義
    title = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    # pass
