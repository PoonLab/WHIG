from django.shortcuts import render, get_object_or_404
from .models import Member, Faculty, Trainee, Staff

def index(request):
    all_members = Member.objects.all()
    all_faculty = Faculty.objects.all()
    all_trainees = Trainee.objects.all()
    all_staff = Staff.objects.all()
    context = {
        'all_members' : all_members,
        'all_faculty' : all_faculty,
        'all_trainees' : all_trainees,
        'all_staff' : all_staff
    }
    return render(request, 'members/index.html', context)

def detail(request, Member_id):
    member = get_object_or_404(Member, pk = Member_id)
    return render(request, 'members/detail.html', {'member' : member})



