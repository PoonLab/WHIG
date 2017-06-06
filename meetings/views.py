from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
    all_events = Event.objects.all().order_by('date').reverse()
    return render(request, 'meetings/index.html', {'all_events' : all_events})

def detail(request, Event_id):
    event = get_object_or_404(Event, pk = Event_id)
    return render(request, 'meetings/detail.html', {'event' : event})

