#coding=UTF-8
from django import template
from ..models import Blog

register = template.Library()

@register.simple_tag
def get_recent_blogs(num=3):
    return Blog.objects.all()[:num]

@register.simple_tag
def archives():
    return Blog.objects.dates('pub_date','month',order='DESC')
