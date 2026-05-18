from django.contrib import admin
from django.urls import path, include # <-- Asegúrate de que tenga importado 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')), # <-- Esto conecta tu archivo de arriba con el proyecto
]