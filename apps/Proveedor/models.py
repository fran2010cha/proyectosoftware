from django.db import models
# Create your models here.
class Proveedor(models.Model):
	nombre_Prove = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	telefono = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.nombre_Prove)

		