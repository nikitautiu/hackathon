from django.conf.urls import url

from . import views

app_name = 'events' # namespace-ul pentru url-uri

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='detail')
]