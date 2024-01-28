from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContentCreator

class ContentCreatorAdmin(SummernoteModelAdmin):
    summernote_fields = ('__all__')

admin.site.register(ContentCreator, ContentCreatorAdmin)