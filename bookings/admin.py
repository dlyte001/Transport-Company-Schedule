from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "ride_type", "date", "time", "created_at")
    list_filter = ("ride_type", "date")
    search_fields = ("name", "phone", "pickup_location", "dropoff_location")
    ordering = ("-created_at",)