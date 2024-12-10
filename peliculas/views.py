from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import Pelicula
from .forms import PeliculaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html") 


@login_required
def nosotros(request):
    return render(request, "paginas/nosotros.html") 

def salir(request):
    logout(request)
    return render(request,'paginas/inicio.html')

@login_required
def peliculas(request):
    peliculas = Pelicula.objects.all() 
    return render(request, "peliculas/index.html" , {"peliculas": peliculas})  

def aportar(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None) 
    if formulario.is_valid(): 
        formulario.save()  
        return redirect("peliculas")  
    return render(request, "paginas/aportar.html", {"formulario": formulario}) 

def crear(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None) 
    if formulario.is_valid(): 
        formulario.save()  
        return redirect("peliculas")  
    return render(request, "peliculas/crear.html", {"formulario": formulario}) 

def editar(request):
    return render(request, "peliculas/editar.html")

def eliminar(request, id):
    peliculas = Pelicula.objects.get(id=id)
    peliculas.delete()
    return redirect("peliculas")

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect("peliculas")
    return render(request, "peliculas/editar.html", {'formulario':formulario})
