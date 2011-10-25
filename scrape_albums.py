#!/usr/bin/env python

# import django env
from django.core.management import setup_environ
import settings
setup_environ(settings)

# import scrapy stuff
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from rstonetop500db.albums.models import *
from rstonetop500db.top.models import *

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
		a={}
		a['position']=x.select("//div[@class='listItemDescriptonDiv']/span[@class='ListItemNumber']/text()").extract()[0]
		at=x.select("//div[@class='listItemDescriptonDiv']/h3/text()").extract()[0]
		at=at.split('-')
		at=[i.strip() for i in at]
		a['title']=at[0]
		a['artist']=at[1]
		a['description']=x.select("//div[@class='listPageContentInfo']/text()").extract()[1].strip()
		a['cover']=x.select("//div[@class='listPageContentImage assetContainer imageStandard']/img/@src").extract()[0]
                try:
                  band=Band.objects.get(name=a['artist'])
                except:
                  band=Band(name=a['artist'])
                  band.save()
                try:
                  album=Album.objects.get(name=a['title'],band=band)
                except:
                  album=Album()
                  album.name=a['title']
                  album.band=band
                  album.description=a['description']
                  album.save()
                try:
                  top=TopAlbum.objects.get(position=int(a['position']))
                except:
                  top=TopAlbum()
                  top.album=album
                  top.position=int(a['position'])
                  top.save()
