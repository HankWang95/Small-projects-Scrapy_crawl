# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban_house.items import DoubanHouseItem
import re
import urllib.request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request 

class HousespicderSpider(CrawlSpider):
    name = 'housespicder'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/group/467221/discussion?start=0']

    rules = (
       
        #详情页
        Rule(LinkExtractor(allow=("group/topic/")),callback="parse_item"),
        #列表页
        Rule(LinkExtractor(allow=("group/467221/discussion"),restrict_xpaths=('//*[@id="content"]/div/div[1]/div[3]/span[4]/a'))),
    )

    def parse_item(self, response):
        item = DoubanHouseItem()
        sel = Selector(response)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        try:
            item['topic_name'] = sel.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tr[2]/td[2]/text()').extract()[0].strip()
        except:
            item['topic_name'] = sel.xpath('//*[@id="content"]/h1/text()').extract()[0].strip().replace("\n"," ")
        item['topic_url'] = response.url
        try:
            item['topic_content'] = sel.xpath('//*[@id="link-report"]/div[1]/p/text()').extract()
        except:
            item['topic_content'] = ""
        return item
