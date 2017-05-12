from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from example_app.views import ChatterBotAppView


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^statues/', include('statues.urls')),
    url(r'^beacons/', include('statues.beacons_urls'))
]

urlpatterns += staticfiles_urlpatterns()

