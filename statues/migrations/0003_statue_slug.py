# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statues', '0002_auto_20170413_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='statue',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=32),
        ),
    ]
