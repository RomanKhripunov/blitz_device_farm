from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from .models import Device
from users.models import User
from .forms import DeviceForm


class DeviceList(ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'devices_farm/devices.html'
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeviceList, self).dispatch(request, *args, **kwargs)


class DeviceDetail(DetailView):
    model = Device
    context_object_name = 'device'
    template_name = 'devices_farm/device.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeviceDetail, self).dispatch(request, *args, **kwargs)


class AddDevice(CreateView):
    model = Device
    fields = '__all__'
    template_name = 'devices_farm/add_device.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AddDevice, self).dispatch(request, *args, **kwargs)


class DeviceUpdate(UpdateView):
    model = Device
    fields = '__all__'
    template_name = 'devices_farm/edit_device.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeviceUpdate, self).dispatch(request, *args, **kwargs)


@login_required()
def change_holder(request):
    if request.method == 'POST':
        device = Device.objects.get(pk=request.POST['device_pk'])
        device.holder = User.objects.get(pk=request.POST['new_holder'])
        device.save()
        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'result': 'nok'})


# TODO
# https://docs.djangoproject.com/en/2.0/topics/db/queries/#retrieving-specific-objects-with-filters
@login_required()
def filter_devices(request, **kwargs):
    filtered_devices = Device.objects.filter(**kwargs)
    context = {'devices': filtered_devices}
    return render(request, 'devices_farm/devices.html', context)
