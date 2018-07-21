#coding=UTF-8
"""kffz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path,re_path
from homepage.feeds import AllBlogsRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls'),name = "home"),
    re_path(r'index.html',include('homepage.urls')),
    re_path(r'articles-list.html',include('homepage.urls')),
    path('faq/',include('homepage.urls')),
    path('contact/',include('homepage.urls')),
    path('diy/',include('diy.urls')),
    path('signup/',include('homepage.urls')),
    path('articles-list.html',include('homepage.urls')),
    path('logout/',include('homepage.urls')),
    re_path(r'child[0-9]+/',include('homepage.urls')),
    re_path(r'more[0-9]+/',include('homepage.urls')),
    re_path(r'^articles-list/(?P<pk>[0-9]+)/',include('homepage.urls'),name = 'detail'),
    re_path(r'',include('comment.urls')),
    path('all/rss/',AllBlogsRssFeed(),name = 'rss'),
    re_path(r'cpu_finder',include('diy.urls')),
    re_path(r'search/',include('haystack.urls'),name = 'search'),
]
