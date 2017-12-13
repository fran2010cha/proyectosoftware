from django.shortcuts import render
from django.http import HttpResponse
from apps.Empleado.forms import EmpleadoForm
from apps.Empleado.models import Empleado
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
 # Create your views here.

def index_empleado(request):
	return render(request, 'empleado/index.html')


def empleado_list(request): 
	empleado = Empleado.objects.all()
	contexto = {'empleado': empleado}
	return render(request, 'empleado/empleado_list.html',contexto)

class EmpleadoList(ListView):
	model = Empleado
	template_name = 'empleado/empleado_list.html'	

class EmpleadoCreate(CreateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'empleado/empleado_form.html'
	success_url = reverse_lazy('empleado_listar')

class EmpleadoUpdate(UpdateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'empleado/empleado_form.html'
	success_url = reverse_lazy('empleado_listar')

class EmpleadoDelete(DeleteView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'empleado/empleado_delete.html'
	success_url = reverse_lazy('empleado_listar')