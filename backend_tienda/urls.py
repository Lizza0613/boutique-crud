from django.urls import path
from . import views  # Importa las vistas de tu aplicación de inventario

urlpatterns = [
    # 1. Página principal: Muestra el formulario y el closet virtual con la lista de prendas
    path('', views.index, name='index'),
    
    # 2. Ruta para Añadir una nueva prenda (Acción del Formulario Rosa)
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    
    # 3. Ruta para Editar/Guardar cambios en línea (Acción de la Tabla Lavanda)
    # <int:pk> o <int:id> pasa el número de ID del producto que se va a actualizar
    path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # 4. Ruta para Eliminar una prenda (Acción del botón Borrar)
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]