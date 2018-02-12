from django.shortcuts import render ,redirect
from django.http import HttpResponse
from apps.Inventario.forms import InventarioForm
from apps.Inventario.models import Inventario
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def Inventarioinicio(request):
	#titulo = "Bienvenidos"
	if request.user.is_authenticated():
		titulo = "hola, %s!" %(request.user)
	form = InventarioForm (request.POST)

	context ={
		"titulo":titulo,
		"form":form
	}
	if form.is_valid():
			instance = form.save(commit=False)
			fecha = form.cleaned_data.get("fecha")
			descripcion = form.cleaned_data.get("descripcion")	
			form.save()
			
			context ={
			"titulo":"descripcion %s, quedo reguistrado correctamente. fecha %s" %(descripcion,fecha)

	}
	return render(request, 'inventario/index.html', context)
	
class InventarioList(ListView):
	model = Inventario
	template_name = 'inventario/inventario_list.html'

class InventarioCreate(CreateView):
	model = Inventario
	form_class = InventarioForm
	template_name = 'inventario/inventario_form.html'
	success_url = reverse_lazy('inventarioproducto:inventariop_crear')

class InventarioUpdate(UpdateView):
	model = Inventario
	form_class = InventarioForm
	template_name = 'inventario/inventario_form.html'
	success_url = reverse_lazy('plato_listar')

class InventarioDelete(DeleteView):
	model = Inventario
	form_class = InventarioForm
	template_name = 'inventario/inventario_delete.html'
	success_url = reverse_lazy('plato_listar')