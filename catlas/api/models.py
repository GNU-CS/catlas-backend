from django.db import models

# Create your models here.

class Member(models.Model):
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=64)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['id']