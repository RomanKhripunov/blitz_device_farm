from django.db import models
from macaddress.fields import MACAddressField

from django.contrib.auth.models import User
from users.models import UserProfile
# class DeviceOS(models.Model):
#     """Operation systems of ours devices_farm"""
#     pass


class Device(models.Model):
    """All information about devices_farm that we have"""
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    WINDOWS = 'WIN PHONE'

    PLATFORMS = (
        (IOS, 'iOS'),
        (ANDROID, 'ANDROID'),
        (WINDOWS, 'WINDOWS PHONE'),
    )

    objects = models.Manager()
    device_platform = models.CharField(
        name='platform',
        max_length=10,
        choices=PLATFORMS,
        default=None,
    )
    device_name = models.CharField(
        max_length=20,
        default=None,
        blank=False,
    )
    device_type = models.CharField(
        name='type',
        max_length=10,
        choices=(
            ('Phone', 'Phone'),
            ('Tablet', 'Tablet'),
        )
    )
    os_version = models.CharField(
        max_length=10,
        default=None,
    )
    device_gpu = models.CharField(
        name='GPU',
        max_length=20,
        default=None,
        null=True,
        blank=True,
        help_text='Only required if Platform is "Android".',
    )
    # current_holder = models.ForeignKey(
    #     UserProfile,
    #     name = 'holder',
    #     db_column='username',
    #     on_delete=models.CASCADE,
    # )
    # current_room = models.ForeignKey(
    #     UserProfile,
    #     name = 'room',
    #     db_column='room',
    #     on_delete=models.CASCADE,
    # )
    # device_owner = models.ForeignKey(
    #     UserProfile,
    #     name='owner',
    #     db_column='username',
    #     on_delete=models.CASCADE,
    # )
    company_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    serial_number = models.CharField(
        max_length=20,
        default='',
    )
    mac_address = MACAddressField(
        null=True,
        blank=True,
        integer=False,
        default='',
    )
    imei_number = models.CharField(
        name='imei',
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    sim_card = models.BooleanField(
        default=True,
    )
    sd_card = models.BooleanField(
        default=False,
    )
    screen_resolution = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    screen_diagonal = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    memory_size = models.IntegerField(
        help_text='Size in GB.',
    )
    device_color = models.CharField(
        name='color',
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    is_active = models.BooleanField(
        default=True,
    )
    characteristics_url = models.URLField(
        default='',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['platform', 'type', 'device_name']

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Device._meta.fields]

    def __str__(self):
        return self.device_name
