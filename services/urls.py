from django.urls import path
from . import views

urlpatterns = [
    path('business/', views.business_services, name='business_services'),
    path('creator/', views.creator_services, name='creator_services'),
]
