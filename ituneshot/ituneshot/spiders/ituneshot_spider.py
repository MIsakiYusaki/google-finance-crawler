# encoding: utf-8

from scrapy.spider import BaseSpider
# from bs4 import BeautifulSoup
from scrapy.selector import HtmlXPathSelector

from ituneshot.items import ItuneshotItem

class ituneshotCrawler(BaseSpider):
    name = 'ituneshot'
    start_urls = ['http://www.apple.com/itunes/charts/free-apps/']

    def parse(self, response):
        domain = 'apple.com'
        # res = BeautifulSoup(response.body)
        hxs = HtmlXPathSelector(response)
        apps = hxs.select('//*[@class = "section-content"]/ul/li')
        count = 0
        items = []
        for app in apps:
            # print apps.select('h3 a')[0].text
            # print apps.select('h4 a')[0].text
            ituneshotitem = ItuneshotItem()
            # print app.select('//h3/a/text()')[count].extract()
            ituneshotitem['app_name'] = app.select('//h3/a/text()')[count].extract()
            ituneshotitem['app_link'] = app.select('//h3/a/@href')[count].extract()
            ituneshotitem['category'] = app.select('//h4/a/text()')[count].extract()
            ituneshotitem['img_src'] = app.select('//a/img/@src')[count].extract()
            items.append(ituneshotitem)
            count += 1
        return items
        # print ituneshotitem
