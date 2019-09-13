from rest_framework import serializers
from imdb.models import *


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre')


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
