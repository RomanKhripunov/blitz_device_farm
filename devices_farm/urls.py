# from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^devices/(?P<device_id>\d+)$', views.device, name='device')
]
