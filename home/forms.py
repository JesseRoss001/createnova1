from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from user_management.models import  StaffMember
from portfolio.models import ContentCreator
import json

class ContentCreatorSignUpForm(UserCreationForm):
    portfolio_url = forms.URLField(required=False)
    expertise_area = forms.CharField(max_length=100)
    social_media_links = forms.CharField(required=False)  # Use JSONField in Django 3.1 and above

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'portfolio_url', 'expertise_area', 'social_media_links')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Deactivate account until it is approved
        if commit:
            user.save()
        return user

class StaffSignUpForm(UserCreationForm):
    department = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)
    access_code = forms.CharField(max_length=20)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'department', 'role', 'access_code')

    def clean_access_code(self):
        access_code = self.cleaned_data.get('access_code')
        valid_codes = ["4B4IYn4eMS06lLlw0mhv", "G2Yzm4fsWJakX9N9d2XL", "BBS4di6qzjp94UAzvA9g", "3nod6OgbBJUhC9aRZfBo", "31qTTrF5F4p0X2vVkq7a", "RXUvfr1WWwLnDkyz4Hbq", "a7PvA8opvq24SkxGVcS5", "mvNtmastmNGo9McgSZxW", "AiLRBr6L8gJ8Hf9J4gZZ", "0HN0DQ4Z3o2Lj5MqZ3kT", "u2aZCpeIxc61jwVRdH1e", "a1EP6NB4kIjBfWCSvolO", "47bV22wpc5VraTLmUJLF", "QvkXgsuqksn2sUSHR5Lv", "gEG9nxrJuFc3sjF8cAdf", "AQ5iJ5D3EFNeGmb8scDA", "Kc9WLeIzP45VJeXsw8qG", "YCgQNyV47Neoz3Lidud6", "VuoiJJw5W3tnFrj9EgDe", "lLXrUslXcAw78EEf2hcO"  # ... include all access codes ...
        ]
        if access_code not in valid_codes:
            raise forms.ValidationError("Invalid access code.")
        return access_code

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Automatically set as staff
        if commit:
            user.save()
        return user