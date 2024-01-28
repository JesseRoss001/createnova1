from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimonial

class TestimonialAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Testimonial, TestimonialAdmin)
