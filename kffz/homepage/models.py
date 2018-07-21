#coding=UTF-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
# Create your models here.

class Myuser(AbstractUser):
    jifen = models.IntegerField('积分',default=0)
    class Meta:
        db_table = 'Myuser'
    def __str__(self):
        return self.username

class BlogCategory(models.Model):
    techology = '科技&DIY'
    finance = '财经'
    coding = '技术'
    reading = '阅读'
    enjoy = '娱乐'
    zero = 0
    CATEGORY_CHOICES = (
        (techology, '科技&DIY'),
        (finance,'财经'),
        (coding,'技术'),
        (reading,'阅读'),
        (enjoy,'娱乐')
    )
    catogory = models.CharField(max_length=10,choices=CATEGORY_CHOICES,default=coding)
    name = models.CharField(max_length=10,default='技术')

class Blog(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.TextField()
    detail = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    authors = models.ForeignKey(Myuser,on_delete=models.CASCADE)
    n_comment = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=10,choices=BlogCategory.CATEGORY_CHOICES,null=True)
    excerpt = models.CharField(max_length=200,blank=True)
    class Meta:
        ordering = ['-pub_date','views']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('homepage:detail',kwargs={'pk':self.pk})
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.detail))[:54]

        super(Blog, self).save(*args, **kwargs)







