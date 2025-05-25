from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas públicas
    path('', views.pagina_principal, name='pagina_principal'), # Tu home pública
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos_lista'), # Vista pública de lista de productos
    path('disponibles/', views.disponibles, name='disponibles'), # Si es diferente a productos_lista

    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='prueba'), name='logout'), # Redirige a la home pública al salir

    # Rutas del dashboard de productos (protegidas)
    path('dashboard/', views.dashboard_productos, name='dashboard_productos'),
    path('dashboard/registrar/', views.registrarProducto, name='registrar_producto'),
    path('dashboard/edicion/<str:codigo>/', views.edicionProducto, name='edicion_producto'), # Asegúrate que el tipo de 'codigo' coincida con tu modelo
    path('dashboard/editar/', views.editarProducto, name='editar_producto'),
    path('dashboard/eliminar/<str:codigo>/', views.eliminarProducto, name='eliminar_producto'), # Asegúrate que el tipo de 'codigo' coincida
]