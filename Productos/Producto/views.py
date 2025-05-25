from django.shortcuts import render
from django.shortcuts import redirect
from .models import Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    productos= Producto.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, "gestionProducto.html", {"productos":productos})

def registrarProducto(request):
    if request.method != 'POST':
        return redirect('/')
    nombre = request.POST['txtNombre']
    peso = request.POST['numPeso']
    caracteristicas = request.POST['txtCaracteristicas']
    foto = request.FILES.get('foto')

    # Validaciones
    if not foto:
        messages.error(request, 'Debe subir una imagen.')
        return redirect('/')
    if foto.size > 20 * 1024 * 1024:
        messages.error(request, 'La imagen no debe superar los 20 MB.')
        return redirect('/')
    if foto.content_type not in ['image/jpeg', 'image/png']:
        messages.error(request, 'Solo se permiten imágenes JPG o PNG.')
        return redirect('/')
    if len(caracteristicas) > 300:
        messages.error(request, 'Las características no pueden superar 300 caracteres.')
        return redirect('/')

    producto = Producto.objects.create(
        nombre=nombre,
        peso=peso,
        caracteristicas=caracteristicas,
        foto=foto
    )
    messages.success(request, '¡Producto Registrado!')
    return redirect('/')

def edicionProducto(request,codigo):
    producto=Producto.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto":producto})
    
def editarProducto(request):
    if request.method != 'POST':
        return redirect('/')
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    peso = request.POST['numPeso']
    caracteristicas = request.POST.get('txtCaracteristicas', '')
    foto = request.FILES.get('foto')

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.peso = peso
    if caracteristicas:
        if len(caracteristicas) > 300:
            messages.error(request, 'Las características no pueden superar 300 caracteres.')
            return redirect(f'/edicionProducto/{codigo}')
        producto.caracteristicas = caracteristicas
    if foto:
        if foto.size > 20 * 1024 * 1024:
            messages.error(request, 'La imagen no debe superar los 20 MB.')
            return redirect(f'/edicionProducto/{codigo}')
        if foto.content_type not in ['image/jpeg', 'image/png']:
            messages.error(request, 'Solo se permiten imágenes JPG o PNG.')
            return redirect(f'/edicionProducto/{codigo}')
        producto.foto = foto
    producto.save()
    messages.success(request, '¡Producto Actualizado!')
    return redirect('/')

def eliminarProducto(request, codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete()
    
    messages.success(request, '¡Producto Eliminado!')
    
    return redirect('/')

@login_required
def login(request):
    return render(request, "login.html")

def inicio(request):
    return render(request, "home.html")

def prueba(request):
    return render(request, "prueba.html")

def contacto(request):
    return render(request, "contacto.html")

def nosotros(request):
    return render(request, "nosotros.html")

#def gestionProducto(request):
    #return render(request, "gestionProducto.html")

def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})

def disponibles(request):
    productos = Producto.objects.all()
    return render(request, "disponibles.html", {"productos": productos})

def exit(request):
    logout(request)
    return redirect('home')