# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse, Http404

from .models import Statue, Beacon


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
    try:
        statue = serializers.serialize('json', Statue.objects.get(id=statue_id))
    except Statue.DoesNotExist:
        raise Http404("No statue matches the given query.")
    return JsonResponse({'statue': statue,})


def get_beacons(request):
    if request.method == "POST":
        try:
            Beacon.save(request.POST)
            return JsonResponse(serializers.serialize('json', Beacon.objects.order_by('-pub_date')[:1]))
        except:
            return JsonResponse(serializers.serialize('json', {'message': 'Error, couldn\'t add this beacon'}))
    latest_beacons_list = serializers.serialize('json', Beacon.objects.order_by('-pub_date'))
    return JsonResponse({'latest_beacon_list': latest_beacons_list,})


def get_one_beacon(request, beacon_slug):
    try:
        beacon = serializers.serialize('json', Beacon.objects.get(slug=beacon_slug))
    except:
        raise Http404("No beacon matches the given query.")
    print beacon
    return JsonResponse({'beacon': beacon,})


def get_statues_beacon(request, beacon_uuid, statue_id):
    lat = request.GET["latitude"]
    lgn = request.GET["longitude"]
    try:
        beacon = serializers.serialize('json', Beacon.object.get(statue=statue_id, uuid=beacon_uuid))
    except Beacon.DoesNotExist:
        raise Http404("No beacon matches the given statue.")

    try:
        statue = serializers.serialize('json', Statue.objects.get(id=statue_id))
    except Statue.DoesNotExist:
        raise Http404("No statue matches the given query.")

    return JsonResponse({'statue': statue, 'message': 'under development'})


def results(request, statue_id):
    response = "You're looking at the results of statue %s."
    return HttpResponse(response % statue_id)


def vote(request, statue_id):
    return HttpResponse("You're voting on statue %s." % statue_id)
