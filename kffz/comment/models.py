from django.db import models
from homepage import models as homemodel
# Create your models here.
class Comment(models.Model):
    n_comment = models.IntegerField(default=0)
    blog = models.ForeignKey(homemodel.Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content[:10]