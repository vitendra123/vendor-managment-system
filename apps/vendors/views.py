# Imports
from apps.vendors.models import Vendor
from apps.vendors.serializers import VendorSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# VendorView
class VendorView(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VendorSerializer

    @swagger_auto_schema(
        operation_id="api--vendors-list",
        operation_description="List all vendors",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="User authentication token",
            ),
            openapi.Parameter(
                name="limit",
                default=10,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Limit the number of vendors to return",
            ),
            openapi.Parameter(
                name="offset",
                default=0,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Offset the number of vendors to return",
            ),
        ],
        responses={
            status.HTTP_200_OK: VendorSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Vendors"],
    )
    def list(self, request):
        limit = request.query_params.get("limit", 10)
        offset = request.query_params.get("offset", 0)

        vendors = Vendor.objects.all()[int(offset) : int(offset) + int(limit)]
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="api--vendors-create",
        operation_description="Create a new vendor",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="User authentication token",
            )
        ],
        request_body=VendorSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Vendor created successfully", schema=VendorSerializer
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Vendors"],
    )
    def create(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="api--vendors-retrieve",
        operation_description="Retrieve a vendor",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="User authentication token",
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="Vendor ID",
            ),
        ],
        responses={
            status.HTTP_200_OK: VendorSerializer,
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Vendors"],
    )
    def retrieve(self, request, id=None):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="api--vendors-update",
        operation_description="Update a vendor",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="User authentication token",
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="Vendor ID",
            ),
        ],
        request_body=VendorSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Vendor updated successfully", schema=VendorSerializer
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Vendors"],
    )
    def update(self, request, id=None):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="api--vendors-destroy",
        operation_description="Delete a vendor",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="User authentication token",
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="Vendor ID",
            ),
        ],
        responses={
            status.HTTP_204_NO_CONTENT: "Vendor deleted successfully",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Vendors"],
    )
    def destroy(self, request, id=None):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
