# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import os

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class Statue(models.Model):
    """ Default values for latitude and longitude are the ones from The Hague
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=32, default='', blank=True)
    pub_date = models.DateTimeField('date published')
    enable = models.BooleanField(default=False)
    outdoor = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    latitude = models.FloatField(default=52.0715712)
    longitude = models.FloatField(default=4.169786)
    pictures = models.ImageField(upload_to='/example_app/static/img/', default='example_app/static/img/no-img.png')
    pictures.short_description = 'Image'
    
    def image_tag(self):
        return mark_safe('<img src="/pic_folder/%s" width="150" height="150" />' % (self.pictures))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Statue, self).save(*args, **kwargs)


class Beacon(models.Model):
    """ Beacon should be joined to a precised statue
    """
    statue = models.ForeignKey(Statue, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=60)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    
    def __str__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Beacon, self).save(*args, **kwargs)


