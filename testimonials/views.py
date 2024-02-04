from django.shortcuts import render, redirect
from .forms import BusinessRegistrationForm
from .models import ServicePackage
from django.contrib import messages
from django.http import Http404

def submit_interest(request):
    if request.method == 'POST':
        form = BusinessRegistrationForm(request.POST)
        if form.is_valid():
            service_package_name = request.POST.get('service_package_of_interest')
            business = form.save(commit=False)
            try:
                service_package = ServicePackage.objects.get(name=service_package_name)
                business.service_package_of_interest = service_package
                business.save()
                form.save_m2m()  # This saves the ManyToMany data for the form.
                messages.success(request, 'Your interest has been registered successfully.')
                return redirect('home')
            except ServicePackage.DoesNotExist:
                messages.error(request, 'Service package not found.')
                return redirect(request.path)
        else:
            messages.error(request, form.errors)
    else:
        form = BusinessRegistrationForm()
    return render(request, 'testimonials/testimonials.html', {'form': form})

def testimonials(request):
    form = BusinessRegistrationForm()
    return render(request, 'testimonials/testimonials.html', {'form': form})
