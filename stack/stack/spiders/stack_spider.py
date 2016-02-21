from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

class StackSpider(Spider):
    name = "stack"
    #allowed_domains = ["stackoverflow.com"]
    allowed_domains = ["reddit.com"]
    start_urls = [
        #"http://stackoverflow.com/questions?pagesize=50&sort=newest",
        "https://www.reddit.com/r/india",
    ]
    def parse(self, response):
        posts = Selector(response).xpath('//p[@class="title"]/a')

        for post in posts:
            item = StackItem()
            item['title'] = post.xpath(
                'text()').extract()[0]
            item['url'] = post.xpath(
                '@href').extract()[0]
            yield item
