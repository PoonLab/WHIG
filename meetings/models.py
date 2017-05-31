from django.db import models
from members.models import Trainee, Staff

class Event(models.Model):
    date = models.DateField(auto_now = False, auto_now_add = False)
    time = models.TimeField(auto_now = False, auto_now_add = False)
    is_cancelled = models.BooleanField()

    def __str__(self):
        return self.date

class Paper(models.Model):
    title = models.CharField(max_length = 1000)
    URL = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title

class Presentation(models.Model):
    trainee_presenter = models.ForeignKey(Trainee, on_delete = models.CASCADE, null = True, blank = True)
    staff_presenter = models.ForeignKey(Staff, on_delete=models.CASCADE, null = True, blank = True)
    meeting = models.ForeignKey(Event, on_delete = models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.meeting.date



