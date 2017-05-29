from django.shortcuts import render
from django.http import Http404
from .models import article

def index(request):
    allArticles = article.objects.all()
    return render(request, 'WHIGNews/index.html', {'allArticles': allArticles})

def detail(request, article_id):
    try:
        Article = article.objects.get(pk=article_id)
    except article.DoesNotExist:
        raise Http404("Article does not exist!")
    return render(request, 'WHIGNews/detail.html', {'Article': Article})