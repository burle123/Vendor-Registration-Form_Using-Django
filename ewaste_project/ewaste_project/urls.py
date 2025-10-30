from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from vendor import views


urlpatterns = [
    path('', lambda request: redirect('vendor_registration')),
    path('admin/', admin.site.urls),
    path('vendor/', include('vendor.urls')),
    
]
 
