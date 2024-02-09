from django import forms
from .models import ContentCreator, LifeCategory
import json
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import filesizeformat
from django.conf import settings
class ContentCreatorProfileForm(forms.ModelForm):
    social_media_link_1 = forms.URLField(required=False)
    social_media_link_2 = forms.URLField(required=False)
    social_media_link_3 = forms.URLField(required=False)
    social_media_link_4 = forms.URLField(required=False)
    social_media_link_5 = forms.URLField(required=False)

    class Meta:
        model = ContentCreator
        fields = ['portfolio_url', 'expertise_area', 'profile_photo', 'life_categories']
        widgets = {
            'life_categories': forms.CheckboxSelectMultiple,
        }
    def clean_profile_photo(self):
        profile_photo = self.cleaned_data.get('profile_photo')
        if profile_photo:
            if profile_photo.size > 0.3 * 1024 * 1024:  # 0.3 MB limit
                raise ValidationError(_('Please keep filesize under {}. Current filesize {}').format(filesizeformat(0.3 * 1024 * 1024), filesizeformat(profile_photo.size)))
        return profile_photo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize form fields for social media links if they exist
        social_media_links = self.instance.social_media_links or []
        for i, link in enumerate(social_media_links, start=1):
            self.fields[f'social_media_link_{i}'].initial = link
