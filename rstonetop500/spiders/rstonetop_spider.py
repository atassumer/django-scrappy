from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from rstonetop500.items import RstonetopItem

class RstoneTopSpider(CrawlSpider):
	name='rstonetop500'
	allowed_domains = ["www.rollingstone.com"]
	start_urls=['http://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-19691231']
	rules = (
        Rule(SgmlLinkExtractor(allow='/music/lists/500-greatest-albums-of-all-time-19691231/[0-9a-zA-Z\-]+$'),
            'parse_item',
            follow=True,
        ),
    )
	def parse_item(self,response):
		x=HtmlXPathSelector(response)
		album=RstonetopItem()
		album['position']=x.select("//div[@class='listItemDescriptonDiv']/span[@class='ListItemNumber']/text()").extract()[0]
		at=x.select("//div[@class='listItemDescriptonDiv']/h3/text()").extract()[0]
		at=at.split('-')
		album['title']=at[0].strip()
		album['artist']=at[1].strip()
		print x.select("//div[@class='listPageContentModule']/div[@class='listPageContentInfo']/text()").extract()
		album['description']=x.select("//div[@class='listPageContentModule']/div[@class='listPageContentInfo']/text()").extract()
		print x.select("//div[@class='listPageContentModule']/div[@class='listPageContentImage']/img[0]/@src").extract()
		album['cover']=x.select("//div[@class='listPageContentModule']/div[@class='listPageContentImage']/img[0]/@src").extract()
		return album
