# Scraper to pull info from r/rabbits subreddit frontpage
# C. B. Salling 2015-03

import scrapy
from rabbit_subr.items import *

class RabbitSubRSpider(scrapy.Spider):
    name = "rabbit_fp"
    allowed_domains = ["reddit.com"]
    start_urls = ["http://www.reddit.com/r/Rabbits/"]

    def parse(self, response):
        for sel in response.xpath('//p[@class = "title"]/a[@*]'):
            item = RabbitSubRPost()
            item['post_title'] = sel.xpath('text()').extract()
            yield item

