from django.db import models


class LifeCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

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

    def __str__(self):
        return self.business_name