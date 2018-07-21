#coding=UTF-8
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
import re

app_name = 'homepage'
urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    re_path(r'index.html',views.IndexView.as_view()),
    path('signup/', views.signup),
    path('articles-list/', views.Article_list.as_view()),
    path('faq/',views.Faq_list.as_view()),
    path('contact/',views.Contact_list.as_view()),
    re_path(r'more[0-9]+/',views.more.as_view()),
    re_path(r'child[0-9]+/',views.child.as_view()),
    re_path(r'articles-list.html',views.Article_list.as_view()),
    path('logout/', views.logout_view),
    re_path(r'^articles-list/(?P<pk>[0-9]+)/', views.BlogDetailView.as_view(), name='detail'),
]
