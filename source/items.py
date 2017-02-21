#需要爬取并整理进数据库的字段

import scrapy

class sourceItem(scrapy.item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #小说名字
    name = scrapy.Field()
    #作者名字
    author = scrapy.Field()
    #网址
    novelurl = scrapy.Field()
    #字数
    serialstatus = scrapy.Field()
    #文章种类
    category = scrapy.Field()
    #文章序号
    name_id = scrapy.Field()

