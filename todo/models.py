from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    completed = models.BooleanField()
