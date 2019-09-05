from django.shortcuts import render
from .models import *

def index1(request):
    all_albums = Album.objects.all()
    return render(request, 'index1.html', context={"all_albums": all_albums})


def music(request, pk):
    all_track = Album.objects.get(pk=pk)
    return render(request, 'music.html', context={'all_track': all_track})
