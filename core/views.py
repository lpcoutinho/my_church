from django.shortcuts import render

from .models import Congregation


def home(request):
    congregation = Congregation.objects.first()  # Buscar a primeira congregação
    return render(request, "home.html", {"congregation": congregation})


def contact_page(request):
    return render(request, "contact.html")
