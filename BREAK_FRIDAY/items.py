# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BreakFridayPage(scrapy.Item):
    # define the fields for your item here like:
    options = scrapy.Field()
    pass

class BreakFridayBanner(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    pass