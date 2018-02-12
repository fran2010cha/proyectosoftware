from django import forms
from apps.Inventario.models import Inventario

class InventarioForm(forms.ModelForm):

	class Meta:
		model = Inventario

		fields = [
			'fecha',
			'descripcion',
		]
		labels = {
			'fecha': 'Fecha',
			'descripcion' : 'Descripcion',
		}
		widgets = {
			'fecha':  forms.TextInput(attrs={'class':'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
		}