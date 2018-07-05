from django.shortcuts import render
from .models import Device


def index(request):
    return render(request, 'devices_farm/index.html')


def devices(request):
    return render(request, 'devices_farm/devices.html')


def device(request, device_id):
    device = Device.objects.get(id=device_id)
    context = {'device': device}
    return render(request, 'devices_farm/device.html', context)
