# from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^devices/(?P<device_id>\d+)$', views.device, name='device'),
    url(r'^devices/add_device$', views.add_device, name='add_device'),
    url(r'^devices/(?P<device_id>\d+)/edit$', views.edit_device, name='edit_device'),
]
