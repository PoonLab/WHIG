from django.shortcuts import render
from django.http import Http404
from .models import Member, Faculty, Trainee, Staff

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
    context = {}
    try:
        faculty = Faculty.objects.get(pk = Member_id)
        context.update({'faculty': faculty})
    except Faculty.DoesNotExist:
        try:
            trainee = Trainee.objects.get(pk = Member_id)
            context.update({'trainees': trainee})
        except Trainee.DoesNotExist:
            try:
                employee = Staff.objects.get(pk = Member_id)
                context.update({'employee': employee})
            except Staff.DoesNotExist:
                raise Http404("Member doesn't exist!")
    return render(request, 'members/detail.html', context)



