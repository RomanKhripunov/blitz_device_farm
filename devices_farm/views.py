from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Device
from .forms import DeviceForm


def index(request):
    return render(request, 'devices_farm/index.html')


# @login_required()
# def devices(request):
#     ordered_devices = Device.objects.order_by('platform')
#     context = {'devices': ordered_devices}
#     return render(request, 'devices_farm/devices.html', context)
class DeviceListView(generic.ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'devices_farm/devices.html'
    paginate_by = 20


# @login_required()
# def device(request, device_id):
#     device = get_object_or_404(Device, id=device_id)
#     context = {'device': device}
#     return render(request, 'devices_farm/device.html', context)
class DeviceDetailView(generic.DetailView):
    model = Device
    context_object_name = 'device'
    template_name = 'devices_farm/device.html'


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
# @login_required()
# def edit_device(request, device_id):
#     pass
class DeviceUpdateView(generic.UpdateView):
    model = Device
    context_object_name = 'device'
    template_name = 'devices_farm/edit_device.html'


# TODO
# https://docs.djangoproject.com/en/2.0/topics/db/queries/#retrieving-specific-objects-with-filters
@login_required()
def filter_devices(request, **kwargs):
    filtered_devices = Device.objects.filter(**kwargs)
    context = {'devices': filtered_devices}
    return render(request, 'devices_farm/devices.html', context)
