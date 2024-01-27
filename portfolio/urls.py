from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/', views.portfolios, name='portfolios'),
]