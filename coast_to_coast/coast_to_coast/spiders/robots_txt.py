# -*- coding: utf-8 -*-
import scrapy


class RobotsTxtSpider(scrapy.Spider):
    name = 'robots_txt'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
