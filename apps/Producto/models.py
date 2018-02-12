from django.db import models
from apps.Proveedor.models import Proveedor

# Create your models here.
class Producto(models.Model):
	nombrepro = models.CharField(max_length=30)
	costo = models.IntegerField()
	proveedor = models.ForeignKey(Proveedor, null=True,blank=True,on_delete=models.CASCADE)


	def __str__(self):
		return '{}'.format(self.nombrepro)

		