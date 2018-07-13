from django import forms
from django.core.validators import EMPTY_VALUES

from devices_farm.models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

    def clean(self):
        current_platform = self.cleaned_data.get('platform')
        if current_platform == Device.ANDROID:
            device_gpu = self.cleaned_data.get('device_gpu', None)
            if device_gpu in EMPTY_VALUES:
                self._errors['device_gpu'] = self.error_class([
                    'Device GPU required when platform is Android'])
        return self.cleaned_data
