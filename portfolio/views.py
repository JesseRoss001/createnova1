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

    initial_data = {}
    if content_creator.social_media_links:
        # Convert the JSON string back to a Python dictionary
        initial_data['social_media_links'] = json.loads(content_creator.social_media_links)
    else:
        initial_data['social_media_links'] = {}

    if request.method == 'POST':
        form = ContentCreatorProfileForm(request.POST, request.FILES, instance=content_creator)

        # Add logic to pack social media links into JSON before saving
        social_media_links = {}
        for key in request.POST:
            if key.startswith('social_media_'):
                social_media_links[key] = request.POST[key]
        content_creator.social_media_links = json.dumps(social_media_links)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('yourprofile')
    else:
        form = ContentCreatorProfileForm(initial=initial_data, instance=content_creator)

    context = {
        'form': form,
        'content_creator': content_creator
    }
    return render(request, 'portfolio/portfolios.html', context)
