from django.db import models
from user_management.models import StaffMember
from services.models import LifeCategory
class ServicePackage(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name
class ServicePackage(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    industry = models.CharField(max_length=100)
    interested_life_categories = models.ManyToManyField(LifeCategory, blank=True)
    service_package_of_interest = models.ForeignKey(ServicePackage, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('email_sent', 'Email Sent'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')
    def __str__(self):
        return self.business_name