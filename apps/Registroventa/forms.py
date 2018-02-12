from django import forms
from apps.Registroventa.models import Registroventa

class RegistroventaForm(forms.ModelForm):

	class Meta:
		model = Registroventa

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