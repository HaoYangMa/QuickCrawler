#爬虫子函数集合包

import  re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from source.items import sourceItem ##这是我定义的需要保存的字段，（导入原本的source项目中，items文件中的sourceItem类）

class Myspider(scrapy.Spider):
    name = 'source'
    allowed_domains = ['163.com']
    bash_url = 'http://music.163.com/'
    start_id = 409060868
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 10000):
            start_id = str(int(start_id)+1)
            url = self.bash_url + '#/song?id=' + start_id + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://music.163.com/#/song?id=409060868', self.parse)

    def parse(self, response):
        print(response.text)

    def get_name(self,response):
        tds = BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find('a').get_text()
            noveurl = td.find('a')['href']
            yield Request(noveurl,callback=self.get_chapterurl,meta={'name': novelname,'url':noveurl})

    def get_chapterurl(self,response):
        item = sourceItem()
        item['name'] = str(response.text,'lxml')
        item['novelurl'] = response.meta['url']
        category = BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text,'lxml').find()
        bash_url = BeautifulSoup
        name_id = str(bash_url)[-6:-1].replace('/','')
        item['category'] = str(category).replace('/','')
        item['author'] = str(author).replace('/','')
        item['name_id'] = name_id

        return item