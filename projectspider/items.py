# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #   pass

    # import scrapy
    # class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # text = scrapy.Field()
    # author = scrapy.Field()
    # tags = scrapy.Field()

    # updated below fields for googlespider.py
    title = scrapy.Field()
    desc = scrapy.Field()
    url = scrapy.Field()
# pass
