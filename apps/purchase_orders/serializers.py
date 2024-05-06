# Imports
from apps.purchase_orders.models import PurchaseOrder
from rest_framework import serializers


# Serializer for PurchaseOrder
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgment_date",
        ]
