from django import forms
from portfolio.models import ContentCreator
import json
from django.core.exceptions import ValidationError

MAX_UPLOAD_SIZE = 300 * 1024  # 300 KB

class ContentCreatorProfileForm(forms.ModelForm):
    # Define a new field for social media links
    new_social_media_links = forms.CharField(
        label='New Social Media Links',
        required=False,  # It's not required since some may be removed
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Media URL'}),
    )

    class Meta:
        model = ContentCreator
        fields = ['portfolio_url', 'expertise_area', 'profile_photo']
        # Note that we've removed 'social_media_links' from the fields list

    def clean_profile_photo(self):
        profile_photo = self.cleaned_data.get('profile_photo')
        if profile_photo and profile_photo.size > MAX_UPLOAD_SIZE:
            raise ValidationError(f"Image file too large ( > 0.3 MB )")
        return profile_photo