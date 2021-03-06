# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statues', '0003_statue_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=60)),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='statue',
            name='enable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='statue',
            name='outdoor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='beacon',
            name='statue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statues.Statue'),
        ),
    ]
