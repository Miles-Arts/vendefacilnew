from django.urls import path
from . import views
from .views import home, productos, exit
from .views import exit
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='prueba'), name='exit'), # Redirige a la home pública al salir
    #path('logout/', exit, name='exit'),
    
    #Rutas Publicas
    path('', views.home),
    path('home/', views.home, name='home'),
    path('prueba/', views.prueba, name='prueba'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    
    # Rutas del dashboard de productos (protegidas)
    #path('registrarProducto/', views.registrarProducto),
    #path('home/edicionProducto/<codigo>', views.edicionProducto),
    #path('home/editarProducto/', views.editarProducto),
    #path('home/eliminarProducto/<codigo>', views.eliminarProducto),
    
    path('productos/registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('editarProducto/', views.registrarProducto, name='gestionProducto'),
    path('edicionProducto/<str:codigo>/', views.edicionProducto, name='edicionProducto'), # Asegúrate que el tipo de 'codigo' coincida con tu modelo
    #path('gestionProducto/', views.editarProducto, name='edicionProducto'),
    path('eliminarProducto/<str:codigo>/', views.eliminarProducto, name='eliminarProducto'), # Asegúrate que el tipo de 'codigo' coincida
    
]

