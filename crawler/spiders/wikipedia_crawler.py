__author__ = 'gumdelli'

from scrapy.spider import Spider

class WikipediaSpider(Spider):
    name = "wikipedia"
    allowed_Domains = ["wikipedia.org"]
    start_urls = [
        "http://www.wikipedia.org/wiki/Hash_table"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
