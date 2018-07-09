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

    device_platform = models.CharField(
        max_length=10,
        choices=PLATFORMS,
        default=None,
    )
    os_version = models.CharField(
        max_length=10,
        default=None,
    )
    device_gpu = models.CharField(
        max_length=20,
        default=None,
        null=True,
        blank=True,
        help_text='Only required if Platform is "Android".',
    )
    device_name = models.CharField(
        max_length=20,
        default=None,
        blank=False,
    )
    # current_holder = models.ForeignKey(
    #     UserProfile,
    #     db_column='username',
    #     on_delete=models.CASCADE,
    # )
    # current_room = models.ForeignKey(
    #     UserProfile,
    #     db_column='room',
    #     on_delete=models.CASCADE,
    # )
    # device_owner = models.ForeignKey(
    #     UserProfile,
    #     db_column='room',
    #     on_delete=models.CASCADE,
    # )
    mac_address = MACAddressField(
        null=True,
        blank=True,
        integer=False,
        default='',
    )
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
    imei_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    sim_card = models.BooleanField(default=True,)
    sd_card = models.BooleanField(default=False,)
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
    memory_size = models.IntegerField()
    device_color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    is_active = models.BooleanField(default=True,)



    def __str__(self):
        return self.device_name
