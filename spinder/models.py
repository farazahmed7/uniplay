from __future__ import unicode_literals


# Create your models here.
from django.contrib.gis.db import models


class Game(models.Model):
    location=models.PointField(max_length=40, null=True)
