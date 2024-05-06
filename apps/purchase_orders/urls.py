# Imports
from django.urls import path
from apps.purchase_orders.views import (
    PurchaseOrderView,
    AcknowledgePurchaseOrderViewSet,
)


# URL patterns
urlpatterns = [
    path(
        "purchase_orders/",
        PurchaseOrderView.as_view({"get": "list", "post": "create"}),
        name="api--purchase_orders-list-create",
    ),
    path(
        "purchase_orders/<int:id>/",
        PurchaseOrderView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="api--purchase_orders-retrieve-update-destroy",
    ),
    path(
        "purchase_orders/<int:id>/acknowledge/",
        AcknowledgePurchaseOrderViewSet.as_view({"post": "acknowledge"}),
        name="api--purchase_orders-acknowledge-purchase-order",
    ),
]
