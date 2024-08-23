import os

from django.contrib.auth import login
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from .forms import CustomUserCreationForm, DonationForm
from .models import Congregation, Donation
from .payment_processor import PaymentProcessor

load_dotenv()

MP_TOKEN = os.getenv("MP_TOKEN")


def home(request):
    congregation = Congregation.objects.first()
    return render(request, "home.html", {"congregation": congregation})


def contact_page(request):
    return render(request, "contact.html")


def signup_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def donation_page(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated:
                donation.user = request.user
            else:
                donation.anonymous = True

            payment_processor = PaymentProcessor(access_token=MP_TOKEN)

            # Converte o valor do amount para float
            amount = float(donation.amount)

            # Cria o pagamento via Mercado Pago
            payment_info = payment_processor.create_payment(
                email=donation.user.email if donation.user else "anon@example.com",
                amount=amount,
                payment_method=donation.payment_method,
            )

            donation.payment_status = "pending"
            donation.payment_id = payment_info.get("id")
            donation.qr_code = payment_info.get("qr_code")
            donation.qr_code_base64 = payment_info.get("qr_code_base64")
            donation.ticket_url = payment_info.get("ticket_url")
            donation.date_created = payment_info.get("date_created")
            donation.last_updated = payment_info.get("last_updated")
            donation.save()

            return redirect("donation_confirmation", donation_id=donation.id)
    else:
        form = DonationForm()

    return render(request, "donation.html", {"form": form})


def donation_confirmation(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    return render(request, "donation_confirmation.html", {"donation": donation})
