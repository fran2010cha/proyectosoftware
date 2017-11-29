from django.shortcuts import render ,redirect
from django.http import HttpResponse
from apps.Plato.forms import PlatoForm
from apps.Plato.models import Plato
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
def index_plato(request):
	return render(request,'plato/index.html')

def plato_view(request):
	if request.method == 'POST':
		form = PlatoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('plato_crear')
	else:
		form = PlatoForm()
    #return render(request,'plato/plato_form.html', {'form':form})
	return render(request, 'plato/plato_form.html', {'form':form})

def plato_list(request):
	plato = Plato.objects.all()
	contexto = {'platos':plato}
	return render(request, 'plato/plato_list.html', contexto)

class PlatoList(ListView):
	model = Plato
	template_name = 'plato/plato_list.html'

class PlatoCreate(CreateView):
	model = Plato
	form_class = PlatoForm
	template_name = 'plato/plato_form.html'
	success_url = reverse_lazy('plato_listar')

class PlatoUpdate(UpdateView):
	model = Plato
	form_class = PlatoForm
	template_name = 'plato/plato_form.html'
	success_url = reverse_lazy('plato_listar')

class PlatoDelete(DeleteView):
	model = Plato
	form_class = PlatoForm
	template_name = 'plato/plato_delete.html'
	success_url = reverse_lazy('plato_listar')