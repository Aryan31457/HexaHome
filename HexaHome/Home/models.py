
from django.db import models

class Property(models.Model):
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'
    PG_HOSTEL = 'PG/Hostel'
    PLOT = 'Plot'
    SHARED_FLATS = 'Shared Flats'

    PROPERTY_TYPE_CHOICES = [
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
        (PG_HOSTEL, 'PG/Hostel'),
        (PLOT, 'Plot'),
        (SHARED_FLATS, 'Shared Flats'),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100) 
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default=RESIDENTIAL,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
