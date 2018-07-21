from django.urls import path,re_path
from . import views

app_name = 'comment'
urlpatterns = [
    re_path(r'^comment/article-list/(?P<blog_pk>[0-9]+)',views.blog_comment,name='blog_comment')
]