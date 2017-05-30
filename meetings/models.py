from django.db import models
from members.models import Faculty, Trainee, Staff

class Event(models.Model):
    date = models.DateField(auto_now = False, auto_now_add = False)
    time = models.TimeField(auto_now = False, auto_now_add = False)
    is_cancelled = models.BooleanField()

class Presentation(models.Model):
    presenter = models.ForeignKey(Faculty, Trainee, Staff, on_delete = models.CASCADE)
    meeting = models.ForeignKey(Event, on_delete = models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete = models.CASCADE)

class Paper(models.Model):
    title = models.CharField(max_length = 1000)
    URL = models.CharField(max_length = 1000)

