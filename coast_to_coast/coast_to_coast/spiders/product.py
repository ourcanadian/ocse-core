# -*- coding: utf-8 -*-
import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
