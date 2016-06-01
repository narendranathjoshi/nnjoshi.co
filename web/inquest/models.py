from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    sdk = models.CharField(max_length=200)
    device = models.CharField(max_length=200)
    build = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    last_ping = models.DateTimeField()

    def __str__(self):
        return self.username
