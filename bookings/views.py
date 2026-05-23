from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookingForm
from .email_utils import send_booking_confirmation
# Main booking page

def book_ride(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
           booking = form.save()
           send_booking_confirmation(booking)
           return redirect("booking_success", booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, "booking/form.html", {"form": form})

from django.shortcuts import get_object_or_404
from .models import Booking

def booking_success(request):
    booking_id = request.GET.get("id")
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "booking/success.html", {"booking": booking})

from django.template.loader import render_to_string
from django.http import HttpResponse

def load_time_slots(request):
    selected_date = request.GET.get("date")

    slots = ["08:00", "10:00", "12:00", "14:00", "16:00"]

    html = render_to_string("booking/time_slots.html", {"slots": slots})
    return HttpResponse(html)