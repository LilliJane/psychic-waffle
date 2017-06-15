# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from eps_app.views import ChatterBotAppView
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^statues/', include('statues.urls')),
    url(r'^beacons/', include('statues.beacons_urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

