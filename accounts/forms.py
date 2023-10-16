from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser, Ropa, Zapatos, Accesorios


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta: 
        model = CustomUser


class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']

class ZapatosForm(forms.ModelForm):
    class Meta:
        model = Zapatos
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']

class AccesoriosForm(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']

