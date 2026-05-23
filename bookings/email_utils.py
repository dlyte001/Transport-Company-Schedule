from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_booking_confirmation(booking):
    subject = "Your Ride Booking Confirmation"
    recipient = [booking.phone + "@sms.gateway"] if False else []  # placeholder

    message = render_to_string("booking/email_confirmation.txt", {
        "booking": booking,
    })

    send_mail(
        subject,
        message,
        None,  # uses DEFAULT_FROM_EMAIL
        [booking.email] if hasattr(booking, "email") else ["test@example.com"],
        fail_silently=False,
    )