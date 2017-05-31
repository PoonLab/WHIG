from django.shortcuts import render
from django.http import HttpResponse
from .models import  Publication
from django.template import loader

def index(request):
    all_publications = Publication.objects.all()
    html = ''
    for publication in all_publications:
        url = '/publications/' + str(publication.id) + '/'
        html += '<a href="' + url + '">' + str(publication.title) + '</a><br>'
    return HttpResponse(html)

def detail(request, Publication_id):
    return HttpResponse("<h2>Details for publication:" + str(Publication_id) + "</<h2>")

