from django.contrib import admin
from django.urls import path, include  # <-- ¡AQUÍ ESTÁ EL TRUCO! Faltaba importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conecta las rutas de tu aplicación de ropa
    path('', include('inventario.urls')), 
]