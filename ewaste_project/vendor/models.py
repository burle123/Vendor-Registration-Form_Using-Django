from django.db import models

class Vendor(models.Model):
    business_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=20)
    year_established = models.IntegerField()
    license_image = models.ImageField(upload_to='licenses/')
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    vendor_type = models.CharField(max_length=50)
    ewaste_categories = models.TextField()
    processing_capacity = models.CharField(max_length=50)
    certifications = models.TextField()
    documents = models.TextField(blank=True, null=True)
    declaration = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
