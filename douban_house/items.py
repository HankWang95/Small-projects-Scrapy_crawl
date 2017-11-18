# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic_name = scrapy.Field()#话题名称
    topic_content = scrapy.Field()
    topic_url = scrapy.Field()#话题链接
    #h_leasing_method = scrapy.Field()#租赁方式
    #h_location = scrapy.Field()#房屋位置
    #h_monthly_rent = scrapy.Field()#每月租金
