from django.db import models
from apps.Plato.models import Plato
from apps.Registroventa.models import Registroventa



# Create your models here.
class Inventarioproducto(models.Model):
	registroventa = models.ForeignKey(Registroventa, null=True,blank=True,on_delete=models.CASCADE)
	plato = models.ForeignKey(Plato, null=True,blank=True,on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	
	