from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    public_address              = models.CharField(max_length=100, null=True, blank=True)
    nonce                       = models.CharField(max_length=100, null=True, blank=True)
    is_administrator            = models.BooleanField(default=False)
    is_store_owner              = models.BooleanField(default=False)
