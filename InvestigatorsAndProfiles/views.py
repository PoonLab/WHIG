from django.shortcuts import render
from django.http import Http404
from .models import investigator

def index(request):
    allInvestigators = investigator.objects.all()
    return render(request, 'InvestigatorsAndProfiles/index.html', {'allInvestigators': allInvestigators})

def detail(request, investigator_id):
    try:
        Investigator = investigator.objects.get(pk=investigator_id)
    except investigator.DoesNotExist:
        raise Http404("Investigator does not exist!")
    return render(request, 'InvestigatorsAndProfiles/detail.html', {'Investigator': Investigator})
