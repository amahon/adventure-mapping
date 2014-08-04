# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SwimmingHole(scrapy.Item):
    name = scrapy.Field()
    parent_name = scrapy.Field()
    latlon = scrapy.Field()

    activities = scrapy.Field()
    areas = scrapy.Field()
    bathingsuits = scrapy.Field()
    camping = scrapy.Field()
    confidence = scrapy.Field()
    dateupdated = scrapy.Field()
    description = scrapy.Field()
    directions = scrapy.Field()
    facilities = scrapy.Field()
    fee = scrapy.Field()
    phone = scrapy.Field()
    sanction = scrapy.Field()
    state = scrapy.Field()
    towns = scrapy.Field()
    type = scrapy.Field()
    verified = scrapy.Field()
    water = scrapy.Field()

