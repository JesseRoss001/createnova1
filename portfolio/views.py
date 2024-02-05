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
            content_creator = form.save(commit=False)
            # Serialize social media links into JSON before saving the model
            social_media_links = {}
            for i in range(1, 6):
                link = form.cleaned_data.get(f'social_media_link_{i}')
                if link:
                    social_media_links[f'link_{i}'] = link
            content_creator.social_media_links = json.dumps(social_media_links)
            content_creator.save()
            form.save_m2m()  # Don't forget to save many-to-many fields if commit=False
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('your_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContentCreatorProfileForm(instance=content_creator)
        # Ensure social_media_links is a valid JSON string
        try:
            social_media_links = json.loads(content_creator.social_media_links) if content_creator.social_media_links else {}
        except json.JSONDecodeError:
            social_media_links = {}

    context = {
        'form': form,
        'social_media_links': social_media_links,
    }
    return render(request, 'portfolio/portfolios.html', context)