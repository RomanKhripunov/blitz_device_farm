from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.DeviceListView.as_view(), name='devices'),
    url(r'^devices/(?P<pk>\d+)$', views.DeviceDetailView.as_view(), name='device'),
    url(r'^devices/add_device$', views.add_device, name='add_device'),
    url(r'^devices/(?P<pk>\d+)/edit$', views.DeviceUpdateView.as_view(), name='edit_device'),
]
