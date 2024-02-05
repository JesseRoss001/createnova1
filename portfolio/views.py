from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portfolio.models import ContentCreator
from portfolio.forms import ContentCreatorProfileForm
from django.contrib import messages

@login_required
def your_profile_view(request):
    content_creator = request.user.contentcreator
    if not content_creator.is_approved:
        messages.error(request, 'Your account is pending approval.')
        return redirect('home')

    if request.method == 'POST':
        form = ContentCreatorProfileForm(request.POST, request.FILES, instance=content_creator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('yourprofile')
    else:
        # Prepopulate the form with existing data
        form = ContentCreatorProfileForm(instance=content_creator)

    context = {
        'form': form,
        'content_creator': content_creator
    }
    return render(request, 'portfolio/portfolios.html', context)
