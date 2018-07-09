from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
    )
    room = models.IntegerField()
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    # email = models.EmailField()
    # last_name = models.CharField(max_length=25)


def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_profile, sender=User)
