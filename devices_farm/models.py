from django.db import models
from django.urls import reverse

from macaddress.fields import MACAddressField
from versionfield import VersionField

from users.models import User


class Device(models.Model):
    """All information about devices_farm that we have"""
    objects = models.Manager()

    ANDROID = 'Android'
    IOS = 'iOS'
    WIN_MOBILE = 'Windows Mobile'
    PLATFORMS = (
        (IOS, IOS),
        (ANDROID, ANDROID),
        (WIN_MOBILE, WIN_MOBILE)
    )

    device_platform = models.CharField(
        name='platform',
        max_length=20,
        choices=PLATFORMS,
    )
    device_name = models.CharField(
        max_length=20,
    )

    PHONE = 'Phone'
    TABLET = 'Tablet'
    TYPES = (
        (PHONE, PHONE),
        (TABLET, TABLET),
    )

    device_type = models.CharField(
        name='type',
        max_length=20,
        choices=TYPES,
        default=PHONE,
    )
    # TODO: needs to use version library
    # os_version = VersionField(
    #     default=''
    # )
    os_version = models.CharField(
        max_length=10,
        default=None,
    )
    device_gpu = models.CharField(
        max_length=20,
        blank=True,
        help_text='Only required if Platform is "Android".',
    )
    device_owner = models.ForeignKey(
        User,
        name='owner',
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_owner'
    )
    current_holder = models.ForeignKey(
        User,
        name='holder',
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_holder'
    )
    company_number = models.CharField(
        max_length=20,
        blank=True,
        default='',
    )
    serial_number = models.CharField(
        max_length=20,
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
        blank=True,
        default='',
    )
    screen_diagonal = models.CharField(
        max_length=20,
        blank=True,
        default='',
    )
    memory_size = models.IntegerField(
        help_text='Size in GB.',
    )
    device_color = models.CharField(
        name='color',
        max_length=20,
        blank=True,
        default='',
    )
    is_active = models.BooleanField(
        default=True,
    )
    characteristics_url = models.URLField(
        default='',
        blank=True,
    )

    class Meta:
        ordering = ['platform', 'type', 'device_name']

    def get_absolute_url(self):
        return reverse('devices_farm:device', args=[str(self.id)])

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Device._meta.fields]

    def __str__(self):
        return self.device_name
