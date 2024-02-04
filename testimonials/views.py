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
            try:
                service_package = ServicePackage.objects.get(name=service_package_name)
                business = form.save(commit=False)
                business.service_package_of_interest = service_package
                business.save()
                messages.success(request, 'Your interest has been registered successfully.')
                return redirect('home')  # Replace 'home' with your home page's URL name
            except ServicePackage.DoesNotExist:
                messages.error(request, 'Service package not found.')
                return redirect(request.path)  # Stay on the same page
        else:
            messages.error(request, form.errors)

    else:
        form = BusinessRegistrationForm()

    # Retrieve the section from the URL query parameter
    section = request.GET.get('section')
    if section:
        # Check if the section corresponds to a service package
        try:
            service_package = ServicePackage.objects.get(name=section)
            context = {
                'form': form,
                'service_package': service_package,
                'section': section,
            }
        except ServicePackage.DoesNotExist:
            raise Http404("Service package does not exist")
    else:
        context = {'form': form}

    return render(request, 'testimonials/testimonials.html', context)

def testimonials(request):
    form = BusinessRegistrationForm()
    return render(request, 'testimonials/testimonials.html', {'form': form})
