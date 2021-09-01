import scrapy
from ..items import DataItem

class Content(scrapy.Spider):
    name = 'datas'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        items = DataItem()
        all_div = response.css('div.quote')
        for foo in all_div:
            des = foo.css(".text::text").extract()
            author = foo.css(".author::text").extract()
            tag = foo.css(".tag::text").extract()
            items['des'] = des
            items['author'] = author
            items['tag'] = tag

            yield items