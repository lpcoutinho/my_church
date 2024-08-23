from django.conf import settings
from django.db import models


class Donation(models.Model):
    # Tipos de arrecadação
    DONATION_TYPE_CHOICES = [
        ("DZ", "Dízimo"),
        ("OF", "Oferta"),
        ("DO", "Doação"),
    ]

    # Métodos de pagamento
    PAYMENT_METHOD_CHOICES = [
        ("DIN", "Dinheiro"),
        ("CC", "Cartão de Crédito"),
        ("CD", "Cartão de Débito"),
        ("PIX", "Pix"),
        ("BTC", "Bitcoin"),
    ]

    donation_type = models.CharField(
        max_length=2,
        choices=DONATION_TYPE_CHOICES,
        help_text="Selecione o tipo de arrecadação.",
    )
    payment_method = models.CharField(
        max_length=5,
        choices=PAYMENT_METHOD_CHOICES,
        help_text="Selecione o método de pagamento.",
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Digite o valor da doação."
    )
    donation_date = models.DateTimeField(
        auto_now_add=True, help_text="Data e hora da doação."
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Usuário que fez a doação. Deixe em branco para doações anônimas.",
    )
    anonymous = models.BooleanField(
        default=False, help_text="Marque se a doação foi anônima."
    )

    # Campos para informações do pagamento
    payment_status = models.CharField(
        max_length=50, null=True, blank=True, help_text="Status do pagamento."
    )
    payment_id = models.CharField(
        max_length=100, null=True, blank=True, help_text="ID do pagamento."
    )
    qr_code = models.TextField(
        null=True, blank=True, help_text="Código QR para pagamento."
    )
    qr_code_base64 = models.TextField(
        null=True, blank=True, help_text="Código QR em Base64."
    )
    ticket_url = models.URLField(
        max_length=255, null=True, blank=True, help_text="URL do ticket de pagamento."
    )
    date_created = models.DateTimeField(
        null=True, blank=True, help_text="Data de criação do pagamento."
    )
    last_updated = models.DateTimeField(
        null=True, blank=True, help_text="Última atualização do pagamento."
    )

    def __str__(self):
        return (
            f"{self.get_donation_type_display()} - {self.amount} ({self.donation_date})"
        )

    class Meta:
        verbose_name = "Doação"
        verbose_name_plural = "Doações"
        ordering = ["-donation_date"]
