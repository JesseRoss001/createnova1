from django.db import models
from django.contrib.auth.models import User

class StaffMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    is_managerial_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username