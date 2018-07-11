from django.contrib import admin

from devices_farm.models import Device, Platform


admin.site.register(Device)
admin.site.register(Platform)
