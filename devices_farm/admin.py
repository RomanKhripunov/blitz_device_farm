from django.contrib import admin

from devices_farm.models import Device, Platform


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['platform', 'device_name', 'os_version', 'device_gpu', 'type']

admin.site.register(Platform)
