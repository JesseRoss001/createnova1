# home/urls.py
from django.urls import path
from . import views
from .views import ContentCreatorApprovalListView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/content-creator/', views.register_content_creator, name='register_content_creator'),
    path('register/staff/', views.register_staff, name='register_staff'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('approve_content_creator/<int:user_id>/', views.approve_content_creator, name='approve_content_creator'),
    path('deny_content_creator/<int:user_id>/', views.deny_content_creator, name='deny_content_creator'),
    path('business/mark_email_sent/<int:business_id>/', views.mark_email_sent, name='mark_email_sent'),
    path('business/mark_completed/<int:business_id>/', views.mark_completed, name='mark_completed'),
    path('business/interests_management/', views.business_interests_management, name='business_interests_management'),
    ]

urlpatterns += [
    # ... other url patterns ...
    path('approvecontentcreator/', ContentCreatorApprovalListView.as_view(), name='approvecontentcreator'),
]


