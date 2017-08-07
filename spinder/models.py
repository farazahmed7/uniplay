from __future__ import unicode_literals


# Create your models here.
import uuid
from django.contrib.auth.models import User
from django.contrib.gis.db import models



class UserProfile(models.Model):
    user = models.ForeignKey(User)
    fullName=models.CharField(max_length=300)
    dp=models.CharField(max_length=300)
    isNew=models.NullBooleanField()
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)


class Game(models.Model):
    host=models.ForeignKey(User)
    type=models.IntegerField()
    latitude=models.CharField(max_length=40)
    longitude=models.CharField(max_length=40)
    location = models.PointField(max_length=40, null=True)
    participants = models.ManyToManyField(User, related_name='participants')
