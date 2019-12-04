# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['icanhazip.com']
    base_url = 'http://icanhazip.com/'

    def start_requests(self):
        for _ in range(10):
            yield scrapy.Request(self.base_url, self.parse, dont_filter=True, meta={'download_timeout': 20, 'max_retry_times': 30})

    def parse(self, response):
        # r = scrapy.http.Response
        # r.body
        self.log(response.body)
