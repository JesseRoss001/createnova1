from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from user_management.models import  StaffMember
from services.models import LifeCategory
from django.contrib.auth.forms import AuthenticationForm
from portfolio.models import ContentCreator
import json
import os



User = get_user_model()

class ContentCreatorSignUpForm(UserCreationForm):
    portfolio_url = forms.URLField(required=False, help_text="Optional: Your portfolio website URL or PDF link")
    expertise_area = forms.CharField(max_length=100)
    social_media_links = forms.CharField(required=False, widget=forms.HiddenInput())  # Store as JSON
    
    life_categories = forms.ModelMultipleChoiceField(
        queryset=LifeCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('portfolio_url', 'expertise_area', 'social_media_links', 'life_categories')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Deactivate account until it is approved
        if commit:
            user.save()
            self.instance.contentcreator.profile_photo = self.cleaned_data.get('profile_photo')
            self.instance.contentcreator.expertise_area = self.cleaned_data.get('expertise_area')
            self.instance.contentcreator.social_media_links = json.loads(self.cleaned_data.get('social_media_links'))
            self.instance.contentcreator.life_categories.set(self.cleaned_data.get('life_categories'))
            self.instance.contentcreator.save()
        return user

class StaffSignUpForm(UserCreationForm):
    department = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)
    access_code = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'department', 'role', 'access_code')

    def clean_access_code(self):
        access_code = self.cleaned_data.get('access_code')
        valid_codes_str = os.environ.get('VALID_ACCESS_CODES', '')
        valid_codes = valid_codes_str.split(',')
        if access_code not in valid_codes:
            raise forms.ValidationError("Invalid access code.")
        return access_code

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pin_code = forms.CharField( required=False, help_text="Enter your 10-digit pin code if you are staff.")

    class Meta:
        fields = ('username', 'password', 'pin_code')
class BusinessNoteForm(forms.Form):
    note = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter notes about communication with the business'}),
        required=False
    )