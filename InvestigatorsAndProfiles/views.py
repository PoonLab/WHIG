from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import investigator

# Create your views here.

def index(request):
    allInvestigators = investigator.objects.all()
    context = {'allInvestigators': allInvestigators}
    return render(request, 'InvestigatorsAndProfiles/index.html', context)

def detail(request, investigator_id):
    return HttpResponse("<h2>Details for Investigator ID:"+str(investigator_id)+"</h2>")