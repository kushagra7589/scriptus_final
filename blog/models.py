from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length = 40, null = True, blank = True)
	email = models.EmailField()
	username = models.CharField(max_length=20)
	#password = models.CharField(max_length=16)
	#n_blogs = models.IntegerField()

	def __unicode__(self):
		return smart_unicode(self.username)