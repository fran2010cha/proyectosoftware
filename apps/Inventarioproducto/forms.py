from django import forms
from apps.Inventarioproducto.models import Inventarioproducto

class InventariopForm(forms.ModelForm):

	class Meta:
		model = Inventarioproducto

		fields = [
			'inventario',
			'producto',
			'cantidad',
		]
		labels = {
			'inventario' : 'Inventario',
			'producto': 'Nombre producto',
			'cantidad' : 'Cantidad',
		}
		widgets = {
			'inventario': forms.Select(attrs={'class':'form-control'}),
			'producto' : forms.Select(attrs={'class':'form-control'}),
			'cantidad' : forms.TextInput(attrs={'class':'form-control'}),
		}