from django.shortcuts import render
from django.shortcuts import redirect
from .models import Producto
from django.contrib import messages

# Create your views here.

def home(request):
    productos= Producto.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, "gestionProducto.html", {"productos":productos})

def registrarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    peso=request.POST['numPeso']
    
    producto=Producto.objects.create(codigo=codigo,nombre=nombre,peso=peso)
    messages.success(request, '¡Productos Registrado!')
    return redirect('/')

def edicionProducto(request,codigo):
    producto=Producto.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto":producto})
    
def editarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    peso=request.POST['numPeso']
    
    producto=Producto.objects.get(codigo=codigo)
    producto.nombre=nombre
    producto.peso=peso
    producto.save()
    
    messages.success(request, '¡Producto Actualizado!')
    
    return redirect('/')

def eliminarProducto(request, codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete()
    
    messages.success(request, '¡Producto Eliminado!')
    
    return redirect('/')