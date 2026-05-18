from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria

# 1. MOSTRAR PRODUCTOS
def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    # Cambia la línea de abajo para que quede solo 'index.html'
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
    return redirect('lista_productos')

# 3. EDITAR PRODUCTO
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        producto.categoria = get_object_or_404(Categoria, id=categoria_id)
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
    return redirect('lista_productos')

# 4. ELIMINAR PRODUCTO
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')