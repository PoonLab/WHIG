from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, Trainee, Staff

def index(request):
    all_faculty = Faculty.objects.all()
    all_trainees = Trainee.objects.all()
    all_staff = Staff.objects.all()
    context = {
        'all_faculty' : all_faculty,
        'all_trainees' : all_trainees,
        'all_staff' : all_staff,
    }
    return render(request, 'members/index.html', context)

def detail(request, Member_id):
    return HttpResponse("<h2>Details for member:" + str(Member_id) + "</<h2>")

