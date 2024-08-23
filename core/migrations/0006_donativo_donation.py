# Generated by Django 4.2.15 on 2024-08-23 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customuser_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_type', models.CharField(choices=[('DZ', 'Dízimo'), ('OF', 'Oferta'), ('DO', 'Doação')], help_text='Selecione o tipo de arrecadação.', max_length=2)),
                ('payment_method', models.CharField(choices=[('DIN', 'Dinheiro'), ('CC', 'Cartão de Crédito'), ('CD', 'Cartão de Débito'), ('PIX', 'Pix'), ('BTC', 'Bitcoin')], help_text='Selecione o método de pagamento.', max_length=5)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Digite o valor da doação.', max_digits=10)),
                ('donation_date', models.DateTimeField(auto_now_add=True, help_text='Data e hora da doação.')),
                ('anonymous', models.BooleanField(default=False, help_text='Marque se a doação foi anônima.')),
                ('user', models.ForeignKey(blank=True, help_text='Usuário que fez a doação. Deixe em branco para doações anônimas.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doação',
                'verbose_name_plural': 'Doações',
                'ordering': ['-donation_date'],
            },
        ),
    ]
