from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ServicePackage, Business

class ServicePackageAdmin(SummernoteModelAdmin):
    summernote_fields = ('details',)

class BusinessAdmin(SummernoteModelAdmin):
    summernote_fields = ('interested_life_categories',)

admin.site.register(ServicePackage, ServicePackageAdmin)
admin.site.register(Business, BusinessAdmin)
