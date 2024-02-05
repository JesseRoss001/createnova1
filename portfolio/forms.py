from django import forms
from portfolio.models import ContentCreator
import json
MAX_UPLOAD_SIZE = 300 * 1024  # 300 KB
class ContentCreatorProfileForm(forms.ModelForm):
    class Meta:
        model = ContentCreator
        fields = ['portfolio_url', 'expertise_area', 'social_media_links', 'profile_photo']

    def clean_social_media_links(self):
        links = self.cleaned_data['social_media_links']
        try:
            # Load the JSON data to ensure it's valid
            json.loads(links)
        except json.JSONDecodeError:
            raise forms.ValidationError('Invalid JSON format.')
        return links
    def clean_profile_photo(self):
        profile_photo = self.cleaned_data.get('profile_photo')
        if profile_photo and profile_photo.size > MAX_UPLOAD_SIZE:
            raise ValidationError(f"Image file too large ( > 0.3 MB )")
        return profile_photo    