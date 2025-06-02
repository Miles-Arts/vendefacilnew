from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    productos= Producto.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, "gestionProducto.html", {"productos":productos})

def inicio(request):
    return render(request, "inicio.html")

def registrarProducto(request):
    if request.method != 'POST':
        return redirect('/home')
    nombre = request.POST['txtNombre']
    peso = request.POST['numPeso']
    caracteristicas = request.POST['txtCaracteristicas']
    # Nuevo campo precio
    precio = request.POST.get('txtPrecio', '0')
    foto = request.FILES.get('foto')

    # Validaciones
    if not foto:
        messages.error(request, 'Debe subir una imagen.')
        return redirect('/home')
    if foto.size > 20 * 1024 * 1024:
        messages.error(request, 'La imagen no debe superar los 20 MB.')
        return redirect('/home')
    if foto.content_type not in ['image/jpeg', 'image/png']:
        messages.error(request, 'Solo se permiten imágenes JPG o PNG.')
        return redirect('/home')
    if len(caracteristicas) > 300:
        messages.error(request, 'Las características no pueden superar 300 caracteres.')
        return redirect('/home')

    producto = Producto.objects.create(
        nombre=nombre,
        peso=peso,
        caracteristicas=caracteristicas,
        foto=foto,
        precio=precio
    )
    messages.success(request, '¡Producto Registrado!')
    return redirect('home')
    #return redirect(request, "gestionProducto.html", {"producto":producto})
    #return render(request, "edicionProducto.html", {"producto":producto})

# def edicionProducto(request,codigo):
#     producto=Producto.objects.get(codigo=codigo)
#     return render(request, "edicionProducto.html", {"producto":producto})
    
def edicionProducto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    if request.method == 'POST':
        # 1) Actualizar campos
        producto.nombre = request.POST.get('txtNombre', producto.nombre)
        producto.peso = request.POST.get('numPeso', producto.peso)
        producto.caracteristicas = request.POST.get('txtCaracteristicas', producto.caracteristicas)
        # Actualizar precio solo si se proporciona un valor
        price_str = request.POST.get('txtPrecio', '').strip()
        if price_str:
            try:
                producto.precio = price_str
            except (ValueError, TypeError):
                pass
        # 2) Si subieron foto, reemplazarla
        nueva_foto = request.FILES.get('foto')
        if nueva_foto:
            producto.foto = nueva_foto
        # 3) Guardar y redirigir
        producto.save()
        messages.success(request, '¡Producto actualizado correctamente!')
        return redirect('home')
    # GET: Mostrar formulario
    return render(request, 'edicionProducto.html', {'producto': producto})    
    
def editarProducto(request):
    if request.method != 'POST':
        return redirect('/home')
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    peso = request.POST['numPeso']
    caracteristicas = request.POST.get('txtCaracteristicas', '')
    # Nuevo campo precio
    precio = request.POST.get('txtPrecio', None)
    #precio = request.POST['txtPrecio']
    foto = request.FILES.get('foto')

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.peso = peso
    if caracteristicas:
        if len(caracteristicas) > 300:
            messages.error(request, 'Las características no pueden superar 300 caracteres.')
            return redirect(f'/edicionProducto/{codigo}')
        producto.caracteristicas = caracteristicas
    # Actualizar precio solo si se proporciona un valor válido
    price_str = request.POST.get('txtPrecio', '').strip()
    if price_str:
        try:
            producto.precio = price_str
        except (ValueError, TypeError):
            pass
    # Procesar foto si fue actualizada
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
    return redirect('/home')

def eliminarProducto(request, codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete()
    
    messages.success(request, '¡Producto Eliminado!')
    
    return redirect('/home')

@login_required
def login(request):
    return render(request, "login.html")

def inicios(request):
    return render(request, "home.html")

def inicio(request):
    return render(request, "inicio.html")

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
    return redirect('productos')


def register(request):
    data = { 
            'form':CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('login')
    
    return render(request, 'registration/register.html',data)