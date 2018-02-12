from django.shortcuts import render ,redirect
from django.http import HttpResponse
from apps.Inventarioproducto.filters import ProductFilter
from apps.Inventarioproducto.forms import InventariopForm
from apps.Inventarioproducto.models import Inventarioproducto
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def Inventariopinicio(request):
	#titulo = "Bienvenidos"
	if request.user.is_authenticated():
		titulo = "hola, %s!" %(request.user)
	form = InventariopForm (request.POST)

	context ={
		"titulo":titulo,
		"form":form
	}
	if form.is_valid():
			instance = form.save(commit=False)
			producto = form.cleaned_data.get("producto")
			inventario = form.cleaned_data.get("inventario")	
			cantidad = form.cleaned_data.get("cantidad")	
			form.save()
			
			context ={
			"titulo":"producto %s,cantidad %s quedo reguistrado correctamente. en el inventario %s" %(producto,cantidad,inventario)

	}
	return render(request, 'inventarioproducto/index.html', context)

def product_list(request):
    f = ProductFilter(request.GET, queryset=Inventarioproducto.objects.all())
    return render(request, 'inventarioproducto/index.html', {'filter': f})

class InventariopList(ListView):
	model = Inventarioproducto
	template_name = 'inventarioproducto/inventariop_list.html'

class InventariopCreate(CreateView):
	model = Inventarioproducto
	form_class = InventariopForm
	template_name = 'inventarioproducto/inventariop_form.html'
	success_url = reverse_lazy('inventarioproducto:inventariop_crear')

class InventariopUpdate(UpdateView):
	model = Inventarioproducto
	form_class = InventariopForm
	template_name = 'inventarioproducto/inventariop_form.html'
	success_url = reverse_lazy('plato_listar')

class InventariopDelete(DeleteView):
	model = Inventarioproducto
	form_class = InventariopForm
	template_name = 'inventarioproducto/inventariop_delete.html'
	success_url = reverse_lazy('plato_listar')