from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150, help_text='Введите имя')
    last_name = models.CharField(max_length=150, help_text='Введите фамилию')
    date_birthday = models.DateField(blank=True, null=True, help_text='Введите дату рождения')
    country = models.CharField(max_length=150, help_text='Введите страну рождения')

    def __str__(self):
        return self.name + " " + self.last_name


class Movie(models.Model):
    name = models.CharField(max_length= 150,)
    genre = models.CharField(max_length=150)
    release_date = models.DateField(blank = True, null=True)
    country = models.CharField(max_length=150)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

