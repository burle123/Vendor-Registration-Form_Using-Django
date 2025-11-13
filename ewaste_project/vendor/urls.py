from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.vendor_registration, name='vendor_registration'),
    path('success/', views.vendor_success, name='vendor_success'),
        path('login/', views.vendor_login, name='vendor_login'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('logout/', views.vendor_logout, name='vendor_logout'),
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
