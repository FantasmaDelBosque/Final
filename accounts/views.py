from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Ropa, Zapatos, Accesorios
from .forms import CustomUserCreationForm,  RopaForm, ZapatosForm, AccesoriosForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# from accounts.models import CustomUser


def home(request):
    return render(request, "home.html")

def home_vendedor (request):
    return render(request, "home_vendedor.html")


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid():

            data = form.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(request, user)
                return render(request, "home_vendedor.html", {"mensaje": f"Bienvenidx {usuario}!"})
           
        return render(request, "home.html", {"mensaje": f"Datos incorrectos"})

    else:
        form = AuthenticationForm() 
        return render(request, "login.html", {"form": form})       




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('profile')
        else:
            messages.error(request, 'El formulario es inválido.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
     

def logoutView(request):
    logout(request)

    messages.success(request, 'Cierre de sesión exitoso.')

    return redirect('home')



@login_required
def agregar_ropa(request):
    if request.method == 'POST':
        form = RopaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_ropa')  # Redirigir a la lista de Ropa o a donde desees
    else:
        form = RopaForm()
    
    return render(request, 'agregar_ropa.html', {'form': form})

def lista_ropa(request):
    elementos_ropa = Ropa.objects.all()# pylint: disable=no-member
    return render(request, 'lista_ropa.html', {'ropa': elementos_ropa})

@login_required
def agregar_zapatos(request):
    if request.method == 'POST':
        form = ZapatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_zapatos')  # Redirigir a la lista de Zapatos o a donde desees
    else:
        form = ZapatosForm()
    
    return render(request, 'agregar_zapatos.html', {'form': form})


def lista_zapatos(request):
    zapatos = Zapatos.objects.all()# pylint: disable=no-member
    return render(request, 'lista_zapatos.html', {'zapatos': zapatos})


@login_required
def agregar_accesorios(request):
    if request.method == 'POST':
        form = AccesoriosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_accesorios')  # Redirigir a la lista de Accesorios o a donde desees
    else:
        form = AccesoriosForm()
    
    return render(request, 'agregar_accesorios.html', {'form': form})

def lista_accesorios(request):
    accesorios = Accesorios.objects.all()# pylint: disable=no-member
    return render(request, 'lista_accesorios.html', {'accesorios': accesorios})



def sobremi(request):
    return render(request, 'sobremi.html')

from django.shortcuts import render

def user_profile(request):
    # Aquí puedes agregar la lógica para mostrar el perfil del usuario
    return render(request, 'profile.html')  # Asumiendo que tienes una plantilla llamada 'profile.html'
