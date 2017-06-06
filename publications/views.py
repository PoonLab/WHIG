from django.shortcuts import render, get_object_or_404
from .models import  Publication

def index(request):
    all_publications = Publication.objects.all().order_by('date').reverse()
    return render(request, 'publications/index.html', {'all_publications' : all_publications})

def detail(request, Publication_id):
    publication = get_object_or_404(Publication, pk = Publication_id)
    return render(request, 'publications/detail.html', {'publication' : publication})

