# -*- coding: utf-8 -*-
import scrapy
from grab_moe_image.items import GrabMoeimgItem

class GrabImgSpider(scrapy.Spider):
    name = 'grab_img'
    allowed_domains = ['moeimg.net']
    start_urls = ['http://moeimg.net/page/1/']

    def parse(self, response):
        print('#' * 60)
        next_page = response.xpath("//div[@class='pagenation']/ul/li[@class='next']/a/@href").extract()
        print()
        if len(next_page):
            node_list = response.xpath("//div[@class='post']/div[@class='entry-header']/h2/a/@href")
            if len(node_list):
                for page in node_list:
                    yield scrapy.Request(page.extract(),callback=self.parse)
            yield scrapy.Request(next_page[0],callback=self.parse)
        else:
            node_list = response.xpath("//div[@class='post']/div[@class='box']")
            name = response.xpath("//div[@class='blog-info-f']/div[@class='tag']/a/text()").extract()
            album = response.xpath("//div[@class='entry-header']/h1/text()").extract()
            for node in node_list:
                item = GrabMoeimgItem()
                item['name'] = name
                item['album'] = album
                item['num'] = node.xpath("./div/text()").extract()
                item['image_link'] = node.xpath("./a/@href").extract()
                print(item)
                yield item