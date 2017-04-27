# -*- coding: utf-8 -*-
# PN: ptt crawler, Created Apr. 2017
# Version 1.1 (dealing with content select)
# Link: 
# http://city.shaform.com/blog/2016/02/28/scrapy.html
# http://blog.bryanbigdata.com/2015/07/python-crawler.html
# --------------------------------------------------- lib import
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ptt.items import PttItem
from bs4 import BeautifulSoup
# --------------------------------------------------- Start!
class PTTSpider(CrawlSpider):
	name = 'ptt'
	allowed_domains = ['ptt.cc']
	start_urls = ['http://www.ptt.cc/bbs/Gossiping/index.html']
	def start_requests(self):
		yield scrapy.Request(self.start_urls[0], self.parse_list, cookies = {'over18':'1'}) 

	def parse_list(self, response):
		domain = 'https://www.ptt.cc/'
		soup = BeautifulSoup(response.body, 'lxml')
		for item in soup.select('.r-ent'):
			yield scrapy.Request(domain + item.select('a')[0]['href'], self.parse_list_detail)
	def parse_list_detail(self, response):
		soup = BeautifulSoup(response.body, 'lxml')
		text = soup.select('div[id="main-content"] div[class="article-metaline"]')
		print(text.find(''))
		# pttitem = PttItem()
		# pttitem['title'] = soup.find('meta', property="og:title")['content']
		# pttitem['author'] = text.find('div')
		# pttitem['date'] = soup.select('.article-metaline+ .article-metaline .article-meta-value')[0].text
		# pttitem['content'] = soup.select('#main-content')[0].text
		# # pttitem['content'] = soup.find('meta', property="og:description")['content']
		# # pttitem['comments'] = soup.select
		# pttitem['url'] = response.url
		# return pttitem