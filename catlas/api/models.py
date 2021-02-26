from enum import IntEnum

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255) # Max length of MySQL VARCHAR
    date_created = models.DateTimeField()
    views = models.IntegerField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')