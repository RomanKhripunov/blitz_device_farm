from django.db import models


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
        (WINDOWS, 'WINDOWS PHONE')
    )
    platform = models.CharField(
        max_length=10,
        choices=PLATFORMS,
        default=None
    )
    # os_version = models.CharField(
    #     max_length=10,
    #     default=None,
    #     blank=True,
    # )
    date_added = models.DateTimeField(
        auto_now_add=True
    )
    # device_name = models.CharField(
    #     max_length=25,
    #     default=None,
    #     blank=True,
    # )

    def __str__(self):
        return self.platform, self.date_added
