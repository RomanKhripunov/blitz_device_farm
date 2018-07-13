from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from devices_farm.models import Device
from devices_farm.forms import DeviceForm


def index(request):
    return render(request, 'devices_farm/index.html')


@login_required()
def devices(request):
    ordered_devices = Device.objects.order_by('platform')
    context = {'devices': ordered_devices}
    return render(request, 'devices_farm/devices.html', context)


@login_required()
def device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    context = {'device': device}
    return render(request, 'devices_farm/device.html', context)


@login_required()
def change_current_holder():
    pass


# TODO
@login_required()
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('devices_farm:devices'))
    else:
        form = DeviceForm()
    context = {'form': form}
    return render(request, 'devices_farm/add_device.html', context)


# TODO
@login_required()
def edit_device(request, device_id):
    pass


# TODO
# https://docs.djangoproject.com/en/2.0/topics/db/queries/#retrieving-specific-objects-with-filters
@login_required()
def filter_devices(request, **kwargs):
    filtered_devices = Device.objects.filter(**kwargs)
    context = {'devices': filtered_devices}
    return render(request, 'devices_farm/devices.html', context)
