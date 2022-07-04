from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"Nombre: {self.nombre}  -  Precio: {self.precio}"

class Datos_productos(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    fecha_fab = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre}  -  Marca: {self.marca}  -  Fecha Fabricacion: {self.fecha_fab}"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}  -  Teléfono: {self.telefono}"

class Avatar(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True , blank=True)       
    