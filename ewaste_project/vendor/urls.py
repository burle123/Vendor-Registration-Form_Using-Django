from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.vendor_registration, name='vendor_registration'),
    path('success/', views.vendor_success, name='vendor_success'),
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
