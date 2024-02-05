from django import forms
from .models import ContentCreator, LifeCategory
import json
from django import forms
from django.core.exceptions import ValidationError
class ContentCreatorProfileForm(forms.ModelForm):
    social_media_link_1 = forms.URLField(required=False)
    social_media_link_2 = forms.URLField(required=False)
    social_media_link_3 = forms.URLField(required=False)
    social_media_link_4 = forms.URLField(required=False)
    social_media_link_5 = forms.URLField(required=False)

    class Meta:
        model = ContentCreator
        fields = ['portfolio_url', 'expertise_area', 'profile_photo', 'life_categories']
        # Note: 'social_media_links' is not included here since it's handled separately

    def clean(self):
        cleaned_data = super().clean()
        social_media_links = {}

        for i in range(1, 6):
            link = cleaned_data.get(f'social_media_link_{i}')
            if link:
                social_media_links[f'link_{i}'] = link

        cleaned_data['social_media_links'] = json.dumps(social_media_links)
        return cleaned_data
