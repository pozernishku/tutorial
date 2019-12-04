# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy.loader import ItemLoader
from random import choice
from scrapy import signals

class WkSpSpider(scrapy.Spider):
    name = 'wk_sp'
    allowed_domains = ['www.work.ua']
    base_url = 'https://www.work.ua/jobs-kyiv-it/?advs=1&page={}&_pjax=%23pjax-job-list&_pjax=%23pjax-job-list'
    # yet = False

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(WkSpSpider, cls).from_crawler(crawler, *args, **kwargs)
        # spider = super().from_crawler(crawler, *args, **kwargs)
        # crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        # crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    # def spider_closed(self, spider):
    #     spider.logger.info('>>>> spider_closed {}'.format(spider.name))
    #     spider.logger.info(type(self.crawler.engine.crawl))
    #     spider.logger.info(self.crawler.engine.crawl)
    #     if not self.yet:
    #         # self.crawler.engine.crawl(self.create_request(), self)
    #         self.crawler.engine.crawl(scrapy.Request('https://www.work.ua/jobs/3599724/'), self)
    #         self.yet = True

    # TODO
    # See also https://docs.scrapy.org/en/latest/topics/practices.html#run-from-script
    # def spider_idle(self, spider):
    #     spider.logger.info('>>>> spider_idle {}'.format(spider.name))
    #     if not self.yet:
    #         self.crawler.engine.crawl(self.create_request(), self)
    #         self.yet = True
    
    # TODO 
    # def create_request(self):
    #     yield scrapy.Request('https://www.work.ua/jobs/3599724/')

    def start_requests(self):
        for i in range(1, 3): # change pages count
            yield scrapy.Request(self.base_url.format(i), self.parse, meta={'download_timeout': 20,
                                                                            'max_retry_times': 300}) # , meta={'proxy': choice(self.proxies)}

    def parse(self, response):
        rows = response.xpath('//div[@id="pjax-job-list"]/div[contains(@class, "job-link")]')

        for row in rows:
            l = ItemLoader(item=TutorialItem(), selector=row, response_context=response)
            l.add_xpath('url', './/h2/a/@href')
            l.add_xpath('job_name', './/h2/a/text()')
            l.context['low_high'] = 0
            l.add_xpath('salary_low_hrn', './/div/b/text()')
            l.context['low_high'] = 1
            l.add_xpath('salary_high_hrn', './/div/b/text()')
            # l.add_xpath('salary_low_usd', './/div/b/text()')
            # l.add_xpath('salary_high_usd', './/div/b/text()')
            yield l.load_item() # not return

        # for row in rows:
        #     job = TutorialItem()
        #     job['url'] = response.urljoin(row.xpath('.//h2/a/@href').get()) # or just row.xpath('h2/a/@href').get()
        #     job['job_name'] = row.xpath('.//h2/a/@title').get()
        #     job['salary'] = row.xpath('.//div/b/text()').get()
        #     yield job