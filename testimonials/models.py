from django.db import models
from user_management.models import StaffMember
from services.models import Business

class Testimonial(models.Model):
    content = models.TextField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial for {self.business.business_name}"