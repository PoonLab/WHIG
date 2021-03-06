from django.db import models

class Member(models.Model):
    given_name = models.CharField(max_length = 1000)
    surname = models.CharField(max_length = 1000)
    profile = models.CharField(max_length = 1000000)
    email = models.CharField(max_length=1000, null = True, blank = True)
    website = models.CharField(max_length = 1000, null = True, blank = True)
    ORCID = models.CharField(max_length = 1000, null = True, blank = True)
    is_active = models.BooleanField()
    is_core = models.BooleanField()
    image = models.ImageField(upload_to = './members/static/members', default = './members/static/members/DefaultImage.png')

    def __str__(self):
        return self.given_name + ' ' + self.surname

class Faculty(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    rank = models.CharField(max_length = 1000) # Position

    def __str__(self):
        return self.member.given_name + ' ' + self.member.surname

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculty'

class Trainee(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    PI = models.ForeignKey(Faculty, on_delete = models.CASCADE)  # Principal Investigator / Adviser
    rank = models.CharField(max_length = 1000) # Position

    def __str__(self):
        return self.member.given_name + ' ' + self.member.surname

class Staff(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    PI = models.ForeignKey(Faculty, on_delete = models.CASCADE)  # Principal Investigator / Adviser
    rank = models.CharField(max_length = 1000) # Position

    def __str__(self):
        return self.member.given_name + ' ' + self.member.surname

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
