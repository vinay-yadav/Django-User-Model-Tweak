from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile = models.CharField(max_length=10, null=True, blank=True)
