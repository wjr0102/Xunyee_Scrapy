# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xunyee.items import QiandaoItem
import pymysql
import datetime


class XunyeePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost', port=3306, user='root', passwd='Likeagod1', db='wxy', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        print(item)
        table_dic = {u'今日榜': 'Xunyee_Daily', u'7日榜': 'Xunyee_Weekly',
                     u'30日榜': 'Xunyee_Monthly', u'半年榜': 'Xunyee_HalfAnnually'}
        print(table_dic.__contains__(item['rank_type']))
        if table_dic.__contains__(item['rank_type']):
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            table_name = table_dic[item['rank_type']]
            sql = "REPLACE INTO %s VALUES ('%s','%s','%s','%s')" % (table_name,
                                                                    date, item['rank'], item['times'], item['trend'])
            self.cursor.execute(sql)
            self.connect.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
