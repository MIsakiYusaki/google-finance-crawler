# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 將抓取下來的資料作清洗、整理、匯入資料庫的動作
import sqlite3 as lite

class ApplenewsPipeline(object):

    def open_spider(self, spider):
        # the process run after spider open
        # connect db, if db not exists, create db
        self.con = lite.connect('apple.sqlite')
        self.cur = self.con.cursor()
        # 若 apple db 不存在時建立
        self.cur.execute("CREATE TABLE IF NOT EXISTS apple(title VARCHAR(100), content TEXT, time VARCHAR(50))")
        # pass
    def close_spider(self, spider):
        # the process run before spider close
        # commit db, then close db
        self.con.commit()
        self.con.close()
        # pass
    def process_item(self, item, spider):
        # put crawler content into db
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        # 產生 sql
        sql = 'INSERT INTO apple({}) values({})'
        self.cur.execute(sql.format(col, placeholders), item.values())
        return item
