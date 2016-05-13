from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    created = models.DateField(auto_now_add=True)
    content = models.TextField()

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_peek(self):
        return self.content[:400]
