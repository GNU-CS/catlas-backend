from enum import IntEnum

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_type = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    views = models.IntegerField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        attributes = [f'Author: {self.user}', f'Created: {self.date_created}', f'Content: {self.content}']
        return "\n".join(attributes)

class Board(IntEnum):
    TALKS = 1
    SCENES = 2