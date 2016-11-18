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

    @property
    def peek(self):
        return self.content[:400]

    @property
    def month_first(self):
        return self.created.strftime("%B")[:3]

    @property
    def month_last(self):
        return self.created.strftime("%B")[3:]

    @property
    def day(self):
        return self.created.day

    @property
    def year(self):
        return self.created.year
