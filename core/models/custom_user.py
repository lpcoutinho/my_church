from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

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
