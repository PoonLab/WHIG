from django.shortcuts import render, get_object_or_404
from .models import  Article

def index(request):
    all_articles = Article.objects.all().order_by('date').reverse()
    return render(request, 'news/index.html', {'all_articles' : all_articles})

def detail(request, Article_id):
    article = get_object_or_404(Article, pk = Article_id)
    return render(request, 'news/detail.html', {'article' : article})

