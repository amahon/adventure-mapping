# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LatLonPipeline(object):

    def process_item(self, item, spider):
        if 'latlon' in item:
            query = item['latlon'].split('q=')[1]
            item['latlon'] = [query.split('+')[0], query.split('+')[1]]
        return item
