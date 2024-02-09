from django import forms
from .models import Business
from django.core.validators import EmailValidator

class BusinessRegistrationForm(forms.ModelForm):
    contact_email = forms.EmailField(
        required=True,
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),
        help_text='Provide a contact email. We aim to respond within 48 hours.'
    )

    class Meta:
        model = Business
        fields = ['business_name', 'contact_email', 'industry', 'interested_life_categories']
        help_texts = {
            'business_name': 'Enter the official name of your business.',
            'industry': 'Select the industry your business operates in.',
            'interested_life_categories': 'Click on the topics to select them as your interests.',
        }
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Name'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'interested_life_categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }