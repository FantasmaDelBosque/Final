from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginView, name='login'),
    path('home/', views.home, name='home'),
    path('home_vendedor/', views.home_vendedor, name='home_vendedor'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_user_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),

    path('agregar-ropa/', views.agregar_ropa, name='agregar_ropa'),
    path('lista-ropa/', views.lista_ropa, name='lista_ropa'),
    path('editar-ropa/<int:ropa_id>/', views.editar_ropa, name='editar_ropa'),


    path('agregar-zapatos/', views.agregar_zapatos, name='agregar_zapatos'),
    path('lista-zapatos/', views.lista_zapatos, name='lista_zapatos'),

    path('agregar-accesorios/', views.agregar_accesorios, name='agregar_accesorios'),
    path('lista-accesorios/', views.lista_accesorios, name='lista_accesorios'),

    path('sobremi/', views.sobremi, name='sobremi')
  

    # Otras URLs de la aplicación accounts si las tienes
]