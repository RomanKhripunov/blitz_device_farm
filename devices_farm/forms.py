from django import forms
from django.core.validators import EMPTY_VALUES

from .models import Device


class DeviceForm(forms):
    class Meta:
        model = Device

    def clean(self):
        current_platform = self.cleaned_data.get('device_platform')
        if current_platform == Device.ANDROID:
            device_gpu = self.cleaned_data.get('device_gpu', None)
            if device_gpu in EMPTY_VALUES:
                self._errors['device_gpu'] = self.error_class([
                    'Device GPU required if platform is Android'])
        return self.cleaned_data
