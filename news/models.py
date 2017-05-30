from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 1000)
    body = models.CharField(max_length = 1000000)
    date = models.DateField.auto_now_add
    lastModified = models.DateField.auto_now
    URL =  models.CharField(max_length = 1000)
    # Pictures are to be uploaded via the administrator interface as files.
