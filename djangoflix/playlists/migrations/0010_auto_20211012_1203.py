# Generated by Django 3.2.5 on 2021-10-12 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0009_tvshowproxy_tvshowseasonproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TVShowProxy',
        ),
        migrations.DeleteModel(
            name='TVShowSeasonProxy',
        ),
        migrations.CreateModel(
            name='TVShowProxy',
            fields=[
            ],
            options={
                'verbose_name': 'TV Show',
                'verbose_name_plural': 'TV Shows',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
        migrations.CreateModel(
            name='TVShowSeasonProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
    ]
