# Imports
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid


# Custom user manager
class CustomUserManager(BaseUserManager):
    # Method to create a user
    def create_user(self, email, password=None, **extra_fields):
        # Raise an error if the email field is not set
        if not email:
            raise ValueError("The Email field must be set")

        # Normalize the email
        email = self.normalize_email(email)

        # Create the user
        user = self.model(email=email, **extra_fields)

        # Set the password
        user.set_password(password)

        # Save the user
        user.save(using=self._db)

        # Return the user instance
        return user

    # Method to create a superuser
    def create_superuser(self, email, password=None, **extra_fields):
        # Set the superuser fields
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Create, save and return the user
        return self.create_user(email, password, **extra_fields)


# Custom user model
class CustomUser(AbstractUser):
    # Fields
    id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=255,
        verbose_name="ID",
    )
    email = models.EmailField(unique=True, max_length=255, verbose_name="Email Address")
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    # Set the email field as the username field
    USERNAME_FIELD = "email"

    # Set the required fields
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    # Custom user manager
    objects = CustomUserManager()

    # String representation
    def __str__(self):
        return self.email

    # Property for the full name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
