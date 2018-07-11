from django.db import models
from django.urls import reverse
from macaddress.fields import MACAddressField
from versionfield import VersionField

from django.contrib.auth.models import User
from users.models import UserProfile


class Platform(models.Model):
    name = models.CharField(
        max_length=20,
        help_text='Create a new platform.'
    )

    def __str__(self):
        return self.name


class Device(models.Model):
    """All information about devices_farm that we have"""
    objects = models.Manager()
    device_platform = models.ForeignKey(
        Platform,
        name='platform',
        on_delete=models.SET_NULL,
        null=True,
    )
    device_name = models.CharField(
        max_length=20,
        default=None,
        blank=False,
    )
    TYPES = (
        ('p', 'Phone'),
        ('t', 'Tablet'),
    )
    device_type = models.CharField(
        name='type',
        max_length=1,
        choices=TYPES,
        default='p',
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
        name='GPU',
        max_length=20,
        default=None,
        null=True,
        blank=True,
        help_text='Only required if Platform is "Android".',
    )
    # current_holder = models.ForeignKey(
    #     UserProfile,
    #     name='holder',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     default='',
    #     to_field=UserProfile.username,
    # )
    # current_room = models.(
    #     UserProfile,
    #     name='room',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     to_field='room',
    # )
    # device_owner = models.ForeignKey(
    #     UserProfile,
    #     name='owner',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     to_field=UserProfile.username,
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

    # def get_absolute_url(self):
    #     return reverse('devices/', args=[str(self.id)])

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Device._meta.fields]

    def __str__(self):
        return self.device_name
