from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class RstoneTopSpider(CrawlSpider):
	name='rstone'
	allowed_domains = ["http://www.rollingstone.com/"]
	start_urls=['http://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-19691231']
	rules=(
		Rule(SgmlLinkExtractor(allow=('*', )),follow=True, callback='parse'),
	)
	def parse(self,response):
		filename=response.url.split("/")[-2]
		open(filename,'wb').write(response.body)