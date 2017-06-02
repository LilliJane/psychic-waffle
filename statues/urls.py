# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

print settings.MEDIA_ROOT
print settings.MEDIA_URL
print static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "statues"
urlpatterns = [
    url(r'^$', views.get_statues, name='get_statues'),
    # ex: /statues/5/
    url(r'^(?P<statue_id>[0-9]+)/$', views.get_one_statue, name='get_one_statue'),
    # ex: /statues/5/results/
    url(r'^(?P<statue_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /statues/5/vote/
    url(r'^(?P<statue_id>[0-9]+)/vote/$', views.vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
