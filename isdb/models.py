from django.db import models


class Compositor(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    date_birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.last_name


class Track(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    compositor = models.ForeignKey(to=Compositor, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.compositor.name + " " + self.name


class Album(models.Model):
    name = models.CharField(max_length=150)
    compositor = models.ForeignKey(to=Compositor, on_delete=models.CASCADE, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.name + " " + str(self.year)


