
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from apps.Registroventa.forms import RegistroventaForm
from apps.Registroventa.models import Registroventa
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def Registroventainicio(request):
	#titulo = "Bienvenidos"
	if request.user.is_authenticated():
		titulo = "hola, %s!" %(request.user)
	form = RegistroventaForm (request.POST)

	context ={
		"titulo":titulo,
		"form":form
	}
	if form.is_valid():
			instance = form.save(commit=False)
			plato = form.cleaned_data.get("plato")
			cantidad= form.cleaned_data.get("cantidad")	
			form.save()
			
			context ={
			"titulo":"plato %s, quedo reguistrado correctamente. cantidad %s" %(plato,cantidad)
			
	}
	return render(request, 'registroventa/index.html', context)
class RegistroventaCreate(CreateView):
		model = Registroventa
		template_name = 'registroventa/registroventa_form.html'
		form_class = RegistroventaForm
		success_url = reverse_lazy('plato_listar')
	##
	#class registroventaUpdate(UpdateView):
	##	model = registroventa
	##	form_class = registroventaForm
	#	template_name = 'registroventa/registroventa_form.html'
	#	success_url = reverse_lazy('registroventa_listar')
	#class registroventaDelete(DeleteView):
	#	model = registroventa
	#	form_class = registroventaForm
	#	template_name = 'registroventa/registroventa_delete.html'
	#	success_url = reverse_lazy('registroventa_listar')

	#class registroventaList(ListView):
	#	model = registroventa
	#	template_name = 'registroventa/registroventa_list.html'


#def post_new(request):
#        if request.method == "POST":
 #            form = PostForm(request.POST)
 #           if form.is_valid():
 #               post = form.save(commit=False)
 #               post.author = request.user
  #              post.published_date = timezone.now()
  #              post.save()
  #              return redirect('post_detail', pk=post.pk)
  #      else:
  #          form = PostForm()
  #      return render(request, 'blog/post_edit.html', {'form': form})

