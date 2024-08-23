from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Donation


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["donation_type", "payment_method", "amount"]
        labels = {
            "donation_type": "Donation type",
            "payment_method": "Payment method",
            "amount": "Amount",
        }
        help_texts = {
            "donation_type": "Select the type of donation.",
            "payment_method": "Select the payment method.",
            "amount": "Enter the donation amount.",
        }

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        # Limitar as opções de método de pagamento para apenas Pix
        self.fields["payment_method"].choices = [
            ("PIX", "Pix"),
        ]
