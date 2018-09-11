from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.DeviceList.as_view(), name='devices'),
    url(r'^(?P<pk>\d+)$', views.DeviceDetail.as_view(), name='device'),
    url(r'^add_device$', views.AddDevice.as_view(), name='add-device'),
    url(r'^(?P<pk>\d+)/edit$', views.DeviceUpdate.as_view(), name='edit-device'),
    url(r'^assign_to_me/$', views.assign_to_me, name='assign_to_me'),
    url(r'^return_to_base/$', views.return_to_base, name='return_to_base'),
]
