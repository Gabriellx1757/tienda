from django.shortcuts import render, redirect
from .forms import ReptilForm, AveForm, AnfibioForm, BuscarMascotaForm
from .models import Reptil, Ave, Anfibio

def home(request):
    return render(request, 'home.html')

def agregar_mascota(request, especie):
    form = None
    if especie == 'Reptil':
        form = ReptilForm(request.POST or None)
    elif especie == 'Ave':
        form = AveForm(request.POST or None)
    elif especie == 'Anfibio':
        form = AnfibioForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'agregar_mascota.html', {'form': form, 'especie': especie})

def buscar_mascota(request):
    form = BuscarMascotaForm(request.POST or None)
    mascotas = []
    
    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data['nombre']
        especie = form.cleaned_data['especie']
        
        if especie == 'Reptil':
            mascotas = Reptil.objects.filter(nombre__icontains=nombre)
        elif especie == 'Ave':
            mascotas = Ave.objects.filter(nombre__icontains=nombre)
        elif especie == 'Anfibio':
            mascotas = Anfibio.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_mascota.html', {'form': form, 'mascotas': mascotas})
