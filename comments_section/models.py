from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
    )

    title = models.CharField(default='', max_length=250)
    slug = models.SlugField(default= '', max_length=250, unique = True)
    content = models.TextField(default = '')
    seo_title = models.CharField(default = '', max_length=250)
    seo_description = models.CharField(default = '', max_length=160) 
    published = models.DateTimeField(default=timezone.now) 


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(default='', max_length=250)
    email = models.EmailField(default='')
    body = models.TextField(default='')
    
     

def __str__(self):
    return self.user
 