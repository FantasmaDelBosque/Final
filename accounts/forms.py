from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
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


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("username", "email", "password1", "password2")

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("¡Las contraseñas no coinciden!")
        return password2
    


