from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Paper, Presentation

def index(request):
    all_events = Event.objects.all()
    return render(request, 'meetings/index.html', {'all_events' : all_events})

def detail(request, Event_id):
    return HttpResponse("<h2>Details for event:" + str(Event_id) + "</<h2>")

