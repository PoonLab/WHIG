from django.shortcuts import render
from members.models import Faculty, Trainee, Staff
from meetings.models import Event
from news.models import Article
from publications.models import Publication

def index(request):
    all_faculty = Faculty.objects.all()
    all_trainees = Trainee.objects.all()
    all_staff = Staff.objects.all()
    all_events = Event.objects.all()
    all_articles = Article.objects.all()
    all_publications = Publication.objects.all()
    context = {
        'all_faculty': all_faculty,
        'all_trainees': all_trainees,
        'all_staff': all_staff,
        'all_events' : all_events,
        'all_articles' : all_articles,
        'all_publications' : all_publications,
    }
    return render(request, 'portal/index.html', context)

