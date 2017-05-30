from django.db import models

class Member(models.Model):
    given_name = models.CharField(max_length = 1000)
    surname = models.CharField(max_length = 1000)
    profile = models.CharField(max_length = 1000000)
    website = models.CharField(max_length = 1000)
    ORCID = models.CharField(max_length = 1000)
    is_active = models.BooleanField()
    is_core = models.BooleanField()
    # Pictures are to be uploaded via the administrator interface as files.

class Faculty(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    rank = models.CharField(max_length = 1000) # Position

class Trainee(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    PI = models.ForeignKey(Faculty, on_delete=models.CASCADE)  # Principal Investigator / Adviser
    rank = models.CharField(max_length = 1000) # Position

class Staff(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    PI = models.ForeignKey(Faculty, on_delete=models.CASCADE)  # Principal Investigator / Adviser
    rank = models.CharField(max_length = 1000) # Position
