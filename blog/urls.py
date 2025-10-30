from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('register')),  # Redirect root to register
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('registrations/', views.registration_list, name='registration_list'),
]