from django.conf.urls import url

from . import views

app_name = 'events' # namespace-ul pentru url-uri

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='detail'),
    url(r'^add$', views.add_event, name='add'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
]