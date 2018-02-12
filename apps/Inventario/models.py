from django.db import models

# Create your models here.
class Inventario(models.Model):
	fecha=models.DateField()
	descripcion = models.CharField(max_length=50)
	
	def __str__(self):
		return '%s - %s - %s' %(self.id,self.descripcion,self.fecha)
