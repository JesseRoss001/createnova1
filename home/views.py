from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from .forms import ContentCreatorSignUpForm, StaffSignUpForm, LoginForm
from user_management.models import StaffMember
from portfolio.models import ContentCreator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.http import JsonResponse


@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def home(request):
    user = request.user
    is_staff_member = StaffMember.objects.filter(user=user).exists()
    is_content_creator = ContentCreator.objects.filter(user=user).exists()
    
    # Count content creators awaiting approval
    content_creators_awaiting_approval = ContentCreator.objects.filter(is_approved=False).count()
    
    # Get the list of awaiting content creators
    awaiting_content_creators = ContentCreator.objects.filter(is_approved=False)
    
    context = {
        'is_staff_member': is_staff_member,
        'is_content_creator': is_content_creator,
        'user_name': user.get_full_name() or user.username if user.is_authenticated else None,
        'content_creators_awaiting_approval': content_creators_awaiting_approval,
        'awaiting_content_creators': awaiting_content_creators,  # Pass the list to the template
    }
    
    if 'just_logged_in' in request.session:
        messages.info(request, 'Welcome to CreateNova!')
        del request.session['just_logged_in']
    
    return render(request, 'home/home.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['just_logged_in'] = True
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid login details.')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

def register_content_creator(request):
    if request.method == 'POST':
        form = ContentCreatorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            ContentCreator.objects.create(
                user=user,
                portfolio_url=form.cleaned_data.get('portfolio_url'),
                expertise_area=form.cleaned_data.get('expertise_area'),
                social_media_links=form.cleaned_data.get('social_media_links')
            )
            messages.success(request, 'Your account has been created and is pending approval.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
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
                department=form.cleaned_data.get('department'),
                role=form.cleaned_data.get('role')
            )
            messages.success(request, 'Staff account created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffSignUpForm()
    return render(request, 'home/register_staff.html', {'form': form})

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def approve_content_creator(request, user_id):
    content_creator = get_object_or_404(ContentCreator, pk=user_id)
    content_creator.is_approved = True
    content_creator.user.is_active = True
    content_creator.user.save()
    content_creator.save()
    return JsonResponse({'status': 'approved'})

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def deny_content_creator(request, user_id):
    content_creator = get_object_or_404(ContentCreator, pk=user_id)
    content_creator.delete()  # or any other logic for denial
    return JsonResponse({'status': 'denied'})
class ContentCreatorApprovalListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ContentCreator
    template_name = 'home/approve_content_creator_list.html'
    context_object_name = 'awaiting_content_creators'
    
    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return ContentCreator.objects.filter(is_approved=False)