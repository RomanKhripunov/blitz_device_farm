from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.DeviceListView.as_view(), name='devices'),
    url(r'^(?P<pk>\d+)$', views.DeviceDetailView.as_view(), name='device'),
    url(r'^add_device$', views.add_device, name='add_device'),
    url(r'^(?P<pk>\d+)/edit$', views.DeviceUpdateView.as_view(), name='edit_device'),
]
