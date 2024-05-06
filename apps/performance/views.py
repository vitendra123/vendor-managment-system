# Imports
from apps.performance.models import HistoricalPerformance
from apps.performance.serializers import HistoricalPerformanceSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# HistoricalPerformanceView
class HistoricalPerformanceView(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HistoricalPerformanceSerializer

    @swagger_auto_schema(
        operation_id="api--historical_performance-retrieve",
        operation_description="Retrieve historical performance for a vendor",
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
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="Vendor ID",
            ),
        ],
        responses={
            status.HTTP_200_OK: HistoricalPerformanceSerializer,
            status.HTTP_404_NOT_FOUND: "Not found",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Performance"],
    )
    def retrieve(self, request, id):
        historical_performance = HistoricalPerformance.objects.get(vendor_id=id)
        serializer = HistoricalPerformanceSerializer(historical_performance)
        return Response(serializer.data)
