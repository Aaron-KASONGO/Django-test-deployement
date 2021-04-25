from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=True)
