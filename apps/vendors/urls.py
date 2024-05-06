# Imports
from django.urls import path
from apps.vendors.views import VendorView


# URL patterns
urlpatterns = [
    path(
        "vendors/",
        VendorView.as_view({"get": "list", "post": "create"}),
        name="api--vendors-list-create",
    ),
    path(
        "vendors/<int:id>/",
        VendorView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="api--vendors-retrieve-update-destroy",
    ),
]
