# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NetaporterscrapeItem(scrapy.Item):
    # class to specify structure of Product Data
    name = scrapy.Field(serializer=str)
    brand = scrapy.Field(serializer=str)
    original_price = scrapy.Field(serializer=float)
    sale_price = scrapy.Field(serializer=float)
    image_url = scrapy.Field(serializer=str)
    product_page_url = scrapy.Field(serializer=str)
    product_category = scrapy.Field(serializer=str)
