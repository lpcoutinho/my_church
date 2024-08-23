from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models


class CustomUser(AbstractUser):
    CATEGORY_CHOICES = [
        ('F', 'Fiel'),
        ('P', 'Pastor'),
        ('CL', 'Colaborador'),
        ('M', 'Missionário'),
        ('PR', 'Presbítero'),        
    ]
    
    DEPARTMENT_CHOICES = [
        ('T', 'Tesouraria'),
        ('ADM', 'Administração'),
        ('MAN', 'Manutenção'),
        ('MKT', 'Marketing'),
    ]

    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        null=True, 
        default='F',
        help_text='Selecione a categoria do usuário.'
    )
    
    department = models.CharField(
        max_length=3,
        choices=DEPARTMENT_CHOICES,
        null=True, 
        blank=True,
        default=None,
        help_text='Selecione o departamento.'
    )

    congregations = models.ManyToManyField('Congregation', blank=True)

    def clean(self):
        if self.category != 'CL':
            self.department = None 
        elif self.category == 'CL' and not self.department:
            raise ValidationError('Colaboradores devem fazer parte um departamento.')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Congregation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Congregação'
        verbose_name_plural = 'Congregações'
    
class Donation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Donation(models.Model):
    # Tipos de arrecadação
    DONATION_TYPE_CHOICES = [
        ('DZ', 'Dízimo'),
        ('OF', 'Oferta'),
        ('DO', 'Doação'),
    ]

    # Métodos de pagamento
    PAYMENT_METHOD_CHOICES = [
        ('DIN', 'Dinheiro'),
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('PIX', 'Pix'),
        ('BTC', 'Bitcoin'),
    ]

    # Definição dos campos
    donation_type = models.CharField(
        max_length=2,
        choices=DONATION_TYPE_CHOICES,
        help_text='Selecione o tipo de arrecadação.'
    )
    payment_method = models.CharField(
        max_length=5,
        choices=PAYMENT_METHOD_CHOICES,
        help_text='Selecione o método de pagamento.'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Digite o valor da doação.'
    )
    donation_date = models.DateTimeField(auto_now_add=True, help_text='Data e hora da doação.')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        help_text='Usuário que fez a doação. Deixe em branco para doações anônimas.'
    )
    anonymous = models.BooleanField(default=False, help_text='Marque se a doação foi anônima.')

    def __str__(self):
        return f'{self.get_donation_type_display()} - {self.amount} ({self.donation_date})'

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'
        ordering = ['-donation_date']
