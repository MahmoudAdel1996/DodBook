from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
# Create your models here.


class Todo(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=120)
    text = models.TextField()
    image = models.ImageField(upload_to='post_image', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
