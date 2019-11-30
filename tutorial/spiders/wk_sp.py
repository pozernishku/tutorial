# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy.loader import ItemLoader

class WkSpSpider(scrapy.Spider):
    name = 'wk_sp'
    allowed_domains = ['www.work.ua']
    base_url = 'https://www.work.ua/jobs-kyiv-it/?advs=1&page={}&_pjax=%23pjax-job-list&_pjax=%23pjax-job-list'

    def start_requests(self):
        for i in range(1, 3): # change pages count
            yield scrapy.Request(self.base_url.format(i), self.parse)

    def parse(self, response):
        rows = response.xpath('//div[@id="pjax-job-list"]/div[contains(@class, "job-link")]')

        for row in rows:
            l = ItemLoader(item=TutorialItem(), selector=row, response_context=response)
            l.add_xpath('url', './/h2/a/@href')
            l.add_xpath('job_name', './/h2/a/text()')
            l.add_xpath('salary', './/div/b/text()')
            yield l.load_item() # not return

        # for row in rows:
        #     job = TutorialItem()
        #     job['url'] = response.urljoin(row.xpath('.//h2/a/@href').get()) # or just row.xpath('h2/a/@href').get()
        #     job['job_name'] = row.xpath('.//h2/a/@title').get()
        #     job['salary'] = row.xpath('.//div/b/text()').get()
        #     yield job