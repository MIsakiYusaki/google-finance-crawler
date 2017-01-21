from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from weather.items import WeatherItem

class WeatherSpider(BaseSpider):
    name = "weather"
    allowed_domains = ["http://www.cwb.gov.tw/"]
    start_urls = ["http://www.cwb.gov.tw/V7/forecast/index.htm"]

    def parse(self, response):
        apps = response.xpath('//*[@class="N_AreaList"]/tbody/tr[3]/text()').extract()
        print apps
        items = []
    	for app in apps:
            item = WeatherItem()
            item['degree'] = app.xpath('//td[2]/a/text()').extract()
            item['rate'] = app.xpath('//td[3]/a/text()').extract()
            item['describe'] = app.xpath('//td[4]/a/div/text()').extract()
            # print apps.xpath('//td[2]/a/text()').extract()
            items.append(item)
        return items
