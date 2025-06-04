from django.urls import path
from . import views
from .views import home, productos, exit, register
from .views import exit
from .views import register
from django.contrib.auth import views as auth_views
from Productos.Producto.views import register

urlpatterns = [
    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='productos'), name='exit'), # Redirige a la home pública al salir 
    path('register/', views.register, name='register'),
    
    #Rutas Publicas
    path('', views.inicio),
    path('home/', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    
    #Rutas Privadas
    path('productos/registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('edicionProducto/<str:codigo>/', views.edicionProducto, name='edicionProducto'),
    path('editarProducto/', views.registrarProducto, name='gestionProducto'),
    path('eliminarProducto/<str:codigo>/', views.eliminarProducto, name='eliminarProducto'), # Asegúrate que el tipo de 'codigo' coincida
    
]

