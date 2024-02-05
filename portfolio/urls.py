from django.urls import path
from .views import your_profile_view

urlpatterns = [
    path('', your_profile_view, name='yourprofile'),
]