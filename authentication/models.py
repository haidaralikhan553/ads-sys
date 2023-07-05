from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    
    CUSTOM_USER_ROLES = [
        ('super-admin', 'Super Admin'),
        ('admin', 'Admin'),
    ]

    user_role = models.CharField(max_length=20, blank=False, null=False, choices=CUSTOM_USER_ROLES, default='admin')