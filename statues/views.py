# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import Statue

def get_statues(request):
    if request.method == "POST":
        try:
            Statue.save(request.POST)
            return JsonResponse(serializers.serialize('json', Statue.objects.order_by('-pub_date')[:1]))
        except:
            return JsonResponse(serializers.serialize('json', {'message': 'Error, couldn\'t add this statue'}))
    latest_statue_list = serializers.serialize('json', Statue.objects.order_by('-pub_date'))
    return JsonResponse({'latest_statue_list': latest_statue_list,})

def get_one_statue(request, statue_id):
    statue = get_object_or_404(Statue, pk=statue_id)
    return JsonResponse(serializers.serialize('json', statue))


def results(request, statue_id):
    response = "You're looking at the results of statue %s."
    return HttpResponse(response % statue_id)

def vote(request, statue_id):
    return HttpResponse("You're voting on statue %s." % statue_id)
