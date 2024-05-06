# Imports
from django.apps import AppConfig


# App configurations
class PurchaseOrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.purchase_orders"

    # Add the signals
    def ready(self):
        # Import signals
        import apps.purchase_orders.signals
