# Imports
from django.urls import path
from apps.performance.views import HistoricalPerformanceView


# URL patterns
urlpatterns = [
    path(
        "vendors/<int:id>/performance/",
        HistoricalPerformanceView.as_view({"get": "retrieve"}),
        name="api--historical_performance-retrieve",
    )
]
