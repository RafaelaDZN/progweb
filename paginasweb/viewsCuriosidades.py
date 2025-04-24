from django.shortcuts import render
from .models import Curiosidade

def lista_curiosidades(request):
    curiosidades = Curiosidade.objects.all()
    return render(request, 'curiosidades/lista.html', {'curiosidades': curiosidades})
