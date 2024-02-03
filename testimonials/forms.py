from django import forms
from .models import Business

class BusinessRegistrationForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['business_name', 'contact_email', 'industry', 'interested_life_categories']