from scrapy.spiders import Spider
from scrapy.selector import Selector

import scrapy

class CraigslistSamItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    pass

class MySpider(Spider):
    name = "carg"
    allowed_domains = ["craglist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/sfc/npo"]

    def parse(self,response):
        hxs = Selector(response)
        titles = hxs.xpath("//p")
        items= []
        for titles in titles:
            item = CraigslistSamItem()
            item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return items
