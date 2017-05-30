from django.db import models
from members.models import Faculty, Trainee, Staff

class Publication(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
    trainee = models.ForeignKey(Trainee, on_delete = models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    title = models.CharField(max_length = 1000)
    date = models.DateField(auto_now = False, auto_now_add = False)
    authors_line = models.CharField(max_length = 1000)

