# encoding: utf-8

import scrapy
from bs4 import BeautifulSoup
from Dmoz.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
    ]

    def parse(self, response):
        domain = ['dmoz.org']
        res = BeautifulSoup(response.body)
