from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .forms import ContentCreatorSignUpForm, StaffSignUpForm
from user_management.models import  StaffMember
from portfolio.models import ContentCreator
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'home/home.html')
# Create your views here.
def login_view(request):
    return render(request, 'home/login.html')
def is_staff_member(user):
    return user.is_authenticated and StaffMember.objects.filter(user=user).exists()

@login_required
@user_passes_test(is_staff_member)
def approve_content_creator(request, user_id):
    try:
        content_creator = ContentCreator.objects.get(user_id=user_id)
        content_creator.is_approved = True
        content_creator.user.is_active = True  # Activate user account
        content_creator.user.save()
        content_creator.save()
        # Redirect to a staff dashboard or a successful approval page
        return render(request, 'home/home.html')
    except ContentCreator.DoesNotExist:
        # Handle the exception if the Content Creator doesn't exist
        return HttpResponseForbidden()

def register_content_creator(request):
    if request.method == 'POST':
        form = ContentCreatorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Do not activate until approved by staff
            user.save()
            ContentCreator.objects.create(
                user=user,
                portfolio_url=form.cleaned_data['portfolio_url'],
                expertise_area=form.cleaned_data['expertise_area'],
                social_media_links=json.loads(form.cleaned_data['social_media_links'])
            )
            # Redirect to a page informing the user that their account awaits approval
            return render(request, 'home/home.html')
    else:
        form = ContentCreatorSignUpForm()
    return render(request, 'home/register_content_creator.html', {'form': form})

def register_staff(request):
    if request.method == 'POST':
        form = StaffSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            StaffMember.objects.create(
                user=user,
                department=form.cleaned_data['department'],
                role=form.cleaned_data['role']
            )
            # Redirect to the staff dashboard or home page after successful registration
            return render(request, 'home/home.html')
    else:
        form = StaffSignUpForm()
    return render(request, 'home/register_staff.html', {'form': form})