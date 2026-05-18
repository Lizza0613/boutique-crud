from django.db import models

class Categoria(models.Model):
    # Django crea el campo 'id' (INT) automáticamente
    nombre = models.CharField(max_length=50)       # Tipo VARCHAR
    descripcion = models.CharField(max_length=250) # Tipo VARCHAR
    fecha_creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # Relación: Una categoría tiene muchos productos (Llave foránea)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=100)      # Tipo VARCHAR
    precio = models.IntegerField()                 # Tipo INT
    stock = models.IntegerField()                  # Tipo INT

    def __str__(self):
        return self.nombre