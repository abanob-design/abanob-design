from django.db import models

# Create your models here.

class user(models.Model):

    First = models.CharField(max_length=128)
    Last = models.CharField(max_length=128)
    Email = models.EmailField(max_length=264)
