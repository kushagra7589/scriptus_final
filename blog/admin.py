from django.contrib import admin
from . import models
from .forms import BlogForm, PostForm, BlogFormAdmin

class BlogAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "author", "no_of_posts", "blog_created", "blog_updated"]
	form = BlogFormAdmin

class PostAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "blog", "no_of_likes", "no_of_comments", "post_created", "post_updated"]
	form = PostForm

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)