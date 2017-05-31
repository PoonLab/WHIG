from django.shortcuts import render
from django.http import HttpResponse
from .models import  Article
from django.template import loader

def index(request):
    all_articles = Article.objects.all()
    html = ''
    for article in all_articles:
        url = '/news/' + str(article.id) + '/'
        html += '<a href="' + url + '">' + str(article.title) + '</a><br>'
    return HttpResponse(html)

def detail(request, Article_id):
    return HttpResponse("<h2>Details for article:" + str(Article_id) + "</<h2>")

