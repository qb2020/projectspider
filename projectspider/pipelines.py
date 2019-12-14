# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class ProjectspiderPipeline(object):
    #    def process_item(self, item, spider):
    #        return item

    # class TutorialPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['spiderdb']
        self.collection = db['spiderCollection']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        # print "Pipeline", item['text']
        return item
