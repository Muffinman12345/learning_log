"""Defines url patterns for users."""

from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views 

from . import views

app_name = 'users'
urlpatterns = [
    # Login page.
    path('login/', LoginView.as_view(template_name='users/login.html'),
        name='login'),
        
    #logout page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #registration
    path('register/', views.register, name='register'),
]
