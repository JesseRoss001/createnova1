from django.urls import path
from .views import your_profile_view

urlpatterns = [
    path('', your_profile_view, name='yourprofile'),
    path('your-profile/', your_profile_view, name='your_profile'),   # Use your_profile_view here
]