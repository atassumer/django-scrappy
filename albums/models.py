from django.contrib.gis.db import models

class Band(models.Model):
  name=models.CharField(max_length=100)
  def __unicode__(self):
    return u"%s"%(self.name,)
  

class Album(models.Model):
  name=models.CharField(max_length=100)
  cover=models.CharField(max_length=250)
  band=models.ForeignKey(Band,related_name='albums')
  description=models.TextField()
  def __unicode__(self):
    return u"%s - %s"%(self.name,self.band)
  
