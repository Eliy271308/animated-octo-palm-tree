from rest_framework import serializers
from imdb.models import *


class DirectorField(serializers.RelatedField):
    def to_representation(self, director):
        return director.name

    def to_internal_value(self, director):
        return Director.objects.get(name=director)


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class DirectorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'last_name')


class MoviesListSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'director')


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorField(queryset=Director.objects.all())

    class Meta:
        model = Movie
        fields = "__all__"








