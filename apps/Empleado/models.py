from django.db import models
from apps.Plato.models import Plato

class Empleado(models.Model):

	nombre=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=10) 
	direccion=models.TextField()
	email=models.EmailField()
	plato = models.ManyToManyField(Plato,blank=True)
	
	def __str__(self):
		return '{}'.format(self.nombre)