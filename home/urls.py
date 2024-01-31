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
    path('deny_content_creator/<int:user_id>/', views.deny_content_creator, name='deny_content_creator'),]

urlpatterns += [
    # ... other url patterns ...
    path('approvecontentcreator/', ContentCreatorApprovalListView.as_view(), name='approvecontentcreator'),
]


