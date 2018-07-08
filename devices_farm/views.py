from django.shortcuts import render
from .models import Device
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'devices_farm/index.html')


@login_required()
def devices(request):
    return render(request, 'devices_farm/devices.html')


@login_required()
def device(request, device_id):
    device = Device.objects.get(id=device_id)
    context = {'device': device}
    return render(request, 'devices_farm/device.html', context)
