from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class Author(models.Model):
#	# name = models.CharField(max_length = 40, null = True, blank = True)
#	# email = models.EmailField()
#	# username = models.CharField(max_length=20)
#	#password = models.CharField(max_length=16)
#	 
#
#	def __unicode__(self):
#		return smart_unicode(self.username)

class Blog(models.Model):
	author = models.ForeignKey(User)
	blog_name = models.CharField(max_length=150, unique = True)
	description = models.TextField(null = True, blank = True)
	no_of_posts = models.IntegerField(null = True , blank = True, default = 0)
	blog_created = models.DateTimeField(auto_now_add = True, auto_now = False)
	blog_updated = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __unicode__(self):
		return smart_unicode(self.blog_name)

class Post(models.Model):
	blog = models.ForeignKey("Blog")
	title = models.CharField(max_length=150)
	content = models.TextField()
	no_of_likes = models.IntegerField(null = True, blank = True)
	no_of_comments = models.IntegerField(null = True, blank = True)
	saved = models.BooleanField(default = False)
	liked_user = models.ManyToManyField(User)
	post_created = models.DateTimeField(auto_now_add = True, auto_now = False)
	post_updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	#bg_image and font colour

	def __unicode__(self):
		return "%s" % (self.title)


class Comment(models.Model):
	post = models.ForeignKey('Post')
	comment_author = models.ForeignKey(User)
	comment_content = models.TextField(null = True, blank = True)
	comment_created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	
	def __unicode__(self):
		# return "%s: %s: %s" %(self.comment_author, self.comment_content, self.comment_created)
		return str(self.id)