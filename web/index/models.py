from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogEntry(models.Model):
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
