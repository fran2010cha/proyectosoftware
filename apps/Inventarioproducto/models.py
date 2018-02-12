from django.db import models
from apps.Producto.models import Producto
from apps.Inventario.models import Inventario


# Create your models here.
class Inventarioproducto(models.Model):
	inventario = models.ForeignKey(Inventario, null=True,blank=True,on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, null=True,blank=True,on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	
	