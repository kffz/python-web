from django.conf.urls import re_path
from . import views

app_name = 'denglu'
urlpatterns = [
    re_path(r'register/',views.register,name='register'),
    re_path(r'^$',views.index,name='index'),
]