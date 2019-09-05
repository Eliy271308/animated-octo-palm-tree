from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from isdb.models import Album
from imdb.models import Movie

class Person(models.Model):
    MAN = "M"
    WOMEN = "W"
    SEX_CHOICES = (
        (MAN, "Man"),
        (WOMEN, "Woman")

    )

    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    Years = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    friends = models.ManyToManyField('self', blank=True)
    favorite_album = models.ManyToManyField(Album)
    favorite_films = models.ManyToManyField(Movie)




    def __str__(self):
        return self.name + " " + self.last_name

