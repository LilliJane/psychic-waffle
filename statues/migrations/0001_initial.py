# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('description', models.CharField(max_length=500)),
                ('latitute', models.DecimalField(decimal_places=10, max_digits=19)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=19)),
                ('pictures', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
