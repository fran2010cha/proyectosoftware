from django import forms
from apps.Proveedor.models import Proveedor

class ProveedorForm(forms.ModelForm):

	class Meta:
		model = Proveedor

		fields = [
			'nombre_Prove',
			'direccion',
			'telefono',
		]
		labels = {
			'nombre_Prove': 'Nombre_Proveedor',
			'direccion' : 'Direccion',
			'telefono' : 'Telefono',
		}
		widgets = {
			'nombre_Prove': forms.TextInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
		}