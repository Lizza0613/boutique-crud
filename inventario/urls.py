from django.urls import path
from inventario import views  

urlpatterns = [
    # 1. Página principal
    path('', views.index, name='index'),
    
    # 2. Añadir prenda
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    
    # 3. Editar prenda
    path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # 4. Eliminar prenda
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]