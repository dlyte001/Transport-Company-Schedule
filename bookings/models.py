from django.db import models

class Booking(models.Model):
    RIDE_TYPES = [
        ("airport", "Airport Shuttle"),
        ("interstate", "Interstate Trip"),
        ("local", "Local Ride"),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    ride_type = models.CharField(max_length=20, choices=RIDE_TYPES)
    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"