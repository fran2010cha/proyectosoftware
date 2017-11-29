from django import forms
from apps.Plato.models import Plato

class PlatoForm(forms.ModelForm):

	class Meta:
		model = Plato

		fields = [
			'nombre_plato',
			'precio',
			'producto',
		]
		labels = {
			'nombre_plato': 'Nombre_plato',
			'precio' : 'Precio',
			'producto' : 'Producto',
		}
		widgets = {
			'nombre_plato': forms.TextInput(attrs={'class':'form-control'}),
			'precio' : forms.TextInput(attrs={'class':'form-control'}),
			'producto' : forms.CheckboxSelectMultiple(),
		}