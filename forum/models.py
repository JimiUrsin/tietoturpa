from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=280)

class RecoveryAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=64)
