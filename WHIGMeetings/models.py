from django.db import models

class meeting(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000000)
    paper = models.CharField(max_length=1000)
    presenter = models.CharField(max_length=1000)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=9)
    year = models.CharField(max_length=4)
    # Pictures are to be uploaded as files later.

    def __str__(self):
        return self.title
