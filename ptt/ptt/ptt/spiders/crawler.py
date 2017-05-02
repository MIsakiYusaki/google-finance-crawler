# -*- coding: utf-8 -*-
# PN: ptt crawler, Created Apr. 2017
# Version 1.3 (figuring crawling prev/back pages)
# Link: 
# http://city.shaform.com/blog/2016/02/28/scrapy.html
# http://blog.bryanbigdata.com/2015/07/python-crawler.html
# --------------------------------------------------- lib import
from datetime import datetime

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ptt.items import PttItem
from bs4 import BeautifulSoup
# --------------------------------------------------- Start!
class PTTSpider(CrawlSpider):
	name = 'ptt'
	allowed_domains = ['ptt.cc']
	start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']

	# 判斷是否要換頁進行爬蟲
	_pages = 0
	_MAX_PAGES = 4

	def start_requests(self):
		yield scrapy.Request(self.start_urls[0], self.parse_page, cookies = {'over18':'1'}) 

	def parse_page(self, response):
		self._pages += 1
		domain = 'https://www.ptt.cc'
		soup = BeautifulSoup(response.body, 'lxml')
		# print(soup.select('.r-ent'))
		for item in soup.select('.r-ent'):
			yield scrapy.Request(domain + item.select('a')[0]['href'], self.parse_post)
		if self._pages < self._MAX_PAGES:
			next_url = soup.select('div[id="action-bar-container"] > div[class="action-bar"] > div:nth-of-type(2) > a:nth-of-type(2)')[0]['href']
			if next_url:
				domain = 'https://www.ptt.cc'
				next_url = domain + next_url
				# print(next_url)
				self.log('page_url: %s' % next_url)
				## 将 「下一页」的链接传递给自身，并重新分析
				yield scrapy.Request(next_url, self.parse_page)
			else:
				print('no next page')
		else:
			print('max pages reached')

	def parse_post(self, response):
		soup = BeautifulSoup(response.body, 'lxml')
		# text = soup.select('div[id="main-content"] div[class="article-metaline"]')
		# text = soup.select('div[id="main-content"]  > div:nth-of-type(4) > span:nth-of-type(2)')[0].text
		pttitem = PttItem()
		pttitem['title'] = soup.find('meta', property="og:title")['content']
		time = soup.select('div[id="main-content"]  > div:nth-of-type(4) > span:nth-of-type(2)')[0].text
		pttitem['date'] = datetime.strptime(time, '%a %b %d %H:%M:%S %Y')
		pttitem['content'] = soup.select('div[id="main-content"]')[0].text
		pttitem['url'] = response.url
		comments = []
		total_score = 0
		for comment in soup.select('div[class="push"]'):
			push_user = comment.select('span[class="f3 hl push-userid"]')[0].text
			push_content = comment.select('span[class="f3 push-content"]')[0].text
			try:
				push_tag = comment.select('span:nth-of-type(1)')[0].text
				if '推' in push_tag:
					score = 1
				elif '噓' in push_tag:
					score = -1
				else:
					score = 0	
			except:
				score = 0	
			comments.append({
            	'user': push_user,
            	'content': push_content,
            	'score': score})
			total_score += score

		pttitem['comments'] = comments
		pttitem['score'] = total_score

		# return pttitem
