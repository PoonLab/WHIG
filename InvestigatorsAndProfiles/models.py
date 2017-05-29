from django.db import models

class investigator(models.Model):
    name = models.CharField(max_length=1000)
    position = models.CharField(max_length=1000)
    profile = models.CharField(max_length=1000000)
    website = models.CharField(max_length=1000)
    # Pictures are to be uploaded as files later.

    def __str__(self):
        return self.name
