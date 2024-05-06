# Imports
from django.db import models


# Model for Vendor
class Vendor(models.Model):
    # Fields
    name = models.CharField(max_length=255, blank=False, null=False)
    contact_details = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    vendor_code = models.CharField(max_length=255, blank=False, null=False, unique=True)
    on_time_delivery_rate = models.FloatField(blank=True, null=True)
    quality_rating_avg = models.FloatField(blank=True, null=True)
    average_response_time = models.FloatField(blank=True, null=True)
    fulfillment_rate = models.FloatField(blank=True, null=True)

    # String representation
    def __str__(self):
        return self.name
