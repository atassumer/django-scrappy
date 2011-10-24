from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from rstonetop500.items import RstonetopItem

class RstoneTopSpider(CrawlSpider):
	name='rstonetop500'
	allowed_domains = ["http://www.rollingstone.com/"]
	start_urls=['http://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-19691231']
	rules=[Rule(SgmlLinkExtractor(allow=('/music/lists/500-greatest-albums-of-all-time-19691231/*',)),'parse_item')]
	def parse_item(self,response):
		x=HtmlXPathSelector(response)
		album=RstonetopItem()
		album['position']=x.select("//div[@class='listItemDescriptonDiv']/div[@class='ListItemNumber']/text()")
		at=x.select("//div[@class='listItemDescriptonDiv']/h3/text()")
		at=at.split('-')
		album['title']=at[0]
		album['artist']=at[1]
		album['description']=x.select("//div[@class='listPageContentModule']/div[@class='listPageContentInfo']/text()")
		album['cover']=x.select("//div[@class='listPageContentModule']/div[@class='listPageContentImage']/img[0]/@src")
		return album
