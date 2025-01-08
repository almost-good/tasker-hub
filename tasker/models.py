from email.mime import image
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasker_tasks')
    is_completed = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)