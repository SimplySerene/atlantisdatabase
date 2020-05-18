from django.shortcuts import render
from django.http import HttpResponse
from .models import Elective


# View where one can search for an elective
def search(request):
    all_electives = Elective.objects.all()
    return render(request, 'elective_search/search.html', {'all_electives': all_electives})


# Detail view of an elective
def detail(request):
    return HttpResponse("WIP. Detail view of an elective")
