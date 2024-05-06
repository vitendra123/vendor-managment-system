# Imports
from django.db import models
from apps.vendors.models import Vendor


class HistoricalPerformance(models.Model):
    # Fields
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    # String representation
    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
