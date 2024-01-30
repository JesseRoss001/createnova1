# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/content-creator/', views.register_content_creator, name='register_content_creator'),
    path('register/staff/', views.register_staff, name='register_staff'),
    path('login/', views.login_view, name='login'), 
        path('logout/', views.logout_view, name='logout'),
] # Assuming you have a login view
