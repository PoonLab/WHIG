from django.shortcuts import render
from django.http import Http404
from .models import meeting

def index(request):
    allMeetings = meeting.objects.all()
    return render(request, 'WHIGMeetings/index.html', {'allMeetings': allMeetings})

def detail(request, meeting_id):
    try:
        Meeting = meeting.objects.get(pk=meeting_id)
    except meeting.DoesNotExist:
        raise Http404("Meeting does not exist!")
    return render(request, 'WHIGMeetings/detail.html', {'Meeting': Meeting})
