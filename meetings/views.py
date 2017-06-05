from django.shortcuts import render
from django.http import Http404
from .models import Event, Paper

def index(request):
    all_events = Event.objects.all()
    return render(request, 'meetings/index.html', {'all_events' : all_events})

def detail(request, Event_id):
    try:
        event = Event.objects.get(pk = Event_id)
    except Event.DoesNotExist:
        raise Http404("Event doesn't exist!")
    return render(request, 'meetings/detail.html', {'event' : event})

