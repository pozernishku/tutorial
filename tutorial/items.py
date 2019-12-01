# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

regex_get_digits = re.compile(r'\D+', re.MULTILINE)

def url_join(href_part, loader_context):
    response_context = loader_context.get('response_context')
    return response_context.urljoin(href_part)

def slr_get(sal, loader_context):
    low_high = loader_context.get('low_high')

    if sal:
        result = sal.split('–')

        if low_high == 0:
            result = result[low_high]
        else:
            result = result[low_high] if len(result) == 2 else ''
            
        match = regex_get_digits.search(result)
        if match:
            return regex_get_digits.sub('', result)
        else:
            return result


class TutorialItem(scrapy.Item):
    url = scrapy.Field(input_processor=MapCompose(url_join), output_processor=Join(),)
    job_name = scrapy.Field(output_processor=Join())
    salary_low_hrn = scrapy.Field(input_processor=MapCompose(slr_get), output_processor=TakeFirst())
    salary_high_hrn = scrapy.Field(input_processor=MapCompose(slr_get), output_processor=TakeFirst())
    # salary_low_usd = scrapy.Field()
    # salary_high_usd = scrapy.Field()
