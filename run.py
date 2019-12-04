import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from tutorial.spiders.wk_sp import WkSpSpider

# process = CrawlerProcess(settings={
#     'FEED_FORMAT': 'json',
#     'FEED_URI': 'items.json'
# })

# process.crawl(WkSpSpider)
process = CrawlerProcess(get_project_settings())

process.crawl('wk_sp') # , domain='scrapinghub.com'
# OR
# process.crawl(WkSpSpider)

process.start() # the script will block here until the crawling is finished
