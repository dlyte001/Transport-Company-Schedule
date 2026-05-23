from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_ride, name="book_ride"),
    path("success/", views.booking_success, name="booking_success"),
    path("htmx/time-slots/", views.load_time_slots, name="load_time_slots"),
]