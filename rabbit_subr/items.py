# -*- coding: utf-8 -*-

# Here I've defined the models for the scraped item (the post title)
# C. B. Salling

import scrapy

class RabbitSubRPost(scrapy.Item):
    post_title = scrapy.Field()
