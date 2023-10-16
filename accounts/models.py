from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models



class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Agregar el campo de contraseña
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    # def __str__(self):
    #     return self.username

class Ropa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='ropa/')  # Asegúrate de configurar correctamente la ruta de carga de imágenes



class Zapatos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='zapatos/')  # Asegúrate de configurar correctamente la ruta de carga de imágenes

    # def __str__(self):
    #     return self.nombre


class Accesorios(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el precio
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='accesorios/')  # Asegúrate de configurar correctamente la ruta de carga de imágenes

    # def __str__(self):
    #     return self.nombre
