from rest_framework import serializers
from imdb.models import *


class DirectorNameField(serializers.RelatedField):
    def to_representation(self, director):
        return director.name + ' ' + director.last_name

    def to_internal_value(self, director):
        name, last_name = director.split(" ")
        return Director.objects.filter(last_name=last_name).get(name=name)


# class DirectorLastField(serializers.RelatedField):
#     def to_representation(self, director):
#         return director.last_name
#
#     def to_internal_value(self, director):
#         return Director.objects.get(last_name=director)
#




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
    director = DirectorNameField(queryset=Director.objects.all())





    class Meta:
        model = Movie
        fields = "__all__"








