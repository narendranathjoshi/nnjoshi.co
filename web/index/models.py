from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(auto_created=True, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogEntry(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(auto_created=True, unique=True, db_index=True)
    image = models.CharField(max_length=150, blank=True, null=True)
    image_caption = models.CharField(max_length=100, blank=True, null=True)
    entry = models.TextField(default='')
    peek = models.CharField(max_length=640, default='')
    tags = models.ManyToManyField(Tag)
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
