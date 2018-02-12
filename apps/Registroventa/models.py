from django.db import models

# Create your models here.
class Registroventa(models.Model):
	descripcion = models.CharField(max_length=50)
	fecha=models.DateField()

	def __str__(self):
		return '{}'.format(self.descripcion)
