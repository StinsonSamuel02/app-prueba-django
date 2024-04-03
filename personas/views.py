from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm


def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista_personas.html', {'personas': personas})


def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/agregar_persona.html', {'form': form})


def home(request):
    return render(request, 'portfolio/index.html')
