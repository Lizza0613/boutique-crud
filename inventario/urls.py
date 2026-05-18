from django.urls import path
from inventario import views  

urlpatterns = [
    # 1. Página principal conectada a la función index
    path('', views.index, name='index'),
    
    # 2. Ruta para Añadir prenda
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    
    # 3. Ruta para Editar (Usa <int:id> igual que la vista)
    path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # 4. Ruta para Eliminar (Usa <int:id> igual que la vista)
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]