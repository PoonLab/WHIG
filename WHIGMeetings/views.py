from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import meeting

# Create your views here.

def index(request):
    allMeetings = meeting.objects.all()
    context = {'allMeetings': allMeetings}
    return render(request, 'WHIGMeetings/index.html', context)

def detail(request, meeting_id):
    return HttpResponse("<h2>Details for Meeting ID:"+str(meeting_id)+"</h2>")
