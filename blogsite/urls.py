"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^signup$', views.register_user, name='signup'),
    #url(r'^signup/register/$', views.registered, name = 'registered'),
    url(r'^logout$', views.logout_user, name='logout'),
    #url(r'^logout/register$', views.registered_user, name = "registered"),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^createblog$', views.create_blog, name='create_blog'),
    url(r'^blog-page/(?P<blog>[0-9]+)$', views.blog_page, name='blog_page'),
    url(r'^add-post/([0-9]+)$', views.post_create, name='post_create'),
    url(r'^post/([0-9]+)$', views.post_page, name='post_page'),
    #url(r'^createblogpost$', views.create_blog_post, name='create_blog_post'),
    # url(r'^blog/(?<blog_name>)\w+$', views.login_user, name='blog_display'),
    url(r'^archive$', views.archive, name='archive'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', views.archive_day, name='archive_day'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', views.archive_month, name='archive_month'),
    url(r'^archive/(?P<year>[0-9]{4})/$', views.archive_year, name='archive_year'),

    url(r'^admin/', include(admin.site.urls)),
]
