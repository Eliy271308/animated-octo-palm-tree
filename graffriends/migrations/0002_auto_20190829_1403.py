# Generated by Django 2.2.4 on 2019-08-29 14:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graffriends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='year',
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
