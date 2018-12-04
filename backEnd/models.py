from django.db import models

# Create your models here.


class EstadoTienda(models.Model):
	codigo_estado=models.IntegerField(primary_key=True)
	estado=models.CharField(max_length=20)


class Tienda(models.Model):
	codigo_tienda=models.AutoField(primary_key=True)
	nombre_tienda=models.CharField(max_length=30)
	nombre_sucursal=models.CharField(max_length=30,null=True)
	direccion=models.CharField(max_length=40)	
	region=models.CharField(max_length=20)
	ciudad=models.CharField(max_length=20)
	estado=models.ForeignKey(EstadoTienda,on_delete=models.CASCADE)

class Producto(models.Model):
	codigo_prod=models.AutoField(primary_key=True)
	nombre_producto=models.CharField(max_length=30,null=False)
	costo_presupuestado=models.IntegerField(null=True)
	costo_real=models.IntegerField(null=True)    
	notas=models.CharField(max_length=30,null=True)
	tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE,null=True)


