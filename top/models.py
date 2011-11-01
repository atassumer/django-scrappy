from django.contrib.gis.db import models
from rstonetop500.albums.models import Album

class TopAlbum(models.Model):
	album=models.OneToOneField(Album)
	position=models.PositiveIntegerField()
	had_it=models.BooleanField(default=False)
	class Meta:
		ordering=('position',)
	def __unicode__(self):
		return u"%s | %s"%(self.position, self.album)
  

