from django.contrib import admin
from django.urls import path
from inventario import views  # Asegúrate de importar tus vistas

urlpatterns = [
    path('admin/', admin.site.get_urls() if hasattr(admin.site, 'get_urls') else admin.site.urls),
    # Esta línea es la clave: al dejar las comillas vacías '', le dices que sea la página de inicio
    path('', views.lista_productos, name='lista_productos'),
    
    # Aquí abajo debes tener tus otras rutas del CRUD, por ejemplo:
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]