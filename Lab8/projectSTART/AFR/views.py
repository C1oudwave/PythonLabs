from django.shortcuts import render

from .models import Orendary, Primischennya, Orenda


def index(request):
    orendaries = Orendary.objects.all()
    primischennyas = Primischennya.objects.all()
    orendas = Orenda.objects.all()

    context = {
        'orendaries': orendaries,
        'primischennyas': primischennyas,
        'orendas': orendas,
    }

    return render(request, 'AFR/first.html', context)
