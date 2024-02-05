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
from testimonials.models import Business
from services.models import LifeCategory

def home(request):
    user = request.user
    is_staff_member = False
    is_content_creator = False

    # Initialize context dictionary here
    context = {
        'is_staff_member': False,
        'is_content_creator': False,
        'user_name': None,
        'content_creators_awaiting_approval': 0,
        'awaiting_content_creators': [],
    }

    if user.is_authenticated:
        is_staff_member = StaffMember.objects.filter(user=user).exists()
        is_content_creator = ContentCreator.objects.filter(user=user).exists()
        context['is_staff_member'] = is_staff_member
        context['is_content_creator'] = is_content_creator
        context['user_name'] = user.get_full_name() or user.username

    if is_staff_member:
        new_business_interests = Business.objects.filter(status='pending').order_by('-id')  # or any specific status
        context['new_business_interests'] = new_business_interests

    # Count content creators awaiting approval
    content_creators_awaiting_approval = ContentCreator.objects.filter(is_approved=False).count()
    context['content_creators_awaiting_approval'] = content_creators_awaiting_approval

    # Get the list of awaiting content creators
    awaiting_content_creators = ContentCreator.objects.filter(is_approved=False)
    context['awaiting_content_creators'] = awaiting_content_creators

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
            pin_code = form.cleaned_data.get('pin_code')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Check if the user is a content creator
                try:
                    content_creator = ContentCreator.objects.get(user=user)
                except ContentCreator.DoesNotExist:
                    content_creator = None

                if content_creator:
                    if not content_creator.is_approved:
                        messages.error(request, 'Your account is pending approval. You will be able to fully access the site once an administrator has approved your account.')
                        return redirect('home')  # Redirect to the home page


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
        form = ContentCreatorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Keep the user inactive until approved
            user.save()
            content_creator = ContentCreator.objects.create(
                user=user,
                portfolio_url=form.cleaned_data.get('portfolio_url'),
                expertise_area=form.cleaned_data.get('expertise_area'),
                social_media_links=form.cleaned_data.get('social_media_links'),
                profile_photo=form.cleaned_data.get('profile_photo')  # Assuming you handle the profile photo upload
            )
            # Assign selected categories to the content creator
            content_creator.life_categories.set(form.cleaned_data.get('life_categories'))
            messages.success(request, 'Your account has been created and is pending approval.')
            return redirect('home')  # Redirect content creators to home
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
def business_interests_management(request):
    businesses = Business.objects.prefetch_related('interested_life_categories').all()
    return render(request, 'home/business_interests_management.html', {'businesses': businesses})


def mark_email_sent(request, business_id):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('home')

    business = get_object_or_404(Business, pk=business_id)
    business.status = 'email_sent'
    business.save()
    messages.success(request, "Email status updated successfully.")
    return redirect('business_interests_management')

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def mark_completed(request, business_id):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('home')

    business = get_object_or_404(Business, pk=business_id)
    business.status = 'completed'
    business.save()
    messages.success(request, f"{business.business_name} has been marked as completed.")
    return redirect('business_interests_management')  # Redirect to the management page

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def deny_business_interest(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    business.delete()  # This will remove the business interest from the database
    messages.success(request, "Business interest has been successfully denied and removed.")
    return redirect('business_interests_management')


@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def completed_business_interests(request):
    completed_businesses = Business.objects.filter(status='completed')
    return render(request, 'home/completed_business_interests.html', {'completed_businesses': completed_businesses})

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def add_business_note(request, business_id):
    if request.method == 'POST':
        form = BusinessNoteForm(request.POST)
        if form.is_valid():
            business = get_object_or_404(Business, pk=business_id)
            # Assuming you have a notes field or related model for Business
            business.notes = form.cleaned_data['note']
            business.save()
            messages.success(request, "Note added successfully.")
            return redirect('completed_business_interests')
    else:
        form = BusinessNoteForm()
    return render(request, 'home/add_business_note.html', {'form': form})

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def mark_business_sold(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    business.is_sold = True
    business.save()
    messages.success(request, "Business marked as sold.")
    return redirect('completed_business_interests')
@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def delete_business_interest(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    business.delete()
    messages.success(request, "Business interest deleted.")
    return redirect('completed_business_interests')

@login_required
@user_passes_test(lambda u: StaffMember.objects.filter(user=u).exists())
def mark_completed_and_paid(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    business.completed_and_paid = True
    business.save()
    messages.success(request, f"Project with {business.business_name} has been marked as completed and paid for.")
    return redirect('completed_business_interests')
