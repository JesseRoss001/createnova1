from django.urls import path
from . import views

urlpatterns = [
    path('business-services/', views.business_services, name='business_services'),
    path('creator-services/', views.creator_services, name='creator_services'),
]