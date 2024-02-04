from django.urls import path
from . import views



urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('submit-interest/', views.submit_interest, name='submit_interest'),  # Make sure to reference the view correctly
]
