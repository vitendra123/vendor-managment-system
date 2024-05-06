# Imports
from django.contrib import admin
from apps.core.models import CustomUser


# Register the models
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Fields
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # List display
    list_display = ("email", "is_staff", "is_superuser")

    # Search fields
    search_fields = ("email",)

    # Ordering
    ordering = ("email",)
