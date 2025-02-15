from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (("author", "Author"), ("reader", "Reader"))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="reader")

    groups = models.ManyToManyField(
        Group, related_name="custom_user_groups", blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions", blank=True
    )

    def __str__(self):
        return self.username
