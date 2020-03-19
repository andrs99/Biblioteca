from django.db import models

# Create your models here.

class Clientes(models.Model):
    cliente_nombre=models.CharField(max_length=50)
    cliente_email=models.EmailField()
    cliente_direccion=models.CharField(max_length=50)
    cliente_telefono=models.CharField(max_length=10)

class Articulos(models.Model):
    articulo_nombre=models.CharField(max_length=30)
    articulo_seccion=models.CharField(max_length=30)
    articulo_precio=models.IntegerField()

class Pedidos(models.Model):
    pedido_numero=models.IntegerField()
    pedido_fecha=models.DateField()
    pedido_entregado=models.BooleanField()
