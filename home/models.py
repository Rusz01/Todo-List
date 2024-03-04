from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30, default='')
    desc = models.TextField(default='')
    time = models.DateTimeField(auto_now_add=True)