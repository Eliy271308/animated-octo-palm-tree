from django.contrib import admin
from django.contrib.admin import forms
from django import forms
from .models import *


# # Register your models here.
#
admin.site.register(Movie)
admin.site.register(Director)


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = "__all__"
#
#     def __init__(self, *args, **kwargs):
#         super(PersonForm, self).__init__(*args, **kwargs)
#         self.fields['friends'].queryset = Person.object.exclude(id_extract=self.instance.id)
#
# class PersonAdmin(Person, PersonAdmin):
#     form = PersonForm