from django import forms 
from apps.Empleado.models import Empleado

class EmpleadoForm(forms.ModelForm):
	
	class Meta:
		model = Empleado 

		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'direccion',
			'email',
		]
		labels = {			
			'nombre':'Nombre',
			'apellidos':'Apellidos',
			'edad': 'Edad',
			'telefono':'Telefono',
			'direccion': 'Direccion',
			'email': 'Correo_Electronico',
		
		} 
		widgets = {
			'nombre':  forms.TextInput(attrs={'class':'form-control'}) ,
			'apellidos':  forms.TextInput(attrs={'class':'form-control'}),
			'edad' :  forms.TextInput(attrs={'class':'form-control'}) ,
			'telefono':  forms.TextInput(attrs={'class':'form-control'}),
			'direccion' :  forms.TextInput(attrs={'class':'form-control'}),
			'email' :  forms.TextInput(attrs={'class':'form-control'}),
		
		}