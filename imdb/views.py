from django.shortcuts import render
from .models import *
from rest_framework import generics
from imdb.serializers import *


def index(request):
    movie_list = Movie.objects.all()
    movie_count = len(movie_list)
    return render(request, 'index.html', context={"all_movie": movie_list, "movie_count": movie_count})


def movie(request, pk):
    current_movie = Movie.objects.get(pk=pk)
    return render(request, 'movie.html', context={'current_movie': current_movie})


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieDetailSerializer


class DirectorCreateView(generics.CreateAPIView):
    serializer_class = DirectorDetailSerializer


class MoviesListView(generics.ListAPIView):
    serializer_class = MoviesListSerializer
    queryset = Movie.objects.all()




class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

