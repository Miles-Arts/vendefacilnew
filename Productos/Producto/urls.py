from django.urls import path
from . import views
from .views import home, productos

urlpatterns = [
    path('', views.home),
    path('registrarProducto/', views.registrarProducto),
    path('home/edicionProducto/<codigo>', views.edicionProducto),
    path('home/editarProducto/', views.editarProducto),
    path('home/eliminarProducto/<codigo>', views.eliminarProducto),
    #Otras secciones
    path('home/', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    
]

