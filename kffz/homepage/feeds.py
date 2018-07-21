#coding=UTF-8
from django.contrib.syndication.views import Feed

from .models import Blog

class AllBlogsRssFeed(Feed):
    title ="test"
    link = '/'
    description = 'test'

    def items(self):
        return Blog.objects.all()

    def item_title(self,item):
        return '[%s] %s' %(item.category, item.title)

    def item_description(self, item):
        return item.detail