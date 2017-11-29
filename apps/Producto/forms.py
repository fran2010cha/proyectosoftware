from django import forms
from apps.Producto.models import Producto

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto

		fields = [
			'nombrepro',
			'costo',
			'proveedor',
		]
		labels = {
			'nombrepro': 'Nombrepro',
			'costo' : 'costo',
			'proveedor' : 'Proveedor',
		}
		widgets = {
			'nombrepro': forms.TextInput(attrs={'class':'form-control'}),
			'costo' : forms.TextInput(attrs={'class':'form-control'}),
			'proveedor' : forms.Select(attrs={'class':'form-control'}),
		}