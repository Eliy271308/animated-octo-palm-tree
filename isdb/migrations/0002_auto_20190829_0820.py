# Generated by Django 2.2.4 on 2019-08-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='tracks',
        ),
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(to='isdb.Track'),
        ),
        migrations.AlterField(
            model_name='compositor',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='compositor',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
