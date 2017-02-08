# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["http://www.jobbole.com/"]
    start_urls = (
        'http://www.http://www.jobbole.com//',
    )

    def parse(self, response):
        pass
