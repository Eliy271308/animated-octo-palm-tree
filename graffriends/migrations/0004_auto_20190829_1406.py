# Generated by Django 2.2.4 on 2019-08-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graffriends', '0003_auto_20190829_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_person_friends_+', to='graffriends.Person'),
        ),
    ]