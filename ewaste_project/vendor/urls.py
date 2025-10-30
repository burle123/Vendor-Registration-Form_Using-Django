from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_registration, name='vendor_registration'),
    path('success/', views.vendor_success, name='vendor_success'),
]
