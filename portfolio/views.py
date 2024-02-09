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
            # Assuming social_media_links is a list in the ContentCreator model
            social_media_links = [
                request.POST.get(f'social_media_link_{i}', '') for i in range(1, 6)
                if request.POST.get(f'social_media_link_{i}', '')
            ]
            content_creator.social_media_links = social_media_links
            content_creator.save()
            messages.success(request, 'Your profile has been updated successfully.')
            # Redirect back to the profile page to show the updated info
            return redirect('your_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContentCreatorProfileForm(instance=content_creator)

    context = {
        'form': form,
        'social_media_links_json': json.dumps(content_creator.social_media_links or []),
    }
    return render(request, 'portfolio/portfolios.html', context)
