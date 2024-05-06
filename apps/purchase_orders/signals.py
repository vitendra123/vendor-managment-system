from django.db import models
from django.db.models import Avg, ExpressionWrapper, F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone
from apps.purchase_orders.models import PurchaseOrder
from apps.performance.models import HistoricalPerformance


# Signals to update performance metrics
@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    vendor = instance.vendor

    # Get or create historical performance record
    historical_performance, _ = HistoricalPerformance.objects.get_or_create(
        vendor=vendor,
        defaults={
            "date": timezone.now(),
            "on_time_delivery_rate": 0,
            "quality_rating_avg": 0,
            "average_response_time": int(timedelta().total_seconds()),
            "fulfillment_rate": 0,
        },
    )

    # Update On-Time Delivery Rate
    if instance.status == "completed":
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status="completed")
        on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now())
        on_time_delivery_rate = (
            on_time_deliveries.count() / completed_pos.count()
            if completed_pos.exists()
            else 0
        )
        vendor.on_time_delivery_rate = on_time_delivery_rate
        historical_performance.on_time_delivery_rate = on_time_delivery_rate

    # Update Quality Rating Average
    if instance.quality_rating is not None:
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status="completed")
        quality_ratings = completed_pos.exclude(quality_rating=None).aggregate(
            avg_quality_rating=Avg("quality_rating")
        )
        vendor.quality_rating_avg = quality_ratings["avg_quality_rating"]
        historical_performance.quality_rating_avg = vendor.quality_rating_avg

    # Save changes
    vendor.save()
    historical_performance.save()


# Signals to update performance metrics
@receiver(post_save, sender=PurchaseOrder)
def calculate_response_time(sender, instance, created, **kwargs):
    vendor = instance.vendor

    # Get or create historical performance record
    historical_performance, _ = HistoricalPerformance.objects.get_or_create(
        vendor=vendor,
        defaults={
            "date": timezone.now(),
            "on_time_delivery_rate": 0,
            "quality_rating_avg": 0,
            "average_response_time": int(timedelta().total_seconds()),
            "fulfillment_rate": 0,
        },
    )

    # Update Average Response Time
    if instance.status == "acknowledged":
        ack_pos = PurchaseOrder.objects.filter(vendor=vendor, status="acknowledged")
        response_times = ack_pos.exclude(acknowledgment_date=None).annotate(
            response_time=ExpressionWrapper(
                F("acknowledgment_date") - F("issue_date"),
                output_field=models.DurationField(),
            )
        )
        avg_response_time = response_times.aggregate(
            avg_response_time=Avg("response_time")
        )
        vendor.average_response_time = int(
            avg_response_time["avg_response_time"].total_seconds()
        )
        historical_performance.average_response_time = vendor.average_response_time

    # Save changes
    vendor.save()
    historical_performance.save()


# Signals to update performance metrics
@receiver(post_save, sender=PurchaseOrder)
@receiver(pre_delete, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    vendor = instance.vendor

    # Calculate Fulfillment Rate
    issued_pos = PurchaseOrder.objects.filter(vendor=vendor)
    total_pos_count = issued_pos.count()
    successful_fulfillments_count = issued_pos.filter(
        status="completed", delivery_date__lte=timezone.now()
    ).count()

    fulfillment_rate = (
        successful_fulfillments_count / total_pos_count if total_pos_count > 0 else 0
    )

    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
