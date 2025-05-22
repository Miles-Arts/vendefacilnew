from django.shortcuts import render
from django.shortcuts import redirect
from .models import Producto

# Create your views here.

def home(request):
    productos= Producto.objects.all()
    return render(request, "gestionProducto.html", {"productos":productos})

def registrarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    peso=request.POST['numPeso']
    
    producto=Producto.objects.create(codigo=codigo,nombre=nombre,peso=peso)
    
    return redirect('/')