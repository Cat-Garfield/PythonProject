# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from grab_moe_image.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline

class GrabMoeImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['image_link'][0]
        print(image_link)
        yield scrapy.Request(image_link)

    def item_completed(self,results,item,info):
        print(results)
        image_path = [x['path'] for ok,x in results if ok]
        path = IMAGES_STORE + item['album'][0] + '\\'
        if not os.path.exists(path):
            os.mkdir(path)
        os.rename(IMAGES_STORE + image_path[0],path + item['num'][0] + '.jpg')
        return item