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
    
    return redirect('/')

def eliminarProducto(request, codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete()
    
    return redirect('/')