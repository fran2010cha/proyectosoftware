from django.db import models
from apps.Producto.models import Producto
# Create your models here.
class Plato(models.Model):
	nombre_plato = models.CharField(max_length=30)
	precio = models.IntegerField()
	producto = models.ManyToManyField(Producto,blank=True)
	

	def __str__(self):
		return '{}'.format(self.nombre_plato)

		