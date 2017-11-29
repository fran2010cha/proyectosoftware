from django.shortcuts import render ,redirect
from django.http import HttpResponse
from apps.Proveedor.forms import ProveedorForm
from apps.Proveedor.models import Proveedor
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
def index_proveedor(request):
	return render(request,'proveedor/index.html')

def proveedor_list(request):
	proveedor = Proveedor.objects.all()
	contexto = {'proveedores':proveedor}
	return render(request, 'proveedor/proveedor_list.html', contexto)

class ProveedorList(ListView):
	model = Proveedor
	template_name = 'proveedor/proveedor_list.html'

class ProveedorCreate(CreateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'proveedor/proveedor_form.html'
	success_url = reverse_lazy('proveedor_listar')

class ProveedorUpdate(UpdateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'proveedor/proveedor_form.html'
	success_url = reverse_lazy('proveedor_listar')

class ProveedorDelete(DeleteView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'proveedor/proveedor_delete.html'
	success_url = reverse_lazy('proveedor_listar')