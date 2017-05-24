from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

print settings.MEDIA_ROOT
print settings.MEDIA_URL
print static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "beacons"
urlpatterns = [
    url(r'^$', views.get_beacons, name='get_beacons'),
    url(r'^(?P<beacon_uuid>[A-Za-z0-9]+)/$', views.get_one_beacon, name='get_one_beacon'),
    url(r'^(?P<beacon_uuid>[0-9]+)/^(?P<statue_id>[0-9]+)/$', views.get_statues_beacon, name='get_statues_beacon'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
