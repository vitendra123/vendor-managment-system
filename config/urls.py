# Imports
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Set the url patters
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls, name="django-admin"),
]


# Add API urls
urlpatterns += [
    path("api/", include("apps.core.urls")),
    path("api/", include("apps.vendors.urls")),
    path("api/", include("apps.purchase_orders.urls")),
    path("api/", include("apps.performance.urls")),
]


# Swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="Vendor Management System API",
        default_version="v1",
        description="**Vendor Management System: Django and Django Rest Framework**",
        contact=openapi.Contact(email="rohit.vilas.ingole@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Swagger urls
urlpatterns += [
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
