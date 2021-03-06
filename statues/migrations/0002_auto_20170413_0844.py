# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statue',
            name='latitute',
            field=models.FloatField(default=52.0715712),
        ),
        migrations.AlterField(
            model_name='statue',
            name='longitude',
            field=models.FloatField(default=4.169786),
        ),
        migrations.AlterField(
            model_name='statue',
            name='pictures',
            field=models.ImageField(default='pic_folder/no-img.png', upload_to='pic_folder/'),
        ),
    ]
