from django.shortcuts import render
from django.http import HttpResponse
from .models import  Article

def index(request):
    all_articles = Article.objects.all()
    return render(request, 'news/index.html', {'all_articles' : all_articles})

def detail(request, Article_id):
    return HttpResponse("<h2>Details for article:" + str(Article_id) + "</<h2>")

