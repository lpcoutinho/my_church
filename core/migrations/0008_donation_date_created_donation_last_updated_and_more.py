# Generated by Django 4.2.15 on 2024-08-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_delete_donativo_alter_congregation_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="date_created",
            field=models.DateTimeField(
                blank=True, help_text="Data de criação do pagamento.", null=True
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="last_updated",
            field=models.DateTimeField(
                blank=True, help_text="Última atualização do pagamento.", null=True
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="payment_id",
            field=models.CharField(
                blank=True, help_text="ID do pagamento.", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="payment_status",
            field=models.CharField(
                blank=True, help_text="Status do pagamento.", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="qr_code",
            field=models.TextField(
                blank=True, help_text="Código QR para pagamento.", null=True
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="qr_code_base64",
            field=models.TextField(
                blank=True, help_text="Código QR em Base64.", null=True
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="ticket_url",
            field=models.URLField(
                blank=True,
                help_text="URL do ticket de pagamento.",
                max_length=255,
                null=True,
            ),
        ),
    ]
