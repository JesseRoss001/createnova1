from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import GalleryItem

class GalleryItemAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(GalleryItem, GalleryItemAdmin)
