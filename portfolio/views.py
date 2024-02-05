# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContentCreator
from .forms import ContentCreatorProfileForm
from django.contrib import messages
import json

@login_required
def your_profile_view(request):
    try:
        content_creator = request.user.contentcreator
    except ContentCreator.DoesNotExist:
        messages.error(request, "You do not have a content creator profile.")
        return redirect('home')

    if request.method == 'POST':
        form = ContentCreatorProfileForm(request.POST, request.FILES, instance=content_creator)
        if form.is_valid():
            # This will now include the combined JSON for the social media links
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('your_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContentCreatorProfileForm(instance=content_creator)

    # No need to separately process social_media_links_json now
    return render(request, 'portfolio/portfolios.html', {'form': form})