from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from services.models import LifeCategory 

class StaffMember(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    is_managerial_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username