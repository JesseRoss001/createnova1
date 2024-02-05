from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portfolio.models import ContentCreator
from portfolio.forms import ContentCreatorProfileForm
from django.contrib import messages
import json
MAX_UPLOAD_SIZE = 300 * 1024  # 300 KB
@login_required
def your_profile_view(request):
    try:
        content_creator = request.user.contentcreator
    except ContentCreator.DoesNotExist:
        messages.error(request, "You do not have a content creator profile.")
        return redirect('home')  # Use the name of the URL pattern for home

    if request.method == 'POST':
        form = ContentCreatorProfileForm(request.POST, request.FILES, instance=content_creator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('your_profile')  # Use the correct URL name you have defined in urls.py for the profile view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContentCreatorProfileForm(instance=content_creator)
        # Pre-load social media links if any
        social_media_links = content_creator.social_media_links or '{}'
        form.fields['social_media_links'].initial = json.dumps(social_media_links)

    return render(request, 'portfolio/portfolios.html', {'form': form, 'content_creator': content_creator})
