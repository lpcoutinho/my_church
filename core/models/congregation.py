from django.db import models


class Congregation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Congregação"
        verbose_name_plural = "Congregações"
