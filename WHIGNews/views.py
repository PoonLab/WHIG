from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import article

# Create your views here.

def index(request):
    allArticles = article.objects.all()
    context = {'allArticles': allArticles}
    return render(request, 'WHIGNews/index.html', context)

def detail(request, article_id):
    return HttpResponse("<h2>Details for Article ID:"+str(article_id)+"</h2>")