from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portfolio.models import ContentCreator
from portfolio.forms import ContentCreatorProfileForm
from django.contrib import messages
import json
MAX_UPLOAD_SIZE = 300 * 1024  # 300 KB
@login_required
def your_profile_view(request):
    content_creator = request.user.contentcreator
    if not content_creator.is_approved:
        messages.error(request, 'Your account is pending approval.')
        return redirect('home')

    if request.method == 'POST':
        # Create a dictionary to store social media links
        social_media_links = {}
        for key, value in request.POST.items():
            if key.startswith('social_media_'):
                platform_name = key.split('_')[-1]
                social_media_links[platform_name] = value

        # Convert the dictionary to a JSON string
        social_media_json = json.dumps(social_media_links)

        # Update the content_creator's social_media_links field
        content_creator.social_media_links = social_media_json

        # Process the form
        form = ContentCreatorProfileForm(request.POST, request.FILES, instance=content_creator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('yourprofile')
    else:
        initial_data = {}
        if content_creator.social_media_links:
            # Convert the JSON string back to a Python dictionary
            initial_data['social_media_links'] = json.loads(content_creator.social_media_links)
        else:
            initial_data['social_media_links'] = {}

        form = ContentCreatorProfileForm(initial=initial_data, instance=content_creator)

    context = {
        'form': form,
        'content_creator': content_creator
    }
    return render(request, 'portfolio/portfolios.html', context)