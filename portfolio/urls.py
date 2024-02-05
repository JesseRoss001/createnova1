from django.urls import path
from .views import your_profile_view

urlpatterns = [
    path('your-profile/', your_profile_view, name='your_profile'),
]