from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Ropa, Zapatos, Accesorios
from .forms import CustomUserCreationForm,  RopaForm, ZapatosForm, AccesoriosForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
# from accounts.models import CustomUser
from django.http import HttpResponseForbidden



def home(request):
    return render(request, "home.html")

def home_vendedor (request):
    return render(request, "home_vendedor.html")

def profile (request):
    return render(request, "profile.html")


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
            return redirect('login')
        else:
            messages.error(request, 'El formulario es inválido.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})


@login_required
def edit_user_profile(request):

    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)

        if form.is_valid():

            data = form.cleaned_data
            usuario.username = data["username"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(request, "profile.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(request, "edit_profile.html", {"form": form})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "edit_profile.html", {"form": form})

     
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





@login_required
def editar_ropa(request, ropa_id):
    ropa = Ropa.objects.get(id=ropa_id)# pylint: disable=no-member

    if request.user != ropa.usuario:
        return HttpResponseForbidden("No tienes permiso para editar esta prenda de ropa")

    if request.method == 'POST':
        form = RopaForm(request.POST, request.FILES, instance=ropa)
        if 'delete' in request.POST:
            ropa.delete() 
            return redirect('lista_ropa')  
        elif form.is_valid():
            form.save()
            return redirect('lista_ropa')  
        form = RopaForm(instance=ropa)

    return render(request, 'editar_ropa.html', {'form': form, 'ropa': ropa})



@login_required
def editar_zapatos(request, zapatos_id):
    zapatos = Zapatos.objects.get(id=zapatos_id)# pylint: disable=no-member

    if request.user != zapatos.usuario:

        return HttpResponseForbidden("No tienes permiso para editar estos zapatos")

    if request.method == 'POST':
        form = ZapatosForm(request.POST, request.FILES, instance=zapatos)
        if 'delete' in request.POST:
            zapatos.delete() 
            return redirect('lista_zapatos')  
        elif form.is_valid():
            form.save()
            return redirect('lista_zapatos')  
        form = ZapatosForm(instance=zapatos)

    return render(request, 'editar_zapatos.html', {'form': form, 'zapatos': zapatos})



@login_required
def editar_accesorios(request, accesorios_id):
    accesorios = Accesorios.objects.get(id=accesorios_id)# pylint: disable=no-member

    if request.user != accesorios.usuario:

        return HttpResponseForbidden("No tienes permiso para editar estos accesorios")

    if request.method == 'POST':
        form = AccesoriosForm(request.POST, request.FILES, instance=accesorios)
        if 'delete' in request.POST:
            accesorios.delete() 
            return redirect('lista_accesorios')  
        elif form.is_valid():
            form.save()
            return redirect('lista_accesorios')  
        form = AccesoriosForm(instance=accesorios)

    return render(request, 'editar_accesorios.html', {'form': form, 'accesorios': accesorios})
