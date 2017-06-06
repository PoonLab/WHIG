from django.shortcuts import render
from django.http import Http404
from .models import  Article

def index(request):
    all_articles = Article.objects.all().order_by('date').reverse()
    return render(request, 'news/index.html', {'all_articles' : all_articles})

def detail(request, Article_id):
    try:
        article = Article.objects.get(pk = Article_id)
    except Article.DoesNotExist:
        raise Http404("Article doesn't exist!")
    return render(request, 'news/detail.html', {'article' : article})

