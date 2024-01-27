from django.shortcuts import render

def user_list(request):
    return render(request, 'user_management/user_list.html')