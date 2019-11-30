# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

def url_join(href_part, loader_context):
    response_context = loader_context.get('response_context')
    return response_context.urljoin(href_part)

class TutorialItem(scrapy.Item):
    url = scrapy.Field(input_processor=MapCompose(url_join), output_processor=Join(),)
    job_name = scrapy.Field(output_processor=Join())
    salary = scrapy.Field()



    # salary_min = scrapy.Field()
    # salary_max = scrapy.Field()