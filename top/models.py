from django.contrib.gis.db import models
from rstonetop500.albums.models import Album

class TopAlbum(models.Model):
  album=models.OneToOneField(Album)
  position=models.PositiveIntegerField()
  def __unicode__(self):
    return u"%s | %s"%(self.position, self.album)
  

