from django.db import models


# Create your models here.

class meeting(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000000)
    paper = models.CharField(max_length=1000)
    presenter = models.CharField(max_length=1000)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    # Pictures are to be uploaded as files later.

