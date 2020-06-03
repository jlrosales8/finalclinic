# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinalclinicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pcp = scrapy.Field()
    plan = scrapy.Field()
    hcocode = scrapy.Field()
    npi = scrapy.Field()