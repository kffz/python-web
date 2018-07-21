#coding=UTF-8
from django.contrib import admin
from . import models
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','tagline','pub_date']

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.Blog,BlogAdmin)
admin.site.register(models.Myuser)
admin.site.register(models.BlogCategory,BlogCategoryAdmin)