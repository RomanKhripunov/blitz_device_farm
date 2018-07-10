from django.shortcuts import render, get_object_or_404
from .models import Device
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'devices_farm/index.html')


@login_required()
def devices(request):
    ordered_devices = Device.objects.order_by('device_platform')
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
