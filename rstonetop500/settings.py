# Scrapy settings for rstonetop500 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'rstonetop500'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['rstonetop500.spiders']
NEWSPIDER_MODULE = 'rstonetop500.spiders'
DEFAULT_ITEM_CLASS = 'rstonetop500.items.RstonetopItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

