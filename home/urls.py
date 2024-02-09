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
    path('business/deny_interest/<int:business_id>/', views.deny_business_interest, name='deny_business_interest'),
    path('completed-business-interests/', views.completed_business_interests, name='completed_business_interests'),
    path('business/add-note/<int:business_id>/', views.add_business_note, name='add_business_note'),
    path('business/mark_sold/<int:business_id>/', views.mark_business_sold, name='mark_business_sold'),
    path('business/delete/<int:business_id>/', views.delete_business_interest, name='delete_business_interest'),
    path('business/completed_and_paid/<int:business_id>/', views.mark_completed_and_paid, name='mark_completed_and_paid'),
    path('creators/', views.content_creator_profiles, name='content_creator_profiles'),
    path('delete_content_creator/<int:user_id>/', views.delete_content_creator, name='delete_content_creator'),
]


urlpatterns += [
    # ... other url patterns ...
    path('approvecontentcreator/', ContentCreatorApprovalListView.as_view(), name='approvecontentcreator'),
]


