from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser, User
from django.db import models
from django.conf import settings


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
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    imagen = models.ImageField(upload_to='ropa/')  
     # Campo para relacionar la prenda de ropa con el usuariomanage.py makemigrations
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    # def __str__(self):
    #     return self.nombre

class Zapatos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    imagen = models.ImageField(upload_to='zapatos/') 
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    # def __str__(self):
    #     return self.nombre


class Accesorios(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    imagen = models.ImageField(upload_to='accesorios/')  
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    # def __str__(self):
    #     return self.nombre


class Avatar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
