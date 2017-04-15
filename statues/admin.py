# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from statues.models import Statue, Beacon
# Register your models here.

admin.site.register(Statue)
admin.site.register(Beacon)