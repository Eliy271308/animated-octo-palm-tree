from django.shortcuts import render
from .models import *


def friends(request):
    all_person = Person.objects.all()
    return render(request, 'friends.html', context={'all_person': all_person})


def list(request, pk):
    person = Person.objects.get(pk=pk)
    return render(request, 'list.html', context={'person': person})

