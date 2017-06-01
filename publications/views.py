from django.shortcuts import render
from django.http import Http404
from .models import  Publication

def index(request):
    all_publications = Publication.objects.all()
    return render(request, 'publications/index.html', {'all_publications' : all_publications})

def detail(request, Publication_id):
    try:
        publication = Publication.objects.get(pk = Publication_id)
    except Publication.DoesNotExist:
        raise Http404("Publication doesn't exist!")
    return render(request, 'publications/detail.html', {'publication' : publication})

