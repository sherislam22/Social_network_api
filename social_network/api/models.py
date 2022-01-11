from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation



class Like(models.Model):
    like_published = models.DateField(format('%Y-%m-%d'), auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    

class Post(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.body
    @property
    def total_likes(self):
        return self.likes.count()


    

