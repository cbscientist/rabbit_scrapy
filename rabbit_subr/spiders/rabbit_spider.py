# Crawl spider that deals with pagination
# C. B. Salling

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from rabbit_subr2.items import *

class RabbitSubRSpider(CrawlSpider):
    name = "rabbit"
    allowed_domains = ["reddit.com"]
    start_urls = ["http://www.reddit.com/r/Rabbits"]

    rules = ( Rule( LxmlLinkExtractor( restrict_xpaths = ('//a[@rel = "nofollow next"]', )),
    callback = 'parse_items', follow = True),)

    def parse_items(self, response):
        for sel in response.xpath('//p[@class = "title"]/a[@*]'):
            item = RabbitSubRItem()
            item['post_title'] = sel.xpath('text()').extract()
            yield item

