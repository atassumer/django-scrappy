# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class RstonetopItem(Item):
	position=Field()
	cover=Field()
	title=Field()
	artist=Field()
	description=Field()
	def __str__(self):
		return u"%s | %s - %s" % (self['position'],self['title'], self['artist'])
	
