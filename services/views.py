from django.shortcuts import render

def business_services(request):
    return render(request, 'services/business_services.html')

def creator_services(request):
    return render(request, 'services/creator_services.html')
# Create your views here.
