from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=200)
    os = models.CharField(max_length=200, blank=True, null=True)
    sdk = models.CharField(max_length=200, blank=True, null=True)
    device = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_pro = models.BooleanField(default=False)
    last_ping = models.DateTimeField(blank=True, null=True)

    def _is_email(self):
        try:
            validate_email(self.username)
            return True
        except ValidationError:
            return False
    is_email = property(_is_email)

    def __str__(self):
        return self.username
