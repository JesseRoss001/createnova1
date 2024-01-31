from django.contrib import admin
from .models import StaffMember

class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role', 'is_managerial_staff')
    list_filter = ('department', 'is_managerial_staff')
    search_fields = ('user__username', 'department', 'role')
    actions = ['make_managerial_staff']

    def make_managerial_staff(self, request, queryset):
        # Update the selected StaffMembers to set is_managerial_staff to True
        queryset.update(is_managerial_staff=True)

    make_managerial_staff.short_description = "Make selected staff members managerial staff"

admin.site.register(StaffMember, StaffMemberAdmin)