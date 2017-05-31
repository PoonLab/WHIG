from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 1000)
    body = models.CharField(max_length = 1000000)
    date = models.DateField(auto_now = False, auto_now_add = True)
    lastModified = models.DateField(auto_now = True, auto_now_add = False)
    URL =  models.CharField(max_length = 1000, null = True, blank = True)
    picture = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.title