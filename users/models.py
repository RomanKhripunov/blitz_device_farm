from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    room = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.username
