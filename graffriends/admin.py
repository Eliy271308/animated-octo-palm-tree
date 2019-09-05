from django.contrib import admin
from django.contrib.admin import forms
from django import forms
from .models import *
from isdb.models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['friends'].queryset = Person.objects.exclude(id__exact=self.instance.id)


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm


admin.site.register(Person, PersonAdmin)

