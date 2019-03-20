# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiandaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_type = scrapy.Field()
    rank = scrapy.Field()
    times = scrapy.Field()
    trend = scrapy.Field()
