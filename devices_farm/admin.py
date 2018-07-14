from django.contrib import admin

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['platform', 'device_name', 'os_version', 'device_gpu', 'type', 'holder']
