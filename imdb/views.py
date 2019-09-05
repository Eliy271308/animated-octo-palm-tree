from django.shortcuts import render
from .models import *
def index(request):
    movie_list= Movie.objects.all()
    movie_count = len(movie_list)
    return render(request, 'index.html', context={"all_movie":movie_list, "movie_count":movie_count})


def movie(request, pk):
    current_movie = Movie.objects.get(pk=pk)
    return render(request,'movie.html', context={'current_movie': current_movie})
