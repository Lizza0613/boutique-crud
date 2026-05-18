from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()

try:
    # 1. Crear el superusuario automático si no existe
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@boutique.com', 'Admin1234')
        print("¡Superusuario creado con éxito!")

    # 2. Crear las 5 categorías fijas automáticamente con sus IDs correctos
    # Buscamos el modelo Categoria de forma segura para evitar errores de carga
    Categoria = apps.get_model('inventario', 'Categoria') # Cambia 'inventario' si tu app se llama distinto
    
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

except Exception as e:
    print(f"Aviso en la carga automática: {e}")