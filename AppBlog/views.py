from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entrada
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppBlog.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView

# Create your views here.
@login_required
def inicio(request):
    blog = Entrada.objects.all()
    return render(request,"AppBlog/inicio.html",{"blog":blog})


def logueate(request):
    return render(request, 'AppBlog/logueate.html')

@login_required
def detalle(request):
    return render(request, "AppBlog/detalle.html")
@login_required
def contactenos(request):
    return render(request, "AppBlog/contactenos.html")
@login_required
def nosotros(request):
    return render(request, "AppBlog/nosotros.html")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu = request.POST['username']
            clave = request.POST['password']

            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppBlog/inicio.html', {'form': form, 'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppBlog/inicio.html', {'form': form, 'mensaje': f"Usuario o contraseña incorrectos"})
        else:
            return render(request, 'AppBlog/login.html', {'form': form, 'mensaje': f"Formulario invalido"})
    else:
        form = AuthenticationForm()
        return render(request, 'AppBlog/login.html', {'form': form})   
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            form.save()
            return render(request, 'AppBlog/inicio.html', {'form': form, 'mensaje': f"Usuario creado: {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'AppBlog/registro.html', {'form': form})

def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        formulario= UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()

            return render (request, "AppBlog/inicio.html")
    else:
        formulario= UserEditForm(instance=usuario)
    return render(request, "AppBlog/editarPerfil.html", {"formulario":formulario, "usuario":usuario.username})

class Error404View(TemplateView):
    template_name = 'AppBlog/detalle.html'