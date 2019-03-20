# -*- coding: utf-8 -*-
import scrapy
from xunyee.items import QiandaoItem


class XunyeerankSpider(scrapy.Spider):
    name = 'xunyeeRank'
    allowed_domains = ['xunyee.cn']
    start_urls = ['http://www.xunyee.cn/rank-person-sign-0.html']

    def parse(self, response):
        print('爬取签到信息...')
        url_list = response.xpath(
            '//div[@class="TimecataRank_header"]/ul/li/a/@href').extract()  # 不同签到url
        rank_type_list = response.xpath(
            '//div[@class="TimecataRank_header"]/ul/li/a/text()').extract()  # 不同签到名称
        for (url, rank_type) in zip(url_list, rank_type_list):
            yield scrapy.Request(url=url, callback=self.parse_rank, meta={'rank_type': rank_type})

    def parse_rank(self, response):
        print('爬取签到信息————<%s>...' % response.meta['rank_type'])
        row = response.xpath(
            '//a[@href="http://www.xunyee.cn/person-194062.html"]')
        item = QiandaoItem()
        for info in row:
            item['rank_type'] = response.meta['rank_type']
            item['rank'] = info.xpath(
                './span[1]/span/i/text()').extract_first()
            item['times'] = info.xpath('./span[3]/b/text()').extract_first()
            trend = info.xpath('./em/@class').extract_first()
            if 'up' in trend:
                item['trend'] = u'上升'
            elif 'down' in trend:
                item['trend'] = u'下降'
            else:
                item['trend'] = u'保持'
            yield item
