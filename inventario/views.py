from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Producto, Categoria

# 1. MOSTRAR PRODUCTOS
def index(request):
    # Si no existen categorías, las creamos con TODOS los campos obligatorios de tu modelo
    if not Categoria.objects.exists():
        hoy = timezone.now().date()  # Obtiene la fecha de hoy (Tipo Date)
        
        Categoria.objects.create(nombre="Blusas", descripcion="Blusas y tops para dama", fecha_creacion=hoy)
        Categoria.objects.create(nombre="Pantalones", descripcion="Pantalones y jeans", fecha_creacion=hoy)
        Categoria.objects.create(nombre="Vestidos", descripcion="Vestidos de noche y casuales", fecha_creacion=hoy)
        Categoria.objects.create(nombre="Accesorios", descripcion="Bolsos, joyería y más", fecha_creacion=hoy)

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'productos': productos, 'categorias': categorias})

# 2. CREAR PRODUCTO
def crear_producto(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        
        Producto.objects.create(
            categoria=categoria,
            nombre=request.POST.get('nombre'),
            precio=request.POST.get('precio'),
            stock=request.POST.get('stock')
        )
    return redirect('index')

# 3. EDITAR PRODUCTO
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        producto.categoria = get_object_or_404(Categoria, id=categoria_id)
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
    return redirect('index')

# 4. ELIMINAR PRODUCTO
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('index')