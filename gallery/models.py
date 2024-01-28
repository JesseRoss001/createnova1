from django.db import models
from portfolio.models import ContentCreator

class GalleryItem(models.Model):
    creator = models.ForeignKey(ContentCreator, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title