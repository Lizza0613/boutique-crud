from django.apps import AppConfig
from django.db.models.signals import post_migrate

def crear_datos_iniciales(sender, **kwargs):
    """Crea el admin y las categorías de forma segura en Render"""
    from django.contrib.auth import get_user_model
    
    try:
        # 1. Crear el superusuario automático si no existe
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@boutique.com', 'Admin1234')
            print("¡Superusuario creado con éxito!")

        # 2. Obtenemos el modelo 'Categoria' usando el sender de la señal de forma ultra segura
        # Esto evita el error AppRegistryNotReady por completo
        try:
            Categoria = sender.get_model('Categoria')
            
            categorias_fijas = [
                (1, "Blusas"),
                (2, "Vestidos"),
                (3, "Pantalones"),
                (4, "Accesorios"),
                (5, "Otros")
            ]
            
            for id_cat, nombre_cat in categorias_fijas:
                if not Categoria.objects.filter(id=id_cat).exists():
                    Categoria.objects.create(id=id_cat, nombre=nombre_cat)
                    print(f"Categoría '{nombre_cat}' creada con éxito.")
        except LookupError:
            print("Aviso: No se encontró el modelo Categoria en esta app.")

    except Exception as e:
        print(f"Aviso en la carga automática: {e}")


class InventarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario' # Asegúrate de que este sea el nombre exacto de tu carpeta

    def ready(self):
        # Conectamos la señal. 'sender=self' asegura que use esta app específica
        post_migrate.connect(crear_datos_iniciales, sender=self)