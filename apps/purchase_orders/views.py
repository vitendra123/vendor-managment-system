# Imports
from apps.purchase_orders.models import PurchaseOrder
from apps.purchase_orders.serializers import PurchaseOrderSerializer
from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# PurchaseOrderView
class PurchaseOrderView(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseOrderSerializer

    @swagger_auto_schema(
        operation_id="api--purchase_orders-list",
        operation_description="List all purchase orders",
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
                description="Limit the number of purchase orders to return",
            ),
            openapi.Parameter(
                name="offset",
                default=0,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Offset the number of purchase orders to return",
            ),
        ],
        responses={
            status.HTTP_200_OK: PurchaseOrderSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Purchase Orders"],
    )
    def list(self, request):
        limit = request.query_params.get("limit", 10)
        offset = request.query_params.get("offset", 0)

        purchase_orders = PurchaseOrder.objects.all()[
            int(offset) : int(offset) + int(limit)
        ]
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="api--purchase_orders-create",
        operation_description="Create a new purchase order",
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
        request_body=PurchaseOrderSerializer,
        responses={
            status.HTTP_201_CREATED: PurchaseOrderSerializer,
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Purchase Orders"],
    )
    def create(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="api--purchase_orders-retrieve",
        operation_description="Retrieve a purchase order",
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
        responses={
            status.HTTP_200_OK: PurchaseOrderSerializer,
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Purchase Orders"],
    )
    def retrieve(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="api--purchase_orders-update",
        operation_description="Update a purchase order",
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
        request_body=PurchaseOrderSerializer,
        responses={
            status.HTTP_200_OK: PurchaseOrderSerializer,
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Purchase Orders"],
    )
    def update(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="api--purchase_orders-destroy",
        operation_description="Delete a purchase order",
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
        responses={
            status.HTTP_204_NO_CONTENT: "Purchase order deleted successfully",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Purchase Orders"],
    )
    def destroy(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AcknowledgePurchaseOrderViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseOrderSerializer

    @swagger_auto_schema(
        operation_id="api--purchase_orders-acknowledge",
        operation_description="Acknowledge a purchase order",
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
                default="",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="Purchase order ID",
            ),
        ],
        responses={
            status.HTTP_200_OK: PurchaseOrderSerializer,
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_404_NOT_FOUND: "Not found",
        },
        tags=["Purchase Orders"],
    )
    @swagger_auto_schema()
    def acknowledge(self, request, id=None):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.status = "acknowledged"
        purchase_order.save()
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data, status=status.HTTP_200_OK)
