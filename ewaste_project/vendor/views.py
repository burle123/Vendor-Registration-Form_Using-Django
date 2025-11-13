from django.shortcuts import render, redirect
from .forms import VendorForm
from django.contrib import messages
from .models import Vendor

def vendor_registration(request):
    if request.method == "POST":
        form = VendorForm(request.POST, request.FILES)

        # collect multiple checkbox values
        ewaste = ",".join(request.POST.getlist('ewaste'))
        certifications = ",".join(request.POST.getlist('certifications'))
        documents = ",".join(request.POST.getlist('documents'))

        if form.is_valid():
            vendor = form.save(commit=False)

            vendor.ewaste_categories = ewaste
            vendor.certifications = certifications
            vendor.documents = documents

            vendor.save()
            return redirect('vendor_success')

        # Debug: show errors
        print(form.errors)

    else:
        form = VendorForm()

    return render(request, 'vendor/registration.html', {"form": form})


def vendor_success(request):
    return render(request, 'vendor/success.html')

def vendor_login(request):
    if request.method == 'POST':
        registration_number = request.POST.get('registration_number')
        gst_number = request.POST.get('gst_number')

        try:
            vendor = Vendor.objects.filter(registration_number=registration_number, gst_number=gst_number).first()
            # Store vendor ID in session
            request.session['vendor_id'] = vendor.id
            messages.success(request, "Login successful!")
            return redirect('vendor_dashboard')
        except Vendor.DoesNotExist:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'vendor/login.html') 


def vendor_dashboard(request):
    vendor_id = request.session.get('vendor_id')
    if not vendor_id:
        return redirect('vendor_login')
    
    vendor = Vendor.objects.get(id=vendor_id)
    return render(request, 'vendor/dashboard.html', {'vendor': vendor})


def vendor_logout(request):
    request.session.flush()
    return redirect('vendor_login')
