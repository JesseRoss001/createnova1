# testimonials/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import BusinessRegistrationForm
from .models import ServicePackage

def testimonials(request):
    form = BusinessRegistrationForm()
    return render(request, 'testimonials/testimonials.html', {'form': form})

def submit_interest(request):
    if request.method == 'POST':
        form = BusinessRegistrationForm(request.POST)
        if form.is_valid():
            # Assuming the ServicePackage name is passed as a string corresponding to the id field
            service_name = request.POST.get('service_package_of_interest')
            service_package = ServicePackage.objects.filter(name=service_name).first()
            if service_package:
                business = form.save(commit=False)
                business.service_package_of_interest = service_package
                business.save()
                # Redirect to a confirmation page or back to form with success message
                return redirect('home')  # Replace with your actual view name
            else:
                # Handle the case where the service package is not found
                form.add_error(None, 'Service package not found.')
    else:
        form = BusinessRegistrationForm()

    return render(request, 'testimonials/testimonials.html', {'form': form})

