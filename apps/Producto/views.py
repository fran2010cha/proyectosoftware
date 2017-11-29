from django.shortcuts import render ,redirect
from django.http import HttpResponse
from apps.Producto.forms import ProductoForm
from apps.Producto.models import Producto
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
def index_producto(request):
	return render(request,'producto/index.html')

def producto_list(request):
	producto = Producto.objects.all()
	contexto = {'productos':producto}
	return render(request, 'producto/producto_list.html', contexto)

class ProductoList(ListView):
	model = Producto
	template_name = 'producto/producto_list.html'

class ProductoCreate(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_form.html'
	success_url = reverse_lazy('producto_listar')

class ProductoUpdate(UpdateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_form.html'
	success_url = reverse_lazy('producto_listar')

class ProductoDelete(DeleteView):
	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_delete.html'
	success_url = reverse_lazy('producto_listar')