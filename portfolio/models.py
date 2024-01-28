from django.db import models
from django.contrib.auth.models import User
from common.models import LifeCategory

class ContentCreator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_url = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    expertise_area = models.CharField(max_length=100)
    social_media_links = models.JSONField(blank=True)
    life_categories = models.ManyToManyField(LifeCategory, blank=True)

    def __str__(self):
        return self.user.username