from django.shortcuts import render

def portfolios(request):
    return render(request, 'portfolio/portfolios.html')