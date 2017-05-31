from django.db import models
from members.models import Faculty, Trainee, Staff

class Publication(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE, null = True, blank = True)
    trainee = models.ForeignKey(Trainee, on_delete = models.CASCADE, null = True, blank = True)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 1000)
    date = models.DateField(auto_now = False, auto_now_add = False)
    authors_line = models.CharField(max_length = 1000)
    URL = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title

