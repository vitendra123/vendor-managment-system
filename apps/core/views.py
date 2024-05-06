# Imports
import os
from apps.core.serializers import CustomAuthTokenSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


# Initialize the user model
User = get_user_model()


# Custom view to obtain an auth token
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    @swagger_auto_schema(
        operation_id="api--obtain-auth-token",
        operation_description="Obtain an auth token for a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "password"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                "The auth token",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={"token": openapi.Schema(type=openapi.TYPE_STRING)},
                ),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
        },
        tags=["Rest API Authentication"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomCreateUserView(APIView):
    # Set the permission class to allow any
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id="api--create-user",
        operation_description="Create a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "username", "first_name", "last_name", "password"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                "The user",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                        "username": openapi.Schema(type=openapi.TYPE_STRING),
                        "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
        },
        tags=["Rest API Authentication"],
    )
    def post(self, request, *args, **kwargs):
        # Extract email and password from request data
        email = request.data.get("email")
        password = request.data.get("password")

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {"error": "Invalid email format."}, status=status.HTTfP_400_BAD_REQUEST
            )

        # Create user
        if email and password:
            try:
                # Create the user with active status set to True
                user = User.objects.create_user(**request.data, is_active=True)
                return Response(
                    {
                        "email": user.email,
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    },
                    status=status.HTTP_201_CREATED,
                )

            # If user with the email already exists
            except IntegrityError:
                return Response(
                    {"error": "User with this email already exists."},
                    status=status.HTTP_409_CONFLICT,
                )
        else:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
