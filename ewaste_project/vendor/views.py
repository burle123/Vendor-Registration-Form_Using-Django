from django.shortcuts import render, redirect
from .forms import VendorForm

def vendor_registration(request):
    if request.method == "POST":
        form = VendorForm(request.POST, request.FILES)

        # for multiple checkbox values
        ewaste = ",".join(request.POST.getlist('ewaste'))
        certifications = ",".join(request.POST.getlist('certifications'))
        documents = ",".join(request.POST.getlist('documents'))

        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.ewaste = ewaste
            vendor.certifications = certifications
            vendor.documents = documents
            vendor.save()
            return redirect('vendor_success')

    return render(request, 'vendor/registration.html')
    

def vendor_success(request):
    return render(request, 'vendor/success.html')
