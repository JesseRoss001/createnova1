from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContentCreator

class ContentCreatorAdmin(SummernoteModelAdmin):
    list_display = ('user', 'portfolio_url', 'expertise_area', 'is_approved')
    list_filter = ('expertise_area', 'is_approved')
    search_fields = ('user__username', 'expertise_area')
    summernote_fields = ('__all__')

admin.site.register(ContentCreator, ContentCreatorAdmin)