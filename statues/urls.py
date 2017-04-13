from django.conf.urls import url

from . import views

app_name = "statues"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /statues/5/
    url(r'^(?P<statue_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /statues/5/results/
    url(r'^(?P<statue_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /statues/5/vote/
    url(r'^(?P<statue_id>[0-9]+)/vote/$', views.vote, name='vote'),
]