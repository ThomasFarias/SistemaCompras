from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
Cliente = get_user_model()


class Tienda(models.Model):
	codigo_tienda=models.AutoField(primary_key=True)
	nombre_tienda=models.CharField(max_length=30)
	nombre_sucursal=models.CharField(max_length=30,null=True, blank=True)
	direccion=models.CharField(max_length=40)	
	region=models.CharField(max_length=20)
	ciudad=models.CharField(max_length=20)
	estado=models.BooleanField(default=False)

class Lista(models.Model):
	codigo_lista=models.AutoField(primary_key=True)
	nombre_lista=models.CharField(max_length=30)
	codigo_usuario=models.ForeignKey(Cliente,on_delete=models.CASCADE)


class Producto(models.Model):
	codigo_prod=models.AutoField(primary_key=True)
	nombre_producto=models.CharField(max_length=30,null=False)
	costo_presupuestado=models.IntegerField(null=True)
	costo_real=models.IntegerField(null=True)    
	notas=models.CharField(max_length=30,null=True)
	tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE,null=True)
	codigo_lista=models.ForeignKey(Lista,on_delete=models.CASCADE)








