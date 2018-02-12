from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.Registroventa.views import  RegistroventaCreate,Registroventainicio
urlpatterns = [
    url(r'^nuevo$',login_required(RegistroventaCreate.as_view()) , name='registro_crear'),
    url(r'^index$',Registroventainicio , name='registro_inicio'),
 	
 	#url(r'^editar/(?P<pk>\d+)/$', login_required(registroventaUpdate.as_view()), name='registroventa_editar'),
	#url(r'^eliminar/(?P<pk>\d+)/$', login_required(registroventaDelete.as_view()), name='registroventa_eliminar'),
    #url(r'^listar', login_required(registroventaList.as_view()), name='registroventa_listar'),
      
]