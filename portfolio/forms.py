from django import forms
from portfolio.models import ContentCreator
import json
from django.core.exceptions import ValidationError

MAX_UPLOAD_SIZE = 300 * 1024  # 300 KB

class ContentCreatorProfileForm(forms.ModelForm):
    class Meta:
        model = ContentCreator
        fields = ['portfolio_url', 'expertise_area', 'profile_photo', 'social_media_links']
    social_media_links = forms.CharField(
        widget=forms.Textarea,
        help_text='Enter your social media links in JSON format. Example: {"twitter": "http://twitter.com/yourprofile"}',
        required=False
    )
    def clean_profile_photo(self):
        profile_photo = self.cleaned_data.get('profile_photo')
        if profile_photo and profile_photo.size > MAX_UPLOAD_SIZE:
            raise ValidationError(f"Image file too large ( > 0.3 MB )")
        return profile_photo

    def clean_social_media_links(self):
        links = self.cleaned_data.get('social_media_links')
        if links:
            try:
                # Ensure it's a valid JSON
                json.loads(links)
            except ValueError:
                raise ValidationError('Invalid JSON format for social media links.')
        return links