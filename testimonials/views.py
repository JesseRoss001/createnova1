from django.shortcuts import render

def testimonials(request):
        # Create a range of numbers for the Lottie files
    lottie_numbers = range(1, 24)  # This will create a range from 1 to 23
    context = {'lottie_numbers': lottie_numbers}
    return render(request, 'testimonials/testimonials.html',context)