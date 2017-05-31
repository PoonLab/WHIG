from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.template import loader

def index(request):
    all_events = Event.objects.all()
    html = ''
    for event in all_events:
        url = '/meetings/' + str(event.id) + '/'
        html += '<a href="' + url + '">' + str(event.date) + '</a><br>'
    return HttpResponse(html)

def detail(request, Event_id):
    return HttpResponse("<h2>Details for event:" + str(Event_id) + "</<h2>")

