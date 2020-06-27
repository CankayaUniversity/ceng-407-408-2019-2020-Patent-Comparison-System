import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=32)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"