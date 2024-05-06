# Imports
from apps.vendors.serializers import VendorSerializer
from apps.performance.models import HistoricalPerformance
from rest_framework import serializers


# Serializer for HistoricalPerformance
class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()

    class Meta:
        model = HistoricalPerformance
        fields = [
            "id",
            "vendor",
            "date",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
