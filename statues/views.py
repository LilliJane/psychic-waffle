# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Statue

def index(request):
    latest_statue_list = Statue.objects.order_by('-pub_date')[:5]
    return render(request, 'statues/index.html', {'latest_statue_list': latest_statue_list,})

def detail(request, statue_id):
    statue = get_object_or_404(Statue, pk=statue_id)
    return render(request, 'statues/detail.html', {'statue': statue})

def results(request, statue_id):
    response = "You're looking at the results of statue %s."
    return HttpResponse(response % statue_id)

def vote(request, statue_id):
    return HttpResponse("You're voting on statue %s." % statue_id)
