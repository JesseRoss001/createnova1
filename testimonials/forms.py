from django import forms
from .models import Business


class BusinessRegistrationForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'contact_email', 'industry', 'interested_life_categories']
        help_texts = {
            'business_name': 'Enter the official name of your business.',
            'contact_email': 'Provide a contact email. We aim to respond within 48 hours.',
            'industry': 'Select the industry your business operates in.',
            'interested_life_categories': 'Click on the topics to select them as your interests.',
        }
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Name'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'interested_life_categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }