from django.contrib.gis import admin

from rstonetop500.top.models import *

class TopAlbumAdmin(admin.ModelAdmin):
	list_display=('position','had_it','title','band')
	list_filter=('had_it',)
	search_fields=('album__name','album__band__name')
	actions=['had_it','dont_had_it']
	def title(self,obj):
		return obj.album.name
	
	def band(self,obj):
		return obj.album.band
	
	def had_it(self,request,queryset):
		queryset.update(had_it=True)

	def dont_had_it(self,request,queryset):
		queryset.update(had_it=False)

	had_it.short_description='I had this album/s'
	dont_had_it.short_description='I Don\'t had this album/s'

admin.site.register(TopAlbum,TopAlbumAdmin)