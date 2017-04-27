# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ApplenewsPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('apple.sqlite')
		self.cur = self.conn.cursor()
		# clean DB first
		sqlstr = 'delete from apple'
		self.cur.execute(sqlstr)
		self.cur.execute("create table if not exists apple(title varchar(100), content text, time varchar(50))")

	def close_spider(self, spider):
		self.conn.commit()
		self.conn.close()

	def process_item(self, item, spider):	
		self.storeInDb(item)
		return item

	def storeInDb(self, item):
		sqlstr = 'INSERT INTO apple(title, content, time) values(?, ?, ?)'
		self.cur.execute(sqlstr, (item['title'], item['content'], item['time']))
		return item