from django.shortcuts import render
from django.http import HttpResponse
from .models import  Publication

def index(request):
    all_publications = Publication.objects.all()
    return render(request, 'publications/index.html', {'all_publications' : all_publications})

def detail(request, Publication_id):
    return HttpResponse("<h2>Details for publication:" + str(Publication_id) + "</<h2>")

